// Email signup for The Fatal Five (Vercel serverless function).
//
// Spam defenses, in order:
//   1. Origin check: only accepts posts from thefatalfive.com pages.
//   2. Signed timing token: the page must first GET a token from this endpoint,
//      and the POST is refused if it comes back faster than a person could fill
//      the form (under 3 seconds) or after 2 hours.
//   3. Honeypot field: a hidden "company" field people never see. Bots fill it.
//      Those posts get a normal-looking success reply and are quietly dropped.
//   4. Strict input checks: valid email shape, a domain that can receive mail
//      (MX lookup), no throwaway-email domains, and no links in the name field.
//   5. Per-visitor rate limit (best effort, per server instance).
//   6. Optional Cloudflare Turnstile check, switched on by setting
//      TURNSTILE_SITE_KEY and TURNSTILE_SECRET_KEY.
//   7. Double opt-in: Kit emails a confirmation link; nobody joins the list
//      until they click it.
//
// Only the email address and optional first name are sent. Assessment answers
// never leave the visitor's browser.
//
// Environment variables (Vercel > Project > Settings > Environment Variables):
//   KIT_API_KEY           Kit v4 API key (required)
//   KIT_FORM_ID           Kit form ID with double opt-in on (required)
//   SIGNUP_SECRET         Any long random string, used to sign timing tokens (required)
//   TURNSTILE_SITE_KEY    Cloudflare Turnstile site key (optional)
//   TURNSTILE_SECRET_KEY  Cloudflare Turnstile secret key (optional)

const crypto = require('crypto');
const dns = require('dns').promises;

const ALLOWED_ORIGINS = [
  'https://thefatalfive.com',
  'https://www.thefatalfive.com',
];
const MIN_FILL_MS = 3000;
const MAX_TOKEN_AGE_MS = 2 * 60 * 60 * 1000;
const RATE_LIMIT = 5;              // signups per visitor
const RATE_WINDOW_MS = 60 * 60 * 1000; // per hour

const DISPOSABLE_DOMAINS = new Set([
  'mailinator.com', 'guerrillamail.com', 'guerrillamail.net', 'sharklasers.com',
  '10minutemail.com', 'tempmail.com', 'temp-mail.org', 'throwawaymail.com',
  'yopmail.com', 'getnada.com', 'trashmail.com', 'dispostable.com',
  'maildrop.cc', 'fakeinbox.com', 'mailnesia.com', 'mintemail.com',
  'spamgourmet.com', 'emailondeck.com', 'mohmal.com', 'tempail.com',
]);

const hits = new Map(); // visitor key -> array of timestamps

function originAllowed(req) {
  const origin = req.headers.origin || '';
  if (ALLOWED_ORIGINS.includes(origin)) return true;
  // Allow Vercel preview deployments of this project for testing.
  return /^https:\/\/thefatalfive-website-[a-z0-9-]+\.vercel\.app$/.test(origin);
}

function sign(value, secret) {
  return crypto.createHmac('sha256', secret).update(String(value)).digest('hex');
}

function makeToken(secret, now = Date.now()) {
  return `${now}.${sign(now, secret)}`;
}

function checkToken(token, secret, now = Date.now()) {
  if (typeof token !== 'string' || !token.includes('.')) return 'missing';
  const [ts, mac] = token.split('.');
  const issued = Number(ts);
  if (!Number.isFinite(issued)) return 'invalid';
  const expected = sign(issued, secret);
  if (mac.length !== expected.length ||
      !crypto.timingSafeEqual(Buffer.from(mac), Buffer.from(expected))) return 'invalid';
  const age = now - issued;
  if (age < MIN_FILL_MS) return 'too_fast';
  if (age > MAX_TOKEN_AGE_MS) return 'expired';
  return 'ok';
}

function rateLimited(key, now = Date.now()) {
  const list = (hits.get(key) || []).filter(t => now - t < RATE_WINDOW_MS);
  list.push(now);
  hits.set(key, list);
  return list.length > RATE_LIMIT;
}

const EMAIL_RE = /^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+$/;

function cleanEmail(raw) {
  if (typeof raw !== 'string') return null;
  const email = raw.trim().toLowerCase();
  if (email.length < 6 || email.length > 254 || !EMAIL_RE.test(email)) return null;
  const domain = email.split('@')[1];
  if (!/\.[a-z]{2,}$/.test(domain)) return null;
  return email;
}

function cleanName(raw) {
  if (raw == null || raw === '') return '';
  if (typeof raw !== 'string') return null;
  const name = raw.trim().replace(/\s+/g, ' ');
  if (name.length > 50) return null;
  // Spam signups stuff links and markup into name fields.
  if (/https?:|www\.|\.(com|net|org|ru|xyz|io|info|top)\b|[<>{}\[\]\\\/@]/i.test(name)) return null;
  return name;
}

async function domainReceivesMail(domain) {
  try {
    const mx = await dns.resolveMx(domain);
    if (mx && mx.length) return true;
  } catch (_) { /* fall through to A record */ }
  try {
    const a = await dns.resolve4(domain);
    return !!(a && a.length);
  } catch (_) {
    return false;
  }
}

async function verifyTurnstile(token, ip, secret) {
  if (!token) return false;
  const body = new URLSearchParams({ secret, response: token });
  if (ip) body.set('remoteip', ip);
  const r = await fetch('https://challenges.cloudflare.com/turnstile/v0/siteverify', {
    method: 'POST', body,
  });
  const data = await r.json().catch(() => ({}));
  return data.success === true;
}

async function kitSubscribe(email, firstName, apiKey, formId) {
  const headers = { 'Content-Type': 'application/json', 'X-Kit-Api-Key': apiKey };
  // Create the subscriber as inactive; they become active only after confirming.
  const create = await fetch('https://api.kit.com/v4/subscribers', {
    method: 'POST', headers,
    body: JSON.stringify({ email_address: email, first_name: firstName || undefined, state: 'inactive' }),
  });
  if (!create.ok && create.status !== 200) throw new Error(`kit_create_${create.status}`);
  // Adding them to the form sends Kit's confirmation (double opt-in) email.
  const add = await fetch(`https://api.kit.com/v4/forms/${encodeURIComponent(formId)}/subscribers`, {
    method: 'POST', headers,
    body: JSON.stringify({ email_address: email, referrer: 'https://thefatalfive.com/assessment/' }),
  });
  if (!add.ok) throw new Error(`kit_form_${add.status}`);
}

function send(res, status, payload) {
  res.setHeader('Cache-Control', 'no-store');
  res.status(status).json(payload);
}

async function handler(req, res) {
  const { KIT_API_KEY, KIT_FORM_ID, SIGNUP_SECRET, TURNSTILE_SITE_KEY, TURNSTILE_SECRET_KEY } = process.env;
  const configured = !!(KIT_API_KEY && KIT_FORM_ID && SIGNUP_SECRET);

  if (req.method === 'GET') {
    if (!configured) return send(res, 503, { ok: false, error: 'not_configured' });
    return send(res, 200, {
      ok: true,
      token: makeToken(SIGNUP_SECRET),
      turnstileSiteKey: TURNSTILE_SECRET_KEY && TURNSTILE_SITE_KEY ? TURNSTILE_SITE_KEY : null,
    });
  }
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'GET, POST');
    return send(res, 405, { ok: false, error: 'method_not_allowed' });
  }
  if (!configured) return send(res, 503, { ok: false, error: 'not_configured' });
  if (!originAllowed(req)) return send(res, 403, { ok: false, error: 'forbidden' });

  const ip = String(req.headers['x-forwarded-for'] || '').split(',')[0].trim() || 'unknown';
  if (rateLimited(ip)) return send(res, 429, { ok: false, error: 'too_many' });

  const body = typeof req.body === 'object' && req.body ? req.body : {};

  // Honeypot: pretend it worked so the bot learns nothing.
  if (body.company) return send(res, 200, { ok: true });

  const tokenState = checkToken(body.token, SIGNUP_SECRET);
  if (tokenState === 'too_fast') return send(res, 200, { ok: true }); // bot speed: drop quietly
  if (tokenState !== 'ok') return send(res, 400, { ok: false, error: 'session_expired' });

  if (body.consent !== true) return send(res, 400, { ok: false, error: 'consent_required' });

  const email = cleanEmail(body.email);
  if (!email) return send(res, 400, { ok: false, error: 'invalid_email' });
  const domain = email.split('@')[1];
  if (DISPOSABLE_DOMAINS.has(domain)) return send(res, 400, { ok: false, error: 'invalid_email' });

  const firstName = cleanName(body.firstName);
  if (firstName === null) return send(res, 400, { ok: false, error: 'invalid_name' });

  if (TURNSTILE_SECRET_KEY && TURNSTILE_SITE_KEY) {
    const human = await verifyTurnstile(body.turnstileToken, ip, TURNSTILE_SECRET_KEY);
    if (!human) return send(res, 400, { ok: false, error: 'verification_failed' });
  }

  if (!(await domainReceivesMail(domain))) return send(res, 400, { ok: false, error: 'invalid_email' });

  try {
    await kitSubscribe(email, firstName, KIT_API_KEY, KIT_FORM_ID);
  } catch (err) {
    console.error('signup_failed', err.message);
    return send(res, 502, { ok: false, error: 'service_unavailable' });
  }
  return send(res, 200, { ok: true });
}

module.exports = handler;
module.exports._test = { makeToken, checkToken, cleanEmail, cleanName, originAllowed, hits };

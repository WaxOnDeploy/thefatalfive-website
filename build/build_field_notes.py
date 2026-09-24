import sys
sys.path.insert(0, '.')
from header_footer import head, nav, footer

def para_html(paragraphs):
    out = ""
    for p in paragraphs:
        out += f"      <p>{p}</p>\n"
    return out

def make_article(slug, tag, title, dek, meta_desc, paragraphs, case_note):
    body = f"""
{nav("../")}

<main>
  <div class="narrow">
    <article class="post">
      <div class="meta">{tag}</div>
      <h1>{title}</h1>
      <p class="dek">{dek}</p>
{para_html(paragraphs)}
      <p style="font-size:14px; color:var(--ink-dim); font-style:italic; margin-top:28px;">{case_note}</p>
      <div class="backlink">
        <a class="link" href="index.html">&larr; All field notes</a>
      </div>
    </article>
  </div>
</main>

{footer("../")}
"""
    html_out = head(f"{title} — The Fatal Five", meta_desc, root="../") + body
    with open(f'/home/claude/fatalfive-repo/field-notes/{slug}.html', 'w') as f:
        f.write(html_out)
    print("wrote", slug)


# --- Article 1: Hindenburg ---
make_article(
    slug="the-ship-everyone-knew-was-a-gamble",
    tag="Case File &middot; Aviation &middot; Case #55",
    title="The Ship That Everyone Knew Was a Gamble",
    dek="A Fatal Five case file",
    meta_desc="The Hindenburg disaster through the Fatal Five framework: a known risk accepted under constraint, and a quality standard that eroded quietly under routine.",
    paragraphs=[
        "May 6, 1937. A German passenger airship 800 feet long &mdash; longer than the <em>Titanic</em> &mdash; was closing in on its mooring mast in Lakehurst, New Jersey, at the end of an Atlantic crossing it had now made routinely for two years. Ground crews had the landing lines in hand. A reporter on the field was drafting the same dull copy he'd filed a dozen times before: another safe arrival, another wire story nobody would read. Then, in thirty-seven seconds, none of that mattered &mdash; the ship came down as a burning skeleton of fabric and duralumin, and 36 people didn't walk away.",
        "Most people know the newsreel footage by heart. Fewer people know the disaster wasn't actually a mystery &mdash; it was a known, named, argued-about risk that the organization flew anyway.",
        "<strong>The risk was on the table for years &mdash; and they flew around it instead of through it.</strong>",
        "The Hindenburg was designed to fly on helium. Helium doesn't burn. American engineers and German airship designers both wanted it. The problem was that in 1937, the United States controlled essentially the entire world's helium supply, and the Helium Control Act of 1927 barred its export &mdash; originally a safeguard against the gas being used for military purposes, and by the mid-1930s a policy nobody in Washington was in a hurry to revisit for a German company. So the Hindenburg's operator, the Deutsche Zeppelin-Reederei, did what organizations under a hard external constraint tend to do: they built the aircraft they could actually fuel. Hydrogen. Lighter, cheaper, more lift &mdash; and catastrophically flammable, a fact nobody on that program needed a report to tell them.",
        "That's Pattern 1 in the Fatal Five framework: <strong>risk management failure.</strong> Not an unforeseen risk &mdash; a <em>fully seen</em> risk, formally assessed, discussed in engineering and government correspondence for a decade, and accepted anyway because the safe alternative was unavailable and the unsafe one was flyable <em>today</em>. Every program that has ever shipped the version it could get through procurement instead of the version it actually wanted will recognize the shape of that decision immediately.",
        "<strong>The second failure is the one investigators actually argued about.</strong>",
        "The prevailing theory &mdash; never conclusively proven, but the best-supported one to come out of both the American and German boards of inquiry &mdash; is that an electrostatic discharge ignited hydrogen venting from the ship's gas cells during the landing approach, most likely through a torn or under-sealed outer cover that let gas seep into open air. The airship's skin, its rigging, and its grounding procedures had been engineered for years of hydrogen operation. That's not nothing. But “years of experience with a known hazard” is exactly the condition under which the margin quietly erodes &mdash; a rigging adjustment here, a fabric patch there, a procedure followed by habit rather than re-verified against the actual risk it was written for. That's Pattern 3: <strong>quality management failure.</strong> Not a single dramatic shortcut, but the slow accumulation of “this has always been fine” in a system that had zero room for “usually fine.”",
        "<strong>Two patterns, one disaster, both patterns already in your organization right now.</strong>",
        "You don't need a hydrogen airship to recognize this. You need a team that shipped the version of the architecture it could actually get infrastructure approval for, instead of the one it wanted &mdash; and called that a done conversation instead of a live risk. You need a process that's run the same way for two years without anyone asking whether “the way we've always done it” still matches the hazard it was built around. Risk accepted under constraint, and quality that erodes quietly under routine, are two of the patterns we return to most often across the 65-case, 175-year research corpus behind this book. The Hindenburg carries both at once, cleanly, in under a minute of real time.",
        "Thirty-six people died in an accident that took investigators years to fully reconstruct and that could, with hindsight, be summarized in two sentences: <em>they flew the airship they could fuel, not the one they wanted, and they trusted years of routine over the hazard the routine was managing.</em> That sentence describes disasters. It also describes a lot of retrospectives.",
    ],
    case_note="The Hindenburg is case #55 in the Fatal Five research corpus &mdash; one of 65 disasters spanning 175 years studied to identify the five failure patterns behind catastrophic organizational breakdowns. Read more in <a class=\"link\" href=\"../index.html#book\">The Fatal Five</a>, or take the free <a class=\"link\" href=\"../drift-check/index.html\">4-question Drift Check</a> to see which pattern shows up first in your own team.",
)

# --- Article 2: Hyatt Regency ---
make_article(
    slug="the-change-order-nobody-recalculated",
    tag="Case File &middot; Construction &middot; Case #61",
    title="The Change Order Nobody Re-Calculated",
    dek="A Fatal Five case file",
    meta_desc="The 1981 Hyatt Regency walkway collapse through the Fatal Five framework: a fabrication convenience that doubled a load-bearing connection's load, approved without a re-calculation.",
    paragraphs=[
        "On the evening of July 17, 1981, more than 1,600 people packed the atrium of the Hyatt Regency in Kansas City for a weekly tea dance &mdash; the kind of casual, low-stakes event a hotel runs a hundred times a year. Three suspended walkways crossed the atrium at the second, third, and fourth floors, stacked directly above one another, packed with people watching the dance below. At 7:05 PM, the fourth-floor walkway tore loose from its connections and dropped straight through the third-floor walkway onto the crowd beneath. 114 people died. It remains one of the deadliest structural failures in U.S. history &mdash; and it wasn't caused by an earthquake, a material defect, or an unforeseeable load. It was caused by a single design change that nobody re-ran the numbers on.",
        "<strong>The original design was already carrying its full rated load. The “equivalent” fix doubled it.</strong>",
        "The atrium's walkways were originally engineered to hang from a set of long steel rods running continuously from the roof down through all three walkway levels, each walkway's box beam supported by a nut threaded onto that single rod. During construction, the fabricator found this design difficult to build &mdash; threading a nut precisely at the mid-span point of a rod that also had to pass load through a second walkway above it was awkward on-site. So the fabricator proposed a change: instead of one continuous rod carrying both walkways, use two separate rods &mdash; one from the roof to the fourth-floor walkway, a second from the fourth-floor walkway down to the second-floor walkway. To the people signing off, it looked like a trivial fabrication convenience. It wasn't. In the original design, each connection point carried the weight of one walkway. In the revised design, the fourth-floor connection now had to carry the weight of <em>two</em> walkways &mdash; its own, plus the one hanging beneath it &mdash; through a box-beam-to-hanger connection never engineered for double load. The change went through review. Nobody re-ran the calculation against the new load path.",
        "That's Pattern 3 in the Fatal Five framework: <strong>quality management failure.</strong> Not a shortcut skipped under pressure &mdash; a change that <em>looked</em> equivalent, approved by people who assumed someone else had verified the math, moving through a review process that checked the drawing without checking the physics. Any engineer, any reviewer, any structural inspector who ran the numbers on the as-built connection would have found it was carrying roughly double its rated capacity from day one. Nobody did, until the rods finally failed under the ordinary, foreseeable weight of a crowd standing on a walkway &mdash; which is, after all, the one thing a walkway is built to hold.",
        "<strong>The second failure is the one every retrospective in this book keeps finding.</strong>",
        "The fabricator's proposed change traveled from the steel detailer to the structural engineer of record for a sign-off that, per later investigation, amounted to a stamp on a drawing rather than an independent re-analysis &mdash; a single point in a long chain where a genuine structural review was assumed to have already happened somewhere else. That's Pattern 2: <strong>communication management failure.</strong> Not a message that got lost &mdash; a decision that moved through multiple hands, each one trusting that the actual engineering judgment lived with somebody else in the chain, until it turned out to live with no one.",
        "<strong>You've approved this exact change. It just wasn't made of steel.</strong>",
        "You know this pattern from the other side of the table: the “equivalent” refactor that changes which service owns a piece of state, approved because it passed code review, when the load characteristics of the <em>new</em> dependency were never re-modeled against the <em>old</em> one's assumptions. The migration that looked like a lift-and-shift until it quietly doubled what a single component had to carry. The architecture decision that got a sign-off from someone who assumed the load analysis happened in an earlier conversation they weren't in. A quality failure paired with a communication failure &mdash; a change that looked equivalent, and a sign-off that trusted the chain instead of verifying the connection &mdash; is one of the clearest, most recurring combinations in the research corpus, and the Hyatt Regency is one of the cleanest examples of it: a fabrication convenience, a missing re-calculation, and a stamp that stood in for a review. It took less than four seconds for the walkway to fall. It took an entire, ordinary approval process to make sure nobody caught it first.",
    ],
    case_note="The Hyatt Regency walkway collapse is case #61 in the Fatal Five research corpus &mdash; one of 65 disasters spanning 175 years studied to identify the five failure patterns behind catastrophic organizational breakdowns. Read more in <a class=\"link\" href=\"../index.html#book\">The Fatal Five</a>, or take the free <a class=\"link\" href=\"../drift-check/index.html\">4-question Drift Check</a> to see which pattern shows up first in your own team.",
)

# --- Article 3: Hartford Circus Fire ---
make_article(
    slug="the-fire-that-happened-before-i-was-born",
    tag="Chapter 8 Preview &middot; Personal &middot; Case #19",
    title="The Fire That Happened Before I Was Born, in the Town Next Door",
    dek="A preview of Chapter 8, “The Fatal Five”",
    meta_desc="A personal preview of Chapter 8: the 1944 Hartford circus fire, twenty minutes from where Jeff Bourke grew up, and what it teaches about normalized risk.",
    paragraphs=[
        "I grew up in Simsbury, Connecticut. Twenty minutes down the road from where I was raised sits Hartford &mdash; the city where, on July 6, 1944, 167 people died in eleven minutes under a circus tent, sixty-eight of them children. I wasn't born yet. My parents weren't born yet. But I grew up in the same stretch of Connecticut where it happened, and by the time I was old enough to hear the story, it had already become one of those pieces of local history everybody just seems to know &mdash; the kind of thing that gets mentioned the way people mention a flood or a blizzard, past tense, safely over.",
        "It is one of the disasters I open Chapter 8 with. Not because it's the deadliest one in the book &mdash; it isn't, not close. Because it's the one that happened closest to home, and because nothing about how it happened required Hartford, or 1944, or a circus. It could have been almost anywhere, almost anytime, and it very nearly still could be.",
        "<strong>Eight thousand people were under that tent. The fire didn't start big. The tent made sure it didn't matter.</strong>",
        "The Ringling Brothers and Barnum &amp; Bailey Circus was performing under canvas that had been waterproofed with a mixture of paraffin wax and gasoline &mdash; a combination that, once lit, behaves less like fabric and more like a tent-shaped candle. Fire inspectors had raised concerns about it before. More than once. By 1944, the warnings weren't being heard as warnings anymore, because nothing had ever gone wrong. That's the sentence I keep coming back to. <em>Nothing had ever gone wrong</em> is not the same thing as <em>nothing was wrong.</em> It just meant the fire hadn't started yet.",
        "When a small fire broke out near the entrance, the waterproofing did exactly what it was chemically built to do: it carried the flame across the entire roof in seconds. Burning canvas began falling into a packed crowd. Exits that had been perfectly adequate for eight thousand people filing out after a normal show became fatal chokepoints the moment eight thousand people tried to use them at once, in a panic, at the same time. Some of the dead were found within feet of the doors.",
        "<strong>This is Pattern 1 from the Fatal Five framework: risk management failure &mdash; a known hazard, flagged, and normalized instead of fixed.</strong>",
        "I've spent thirty-five years in EMS. I've stood in the aftermath of things that went wrong the way the Hartford fire went wrong &mdash; not because anyone set out to hurt someone, but because a risk that had been sitting in plain sight long enough stopped registering as a risk at all. I've also spent most of my professional life running Agile Release Trains, watching teams do the organizational version of the exact same thing: a known issue gets raised, gets logged, gets discussed in a retro &mdash; and then, because nothing catastrophic happens the next sprint, or the one after that, it quietly stops being treated like the live risk it still is. The tent doesn't catch fire every day. Until the one day it does.",
        "<strong>Chapter 8 is where the book stops being about famous disasters and starts being about the ones nobody remembers &mdash; which, it turns out, is most of them.</strong>",
        "Hartford sits alongside the Iroquois Theater fire, the Cocoanut Grove, Our Lady of the Angels, the Beverly Hills Supper Club, the Station nightclub fire &mdash; six disasters, more than a century apart, every one of them driven by the same handful of organizational failures wearing a different costume. Strip away the decade and the setting and you're left with a warning that stopped being heard, an exit that was adequate right up until it wasn't, a shortcut that quietly became structural. That chapter exists because I don't think you need a hundred-and-sixty-seven deaths to recognize the pattern. I think you just need to have watched a team ignore a known risk long enough to believe it wasn't really a risk &mdash; which, if you've worked in software delivery for more than a year or two, you almost certainly have.",
        "I didn't set out to write a book about the town next door. But once I started building the research corpus, Hartford was already there, sitting quietly in Connecticut history the way it's sat quietly in mine &mdash; and I realized it might be the clearest, closest example I had of the exact thing this whole book is trying to say: the patterns that kill people and the patterns that kill projects are the same patterns. Distance doesn't change that. Neither does time.",
    ],
    case_note="The Hartford Circus Fire is case #19 in the Fatal Five research corpus, one of 65 disasters spanning 175 years studied to identify the five organizational failure patterns behind catastrophic breakdowns. It's part of Chapter 8 in <a class=\"link\" href=\"../index.html#book\">The Fatal Five</a>. Or take the free <a class=\"link\" href=\"../drift-check/index.html\">4-question Drift Check</a> to see which pattern shows up first in your own team.",
)

# --- Field notes index ---
fn_index_body = f"""
{nav("../")}

<main>
  <div class="wrap page-hero">
    <div class="eyebrow">Field Notes</div>
    <h1>Case files from the research corpus</h1>
    <p class="lede">Short, standalone breakdowns of individual cases from the 65-case corpus &mdash; each one traced through a specific Fatal Five pattern.</p>
  </div>
  <div class="wrap" style="padding-bottom:80px;">
    <div class="fn-grid">
      <a class="fn-card" href="the-ship-everyone-knew-was-a-gamble.html">
        <div class="tag">Case File &middot; Aviation</div>
        <h3>The Ship That Everyone Knew Was a Gamble</h3>
        <p>The Hindenburg's operator flew the airship it could fuel, not the one it wanted &mdash; and trusted two years of routine over the hazard that routine was managing.</p>
        <div class="readmore link">Read the case &rarr;</div>
      </a>
      <a class="fn-card" href="the-change-order-nobody-recalculated.html">
        <div class="tag">Case File &middot; Construction</div>
        <h3>The Change Order Nobody Re-Calculated</h3>
        <p>A fabrication convenience doubled the load on the Hyatt Regency's walkway connections. A sign-off checked the drawing, not the physics.</p>
        <div class="readmore link">Read the case &rarr;</div>
      </a>
      <a class="fn-card" href="the-fire-that-happened-before-i-was-born.html">
        <div class="tag">Chapter 8 Preview &middot; Personal</div>
        <h3>The Fire That Happened Before I Was Born</h3>
        <p>Twenty minutes from where I grew up, 167 people died under a circus tent in eleven minutes. A known hazard, flagged, and normalized instead of fixed.</p>
        <div class="readmore link">Read the case &rarr;</div>
      </a>
    </div>
  </div>
</main>

{footer("../")}
"""
html_fn = head("Field Notes — The Fatal Five", "Case files from the Fatal Five research corpus.", root="../") + fn_index_body
with open('/home/claude/fatalfive-repo/field-notes/index.html', 'w') as f:
    f.write(html_fn)
print("wrote field-notes/index.html")

import sys
sys.path.insert(0, '.')
from header_footer import head, nav, footer

paragraphs = [
    "I was nine years old the first time a disaster reached out and touched me.",
    "It was the summer of 1984, and I was walking across my grandparents' farm in Simsbury, Connecticut &mdash; the short stretch of ground between the farm stand and the house, heading in for a late lunch. I can still stand in that exact spot today and see it. First the sound: the loudest thing I had ever heard, a concussion more than a noise. Then the ground shook under my feet. And then, rising over the horizon where I could not see the factory or the bunkers but knew they were there, a column of black smoke climbing into the sky.",
    "It was Ensign-Bickford, the explosives manufacturer that had been part of my town longer than anyone alive. Three men had been mixing chemicals in a hundred-gallon vat when it detonated. The blast killed all three, demolished the building, shattered windows half a mile away, and pushed a cloud of smoke and fumes over the town that drove two hundred people from their homes. It was felt a mile away. I know these facts now because I have read the record as an adult. What I knew then was the sound, the shaking, the smoke &mdash; and, for hours afterward, the sirens. So many sirens.",
    "I should tell you the truth about what hooked a nine-year-old that day, because the truth is the reason this book exists. It was not the size of the blast, or the spectacle, or even the whispered rumors about the men who died. What caught me and never let go was a set of questions I could not stop asking. <em>Someone called for help &mdash; what did help do?</em> I heard all those sirens; where were they going, and what happened when they got there? I saw it on the news and I had felt it under my own feet, and that made it real in a way nothing in a book ever had been. I was genuinely, relentlessly curious: what did they <em>do</em>? How did they respond? How did they fix it?",
    "I did not have the words for it then, but I had already found my life's two questions &mdash; the ones this book is built on. When everything breaks, what do the people who run toward it actually do? And why did it break in the first place?",
    "I have spent the forty years since chasing the answers, walking toward the sirens instead of away. For thirty-five of them I have been an emergency medical responder &mdash; an EMT, a training officer, trained at the Department of Homeland Security's disaster-preparedness school to work chemical and mass-casualty scenes. I became the help I wondered about at nine. And along the way, the second question grew into something as urgent as the first: not just <em>how do we respond?</em> but <em>why did this happen?</em> Why the vat exploded. Why the warnings that almost always exist were almost always missed. Why competent, careful people end up standing in the smoke of a disaster that, viewed afterward, looks like it should have been obvious.",
    "That question is the reason I can tell you this next part plainly.",
    "It is always easier to analyze decisions with the benefit of hindsight. Hindsight offers a clarity that those in the midst of crisis simply do not have &mdash; a perspective unavailable to people facing impossible choices in real time, often with limited information and the highest of stakes. In the wake of tragedy it is natural to ask what might have been done differently. But the honest answer requires humility, because the people who were there did not have the answer key we are reading from now.",
    "The men and women at the center of these events &mdash; the engineers, the pilots, the operators, the managers, the first responders &mdash; were not villains. They were people acting with courage, instinct, and determination, using the best knowledge available to them under immense pressure and uncertainty. Their actions were not guided by the luxury of reflection but by the urgent need to respond in the moment. They stood in the face of adversity and did their utmost to protect and save others, and that is how this book treats them.",
    "I learned that respect the hard way, in the field. At the Department of Homeland Security's Center for Domestic Preparedness, my final exam was a simulated phosgene attack on a courthouse: suit up, make entry, bring the victims out, decontaminate, treat, transport. Nothing about that exercise tested whether I knew the chemistry of phosgene. It tested whether the process would hold when everything was designed to break it. I have spent the years since watching that same test administered &mdash; to rig crews, flight crews, condo boards, and software teams &mdash; by events that were not simulations. That experience shapes every page of this book: I know the difference between what the record shows and what the moment felt like, and I will not pretend the people in these pages had access to the clarity we now enjoy.",
    "The same principle extends to the readers of this book. It applies to anyone who has ever been handed a commitment they were not sure they could honestly keep, and been expected to deliver it anyway. The Scrum Master navigating organizational dysfunction. The release train engineer holding a train together through a doomed increment. The product owner caught between irreconcilable demands, the project lead, the engineer, the nurse, the site supervisor, the team member working under impossible pressure to deliver despite every systemic impediment in the way. You are the people closest to the work, which means you are almost always the first to see the smoke. You, too, are making decisions without the benefit of hindsight. You, too, deserve to be judged by what you could know at the time.",
    "And if you lead those people &mdash; if you set the commitments, fund the work, and answer for what happens &mdash; this book is written for you in a different way. You may be too far from the ground to see the early signs yourself; that is not a failing, it is a fact of altitude. But the people beneath you can see them, and in nearly every disaster in these pages, someone did. The warning existed. It was on a desk, in an email, in a meeting, in a voice that went quiet when no one above listened. The single most powerful thing a leader can do to prevent the next catastrophe is almost embarrassingly simple: listen when the people closest to the work start sounding an alarm, and make it safe for them to sound it loudly. This book will show you, again and again, what it costs when they don't.",
    "This book deconstructs moments of catastrophic failure, not to place blame, but to find the patterns that can prevent future tragedies. We analyze these events to prevent others from experiencing the same pain &mdash; to steal these hard-won lessons before we are forced to learn them the same way, and to carry the responsibility of applying them before the next crisis strikes. To learn from history is not to judge it unfairly. It is to honor those who came before us by ensuring their experiences contribute to a safer, more resilient future for us all.",
    "The courage to act in the moment deserves our respect. The wisdom to learn from experience demands our commitment. It started for me with smoke on a horizon in Connecticut, and a boy who needed to know what the people who ran toward it would do. I have spent a life finding out. It has never stopped mattering.",
]

para_html = "\n".join(f"      <p>{p}</p>" for p in paragraphs)

body = f"""
{nav("../")}

<main>
  <div class="narrow">
    <article class="post">
      <div class="meta">Preface</div>
      <h1>The Monday Morning Quarterback</h1>
      <p class="dek">The opening pages of <em>The Fatal Five</em>, in full.</p>
{para_html}
      <div class="backlink">
        <a class="link" href="../index.html#book">&larr; Back to the book</a>
        &nbsp;&middot;&nbsp;
        <a class="link" href="../index.html#contact">Get launch updates &rarr;</a>
      </div>
    </article>
  </div>
</main>

{footer("../")}
"""

html_out = head(
    "Preface: The Monday Morning Quarterback — The Fatal Five",
    "Read the full Preface to The Fatal Five by Jeff Bourke — the Ensign-Bickford explosion, thirty-five years in EMS, and the question the whole book is built on.",
    root="../",
) + body

with open('/home/claude/fatalfive-repo/preface/index.html', 'w') as f:
    f.write(html_out)
print("wrote preface/index.html", len(html_out), "bytes")

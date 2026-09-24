import sys, csv, html
sys.path.insert(0, '.')
from header_footer import head, nav, footer

rows = []
with open('/tmp/claude-0/-home-claude/89ac320e-4200-5ea1-8231-9de01bf7dc4e/scratchpad/fatal-five-corpus-clean.csv') as f:
    r = csv.DictReader(f)
    for row in r:
        rows.append(row)

trs = ""
for row in rows:
    trs += f"""      <tr>
        <td>{row['Case #']}</td>
        <td>{html.escape(row['Disaster'])}</td>
        <td>{html.escape(row['Year'])}</td>
        <td>{html.escape(row['Domain'])}</td>
        <td>{html.escape(row['Toll'])}</td>
        <td>{html.escape(row['Anchor Source'])}</td>
      </tr>
"""

body = f"""
{nav("../")}

<main>
  <div class="wrap page-hero">
    <div class="eyebrow">The Research Corpus</div>
    <h1>The 65 cases</h1>
    <p class="lede">This is the pre-registered, frozen list of every disaster studied to build the Fatal Five framework &mdash; 65 cases, 175 years, 1849&ndash;2024. Every row is anchored to its official investigation record. This is a reference table, not a marketing page: you can check every one.</p>
  </div>

  <div class="wrap" style="padding-bottom:80px;">
    <div class="corpus-table-wrap">
      <table class="corpus">
        <thead>
          <tr>
            <th>#</th>
            <th>Disaster</th>
            <th>Year</th>
            <th>Domain</th>
            <th>Toll</th>
            <th>Anchor source</th>
          </tr>
        </thead>
        <tbody>
{trs}        </tbody>
      </table>
    </div>
    <p class="corpus-note">Toll figures are approximate where cited sources disagree, and reflect direct fatalities unless noted otherwise. Pattern-frequency percentages are intentionally not shown here: the formal two-coder pattern-coding protocol against this corpus has not yet completed, and this page will be updated with those figures, labeled preliminary, once it has.</p>
  </div>
</main>

{footer("../")}
"""

html_out = head(
    "The 65 Cases — The Fatal Five Research Corpus",
    "The full, frozen 65-case research corpus behind The Fatal Five — 65 disasters, 175 years, each anchored to its official investigation record.",
    root="../",
) + body

with open('/home/claude/fatalfive-repo/corpus/index.html', 'w') as f:
    f.write(html_out)
print("wrote corpus/index.html with", len(rows), "rows")

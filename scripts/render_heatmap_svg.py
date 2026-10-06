import json
from datetime import date
from pathlib import Path

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]
S, G, X0, Y0 = 13, 3, 30, 30
data = json.loads(Path("data/contributions.json").read_text())
days = data["days"]
off = (date.fromisoformat(days[0]["date"]).weekday() + 1) % 7  # Sunday-first rows
cells = []
for i, d in enumerate(days):
    w, r = divmod(i + off, 7)
    lvl = min(d["level"], 4) + (
        d["level"] >= 4 and d["count"] >= 10
    )  # level 5 = neon, 10+ commits
    cells.append(
        f'<rect class="c" x="{X0 + w * (S + G)}" y="{Y0 + r * (S + G)}" width="{S}" height="{S}" rx="3" '
        f'fill="{PALETTE[lvl]}" style="animation-delay:{(w + r) * 25}ms"/>'
    )
W = X0 + ((len(days) + off) // 7 + 1) * (S + G) + 10
H = Y0 + 7 * (S + G) + 40
legend = "".join(
    f'<rect x="{W - 160 + i * 16}" y="{H - 22}" width="12" height="12" rx="3" fill="{c}"/>'
    for i, c in enumerate(PALETTE)
)
stats = f"{data['total']} contributions   streak {data['current_streak']}d   longest {data['longest_streak']}d   best day {data['best_day']}"
Path("img/contrib-heatmap.svg").write_text(
    f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="monospace" font-size="11" fill="#8b949e">
<style>.c{{opacity:0;transform:translateY(-8px);animation:in .5s ease-out forwards}}@keyframes in{{to{{opacity:1;transform:none}}}}</style>
<rect width="100%" height="100%" rx="8" fill="#0d1117"/>
{"".join(cells)}
<text x="{X0}" y="{H - 12}">{stats}</text>
<text x="{W - 190}" y="{H - 12}" text-anchor="end">Less</text>{legend}<text x="{W - 70}" y="{H - 12}">More</text>
</svg>"""
)

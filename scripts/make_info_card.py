"""Render the neofetch-style whoami window: ASCII portrait (rows taken from img/avi-ascii.svg) next to the info lines."""

import os
import re
from html import escape
from pathlib import Path

LINES = [
    ("Name", "Artur Komaristych"),
    ("Now", "Senior Software Developer @ Infolytics AG"),
    ("M.Sc.", "CS @ University of Cologne, 2026, honors"),
    ("", "└ Master Thesis @ DLR"),
    ("B.Sc.", "CS @ RWTH Aachen, 2022"),
    ("", "└ Bachelor Thesis @ Fraunhofer IPT"),
    ("Stack", ""),
    ("└ Languages", "Java, C#, TypeScript, C++, Python"),
    ("└ Infra", "Kubernetes, OpenShift, Argo CD, Ansible"),
    ("└ Cloud", "Google Compute Engine, Oracle Cloud"),
    ("Focus", "Distributed systems, backend, DevOps"),
    ("Offline", "Scuba diving, climbing, badminton"),
]
static = os.environ.get("STATIC")
W, H, PORTRAIT_X, INFO_X = 860, 450, 24, 404


def row(i, k, v):
    y, d = 102 + i * 26, f'style="animation-delay:{i * 250}ms"'
    sub = k.startswith("└")
    if not k:  # thesis sub-line under its degree
        return f'<text class="l" x="{INFO_X + 24}" y="{y}" {d} fill="#8b949e">{escape(v)}</text>'
    key = (
        f'<tspan fill="#8b949e">└ </tspan><tspan fill="#39d353">{k[2:]}</tspan>'
        if sub
        else f'<tspan fill="#39d353">{k}</tspan>'
    )
    val = (
        f'<tspan fill="#8b949e">: </tspan><tspan fill="#c9d1d9">{escape(v)}</tspan>'
        if v
        else ""
    )
    return f'<text class="l" x="{INFO_X + 24 if sub else INFO_X}" y="{y}" {d}>{key}{val}</text>'


rows = "".join(row(i, k, v) for i, (k, v) in enumerate(LINES))
portrait = "".join(
    re.findall(
        r'<text class="r".*?</text>', Path("img/avi-ascii.svg").read_text(), re.DOTALL
    )
)
anim = (
    ""
    if static
    else ".l{animation:in .4s cubic-bezier(.16,1,.3,1) backwards}.r{animation:w .9s steps(24) backwards}"
    "@keyframes in{from{opacity:0;transform:translateX(-8px)}}@keyframes w{from{clip-path:inset(0 100% 0 0)}}"
    "@media (prefers-reduced-motion:reduce){.l,.r{animation:none}}"
)
Path("img/whoami.svg").write_text(
    f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" font-family="monospace" font-size="14">
<title>whoami: Artur Komaristych</title>
<style>.r{{white-space:pre}}{anim}</style>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="8" fill="#0d1117" stroke="#30363d"/>
<path d="M.5 32V8.5a8 8 0 0 1 8-8h{W - 17}a8 8 0 0 1 8 8V32z" fill="#161b22"/>
<circle cx="18" cy="16" r="5" fill="#ff5f56"/><circle cx="36" cy="16" r="5" fill="#ffbd2e"/><circle cx="54" cy="16" r="5" fill="#27c93f"/>
<g transform="translate({PORTRAIT_X},48)" font-size="7.6" fill="#c9d1d9">{portrait}</g>
{rows}
</svg>"""
)

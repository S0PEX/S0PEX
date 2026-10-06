import os
from html import escape
from pathlib import Path

LINES = [
    ("Name", "Artur Komaristych"),
    ("Now", "Software Developer @ Infolytics AG"),
    ("M.Sc.", "Computer Science @ Uni Cologne, 2025, honors"),
    ("", "└ Master Thesis @ DLR"),
    ("B.Sc.", "Computer Science @ RWTH Aachen, 2022"),
    ("", "└ Bachelor Thesis @ Fraunhofer IPT"),
    ("Stack", "Java, C#, TypeScript, C++, Python"),
    ("Infra", "Kubernetes, Docker, Proxmox, Ansible"),
    ("Cloud", "Google Compute Engine, Oracle Cloud"),
    ("Focus", "Distributed systems, backend, DevOps"),
    ("Offline", "Badminton, bouldering, outdoors"),
]
static = os.environ.get("STATIC")


def row(i, k, v):
    y, d = 76 + i * 28, f'style="animation-delay:{i * 250}ms"'
    if not k:  # thesis sub-line under its degree
        return f'<text class="l" x="48" y="{y}" {d} fill="#8b949e">{escape(v)}</text>'
    return (
        f'<text class="l" x="24" y="{y}" {d}><tspan fill="#39d353">{k}</tspan>'
        f'<tspan fill="#8b949e">: </tspan><tspan fill="#c9d1d9">{escape(v)}</tspan></text>'
    )


rows = "".join(row(i, k, v) for i, (k, v) in enumerate(LINES))
anim = (
    ""
    if static
    else ".l{opacity:0;transform:translateX(-8px);animation:in .4s ease-out forwards}@keyframes in{to{opacity:1;transform:none}}"
)
Path("img/info-card.svg").write_text(
    f"""<svg xmlns="http://www.w3.org/2000/svg" width="490" height="386" font-family="monospace" font-size="14">
<style>.l{{}}{anim}</style>
<rect width="100%" height="100%" rx="8" fill="#0d1117"/>
<rect width="100%" height="32" rx="8" fill="#161b22"/>
<circle cx="18" cy="16" r="5" fill="#ff5f56"/><circle cx="36" cy="16" r="5" fill="#ffbd2e"/><circle cx="54" cy="16" r="5" fill="#27c93f"/>
{rows}
</svg>"""
)

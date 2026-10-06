"""Render the Experience, Education, Stack and Offline sections as SVG (GitHub strips CSS/JS from README)."""

import os
from html import escape
from pathlib import Path
from textwrap import wrap

W = 860
BG, LINE, TEXT, MUTED, ACCENT = "#0d1117", "#30363d", "#c9d1d9", "#8b949e", "#39d353"
SANS = "-apple-system,'Segoe UI',Helvetica,Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"
NODE_X, TEXT_X, WRAP = 176, 204, 78

STYLE = f"""<style>
text{{font-family:{SANS};fill:{TEXT}}}
.m{{font-family:{MONO};fill:{MUTED}}}
.d{{fill:{MUTED}}}
.h{{font-weight:600;font-size:16px;fill:#f0f6fc}}
.b{{font-size:14px}}
.a{{{"" if os.environ.get("STATIC") else "animation:in .7s cubic-bezier(.16,1,.3,1) backwards"}}}
@keyframes in{{from{{opacity:0;transform:translateY(8px)}}}}
@media (prefers-reduced-motion:reduce){{.a{{animation:none}}}}
</style>"""


def star(text):
    """Bold the footnote asterisk."""
    return escape(text).replace("*", '<tspan font-weight="700">*</tspan>')


def svg(h, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" role="img">'
        f"<title>{escape(title)}</title>{STYLE}"
        f'<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="8" fill="{BG}" stroke="{LINE}"/>{body}</svg>'
    )


def timeline(items):
    """items: (period lines, role, place, bullets). Returns (height, body)."""
    y, out, nodes = 40, [], []
    for i, (period, role, place, bullets) in enumerate(items):
        top, rows = y, []
        delay = f'style="animation-delay:{i * 180}ms"'
        if period:
            rows.append(
                f'<text class="m" x="{NODE_X - 24}" y="{y + 5}" text-anchor="end" font-size="12">{escape(" - ".join(period))}</text>'
            )
        rows.append(
            f'<text class="h" x="{TEXT_X}" y="{y + 5}">{escape(role)}'
            f'<tspan class="d" font-weight="400" font-size="14"> {escape(place)}</tspan></text>'
        )
        y += 30
        for b in bullets:
            text, subs = b if isinstance(b, tuple) else (b, [])
            for indent, item in [(0, text)] + [(1, t) for t in subs]:
                for k, line in enumerate(wrap(item, WRAP - indent * 6)):
                    if k == 0:
                        rows.append(
                            f'<circle cx="{TEXT_X + 3 + indent * 18}" cy="{y - 4}" r="{2 - indent * 0.5}" fill="{MUTED}"/>'
                        )
                    rows.append(
                        f'<text class="b" x="{TEXT_X + 16 + indent * 18}" y="{y}">{star(line)}</text>'
                    )
                    y += 21
                y += 4
        nodes.append((top + 1, i == 0))
        out.append(f'<g class="a" {delay}>{"".join(rows)}</g>')
        y += 22
    bottom = y - 22
    spine = f'<line x1="{NODE_X}" y1="{nodes[0][0]}" x2="{NODE_X}" y2="{nodes[-1][0]}" stroke="{LINE}" stroke-width="2"/>'
    dots = "".join(
        f'<circle cx="{NODE_X}" cy="{cy}" r="6" fill="{ACCENT if first else BG}" stroke="{ACCENT if first else MUTED}" stroke-width="2"/>'
        for cy, first in nodes
    )
    return bottom + 40, spine + dots + "".join(out)


def chips(groups):
    y, out = 40, []
    for i, (label, names) in enumerate(groups):
        x = TEXT_X - 28
        parts = [
            f'<text class="m" x="{NODE_X - 24}" y="{y + 18}" text-anchor="end" font-size="12">{escape(label)}</text>'
        ]
        for n in names:
            w = round(len(n) * 7.6 + 24)
            if x + w > W - 24:
                x, y = TEXT_X - 28, y + 36
            parts.append(
                f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="6" fill="#161b22" stroke="{LINE}"/>'
                f'<text class="b" x="{x + w / 2}" y="{y + 18}" text-anchor="middle" font-size="13">{escape(n)}</text>'
            )
            x += w + 8
        out.append(
            f'<g class="a" style="animation-delay:{i * 120}ms">{"".join(parts)}</g>'
        )
        y += 50
    return y - 14, "".join(out)


EXPERIENCE = [
    (
        ["2026", "present"],
        "Senior Software Developer",
        "Infolytics AG",
        [
            "Technical owner of three business domains of a live public-sector platform (Spring Boot, Angular, OpenShift) where applications are submitted and processed by caseworkers",
            "End-to-end responsibility for these domains: architecture, delivery, operations and direct customer contact",
            "Still active on SDF, the Infolytics signal data platform: feature development and consulting",
            "Mentor junior developers and working students",
        ],
    ),
    (
        ["2022", "2026"],
        "Software Developer",
        "Infolytics AG",
        [
            "Continued developing SDF alongside new responsibilities",
            "Led the migration of the SDF frontend applications from jQuery to Angular, and of the backend from MaxDB to PostgreSQL including all existing data, with no downtime",
            "Tracked down hard production issues (memory leaks, network protocol bugs) and shipped the fixes",
            "Replaced manual deploys with GitOps on Kubernetes and Argo CD",
        ],
    ),
    (
        ["2018", "2022"],
        "Working Student",
        "Infolytics AG",
        [
            "Developed the Java client library for the native TCP protocol of SDF, the signal data platform behind WiValdi*, a DLR wind research project with 2,000+ sensors. Also worked on the C++ backend",
            "Other Java projects: optimization and maintenance",
            "Hired full-time right after the B.Sc.",
        ],
    ),
]

EDUCATION = [
    (
        ["2023", "2026"],
        "M.Sc. Computer Science, with honors",
        "University of Cologne",
        [
            "Focus areas: Software-Intensive Systems and High-Performance Computing",
            (
                'Master thesis at the German Aerospace Center (DLR), Distributed Software Systems group: "A Unifying Framework for Provisioning and Executing Computational Tools across Heterogeneous Computing Environments"',
                [
                    "Designed a coordinator-worker architecture and implemented a prototype that unifies tool execution across heterogeneous computing environments (Kubernetes, Slurm, native Linux, Windows) behind a single REST API*",
                    "In production use at DLR, open source release planned",
                ],
            ),
            "Member of the faculty selection committee",
        ],
    ),
    (
        ["2018", "2022"],
        "B.Sc. Computer Science",
        "RWTH Aachen University",
        [
            "Minor in Business Administration",
            (
                'Bachelor thesis at Fraunhofer IPT: "Development and Deployment of a Cloud-Based System Architecture for Domain-Specific AutoML Systems"',
                [
                    "Migrated an AutoML pipeline to Kubernetes (Oracle OKE) and built a cloud-native architecture with a NestJS backend and ReactJS frontend",
                ],
            ),
        ],
    ),
    (
        ["2015", "2018"],
        "IT Assistant with A-levels",
        "Georg-Simon-Ohm-Berufskolleg",
        [
            "School-based vocational training in Germany (schulische Ausbildung) in programming, networking and more, completed together with the Abitur (German A-levels)"
        ],
    ),
]

STACK = [
    ("Languages", ["Java", "C#", "TypeScript", "C++", "Python"]),
    (
        "Frameworks",
        ["Spring Boot", "ASP.NET Core", "NestJS", "Angular", "React", "Next.js"],
    ),
    (
        "Infrastructure",
        [
            "Kubernetes",
            "OpenShift",
            "Docker",
            "Helm",
            "Argo CD",
            "Proxmox VE",
            "Ansible",
            "GitLab CI",
            "GitHub Actions",
        ],
    ),
    ("Cloud", ["Google Compute Engine", "Oracle Cloud Infrastructure"]),
    (
        "Data",
        [
            "PostgreSQL",
            "MySQL",
            "MariaDB",
            "JPA",
            "Hibernate",
            "Entity Framework",
            "Drizzle",
        ],
    ),
]


# Material Design Icons (Apache 2.0) via Iconify, one family for all three
ICONS = {
    "diving-scuba": [
        "M1 13c0-1.1.9-2 2-2s2 .9 2 2s-.9 2-2 2s-2-.9-2-2m7.89-2.89l4.53-1.21l-.78-2.9l-4.53 1.21c-.8.21-1.28 1.04-1.06 1.84s1.04 1.28 1.84 1.06M20.5 5.9L23 3l-1-1l-3 3l-2 4l-9.5 2.87c-.8.2-1.37.89-1.5 1.68L5.24 18L2.4 21.8L4 23l3-4l1.14-3.14L14 14l5-3.5z"
    ],
    "carabiner": [
        "M8 17.5c0 .83-.67 1.5-1.5 1.5S5 18.33 5 17.5S5.67 16 6.5 16s1.5.67 1.5 1.5M18 5.59C17.79 3.54 16.18 2 14.24 2H8.88C6.95 2 5.36 3.5 5.15 5.53L5 6.59C4.92 7.34 5.5 8 6.24 8c.63 0 1.15-.47 1.23-1.09l.14-1.09c.07-.75.62-1.32 1.27-1.32h5.36c.65 0 1.2.57 1.26 1.32l1 11.06c.09.86-.5 1.62-1.25 1.62l-5.21-.68a3.46 3.46 0 0 1-1.24 2.36l6.13.82h.32c1.02 0 2.01-.44 2.71-1.22A4.22 4.22 0 0 0 19 16.65zm-6.34 2.35c-.58-.37-1.35-.19-1.72.4L6.39 14h.11c.88 0 1.68.34 2.3.88l3.26-5.22c.37-.58.19-1.35-.4-1.72"
    ],
    "badminton": [
        "M12.3 2c-.97.03-1.72.84-1.69 1.8c.01.24.06.47.16.7l.29.64c.04.13-.03.27-.17.31c-.09.05-.19 0-.26-.08l-.42-.55c-.33-.42-.83-.68-1.36-.69c-.97-.02-1.77.75-1.79 1.71c-.01.42.13.82.39 1.16l.42.5h.01c.08.13.05.29-.06.37c-.09.07-.21.07-.29 0L7 7.45c-.34-.26-.75-.4-1.16-.39c-.96.02-1.73.82-1.71 1.79c.01.53.27 1.03.69 1.36l.57.44c.11.1.11.26-.01.35a.23.23 0 0 1-.26.05h-.01l-.61-.28c-.23-.09-.46-.15-.7-.16c-.96-.03-1.77.73-1.8 1.7c0 .72.4 1.38 1.06 1.66l11.39 5.07l4.59-4.59l-5.07-11.39C13.69 2.39 13 1.97 12.3 2m.83 4.1c.42-.01.8.23.96.61l3.05 6.84l-3.95-3.94l-.93-2.11c-.3-.63.16-1.38.87-1.4M9.85 8.85c.27 0 .52.1.71.3l4.81 4.81c.4.38.41 1.01.03 1.41c-.4.4-1.02.41-1.44 0l-4.81-4.81a.987.987 0 0 1-.02-1.41c.19-.2.45-.3.72-.3m-2.72 3.32c.13 0 .27.04.37.09l2.13.94l3.94 3.94l-6.86-3.05c-1.02-.44-.68-1.95.42-1.92m13.15 3.87l-4.24 4.24l.85.85c.76.75 1.86 1.04 2.89.77a3.02 3.02 0 0 0 2.12-2.12c.27-1.03-.02-2.13-.77-2.89z"
    ],
}

OFFLINE = [
    ("diving-scuba", "Scuba diving"),
    ("carabiner", "Bouldering and climbing"),
    ("badminton", "Badminton"),
]


def offline():
    cols, parts = 3, []
    for i, (icon, label) in enumerate(OFFLINE):
        cx = W / cols * (i + 0.5)
        paths = "".join(f'<path d="{d}"/>' for d in ICONS[icon])
        parts.append(
            f'<g class="a" style="animation-delay:{i * 150}ms">'
            f'<g transform="translate({cx - 30},28) scale(2.5)" fill="{ACCENT}">{paths}</g>'
            f'<text class="h" x="{cx}" y="118" text-anchor="middle" font-size="15">{escape(label)}</text></g>'
        )
        if i:
            x = W / cols * i
            parts.append(f'<line x1="{x}" y1="30" x2="{x}" y2="122" stroke="{LINE}"/>')
    return 150, "".join(parts)


def bullet_md(b):
    text, subs = b if isinstance(b, tuple) else (b, [])
    bold = lambda t: t.replace("*", "<b>*</b>")  # bold asterisk, flanking-rule safe
    return "\n".join([f"- {bold(text)}"] + [f"  - {bold(t)}" for t in subs])


NOTES = {
    "experience": "* WiValdi (also called DFWind) is a DLR research project. I worked on SDF, the Infolytics signal data platform it runs on, not on WiValdi itself.",
    "education": "* Tools are described in a declarative YAML specification (name, version, typed inputs and outputs, runtime). Workers parse it and register their tools with the central coordinator. Its REST API lists the registered tools and accepts jobs with binary or primitive inputs. Each job is scheduled onto a suitable worker, which stages the artifacts, executes the task and uploads the results. Failed jobs are retried, and users follow job progress through real-time events instead of polling.",
}


def with_note(h, body, text):
    """Append a footnote under a timeline. Returns (height, body)."""
    lines, y0 = wrap(text, 80), h - 40 + 24
    note = "".join(
        f'<text class="m" x="{TEXT_X}" y="{y0 + i * 17}" font-size="12">{star(t)}</text>'
        for i, t in enumerate(lines)
    )
    return y0 + 17 * (len(lines) - 1) + 24, body + note


def plain_text():
    """Same content as the SVGs, as markdown for search engines and copy/paste."""

    def block(items):
        return "\n\n".join(
            f"**{role}**, {place}{f' ({period[0]} to {period[1]})' if len(period) > 1 else f' ({period[0]})' if period else ''}\n\n"
            + "\n".join(bullet_md(b) for b in bullets)
            for period, role, place, bullets in items
        )

    stack = "\n".join(f"- **{g}:** {', '.join(n)}" for g, n in STACK)
    return (
        "<details>\n<summary>Plain text version</summary>\n\n"
        f"#### Experience\n\n{block(EXPERIENCE)}\n\n<b>*</b> {NOTES['experience'][2:]}\n\n"
        f"#### Stack\n\n{stack}\n\n"
        f"#### Education\n\n{block(EDUCATION)}\n\n<b>*</b> {NOTES['education'][2:]}\n\n</details>"
    )


def inject_readme():
    start, end = "<!-- plain-text:start -->", "<!-- plain-text:end -->"
    text = Path("README.md").read_text()
    head, found, rest = text.partition(start)
    _, found_end, tail = rest.partition(end)
    assert found and found_end, "plain-text markers missing in README.md"
    Path("README.md").write_text(f"{head}{start}\n{plain_text()}\n{end}{tail}")


if __name__ == "__main__":
    h, body = with_note(*timeline(EXPERIENCE), NOTES["experience"])
    Path("img/experience.svg").write_text(svg(h, body, "Experience at Infolytics AG"))
    h, body = with_note(*timeline(EDUCATION), NOTES["education"])
    Path("img/education.svg").write_text(svg(h, body, "Education"))
    h, body = offline()
    Path("img/offline.svg").write_text(
        svg(
            h,
            body,
            "Away from the keyboard: scuba diving, bouldering and climbing, badminton",
        )
    )
    h, body = chips(STACK)
    Path("img/stack.svg").write_text(svg(h + 26, body, "Tech stack"))
    inject_readme()

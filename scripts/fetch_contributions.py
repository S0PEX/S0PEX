import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup

USER = "S0PEX"
html = requests.get(f"https://github.com/users/{USER}/contributions", timeout=30).text
soup = BeautifulSoup(html, "html.parser")
tips = {t["for"]: t.text for t in soup.find_all("tool-tip")}
days = []
for td in soup.select("td.ContributionCalendar-day[data-date]"):
    m = re.match(r"(\d+)", tips.get(td["id"], ""))
    days.append(
        {
            "date": td["data-date"],
            "level": int(td["data-level"]),
            "count": int(m[1]) if m else 0,
        }
    )
days.sort(key=lambda d: d["date"])

longest = cur = 0
for d in days:
    cur = cur + 1 if d["count"] else 0
    longest = max(longest, cur)
streak = 0
for d in reversed(days):
    if d["count"]:
        streak += 1
    elif d is not days[-1]:
        break  # today may still be empty
Path("data/contributions.json").write_text(
    json.dumps(
        {
            "days": days,
            "total": sum(d["count"] for d in days),
            "current_streak": streak,
            "longest_streak": longest,
            "best_day": max(d["count"] for d in days),
        },
        indent=1,
    )
)

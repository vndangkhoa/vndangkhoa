import json, re, os, urllib.request, datetime

# Configuration
USER = "vndangkhoa"
TOKEN = os.environ.get("GITHUB_TOKEN", "")

# Birthdate: Defaults to 1993-01-01 (Adjust to your exact date if desired)
BIRTH_YEAR = int(os.environ.get("BIRTH_YEAR", 1993))
BIRTH_MONTH = int(os.environ.get("BIRTH_MONTH", 1))
BIRTH_DAY = int(os.environ.get("BIRTH_DAY", 1))

def calculate_uptime(born_date: datetime.date) -> str:
    today = datetime.date.today()
    years = today.year - born_date.year
    months = today.month - born_date.month
    days = today.day - born_date.day

    if days < 0:
        months -= 1
        # days in previous month
        prev_month = today.month - 1 or 12
        prev_year = today.year if today.month > 1 else today.year - 1
        days_in_prev = (datetime.date(today.year, today.month, 1) - datetime.date(prev_year, prev_month, 1)).days
        days += days_in_prev

    if months < 0:
        years -= 1
        months += 12

    y_unit = "year" if years == 1 else "years"
    m_unit = "month" if months == 1 else "months"
    d_unit = "day" if days == 1 else "days"

    return f"{years} {y_unit}, {months} {m_unit}, {days} {d_unit}"

def fetch_user_stats() -> dict:
    req = urllib.request.Request(
        f"https://api.github.com/users/{USER}",
        headers={"Authorization": f"Bearer {TOKEN}"} if TOKEN else {"User-Agent": "vndangkhoa-stats"}
    )
    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode())
            return {
                "repos": data.get("public_repos", 17),
                "followers": data.get("followers", 6),
                "following": data.get("following", 2),
            }
    except Exception as e:
        print(f"Warning: Failed to fetch live GitHub stats: {e}")
        return {"repos": 17, "followers": 6, "following": 2}

def update_svg(svg_path: str = "assets/terminal.svg"):
    if not os.path.exists(svg_path):
        print(f"Error: {svg_path} not found")
        return

    with open(svg_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Uptime
    uptime_str = calculate_uptime(datetime.date(BIRTH_YEAR, BIRTH_MONTH, BIRTH_DAY))
    content = re.sub(
        r'(<tspan class="key">Uptime:\s*</tspan><tspan class="val">)(.*?)(</tspan>)',
        rf'\g<1>{uptime_str}\g<3>',
        content
    )

    # 2. Update GitHub Stats
    stats = fetch_user_stats()
    stats_str = f"Repos: {stats['repos']} | Followers: {stats['followers']} | Following: {stats['following']}"
    content = re.sub(
        r'(<tspan class="key">Git(Hub)? Stats:\s*</tspan><tspan class="val">)(.*?)(</tspan>)',
        rf'\g<1>{stats_str}\g<3>',
        content
    )

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Successfully updated {svg_path} with Uptime: '{uptime_str}' and Stats: '{stats_str}'")

if __name__ == "__main__":
    svg_file = os.path.join(os.path.dirname(__file__), "../../assets/terminal.svg")
    if not os.path.exists(svg_file):
        svg_file = "assets/terminal.svg"
    update_svg(svg_file)

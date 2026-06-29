import json, re, os, urllib.request

TOKEN = os.environ.get("GITHUB_TOKEN", "")
USER = "vndangkhoa"

# Fetch repos sorted by pushed date
req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?sort=pushed&direction=desc&per_page=10",
    headers={"Authorization": f"Bearer {TOKEN}"} if TOKEN else {}
)
resp = urllib.request.urlopen(req)
repos = json.loads(resp.read())

# Find the latest non-profile repo
latest_name, latest_desc, latest_url = None, None, None
for r in repos:
    if r["name"] == USER:
        continue
    latest_name = r["name"]
    latest_desc = r.get("description") or "No description"
    latest_url = r["html_url"]
    break

if not latest_name:
    print("No repos found")
    exit(0)

# Update README
with open("README.md", "r") as f:
    content = f.read()

start = "<!-- LATEST_REPO:START -->"
end = "<!-- LATEST_REPO:END -->"
replacement = f'{start}\n🔭 Currently building <a href="{latest_url}"><b>{latest_name}</b></a> — {latest_desc}\n{end}'

new_content = re.sub(
    re.escape(start) + ".*?" + re.escape(end),
    replacement,
    content,
    flags=re.DOTALL,
)

with open("README.md", "w") as f:
    f.write(new_content)

print(f"Updated to: {latest_name}")

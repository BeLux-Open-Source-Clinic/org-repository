import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

org = data["data"]["organization"]
repos = org["repositories"]["nodes"]
members = org["membersWithRole"]["nodes"]

# ✅ Organization-Wide Metrics
readme_content = "# 🚀 Organization-Wide Metrics\n\n"
readme_content += "| Repository | ⭐ Stars | 🍴 Forks | ✅ Merged PRs | 🐞 Closed Issues |\n"
readme_content += "|------------|----------|-----------|-----------------|-----------------|\n"

for repo in repos:
    name = repo['name']
    stars = repo['stargazers']['totalCount']
    forks = repo['forks']['totalCount']
    merged_prs = repo['pullRequests']['totalCount']
    closed_issues = repo['issues']['totalCount']

    readme_content += f"| [{name}](https://github.com/<YOUR_ORG_NAME>/{name}) "
    readme_content += f"| {stars} | {forks} | {merged_prs} | {closed_issues} |\n"

# ✅ Dynamic Contributor Leaderboard
readme_content += "\n## 🏆 Contributor Leaderboard (Updated Daily)\n\n"
readme_content += "| Rank | Contributor | ✅ PRs Merged | 🐞 Issues Closed |\n"
readme_content += "|------|------------|--------------|----------------|\n"

# Sort members by highest contributions (PRs + Issues Closed)
sorted_members = sorted(
    members, 
    key=lambda m: (
        m["contributionsCollection"]["totalPullRequestContributions"] +
        m["contributionsCollection"]["totalIssueContributions"]
    ), reverse=True
)[:10]  # Top 10 contributors

for idx, member in enumerate(sorted_members, 1):
    login = member['login']
    cc = member['contributionsCollection']
    prs = cc['totalPullRequestContributions']
    closed_issues = cc['totalIssueContributions']

    readme_content += f"| {idx} | [@{login}](https://github.com/{login}) | {prs} | {closed_issues} |\n"

# ✅ Dynamic Metrics Table (Generated from Data)
readme_content += "\n## 📊 Organization Metrics\n\n"
readme_content += "| 🚀 Organization Stats | 🌍 Contributors |\n"
readme_content += "|----------------------|----------------|\n"
readme_content += f"| ![Stars](https://img.shields.io/github/stars/<YOUR_ORG>/<REPO>) "
readme_content += f"| ![Total Contributors](https://img.shields.io/github/contributors/<YOUR_ORG>/<REPO>) |\n"
readme_content += f"| ![Closed PRs](https://img.shields.io/github/issues-pr-closed-raw/<YOUR_ORG>/<REPO>) "
readme_content += f"| ![Closed Issues](https://img.shields.io/github/issues-closed/<YOUR_ORG>/<REPO>) |\n"

# ✅ Write to README file
with open("README.md", "w") as f:
    f.write(readme_content)


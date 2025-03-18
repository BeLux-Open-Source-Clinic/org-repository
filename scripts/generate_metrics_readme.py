import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

org = data["data"]["organization"]
repos = org["repositories"]["nodes"]
members = org["membersWithRole"]["nodes"]

# ✅ Determine the most active repository (Stars + PRs + Forks)
top_repo = next((repo for repo in repos if repo["stargazers"]["totalCount"] > 0), repos[0])
top_repo_name = top_repo["name"]

# ✅ Count Total PRs Merged & Issues Closed
total_prs_merged = sum(repo["pullRequests"]["totalCount"] for repo in repos)
total_issues_closed = sum(repo["issues"]["totalCount"] for repo in repos)

# Ensure contributions are scoped to the organization repositories
org_repo_names = {repo["name"] for repo in repos}  # Set for fast lookup

# Find the top contributor based on contributions within the organization
top_contributor = max(
    members,
    key=lambda m: sum(
        contrib["pullRequestContributions"]["totalCount"]
        + contrib["issueContributions"]["totalCount"]
        for contrib in m.get("contributionsCollection", {}).get("repositoryContributions", [])
        if contrib["repository"]["name"] in org_repo_names
    ),
    default=None
)

top_contributor_name = top_contributor["login"] if top_contributor else "No Contributor"

# ✅ Calculate Engagement Score (Total PRs, Issues, Stars, Contributions)
engagement_score = sum(
    repo["stargazers"]["totalCount"] + repo["pullRequests"]["totalCount"] + repo["issues"]["totalCount"]
    for repo in repos
)

# ✅ PRs vs Issues Trend
prs_vs_issues = "📈 PRs Leading" if total_prs_merged > total_issues_closed else "🐞 More Issues Closed"

# ✅ Organization-Wide Metrics Table
readme_content = "# 🚀 Organization-Wide Metrics\n\n"
readme_content += "| Repository | ⭐ Stars | 🍴 Forks | ✅ Merged PRs | 🐞 Closed Issues |\n"
readme_content += "|------------|----------|-----------|-----------------|-----------------|\n"

for repo in repos:
    name = repo["name"]
    stars = repo["stargazers"]["totalCount"]
    forks = repo["forks"]["totalCount"]
    merged_prs = repo["pullRequests"]["totalCount"]
    closed_issues = repo["issues"]["totalCount"]

    readme_content += f"| [{name}](https://github.com/BeLux-Open-Source-Clinic/{name}) "
    readme_content += f"| {stars} | {forks} | {merged_prs} | {closed_issues} |\n"

# ✅ Top Contributors Leaderboard
readme_content += "\n## 🏆 Contributor Leaderboard (Updated Daily)\n\n"
readme_content += "| Rank | Contributor | ✅ PRs Merged | 🐞 Issues Closed |\n"
readme_content += "|------|------------|--------------|----------------|\n"

sorted_members = sorted(
    members, 
    key=lambda m: (
        m["contributionsCollection"]["totalPullRequestContributions"] +
        m["contributionsCollection"]["totalIssueContributions"]
    ), reverse=True
)[:10]  # Top 10 contributors

for idx, member in enumerate(sorted_members, 1):
    login = member["login"]
    cc = member["contributionsCollection"]
    prs = cc["totalPullRequestContributions"]
    closed_issues = cc["totalIssueContributions"]

    readme_content += f"| {idx} | [@{login}](https://github.com/{login}) | {prs} | {closed_issues} |\n"

# ✅ Revamped Organization Metrics Table
readme_content += "\n## 📊 Organization Insights\n\n"
readme_content += "| 🔹 Metric | 📊 Value |\n"
readme_content += "|----------------------|------------------|\n"
readme_content += f"| 🏆 **Top Contributor** | [@{top_contributor_name}](https://github.com/{top_contributor_name}) |\n"
readme_content += f"| 🚀 **Most Active Repo** | [{top_repo_name}](https://github.com/BeLux-Open-Source-Clinic/{top_repo_name}) |\n"
readme_content += f"| 🔄 **PRs vs Issues Trend** | {prs_vs_issues} |\n"
readme_content += f"| 💡 **Engagement Score** | {engagement_score} |\n"

# ✅ Improved Badge Display with Dynamic Repo
readme_content += "\n## 📊 Dynamic Organization Badges for Top Repo\n\n"
readme_content += "| 🚀 Stars | 🌍 Contributors | ✅ PRs Closed | 🐞 Issues Closed |\n"
readme_content += "|----------|----------------|---------------|-----------------|\n"
readme_content += f"| ![Stars](https://img.shields.io/github/stars/BeLux-Open-Source-Clinic/{top_repo_name}?style=for-the-badge) "
readme_content += f"| ![Contributors](https://img.shields.io/github/contributors/BeLux-Open-Source-Clinic/{top_repo_name}?style=for-the-badge) "
readme_content += f"| ![PRs Closed](https://img.shields.io/github/issues-pr-closed-raw/BeLux-Open-Source-Clinic/{top_repo_name}?style=for-the-badge) "
readme_content += f"| ![Issues Closed](https://img.shields.io/github/issues-closed/BeLux-Open-Source-Clinic/{top_repo_name}?style=for-the-badge) |\n"

# ✅ Write Updated README
with open("README.md", "w") as f:
    f.write(readme_content)

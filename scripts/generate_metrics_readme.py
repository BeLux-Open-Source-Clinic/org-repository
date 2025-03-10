import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

org = data["data"]["organization"]
repos = org["repositories"]["nodes"]
members = org["membersWithRole"]["nodes"]

# ✅ Organization-wide metrics
print("# 🚀 Organization-Wide Metrics\n")
print("| Repository | ⭐ Stars | 🍴 Forks | ✅ Merged PRs | 🐞 Closed Issues |")
print("|------------|----------|-----------|-----------------|-----------------|")

for repo in repos:
    name = repo['name']
    stars = repo['stargazers']['totalCount']
    forks = repo['forks']['totalCount']
    merged_prs = repo['pullRequests']['totalCount']
    closed_issues = repo['issues']['totalCount']

    print(f"| [{name}](https://github.com/BeLux-Open-Source-Clinic/{name}) "
          f"| {stars} | {forks} | {merged_prs} | {closed_issues} |")

# ✅ Top Contributors
print("\n# 🥇 Top Contributors\n")
print("| Rank | Contributor | Commits | PR Reviews | PRs Opened | Issues Created | Issues Closed |")
print("|------|-------------|---------|------------|------------|-----------------|-----------------|")

# Sort members by highest contributions (Commits + PR Reviews + PRs + Issues)
sorted_members = sorted(
    members, 
    key=lambda m: (
        m["contributionsCollection"]["totalCommitContributions"] +
        m["contributionsCollection"]["totalPullRequestReviewContributions"] +
        m["contributionsCollection"]["totalPullRequestContributions"] +
        m["contributionsCollection"]["totalIssueContributions"]
    ), reverse=True
)[:10]  # Top 10 contributors

for idx, member in enumerate(sorted_members, 1):
    login = member['login']
    cc = member['contributionsCollection']
    commits = cc['totalCommitContributions']
    reviews = cc['totalPullRequestReviewContributions']
    prs = cc['totalPullRequestContributions']
    issues = cc['totalIssueContributions']
    closed_issues = cc['totalIssueContributions']  # Using same field for now

    print(f"| {idx} "
          f"| [{login}](https://github.com/{login}) "
          f"| {commits} | {reviews} | {prs} | {issues} | {closed_issues} |")

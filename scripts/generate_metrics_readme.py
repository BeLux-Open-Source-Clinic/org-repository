import json
import sys

with open(sys.argv[1]) as f:
    data = json.load(f)

repos = data["data"]["organization"]["repositories"]["nodes"]

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

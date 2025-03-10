import json, sys

data = json.load(open(sys.argv[1]))

repos = data["data"]["organization"]["repositories"]["nodes"]

print("# 🚀 Organization-Wide Metrics\n")
print("| Repo | ⭐ Stars | 🍴 Forks | 🔍 Watchers | ✅ Merged PRs | 🐞 Closed Issues |")
print("|------|----------|----------|--------------|----------------|------------------|")

for repo in repos:
    print(f"| [{repo['name']}](https://github.com/BeLux-Open-Source-Clinic/{repo['name']}) "
          f"| {repo['stargazers']['totalCount']} "
          f"| {repo['forks']['totalCount']} "
          f"| {repo['watchers']['totalCount']} "
          f"| {repo['pullRequests']['totalCount']} "
          f"| {repo['issues']['totalCount']} |")

# 🚀 Organization-Wide Metrics

| Repository | ⭐ Stars | 🍴 Forks | ✅ Merged PRs | 🐞 Closed Issues |
|------------|----------|-----------|-----------------|-----------------|
{% for repo in repos %}
| [{{ repo.name }}](https://github.com/BeLux-Open-Source-Clinic/{{ repo.name }}) | {{ repo.stargazers.totalCount }} | {{ repo.forks.totalCount }} | {{ repo.pullRequests.totalCount }} | {{ repo.issues.totalCount }} |
{% endfor %}

---

## 🎖️ Contributor Leaderboard (Updated Daily)

| 🏆 Rank | 👤 Contributor | ✅ PRs Merged | 🐞 Issues Closed | 📌 Commits |
|--------|--------------|--------------|----------------|----------|
{% for contributor in top_contributors %}
| {{ loop.index }} | [@{{ contributor.login }}](https://github.com/{{ contributor.login }}) | {{ contributor.pullRequests.totalCount }} | {{ contributor.issues.totalCount }} | {{ contributor.commits.totalCount }} |
{% endfor %}

---

## 📊 Organization Stats & Dynamic Badges

| 🌟 Stars | 🍴 Forks | 🚀 PRs Merged | 🐞 Issues Closed |
|----------------------|----------------|----------------|----------------|
| ![Stars](https://img.shields.io/github/stars/BeLux-Open-Source-Clinic/{{ top_repo_name }}) | ![Forks](https://img.shields.io/github/forks/BeLux-Open-Source-Clinic/{{ top_repo_name }}) | ![Closed PRs](https://img.shields.io/github/issues-pr-closed-raw/BeLux-Open-Source-Clinic/{{ top_repo_name }}) | ![Closed Issues](https://img.shields.io/github/issues-closed/BeLux-Open-Source-Clinic/{{ top_repo_name }}) |

🔄 **Updated Daily via GitHub Actions**

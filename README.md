<h1 align="center">Jay Katta</h1>

<p align="center">
  <code>security engineer</code> · <code>supply chain</code> · <code>automation</code>
</p>

<p align="center">
  <a href="https://github.com/Jaykatta17?tab=repositories">
    <img src="https://img.shields.io/badge/repos-public-0f172a?style=flat-square&labelColor=0f172a" alt="Repos" />
  </a>
  <a href="https://github.com/Jaykatta17?tab=followers">
    <img src="https://img.shields.io/github/followers/Jaykatta17?style=flat-square&color=0f172a&labelColor=0f172a" alt="Followers" />
  </a>
</p>

```python
from dataclasses import dataclass, field


@dataclass
class SecurityEngineer:
    """Turns manual security review into tooling that scales."""

    name: str = "Jay Katta"
    handle: str = "@Jaykatta17"
    role: str = "Application & Supply Chain Security"

    languages: list = field(default_factory=lambda: [
        "Python",   # scanners, orchestration, reporting
        "Go",       # anything that has to be fast
        "Kotlin",   # when it needs a UI
        "Shell",    # the glue holding it together
    ])

    toolchain: list = field(default_factory=lambda: [
        "gitleaks", "grype", "syft", "trivy",
        "cyclonedx", "spdx", "cis-benchmarks",
    ])

    focus: dict = field(default_factory=lambda: {
        "secrets":      "detect before commit, not after breach",
        "sca_sbom":     "know every dependency you actually ship",
        "ai_security":  "threat modeling LLM endpoints",
        "scale":        "hundreds of repos, one pipeline",
    })

    def philosophy(self) -> str:
        return "If I have to do it twice, it becomes a scanner."

    def __str__(self) -> str:
        return f"{self.name} — {self.role}"
```

---

### 🚀 Projects

| Project | What it does | Stack |
| --- | --- | --- |
| [**project-trace**](https://github.com/Jaykatta17/project-trace) | Threat & Risk Assessment for Chain Evaluation of LLM endpoints | `Python` |
| [**gitleaks-scanner**](https://github.com/Jaykatta17/gitleaks-scanner) | Bulk secrets scanning across many Git repos, with XLSX + HTML reporting | `Python` `Gitleaks` |
| [**SCA-Bulk-Scanner**](https://github.com/Jaykatta17/SCA-Bulk-Scanner) | Batch software composition analysis powered by Grype and Syft | `Python` `Grype` `Syft` |
| [**gitlab-management-toolkit**](https://github.com/Jaykatta17/gitlab-management-toolkit) | Administration and auditing helpers for GitLab at scale | `Python` |

---

### 🧰 Stack

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white" alt="Go" />
  <img src="https://img.shields.io/badge/Kotlin-7F52FF?style=flat-square&logo=kotlin&logoColor=white" alt="Kotlin" />
  <img src="https://img.shields.io/badge/Shell-4EAA25?style=flat-square&logo=gnubash&logoColor=white" alt="Shell" />
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/GitLab%20CI-FC6D26?style=flat-square&logo=gitlab&logoColor=white" alt="GitLab CI" />
  <img src="https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" />
</p>

---

### 📊 Activity

<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Jaykatta17&bg_color=00000000&color=6e7781&line=0969da&point=0969da&area=true&area_color=0969da&title_color=0969da&hide_border=true&days=90" alt="Contribution activity graph" />
</p>

<p align="center">
  <img height="160" src="https://github-readme-stats.vercel.app/api?username=Jaykatta17&show_icons=true&hide_border=true&bg_color=00000000&title_color=0969da&icon_color=0969da&text_color=6e7781&count_private=true" alt="GitHub stats" />
  <img height="160" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Jaykatta17&layout=compact&hide_border=true&bg_color=00000000&title_color=0969da&text_color=6e7781&langs_count=6" alt="Top languages" />
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/Jaykatta17/Jaykatta17/output/snake.svg" alt="Contribution snake" />
</p>

---

### 🤝 Connect

<p>
  <a href="https://github.com/Jaykatta17">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <!-- Uncomment and fill in when you're ready:
  <a href="https://linkedin.com/in/YOUR-HANDLE">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="mailto:YOUR-EMAIL">
    <img src="https://img.shields.io/badge/Email-EA4335?style=flat-square&logo=gmail&logoColor=white" alt="Email" />
  </a>
  -->
</p>

<sub>💬 Always happy to talk supply chain security, scanner tuning, or AI security.</sub>

# Release Checklist

Use this checklist before publishing a release.

- [ ] `journal-formatting/SKILL.md` has valid frontmatter with `name` and `description`.
- [ ] No private manuscript text, user files, local paths, API keys, or personal notes are included.
- [ ] `README.md` installation instructions are current.
- [ ] `LICENSE` has the intended copyright holder and license.
- [ ] `journal-formatting/scripts/inspect_docx.py` compiles.
- [ ] `journal-formatting/scripts/inspect_docx.py --help` works.
- [ ] `journal-formatting/references/journal-packs/README.md` lists every bundled journal pack.
- [ ] Journal packs contain official source URLs and avoid unverified exact limits.
- [ ] The skill can be copied into `~/.codex/skills/journal-formatting`.
- [ ] Example prompts in `README.md` still match the skill behavior.
- [ ] A version tag is created, for example `v0.1.0`.

Suggested first release:

```bash
git tag v0.1.0
git push origin v0.1.0
```

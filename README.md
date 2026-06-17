# Journal Formatting Skill

`journal-formatting` is a Codex skill for formatting, auditing, and revising academic manuscripts against journal author guidelines, templates, and submission checklists.

It is designed for tasks such as:

- Formatting a manuscript for a named journal.
- Building a journal requirement table from author guidelines.
- Auditing a DOCX manuscript structure before submission.
- Checking title page, abstract, keywords, headings, figures, tables, references, declarations, and supporting information.
- Producing a formatted manuscript plus a concise compliance report.

## Repository Layout

```text
journal-formatting-skill-open-source/
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── RELEASE_CHECKLIST.md
└── journal-formatting/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    ├── references/
    │   ├── format-checklist.md
    │   └── journal-packs/
    │       ├── README.md
    │       ├── nature-portfolio.md
    │       ├── science-aaas.md
    │       ├── cell-press.md
    │       ├── wiley-materials.md
    │       ├── acs.md
    │       ├── elsevier.md
    │       ├── springer-nature-bmc.md
    │       ├── ieee.md
    │       ├── mdpi.md
    │       └── plos.md
    └── scripts/
        └── inspect_docx.py
```

## Installation

Copy the `journal-formatting` folder into your Codex skills directory.

On Windows:

```powershell
Copy-Item -Recurse .\journal-formatting "$env:USERPROFILE\.codex\skills\journal-formatting"
```

On macOS or Linux:

```bash
cp -R journal-formatting ~/.codex/skills/journal-formatting
```

Restart Codex or refresh the skills list if needed.

## Usage

Example prompts:

```text
Use $journal-formatting to format my manuscript according to Advanced Materials author guidelines.
```

```text
Use $journal-formatting to audit this DOCX against the target journal submission checklist.
```

```text
Use $journal-formatting to prepare a formatted manuscript and compliance report for Nature Communications.
```

## Included Script

The skill includes a lightweight DOCX inspection utility that uses only the Python standard library:

```bash
python journal-formatting/scripts/inspect_docx.py manuscript.docx
python journal-formatting/scripts/inspect_docx.py manuscript.docx --json
```

The script reports paragraph counts, table counts, embedded media, page margins, heading styles, and the first nonempty paragraphs.

## Bundled Journal Packs

The skill includes conservative routing packs for mainstream journals and publishers:

- Nature Portfolio
- Science / AAAS
- Cell Press
- Wiley / Advanced Materials
- ACS Publications
- Elsevier
- Springer Nature / BMC
- IEEE
- MDPI
- PLOS

These packs are starting points. Codex should still verify the current official author guidelines for the exact target journal and article type before applying detailed limits.

## Notes

- This skill does not hard-code journal-specific requirements. It instructs Codex to verify official author guidelines before applying detailed journal rules.
- It is safest to use official journal pages, templates, or PDF guidelines as source material.
- The skill is intended to preserve scientific content unless the user explicitly asks for rewriting or translation.

## License

MIT License. See [LICENSE](LICENSE).

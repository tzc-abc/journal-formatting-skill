---
name: journal-formatting
description: Format, audit, and revise academic manuscripts to match specific journal author guidelines, Word templates, or submission checklists. Use when the user asks for journal paper formatting, manuscript layout, target journal format conversion, author-guideline compliance, submission formatting, Word manuscript formatting, reference/style consistency, figure/table placement, title page/abstract/keywords/section heading formatting, or preparing a DOCX/PDF for submission to a named journal or publisher.
---

# Journal Formatting

Use this skill to turn a manuscript into a submission-ready package for a specific journal. Prefer editing the user's actual `.docx` when available; otherwise produce a precise formatting plan and marked revision instructions.

## Intake

Collect or infer these inputs before changing files:

- Target journal name and publisher.
- Current manuscript file, usually `.docx`; optionally `.pdf`, `.tex`, `.rtf`, or pasted text.
- Official author guidelines, template, sample article, or submission checklist. If the user gives only a journal name, verify the current official instructions before applying detailed requirements.
- Required output: clean formatted manuscript, tracked-changes/redline version, formatting audit report, cover/title page, reference conversion, or all of these.

If a requirement is missing and cannot be safely inferred, ask only for the blocking item. Do not invent journal-specific limits for word count, abstract structure, reference style, figure resolution, supplementary files, or title-page declarations.

## Workflow

1. Build the journal requirements table.
   - Record source, access date, and version/template date when available.
   - Separate mandatory requirements from preferences and submission-system checks.
   - Use `references/format-checklist.md` as the baseline checklist.

2. Inspect the manuscript.
   - For `.docx`, run `scripts/inspect_docx.py <file.docx>` for a quick structural audit.
   - For Word work, use the `documents:documents` skill when available, especially for rendering and visual QA.
   - Preserve existing scientific content unless the user explicitly asks for rewriting.

3. Map manuscript structure to the journal format.
   - Title page: title, running title, author order, affiliations, corresponding author, ORCID, equal contribution, acknowledgements, funding, competing interests, ethics, data/code availability, author contributions.
   - Main text: abstract type and length, keywords, heading levels, IMRaD or journal-specific order, line numbering, page numbering, abbreviations, units, nomenclature.
   - Figures/tables: numbering, callouts, legends, placement, resolution notes, file naming, source data or supplementary links.
   - References: citation style, ordering, punctuation, DOI/PMID handling, max references, journal abbreviations.
   - Supplementary material: naming, captions, cross-references, separate files, reporting checklists.

4. Edit with minimal disruption.
   - Apply styles and layout changes without altering claims.
   - Keep user-provided author names, affiliations, funding numbers, and declarations intact.
   - Flag missing content with comments/placeholders instead of fabricating it.
   - When converting references, maintain a report of uncertain or incomplete entries.

5. Verify before delivery.
   - Render the edited document to page images/PDF when possible and inspect title page, abstract, first body page, representative figure/table pages, and references.
   - Re-run the DOCX inspection script after editing if applicable.
   - Check that visible text does not overlap, headings are consistent, tables fit, figure legends remain attached, and page/line numbering is present when required.

## Deliverables

Default deliverables for a formatting task:

- Formatted manuscript file.
- Short audit report listing: compliant items, changed items, unresolved items needing user input, and source guidelines used.
- Optional tracked-changes/redline version when requested or when substantive formatting changes are extensive.

Use clear file naming:

- `<stem>_<journal>_formatted.docx`
- `<stem>_<journal>_format-audit.md`
- `<stem>_<journal>_tracked.docx`

## References

- Read `references/format-checklist.md` when building the requirements table or audit report.

## Scripts

- `scripts/inspect_docx.py <docx>`: quick DOCX structure and layout audit using only Python standard library.
- `scripts/inspect_docx.py <docx> --json`: machine-readable output for comparing before/after states.

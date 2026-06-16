#!/usr/bin/env python3
"""Quick structural audit for DOCX manuscripts using only stdlib."""

from __future__ import annotations

import argparse
import json
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
    "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships",
}


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def read_xml(docx: zipfile.ZipFile, name: str) -> ET.Element | None:
    try:
        return ET.fromstring(docx.read(name))
    except KeyError:
        return None


def text_of(paragraph: ET.Element) -> str:
    parts = []
    for node in paragraph.iter():
        if local_name(node.tag) == "t" and node.text:
            parts.append(node.text)
    return "".join(parts).strip()


def attr(node: ET.Element | None, name: str) -> str | None:
    if node is None:
        return None
    return node.get(f"{{{NS['w']}}}{name}")


def twips_to_inches(value: str | None) -> float | None:
    if value is None:
        return None
    try:
        return round(int(value) / 1440, 2)
    except ValueError:
        return None


def inspect_docx(path: Path) -> dict:
    if not path.exists():
        raise FileNotFoundError(path)
    if path.suffix.lower() != ".docx":
        raise ValueError("Expected a .docx file")

    with zipfile.ZipFile(path) as docx:
        document = read_xml(docx, "word/document.xml")
        styles = read_xml(docx, "word/styles.xml")
        if document is None:
            raise ValueError("word/document.xml not found")

        paragraphs = document.findall(".//w:p", NS)
        tables = document.findall(".//w:tbl", NS)
        drawings = document.findall(".//w:drawing", NS)
        inline_shapes = document.findall(".//wp:inline", {"wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"})
        anchored_shapes = document.findall(".//wp:anchor", {"wp": "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"})

        nonempty_paragraphs = [p for p in paragraphs if text_of(p)]
        first_text = [text_of(p) for p in nonempty_paragraphs[:10]]

        heading_counts: dict[str, int] = {}
        style_counts: dict[str, int] = {}
        for paragraph in paragraphs:
            p_style = paragraph.find("./w:pPr/w:pStyle", NS)
            style_id = attr(p_style, "val")
            if style_id:
                style_counts[style_id] = style_counts.get(style_id, 0) + 1
                if style_id.lower().startswith("heading"):
                    heading_counts[style_id] = heading_counts.get(style_id, 0) + 1

        section = document.find(".//w:sectPr", NS)
        pg_sz = section.find("./w:pgSz", NS) if section is not None else None
        pg_mar = section.find("./w:pgMar", NS) if section is not None else None
        page = {
            "width_twips": attr(pg_sz, "w"),
            "height_twips": attr(pg_sz, "h"),
            "top_margin_in": twips_to_inches(attr(pg_mar, "top")),
            "bottom_margin_in": twips_to_inches(attr(pg_mar, "bottom")),
            "left_margin_in": twips_to_inches(attr(pg_mar, "left")),
            "right_margin_in": twips_to_inches(attr(pg_mar, "right")),
        }

        style_names = []
        if styles is not None:
            for style in styles.findall(".//w:style", NS):
                name = style.find("./w:name", NS)
                val = attr(name, "val")
                if val:
                    style_names.append(val)

        media_files = [name for name in docx.namelist() if name.startswith("word/media/")]

    return {
        "file": str(path),
        "paragraphs": len(paragraphs),
        "nonempty_paragraphs": len(nonempty_paragraphs),
        "tables": len(tables),
        "drawings": len(drawings),
        "inline_shapes": len(inline_shapes),
        "anchored_shapes": len(anchored_shapes),
        "media_files": len(media_files),
        "heading_counts": dict(sorted(heading_counts.items())),
        "top_style_counts": dict(sorted(style_counts.items(), key=lambda item: item[1], reverse=True)[:15]),
        "page": page,
        "first_nonempty_paragraphs": first_text,
        "defined_style_names_sample": sorted(style_names)[:30],
    }


def print_markdown(report: dict) -> None:
    print(f"# DOCX Inspection: {Path(report['file']).name}")
    print()
    print(f"- Paragraphs: {report['paragraphs']} ({report['nonempty_paragraphs']} nonempty)")
    print(f"- Tables: {report['tables']}")
    print(f"- Drawings: {report['drawings']} ({report['media_files']} media files)")
    print(f"- Inline shapes: {report['inline_shapes']}")
    print(f"- Anchored shapes: {report['anchored_shapes']}")
    print(f"- Page: {report['page']}")
    print()
    print("## Heading Counts")
    if report["heading_counts"]:
        for key, value in report["heading_counts"].items():
            print(f"- {key}: {value}")
    else:
        print("- No Heading* paragraph styles detected")
    print()
    print("## First Nonempty Paragraphs")
    for index, text in enumerate(report["first_nonempty_paragraphs"], 1):
        preview = text if len(text) <= 160 else text[:157] + "..."
        print(f"{index}. {preview}")


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Inspect DOCX manuscript structure.")
    parser.add_argument("docx", type=Path, help="Path to a .docx file")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of Markdown")
    args = parser.parse_args(argv)

    try:
        report = inspect_docx(args.docx)
    except Exception as exc:
        print(f"inspect_docx.py: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print_markdown(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

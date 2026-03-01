#!/usr/bin/env python3
"""
Generate Statistical_Analysis_Report.pdf from Statistical_Analysis_Report.md.
Requires: pip install fpdf2
Alternative: open the .md in VS Code and use File > Print > Save as PDF.
"""
import os
import re

def md_to_plain_chunks(md_path):
    """Convert markdown to a list of (style, text) for fpdf2. style: 'h1', 'h2', 'body'."""
    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()
    # Replace unicode that might not render in default Latin-1 font
    content = content.replace("\u2080", "0").replace("\u2081", "1")  # subscript
    content = content.replace("\u2014", "-").replace("\u2013", "-")  # dashes
    content = content.replace("\u03b1", "alpha")  # Greek alpha (e.g. significance level)
    content = content.replace("\u2019", "'").replace("\u2018", "'")  # smart quotes
    content = content.replace("\u201c", '"').replace("\u201d", '"')
    # Fallback: replace any remaining non-Latin-1 chars so fpdf2 default font works
    content = content.encode("ascii", errors="replace").decode("ascii")
    chunks = []
    for line in content.split("\n"):
        line = line.strip()
        if not line:
            chunks.append(("body", ""))
            continue
        if line.startswith("# "):
            chunks.append(("h1", line[2:].strip()))
        elif line.startswith("## "):
            chunks.append(("h2", line[3:].strip()))
        elif line.startswith("- "):
            chunks.append(("body", "  " + line))
        else:
            # Remove markdown bold/italic for plain text
            plain = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
            plain = re.sub(r"\*([^*]+)\*", r"\1", plain)
            chunks.append(("body", plain))
    return chunks

def main():
    from fpdf import FPDF

    md_path = os.path.join(os.path.dirname(__file__), "Statistical_Analysis_Report.md")
    pdf_path = os.path.join(os.path.dirname(__file__), "Statistical_Analysis_Report.pdf")

    chunks = md_to_plain_chunks(md_path)
    pdf = FPDF()
    pdf.set_auto_page_break(True, margin=15)
    pdf.add_page()
    pdf.set_font("Helvetica", "", 11)

    for style, text in chunks:
        if style == "h1":
            pdf.set_font("Helvetica", "B", 16)
            pdf.multi_cell(0, 10, text)
            pdf.ln(2)
            pdf.set_font("Helvetica", "", 11)
        elif style == "h2":
            pdf.set_font("Helvetica", "B", 13)
            pdf.multi_cell(0, 8, text)
            pdf.ln(2)
            pdf.set_font("Helvetica", "", 11)
        else:
            if text:
                pdf.multi_cell(0, 6, text)
            else:
                pdf.ln(4)

    pdf.output(pdf_path)
    print(f"Generated: {pdf_path}")

if __name__ == "__main__":
    try:
        from fpdf import FPDF
    except ImportError:
        print("Install fpdf2: pip install fpdf2")
        raise SystemExit(1)
    main()

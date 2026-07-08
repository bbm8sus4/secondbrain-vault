---
name: reference_thai_doc_generation
description: "How to generate polished Thai PDF and Word (.docx) documents (quotations, playbooks) with correct fonts and layout"
metadata: 
  node_type: memory
  type: reference
  originSessionId: c25a2b2a-038e-44d1-aaab-2832fc3e8ae9
---

Workflow for producing client-facing Thai documents (quotations, invoices, playbooks) with good design:

- **PDF** (best fidelity, use for sending clients): write styled HTML, render with Chrome headless — `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --no-pdf-header-footer --print-to-pdf=out.pdf file://in.html`. Set `@page{size:A4;margin:0}` + `.page{height:297mm;overflow:hidden}` so each section = exactly 1 sheet (otherwise footers spill to blank pages). Thai renders crisp.
- **Editable Word (.docx)**: do NOT use pandoc (tables collapse, no color) or textutil / LibreOffice HTML-import (Writer/Web ignores table widths → tables overflow the page). Build the .docx directly with **python-docx** — full control over column widths (Cm), cell shading (w:shd), font colors, and Thai complex-script fonts (set `rFonts` w:cs + w:eastAsia to "Sarabun"). Use a venv: `python3 -m venv venv && venv/bin/pip install python-docx`.
- **Verify before sending**: LibreOffice (installed via `brew install --cask libreoffice`, binary `soffice`) converts docx→pdf for eyeballing: `soffice --headless --convert-to pdf --outdir DIR file.docx`. Read the PDF to confirm layout.
- Keep the build script alongside the output so numbers/scope can be regenerated. Example lives at `~/SecondBrain/01 Projects/AI Workshop - ขอนแก่นอิเล็คทริค/Files/Costs/AI-Workshop-Quotation-build_docx.py`.

Reference layout that the user likes ("จัดเจน/ชัดเจน"): the Cotactic 5-page service-contract format — parties block (both Tax IDs), scope as counted deliverables, totals box, KPI/outcomes table, payment schedule with dates, transfer details, dual signatures. Related: [[SeatMap app|project_seatmap]] (Thunder brand), [[HTML dark-purple design|reference_html_dark_purple_design]].

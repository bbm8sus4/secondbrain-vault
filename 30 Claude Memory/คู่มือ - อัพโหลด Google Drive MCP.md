---
name: reference-google-drive-mcp-upload
description: "How to upload files to Google Drive via the claude.ai Google_Drive MCP (correct field names, CSV→Sheet conversion)"
metadata: 
  node_type: memory
  type: reference
  originSessionId: dd2aa127-e1a7-4dc3-bb0f-dd764571bcc8
---

Uploading to Google Drive via `mcp__claude_ai_Google_Drive__create_file`.

**Correct field names** (the deprecated ones in older calls FAIL): use `title` (NOT `name`), `contentMimeType` (NOT `mime_type`/`mimeType` — those are deprecated/rejected), `textContent` for UTF-8 text, `base64Content` for binary. `parentId` to place in a folder.

**CSV → native Google Sheet:** upload with `contentMimeType: "text/csv"` + `textContent: <csv>`. Drive auto-converts text/csv → native `application/vnd.google-apps.spreadsheet` (one CSV = one sheet, single tab). text/plain → Google Doc likewise. Returns `id` + `webViewLink` (stable URL).

**Multi-tab + formulas:** a single CSV can't carry multiple tabs or formulas. Options: (a) build an `.xlsx` locally with openpyxl (multi-tab, SUMIFS, formatting) and have the user drag it to Drive — Drive converts on open; uploading the .xlsx via `base64Content` means inlining the whole base64 in the tool call (expensive, ~1.3× file size in tokens). (b) upload the core fact table as CSV→Sheet, keep the full .xlsx local. There is NO Google Sheets API MCP connected (only Drive) — can't add tabs/formulas to an existing Sheet programmatically.

**search_files query:** uses `title contains '...'`, NOT `name`. Fields: title, fullText, mimeType, modifiedTime, parentId, owner, sharedWithMe.

Used 2026-05-29 to publish EasyBOT finance DB. See [[project_easybot_finance]].

---
name: html-dark-purple-design
description: "User's preferred HTML design style for internal playbooks/docs. Dark theme + purple accent + IBM Plex Sans Thai + Inter. Full spec + boilerplate in Obsidian."
metadata: 
  node_type: memory
  type: reference
  originSessionId: 53119bdc-53f9-462d-9243-6ac7c70c15f2
---

Standard design system for internal playbooks / docs / SOPs (คู่มือทีม). User rejected generic light-theme design and directed me to this style via `reve2-guide.html`.

**Full spec + code blocks:** `~/SecondBrain/03 Resources/คู่มือ - HTML ดีไซน์ dark purple.md`

**Style signature (recognize by these):**
- Dark bg `#0a0a0f`, surface `#12121a`, purple accent `#6c5ce7` + light `#a29bfe`
- IBM Plex Sans Thai (body) + Inter (headings, numbers, uppercase labels)
- Hero: badge with pulsing dot + gradient text h1 (white → accent-light) + radial glow bg
- Cards on `--surface` with border hover-highlight to accent
- Flow with vertical gradient line + numbered purple circles (`data-step` attr)
- Tables: uppercase 11px `--text-dim` thead, subtle row hover
- Tag pills: 3 tiers red/orange/green with 0.12 opacity bg + full-color text

**Reference files (copy-then-modify):**
- `~/cs-announcement-playbook.html` — most complete boilerplate (SOP + templates + checklist + accordion)
- `~/reve2-guide.html` — original source of the style

**Mobile/a11y baked in — don't strip:** viewport-fit=cover, safe-area-insets, tap-highlight transparent, 44px min touch, focus-visible outline, prefers-reduced-motion, print stylesheet, inline SVG favicon (2-letter monogram in purple square).

How to apply: when user asks for an internal playbook/doc/SOP as HTML, use this style by default. Don't ask "should I make it dark?" — this is the default. Only ask if the target is external (customer-facing) — then confirm before applying.

When NOT to use (from the Obsidian guide):
- Exec presentation slides → use [[CS Announcement Framework (-announce)|cs-announcement-framework]] sibling: `คู่มือ - สไลด์ HTML ปิดบังตัวเลข.md` (Apple-style, light)
- Customer-facing docs → depends on customer brand
- Marketing landing → different design brief

Related: [[CS Announcement Framework (-announce)|cs-announcement-framework]] (the first artifact built in this style).

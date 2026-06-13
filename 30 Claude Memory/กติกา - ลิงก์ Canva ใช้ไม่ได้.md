---
name: feedback-canva-mcp-links
description: Canva MCP generated URLs (/d/...) always return 403 Forbidden — tell user to find design on canva.com homepage instead
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 9913b203-76e1-4239-9e8f-2119bbb9837c
---

Canva MCP short links (`https://www.canva.com/d/...`) from `create-design-from-candidate` and `get-design` consistently return 403 Forbidden when opened in browser.

**Why:** Known limitation of the Canva MCP connector — the generated share URLs are not properly permissioned for direct browser access. User has hit this multiple times.

**How to apply:** After creating or saving a design via Canva MCP, do NOT present the `/d/...` links as clickable. Instead, tell the user to find the design on canva.com homepage under "Recent designs" by its title. Mention the design title clearly so they can locate it. Related: [[กติกา - Chrome MCP transport|feedback-chrome-mcp-transport]].

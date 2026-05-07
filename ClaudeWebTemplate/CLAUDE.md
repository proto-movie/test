# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a MUBI **TV prototype** workspace. All prototypes are built exclusively for the TV / 10-foot UI (1920×1080px). Files are self-contained HTML prototypes built for capture into Figma via the Figma MCP HTML-to-design script. There is no build system, package manager, or framework — everything is vanilla HTML/CSS in single files.

## File Inventory

| File | Description | Viewport |
|------|-------------|----------|
| `mubi-academy-desktop.html` | MUBI Academy feature — desktop | 1440px wide |
| `mubi-academy-tv.html` | MUBI Academy feature — TV / 10-foot UI | 1920×1080px |
| `dating-app.html` | "Spark" dating app concept (non-MUBI) | 390×844px (mobile) |
| `brand_assets/` | MUBI SVG logos + web fonts + brand images |
| `brand_assets/mubi-collections.csv` | Real MUBI collection data for designs |
| `brand_assets/mubi-content.csv` | Real MUBI film data for designs |

## MUBI Brand Design System

Full token reference is in [`design-system.md`](./design-system.md). Key conventions:

**Colors:** All declared as CSS custom properties — `--red: #001489` (brand navy, named "red" historically), `--bg` through `--bg-4`, `--text` through `--text-3`, `--gold`, `--green`, `--border`, `--border-2`. TV prototype uses slightly darker bg values and adds `--focus` for D-pad ring.

**Typography:**
- Body/UI: `'DM Sans', sans-serif` (Google Fonts variable, 100–1000)
- Display/headings: `'Riforma', sans-serif` (served from `assets.mubicdn.net` as woff2 — Regular, Medium, Bold, Italic)

**Logo:** Always use SVG assets — never recreate in text.
- `brand_assets/Mubi_logo_white.svg` — full wordmark (nav, footer)
- `brand_assets/Mubi_logo_icon_only.svg` — dot-grid icon only

## Figma Capture Script

Every prototype must include this in `<head>` to enable Figma MCP capture:
```html
<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
```

## TV / 10-Foot UI Conventions (`mubi-academy-tv.html`)

- Fixed 1920×1080px canvas (`overflow: hidden`)
- TV safe zone: 40px top/bottom, 60px left/right margins via `.tv-safe`
- Focus rings use `box-shadow: 0 0 0 3px var(--focus)` (never `outline`) — supports D-pad navigation
- `--focus: rgba(0,20,137,0.8)` — blue glow for focused elements
- Font sizes are ~1.3× larger than desktop equivalents (min 16px body, 18px+ nav)
- No hover states; use `:focus` instead for TV interactivity

## Cinematic Visual Techniques

Used in MUBI hero sections to create atmosphere without real imagery:
- Layered `radial-gradient` for colored light pools (blue/teal = film noir, deep red/purple = drama)
- SVG `feTurbulence` filter as inline data URI for film grain texture overlay (`opacity: 0.03–0.05`)
- Letterbox bars (56px top/bottom black bars) for cinematic framing
- Film strip edge decoration with `.sprocket` elements

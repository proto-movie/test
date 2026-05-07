# MUBI Design System

Reference for all prototypes in this project. Keep in sync as new components are built.

---

## Fonts

### Brand Fonts

**Riforma** — brand display & heading font (served from MUBI CDN)

```css
@font-face {
  font-family: 'Riforma';
  font-display: swap;
  src: url(https://assets.mubicdn.net/static/fonts/RiformaLLWeb-Regular.woff2) format('woff2');
}
@font-face {
  font-family: 'Riforma';
  font-display: swap;
  src: url(https://assets.mubicdn.net/static/fonts/RiformaLLWeb-Medium.woff2) format('woff2');
  font-weight: 500;
}
@font-face {
  font-family: 'Riforma';
  font-display: swap;
  src: url(https://assets.mubicdn.net/static/fonts/RiformaLLWeb-Bold.woff2) format('woff2');
  font-weight: bold;
}
@font-face {
  font-family: 'Riforma';
  font-display: swap;
  src: url(https://assets.mubicdn.net/static/fonts/RiformaLLWeb-Italic.woff2) format('woff2');
  font-style: italic;
}
```

**DM Sans** — UI & body font (Google Fonts, variable weight 100–1000)

```css
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@100..1000&display=swap');
```

Or via `<link>`:
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@100..1000&display=swap" rel="stylesheet">
```

### Usage Rule

| Role | Font | Notes |
|---|---|---|
| Body / UI / nav / labels | `'DM Sans', sans-serif` | All weights via variable font |
| Display titles / course headings / editorial | `'Riforma', sans-serif` | **500 Medium** for titles; 400 italic for subtitles |
| Logo wordmark | SVG asset (`brand_assets/Mubi_logo_white.svg`) | Do not recreate in text |

---

## Colour Tokens

All prototypes declare these as CSS custom properties on `:root`.

### Backgrounds

| Token | Value | Usage |
|---|---|---|
| `--bg` | `#111111` | Page / outermost background |
| `--bg-2` | `#181818` | Cards, sidebars, section fills |
| `--bg-3` | `#202020` | Input fields, selectable options |
| `--bg-4` | `#282828` | Elevated / hover states |

> **TV variant:** `--bg` is `#0A0A0A` (slightly deeper black for OLED screens).

### Text

| Token | Value | Usage |
|---|---|---|
| `--text` | `#FFFFFF` | Primary — headings, active labels |
| `--text-2` | `#ABABAB` | Secondary — body copy, nav links |
| `--text-3` | `#666666` | Muted — captions, metadata, disabled |

> **TV variant:** `--text-2` is `#B0B0B0`.

### Brand & Semantic

| Token | Value | Usage |
|---|---|---|
| `--red` | `#001489` | Brand accent — badges, active borders, radio dots |
| `--red-dark` | `#001070` | Pressed / active accent state (desktop) |
| `--red-hover` | `#001AAF` | Hover accent state (TV) |
| `--btn` | `#001489` | **Primary button background** |
| `--btn-hover` | `#001AAF` | **Primary button hover / focus background** |
| `--gold` | `#F5A623` | Star ratings, awards (dark theme) |
| `--green` | `#2DC75E` | Enrolled status, free episode badge |

> **Light theme overrides:** `--gold` is `#001489` (brand blue — orange is replaced by brand blue on light backgrounds). See [Light Theme Variant](#light-theme-variant) below.

### Borders

| Token | Value | Usage |
|---|---|---|
| `--border` | `rgba(255,255,255,0.07)` | Subtle dividers, card edges |
| `--border-2` | `rgba(255,255,255,0.14)` | Stronger borders, active outlines |

> **TV variant:** `--border` is `rgba(255,255,255,0.08)`, `--border-2` is `rgba(255,255,255,0.16)`.

### TV-only

| Token | Value | Usage |
|---|---|---|
| `--focus` | `rgba(0,20,137,0.8)` | D-pad focus ring (blue glow) |

---

## Typography Scale

### Display (Riforma)

All Riforma titles use `text-transform: uppercase` and `letter-spacing: -0.4px`.

| Usage | Size | Weight | Line-height | Letter-spacing |
|---|---|---|---|---|
| Hero title | 54px | 500 | 1.04 | −0.4px |
| Hero subtitle | 20px | 400 italic | — | — |
| Course title (main) | 40px | 500 | 1.1 | −0.4px |
| Course subtitle | 18px | 400 italic | — | — |
| Section heading (lg) | 26px | 500 | — | −0.4px |
| Section heading (sm) | 22px | 500 | — | −0.4px |
| Card title | 16px | 500 | 1.3 | −0.4px |
| Mobile genre tile title | 14px | 500 | 1.2 | −0.4px |
| Mobile collection title | 12.5px | 500 | 1.3 | −0.4px |
| Instructor bio name | 26px | 500 | — | −0.4px |

### UI (DM Sans)

| Usage | Size | Weight | Notes |
|---|---|---|---|
| Navigation links | 14px | 500 | — |
| Body copy | 15px | 400 | line-height 1.78 |
| Episode title | 14–14.5px | 600 | — |
| Price amount | 24px | 800 | letter-spacing −0.5px |
| Button (primary) | 15px | 700 | — |
| Button (secondary) | 14px | 600 | — |
| Section eyebrow labels | 10px | 700 | UPPERCASE, letter-spacing −0.1px, `--text-3` or `--red` |
| Explore By pill labels | 13px | 500 | UPPERCASE, letter-spacing −0.1px, `--text-2` |
| Trending metadata | 11.5px | 400 | UPPERCASE, letter-spacing −0.1px, `--text-3` |
| Metadata / captions | 12–13px | 400–600 | `--text-3` |
| Micro badge text | 8–9px | 800 | UPPERCASE, letter-spacing 1.5–2px |

### TV Scale (≈1.3× desktop)

| Usage | Font | Size | Weight | Notes |
|---|---|---|---|---|
| Marquee nav items | Riforma | 24px | 500 (Medium) | Uppercase, `letter-spacing: -0.4px`; same weight active and inactive |
| Marquee film metadata | DM Sans | 24px | 400 | Uppercase; director bold (700), country/year full white |
| Marquee Our Take | Riforma | 24px | 400 | Bottom right, 860px wide |
| Collection synopsis | Riforma | 24px | 400 | `line-height: 1.5`, `text-shadow: 0 1px 8px rgba(0,0,0,0.8)`, max-width 420px; class `.collection-synopsis` |
| TV pill buttons | Riforma | 24px | 500 (Medium) | Uppercase, `letter-spacing: -0.4px` |
| Hero/course title | Riforma | 52px | 400 | — |
| Hero subtitle | Riforma | 22px | 400 italic | — |
| Body / description | DM Sans | 17px | 400 | — |
| CTA buttons | DM Sans | 20px | 700 | Desktop-only pattern; use pill style on TV |
| Episode card title | DM Sans | 14px | 600 | — |

---

## Component Rules

### Section Eyebrows / Pre-titles
Small uppercase labels above section titles (e.g. "Curated Daily", "Just Added", "Director Spotlight") are allowed but must have **no decorative line or dash** before the text — no `::before` rule. Text only.

- Dark mode: `#7DD8E0` (light cyan) — dark navy is illegible on dark backgrounds
- Light mode sections (on light bg): `var(--red)` (#001489 navy)
- Collection banners (always on dark image): `#7DD8E0`

---

## Spacing

| Context | Value |
|---|---|
| Page horizontal padding | 48px |
| Nav height (desktop) | 64px |
| Section vertical padding | 64px |
| Card gap (grid) | 20px |
| Internal component gap | 16–24px |
| Sidebar top sticky offset | 80px |

### TV Safe Zone

```css
.tv-safe {
  position: absolute;
  top: 40px; left: 60px; right: 60px; bottom: 40px;
}
```

---

## Border Radius

| Element | Radius |
|---|---|
| Buttons (primary/secondary) | 4–6px |
| Cards, pricing card, panels | 8px |
| Pricing card (outer) | 12px |
| Micro badges (`MUBI`, `FREE`) | 2–3px |
| Pill/tag (enrolled status, round) | 20px |
| Avatars / profile photos | 50% |

---

## Component Patterns

### Buttons

```css
/* Primary */
background: var(--btn); color: #fff;
border-radius: 6px; padding: 15px 22px;
font-size: 15px; font-weight: 700; text-transform: uppercase;

/* Primary hover */
background: var(--btn-hover);

/* Secondary / outline */
background: transparent; color: var(--text-2);
border: 1px solid var(--border-2); border-radius: 6px;
padding: 13px; font-size: 14px; font-weight: 600; text-transform: uppercase;
```

Button text is **always uppercase** (`text-transform: uppercase`).

#### TV Pill Buttons

TV buttons use a pill shape — rounded ends, frosted glass default, solid white on focus:

```css
/* Default (both primary and secondary share one style on TV) */
height: 72px;
padding: 0 40px;
border-radius: 36px;
background: rgba(255,255,255,0.20);
color: #fff;
border: none;
font-family: 'Riforma', sans-serif;
font-size: 24px;
font-weight: 500;       /* Medium */
text-transform: uppercase;
letter-spacing: -0.4px;

/* Focus (D-pad select) */
background: #fff;
color: #000;            /* icons inherit via currentColor */
outline: none;          /* never use outline on TV */
```

No hover states on TV — `:focus` is the only interactive state.

### Badges & Chips

```css
/* Brand red badge (MUBI, ACADEMY) */
background: var(--red); color: #fff;
font-size: 8–9px; font-weight: 800; letter-spacing: 1.5–2px; text-transform: uppercase;
padding: 3–5px 8–12px; border-radius: 2px;

/* Outlined red tag (COURSE type) */
background: rgba(0,20,137,0.1); border: 1px solid rgba(0,20,137,0.22);
color: var(--red); font-size: 10px; font-weight: 700;
letter-spacing: 2px; text-transform: uppercase;
padding: 5px 12px; border-radius: 3px;

/* Green enrolled/free badge */
background: rgba(45,199,94,0.1); border: 1px solid rgba(45,199,94,0.25–0.28);
color: var(--green); font-size: 9–11px; font-weight: 700–800;
```

### Eyebrow Labels

All-caps small label above a heading. Used throughout:
```css
font-size: 10px; font-weight: 700;
letter-spacing: 2–3px; text-transform: uppercase;
color: var(--red);  /* or var(--text-3) for neutral */
```
The red variant optionally includes a decorative line via `::before { width: 22px; height: 1.5px; background: var(--red); }`.

### Cards

```css
background: var(--bg-3); border: 1px solid var(--border);
border-radius: 8px; overflow: hidden;
transition: transform 0.2s, border-color 0.2s;
/* Hover: */ transform: translateY(-3px); border-color: var(--border-2);
```

### Selectable Options (pricing)

```css
/* Default */
background: var(--bg-3); border: 1px solid var(--border-2); border-radius: 8px;

/* Active */
border-color: var(--red); background: rgba(0,20,137,0.06);
```

### Stat / Info Chips

```css
display: flex; align-items: center; gap: 6–8px;
background: var(--bg-3); border: 1px solid var(--border-2);
padding: 8px 16px; border-radius: 6px;
font-size: 13–15px; color: var(--text-2); font-weight: 500;
```

### TV Focus Ring

Never use `outline`. Use `box-shadow` only:
```css
.tv-focusable:focus {
  box-shadow: 0 0 0 3px var(--focus);  /* blue glow */
  border-radius: 6px;
  outline: none;
}
/* Stronger variant for CTA buttons: */
box-shadow: 0 0 0 4px var(--focus);
```

**Exception — top nav items:** Nav buttons use a white-pill focus style (same as TV pill buttons) rather than the blue box-shadow ring:
```css
.marquee-nav-item:focus {
  background: #fff;
  color: #000;
  outline: none;
  box-shadow: none;
}
```

---

## Cinematic Background Technique

Used in hero sections and video thumbnails to simulate film atmosphere without real imagery.

```css
/* Layered colour pools */
background:
  radial-gradient(ellipse 60% 80% at 25% 60%, rgba(10,35,65,0.9) 0%, transparent 70%),
  radial-gradient(ellipse 50% 60% at 75% 30%, rgba(55,15,35,0.7) 0%, transparent 65%),
  linear-gradient(160deg, #06101E 0%, #0F0618 40%, #040408 100%);

/* Film grain overlay — use as separate element */
background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='grain'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23grain)' opacity='1'/%3E%3C/svg%3E");
background-size: 200px 200px;
opacity: 0.035;  /* keep between 0.03–0.05 */
```

**Letterbox bars:** 56px black bars top and bottom (`z-index: 4`).
**Film strip edges:** 22px black column each side, sprocket holes 10×8px rounded.

---

## Platform Canvas Sizes

| Platform | Canvas | Viewport meta |
|---|---|---|
| Responsive web | fluid, breakpoints below | `width=device-width` |
| Desktop | 1440px wide, flexible height | `width=1440` |
| TV | 1920×1080px fixed | `width=1920` |
| Mobile (Spark prototype) | 390×844px | `width=device-width, initial-scale=1.0` |

---

## Responsive Web — Container & Breakpoints

Exact breakpoints extracted from `mubi.com` production CSS. Used in `mubi-showing.html`.

```css
.wrap {
  width: 100%;
  padding: 0 20px;
  margin: 0 auto;
}
@media (min-width: 810px)  { .wrap { padding: 0 22px; max-width: 836px; } }
@media (min-width: 1186px) { .wrap { max-width: 1124px; } }
@media (min-width: 1562px) { .wrap { max-width: 1500px; } }
```

The `.now-showing` section, `.nav-desktop`, and `.site-footer` are constrained to match `.wrap` at each breakpoint using explicit `max-width + margin: 0 auto` rules (they don't use `.wrap` directly because the film grid spans full-width at each step):

```css
@media (min-width: 1186px) {
  .nav-desktop, .now-showing, .site-footer { max-width: 1124px; margin: 0 auto; }
}
@media (min-width: 1562px) {
  .nav-desktop, .now-showing, .site-footer { max-width: 1500px; }
}
```

---

## Responsive Web — Now Showing Page

### Light / white theme

`mubi.com` uses a white/light theme — the opposite of the dark design tokens.

| Element | Value |
|---|---|
| Page background | `#FFFFFF` |
| Primary text | `#323232` |
| Secondary text (director, year) | `#7d7d7d` |
| Borders / dividers | `#EAEAEA` |
| Body font | `Riforma, Helvetica, Arial, sans-serif` (Riforma is primary on web, not DM Sans) |
| Nav height — mobile | `60px` |
| Nav height — desktop (≥1186px) | `50px` |

### Transparent nav

The header has no background — the hero image/video shows through. Nav links, logo, and search are always white (coloured for legibility against the dark hero).

```css
.site-header {
  position: relative;
  height: 60px;
  z-index: 10;
  /* no background */
}
@media (min-width: 1186px) { .site-header { height: 50px; } }
```

### Hero — video/image extending behind nav

The hero uses a padding-based 16:9 aspect ratio on desktop. The background container extends UP behind the transparent nav by using negative `top` and an explicit calculated height:

```css
.hero {
  position: relative;
  width: 100%;
  height: 75vh;
  min-height: 630px;
  overflow: hidden;
}
@media (min-width: 810px) {
  .hero { height: 0; padding-bottom: 56.25%; overflow: visible; min-height: 0; }
}

.hero-bg {
  position: absolute;
  top: -60px; left: 0; right: 0;
  height: calc(75vh + 60px);
  min-height: calc(630px + 60px);
  overflow: hidden;
}
@media (min-width: 810px) { .hero-bg { height: calc(56.25vw + 60px); min-height: 0; } }
@media (min-width: 1186px) { .hero-bg { top: -50px; height: calc(56.25vw + 50px); } }
```

> **Critical:** `height: 100%` on children of `.hero-bg` won't resolve correctly when `.hero` uses `padding-bottom` for its aspect ratio (parent computed height = 0). Always give `.hero-bg` an explicit `height` using `vw` or `vh` units so children's percentage heights resolve.

### Hero video — filling without black bars

Use `object-fit: cover` with `inset: 0; width: 100%; height: 100%` once `.hero-bg` has an explicit height:

```css
.hero-video {
  position: absolute;
  inset: 0;
  width: 100%; height: 100%;
  object-fit: cover;
  object-position: {focalX*100}% {focalY*100}%;
}
```

If the source video has encoded letterbox bars, detect and strip them with ffmpeg:

```bash
# detect bars (run from ~5s in to skip fade-in)
ffmpeg -ss 5 -i input.mp4 -vf "cropdetect=16:2:0" -frames:v 30 -f null - 2>&1 | grep "crop="

# strip bars (e.g. crop=1280:698:0:10 means 10px top bar, 12px bottom)
ffmpeg -i input.mp4 -vf "crop=1280:698:0:10" -c:v libx264 -preset fast -crf 18 -c:a copy output.mp4
```

### Hero gradients (from MUBI production CSS)

```css
/* Two stacked overlays inside .hero-bg */
.hero-grad-1 {
  position: absolute; inset: 0;
  background:
    linear-gradient(to bottom, transparent 0%, transparent 50%, rgba(0,0,0,0.4) 80%, rgba(0,0,0,0.4) 100%),
    linear-gradient(to top,    transparent 0%, transparent 70%, rgba(0,0,0,0.25) 90%, rgba(0,0,0,0.35) 100%);
}
.hero-grad-2 {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.375) 0%, transparent 50%);
}
```

### Hero info layout

Full-height flex column: title treatment pinned to top (below nav), film meta + actions at bottom.

```css
.hero-info {
  position: absolute;
  top: 0; bottom: 0; left: 0; right: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  padding: 72px 20px 28px; /* top = nav height + gap */
  z-index: 2;
}
/* Align with container at each breakpoint */
@media (min-width: 1186px) {
  .hero-info {
    left: max(0px, calc((100% - 1124px) / 2));
    right: max(0px, calc((100% - 1124px) / 2));
    padding: 62px 22px 52px;
  }
}
@media (min-width: 1562px) {
  .hero-info {
    left: max(0px, calc((100% - 1500px) / 2));
    right: max(0px, calc((100% - 1500px) / 2));
  }
}
```

### Our Take paragraph

The editorial blurb sits in the hero bottom row, to the right of the action buttons. It has a `margin-left` to indent it from the left edge of the container, creating visual breathing room from the buttons.

```css
.hero-our-take {
  font-family: Riforma, sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 1.55;
  color: #fff;
  max-width: 798px;
  margin-left: 200px;
}
```

### Film grid — Now Showing (row sections)

Films are grouped into rows of 4, each with a numbered label (ROW 1, ROW 2…) and 20px gap between sections. The 4th card is hidden at narrower breakpoints so rows never wrap.

```css
.row-section { margin-bottom: 20px; }
.row-section:last-child { margin-bottom: 0; }

.row-header { padding: 0 0 10px; }
.row-title {
  font-family: Riforma, sans-serif;
  font-size: 14px; font-weight: 500;
  text-transform: uppercase; color: #323232;
}

.row-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  column-gap: 4px; row-gap: 1px;
  background: #EAEAEA;
  border-top: 1px solid #EAEAEA;
  border-bottom: 1px solid #EAEAEA;
}
@media (min-width: 650px)  { .row-grid { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 1562px) { .row-grid { grid-template-columns: repeat(4, 1fr); } }

/* Hide overflow cards so rows never wrap */
@media (max-width: 649px)  { .row-grid .film-card:nth-child(n+3) { display: none; } }
@media (min-width: 650px) and (max-width: 1561px) { .row-grid .film-card:nth-child(4) { display: none; } }
```

### Film card — Now Showing

Cards use **371×209 (≈16:9) aspect ratio**. Title, director, country, and year are overlaid on the image via a bottom gradient — no separate info panel below the image.

```css
.card-img-wrap {
  position: relative;
  aspect-ratio: 371 / 209;
  overflow: hidden;
}
.card-overlay {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,0,0,0.72) 0%, rgba(0,0,0,0.18) 55%, transparent 100%);
  display: flex; flex-direction: column; justify-content: flex-end;
  padding: 12px 14px;
}
.card-title {
  font-family: Riforma, sans-serif;
  font-size: 22px; font-weight: 500;
  text-transform: uppercase; color: #fff;
  margin-bottom: 4px;
}
.card-meta {
  font-family: Riforma, sans-serif;
  font-size: 12px; font-weight: 400;
  text-transform: uppercase; color: #fff;
  white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.card-meta-director { font-weight: 700; }
```

Meta line format: `[Director bold] [Country] [Year]` — all on one line, no separator dot.

### Days-left badge colours

| State | Background | Text |
|---|---|---|
| Last day | `#c0392b` | `#fff` |
| 2–3 days | `rgba(160,80,0,0.80)` | `#fff` |
| 4+ days | `rgba(30,30,30,0.72)` | `rgba(255,255,255,0.9)` |

---

## Logo Usage

Always use the SVG assets — never recreate the wordmark in text.

| Asset | Usage |
|---|---|
| `brand_assets/Mubi_logo_white.svg` | Navigation, footer — size via `height` attribute only |
| `brand_assets/Mubi_logo_icon_only.svg` | Favicon, standalone icon contexts |

### Inline SVG (preferred for self-contained prototypes)

Embed the wordmark directly in HTML so the file has no external asset dependency. Use `fill="currentColor"` on both paths so the logo inherits the surrounding text colour — white on dark backgrounds, dark on light backgrounds, automatically.

```html
<svg height="18" viewBox="0 0 263 80" fill="none" xmlns="http://www.w3.org/2000/svg" aria-label="MUBI">
  <path d="M67.04 61.1345C67.0396 62.9044 67.3073 64.4769 67.8438 65.8513C68.3802 67.2256 69.138 68.3905 70.1152 69.3455C71.0908 70.3003 72.266 71.0336 73.6406 71.5457C75.0154 72.0578 76.5411 72.3142 78.2178 72.3142C79.8964 72.3142 81.4222 72.0578 82.7949 71.5457C84.1675 71.0336 85.3427 70.3003 86.3203 69.3455C87.2979 68.3872 88.0548 67.2222 88.5908 65.8513C89.1269 64.4802 89.3955 62.9077 89.3955 61.1345V30.0447H98.4824V61.1335C98.4824 63.7429 98.0163 66.2006 97.084 68.5056C96.1813 70.7679 94.8128 72.8155 93.0674 74.5144C91.4297 76.1099 89.4539 77.3877 87.1406 78.3474L86.6729 78.533C84.1567 79.511 81.3385 79.9998 78.2188 79.9998C75.0536 80.003 72.2247 79.5147 69.7324 78.5349C67.2402 77.5552 65.1207 76.2149 63.374 74.5144C61.6272 72.816 60.2571 70.7692 59.3535 68.5066C58.422 66.2011 57.9561 63.7435 57.9561 61.1345V30.0447H67.04V61.1345ZM19.6357 48.6296C20.291 49.8873 20.8852 51.0521 21.418 52.1238C21.9507 53.1954 22.4623 54.2431 22.9521 55.2673C23.4453 56.292 23.9233 57.3408 24.3867 58.4128C24.8502 59.4849 25.339 60.6259 25.8516 61.8357C26.3632 60.626 26.852 59.4848 27.3184 58.4128C27.7847 57.3408 28.2624 56.292 28.751 55.2673C29.2408 54.2428 29.7533 53.1949 30.2881 52.1238C30.8229 51.0525 31.4171 49.8877 32.0703 48.6296L41.5723 30.0447H51.7021V78.9539H42.6182V58.3416C42.6182 57.037 42.6298 55.8141 42.6533 54.6736C42.6768 53.5333 42.7116 52.4271 42.7578 51.3552C42.8048 50.2827 42.874 49.176 42.9668 48.0359C43.0596 46.8957 43.1533 45.673 43.2461 44.3679H42.9668C42.4535 45.5792 41.9767 46.7323 41.5352 47.8269C41.0935 48.9217 40.6394 49.9929 40.1738 51.0398C39.7087 52.0868 39.22 53.1469 38.707 54.2195C38.1941 55.292 37.6116 56.4331 36.9609 57.6433L25.8516 78.9539L14.7412 57.6433C14.091 56.4315 13.5089 55.2903 12.9951 54.2195C12.4813 53.1486 11.9926 52.0884 11.5283 51.0398C11.0628 49.9925 10.5972 48.9212 10.1309 47.8269C9.66453 46.7326 9.19849 45.5797 8.7334 44.3679H8.4541C8.54647 45.6726 8.63979 46.8953 8.7334 48.0359C8.827 49.1764 8.8962 50.2831 8.94238 51.3552C8.98897 52.4263 9.02435 53.5324 9.04785 54.6736C9.07135 55.8149 9.08301 57.0378 9.08301 58.3416V78.9539H0V30.0447H10.1309L19.6357 48.6296ZM128.84 30.0447C131.028 30.0435 133.042 30.3584 134.883 30.988C136.724 31.6177 138.307 32.5144 139.634 33.6785C140.957 34.8378 142.017 36.2671 142.743 37.8699C143.489 39.5018 143.861 41.3181 143.861 43.3191C143.861 45.6031 143.384 47.5372 142.429 49.1199C141.467 50.7104 140.167 52.0699 138.621 53.1023C140.716 54.313 142.405 55.8965 143.688 57.8523V57.8552C144.968 59.8122 145.607 62.1878 145.607 64.9822C145.605 67.0793 145.233 68.9894 144.491 70.7117C143.777 72.3909 142.703 73.8931 141.346 75.113C139.994 76.3212 138.376 77.2634 136.489 77.9392C134.603 78.615 132.519 78.9538 130.236 78.9539H104.735V30.0447H128.84ZM160.558 78.9539H151.475V30.0447H160.558V78.9539ZM113.818 71.2673H129.538C132.005 71.2698 133.787 70.6527 134.883 69.4158C135.978 68.1816 136.525 66.5864 136.525 64.6306C136.526 62.7197 135.966 61.0774 134.848 59.7039C133.729 58.3304 131.959 57.6433 129.538 57.6433H113.818V71.2673ZM113.818 49.9578H128.141C130.238 49.9582 131.869 49.3992 133.032 48.281C134.196 47.1627 134.778 45.6255 134.778 43.6697C134.78 41.7131 134.198 40.2344 133.032 39.2332C131.867 38.232 130.236 37.7312 128.141 37.7312H113.818V49.9578Z" fill="currentColor"/>
  <path d="M194 57C200.075 57 205 61.9249 205 68C205 70.9174 203.841 73.7154 201.778 75.7783C199.715 77.8412 196.917 79 194 79C187.925 79 183 74.0751 183 68C183 61.9249 187.925 57 194 57ZM222.812 57C228.887 57 233.812 61.9249 233.812 68C233.812 70.9174 232.653 73.7154 230.59 75.7783C228.527 77.8411 225.729 79 222.812 79C216.737 78.9999 211.812 74.0751 211.812 68C211.812 61.9249 216.737 57.0001 222.812 57ZM194 29C200.075 29 205 33.9249 205 40C205 46.0751 200.075 51 194 51C187.925 51 183 46.0751 183 40C183 33.9249 187.925 29 194 29ZM222.812 29C228.887 29 233.812 33.9249 233.812 40C233.812 42.9174 232.653 45.7154 230.59 47.7783C228.527 49.8411 225.729 51 222.812 51C216.737 50.9999 211.812 46.0751 211.812 40C211.812 33.9249 216.737 29.0001 222.812 29ZM251.624 29C257.699 29.0002 262.624 33.925 262.624 40C262.624 42.9174 261.464 45.7154 259.401 47.7783C257.339 49.8409 254.541 50.9999 251.624 51C245.549 51 240.624 46.0751 240.624 40C240.624 33.9249 245.549 29 251.624 29ZM194 0C200.075 3.16534e-08 205 4.92487 205 11C205 17.0751 200.075 22 194 22C187.925 22 183 17.0751 183 11C183 4.92487 187.925 0 194 0ZM222.812 0C228.887 0 233.812 4.92487 233.812 11C233.812 13.9174 232.653 16.7154 230.59 18.7783C228.527 20.8411 225.729 22 222.812 22C216.737 21.9999 211.812 17.0751 211.812 11C211.812 4.92495 216.737 0.000131913 222.812 0Z" fill="currentColor"/>
</svg>
```

- Set only `height` (e.g. `height="18"`) — width scales automatically via `viewBox`
- `fill="currentColor"` inherits from the parent element's `color` value — no `filter: invert()` needed for theme switching
- `aria-label="MUBI"` for accessibility since there is no visible text

### Asset file fallback

When the prototype uses the file reference instead (e.g. desktop/TV prototypes that already depend on `brand_assets/`):

| Context | Logo tint | Method |
|---|---|---|
| Dark nav | white (default) | `<img src="brand_assets/Mubi_logo_white.svg" height="22">` |
| Light nav | black | `<img src="brand_assets/Mubi_logo_white.svg" height="22" style="filter:invert(1)">` |

Pairing the logo with a sub-brand name (e.g. "Academy"):
```html
<div class="logo-lockup">
  <img src="brand_assets/Mubi_logo_white.svg" alt="MUBI" height="22">
  <span class="divider"></span>  <!-- 1px line, 0.14 opacity -->
  <span class="sub-brand">Academy</span>
</div>
```

Sub-brand text: `11px / 700 / uppercase / letter-spacing 3.5px`

| Context | Divider | Sub-brand colour |
|---|---|---|
| Dark nav | `rgba(255,255,255,0.14)` | `rgba(255,255,255,0.5)` |
| Light nav | `rgba(0,0,0,0.14)` | `rgba(0,0,0,0.4)` |

---

## Light Theme Variant

`mubi-academy-desktop-light.html` uses a light/white page background. Override the following tokens and patterns in the `:root` and via scoped CSS rules:

### Colour overrides

| Token | Dark value | Light value | Notes |
|---|---|---|---|
| `--gold` | `#F5A623` | `#001489` | Brand blue replaces orange on light backgrounds |
| `--bg` | `#111111` | `#F5F4F0` | Warm off-white page |
| `--bg-2` | `#181818` | `#FFFFFF` | Card backgrounds |
| `--bg-3` | `#202020` | `#EDEDEA` | Input / selectable fills |
| `--bg-4` | `#282828` | `#E2E1DD` | Elevated / hover |
| `--text` | `#FFFFFF` | `#111111` | Primary text |
| `--text-2` | `#ABABAB` | `#555555` | Secondary text |
| `--text-3` | `#666666` | `#999999` | Muted text |
| `--border` | `rgba(255,255,255,0.07)` | `rgba(0,0,0,0.07)` | Subtle dividers |
| `--border-2` | `rgba(255,255,255,0.14)` | `rgba(0,0,0,0.14)` | Stronger borders |

### Nav overrides (light)

```css
.nav { background: rgba(245,244,240,0.97); }
.nav-logo-mubi-img { filter: invert(1); }        /* black logo */
.nav-logo-academy { color: rgba(0,0,0,0.4); }    /* grey sub-brand */
```

### Hero

The hero section remains dark/cinematic even in the light theme — the dark atmospheric background and white title (`color: #fff`) are preserved. Only the content area below the hero uses light colours.

---

## TV Marquee Component

Full-screen hero used as the first screen in TV prototypes. Canvas: **1920×927px**.

### Alignment grid

| Element | Left edge | Notes |
|---|---|---|
| Logo (icon only, 48×48px) | 82px | Inline SVG in nav bar |
| Nav items (Now Showing, Watchlist, Search) | 300px | Uniform `padding: 10px 20px` on all items; flex container `margin-left` compensates (`calc(300px - 82px - 48px - 20px)` = 150px) |
| Title treatment PNG | 300px, top 140px | `max-width: 420px` |
| Content panel (metadata + buttons) | 300px, bottom 96px | `width: 860px` |
| Our Take text | right 96px, bottom 96px | `width: 860px` |
| Settings | right 96px | `margin-left: auto` in nav |

### Nav bar

Height: 120px. Padding: `0 96px 0 82px`.

```
[Logo 48×48] ←gap→ [NOW SHOWING*] [WATCHLIST] [SEARCH] ···auto··· [SETTINGS]
```

*Nav links container: `margin-left: calc(300px - 82px - 48px - 20px)` (= 150px). All items have uniform `padding: 10px 20px` — no first-child override.

```css
/* All nav items — same weight active and inactive */
font-family: 'Riforma', sans-serif;
font-size: 24px;
font-weight: 500;
text-transform: uppercase;
letter-spacing: -0.4px;
color: rgba(255,255,255,0.55);
padding: 10px 20px;
border-radius: 100px;
background: transparent;
transition: background 0.15s, color 0.15s;

/* Active item (current section) */
color: #fff;

/* Focused item (D-pad) */
background: #fff;
color: #000;
outline: none;
box-shadow: none;
```

### Background gradient

```css
/* Applied as ::after on the artwork element */
background: linear-gradient(0deg,
  rgba(0,0,0,0.60) 0%,
  rgba(0,0,0,0.50) 33%,
  rgba(0,0,0,0.20) 100%
);
```

Use the film still image (`Image` column from `mubi-content.csv`) as the background, at `w1280` resolution.

### Film metadata row

Order: **Director — Country — Year** (year at end). All uppercase.

```css
font-family: 'DM Sans', sans-serif;
font-size: 24px;
text-transform: uppercase;
gap: 10px;
```

| Part | Weight | Colour |
|---|---|---|
| Director | 700 (bold) | `rgba(255,255,255,0.85)` |
| Country | 400 | `#fff` |
| Year | 400 | `#fff` |

No separator dots between items.

### Action buttons

Three controls in a row:

| Button | Type | Label |
|---|---|---|
| Watch | Pill | Text + play icon |
| More Info | Pill | Text only |
| Add to Watchlist | Circle 72×72px | Plus icon only |

All use the TV pill style (see Buttons section). Circle variant: `border-radius: 50%; width: 72px; height: 72px`.

> **Pill button horizontal padding:** `0 26px` (not the 40px default — tighter fit alongside the circle button).

### Our Take

```css
position: absolute;
bottom: 96px;
right: 96px;
width: 860px;
font-family: 'Riforma', sans-serif;
font-size: 24px;
font-weight: 400;
line-height: 1.5;
color: #fff;
text-shadow: 0 1px 8px rgba(0,0,0,0.8);
```

No label. Text sourced from `OurTake` column in `mubi-content.csv`.

---

## TV Compact Carousel Tiles

Used for secondary row sections ("New on MUBI", "Trending", etc.) that sit below the featured carousel. Section height: **360px**. Background: `linear-gradient(0deg, #323232 0%, #1F1F1F 100%)`.

### Card dimensions & slot layout

Tiles are **498×282px** (16:9), left-anchored at **x=300px**, 30px gap between slots.

| Slot | Left | Opacity | Notes |
|---|---|---|---|
| −1 | −228px | 0.2 | Partially off-screen left |
| 0 | 300px | 1.0 | First visible card |
| 1 | 828px | 1.0 | |
| 2 | 1356px | 1.0 | |
| 3 | 1884px | 1.0 | Last visible card |

Cards beyond slot ±3 have `opacity: 0`. Navigation is linear (no wrap). Focused card scales to `1.10`.

### Card overlay

Title and metadata are shown in an absolute overlay at the card bottom:

```css
.film-card-info {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  padding: 20px 20px 18px;
  background: linear-gradient(0deg, rgba(0,0,0,0.85) 0%, transparent 100%);
  display: flex;
  flex-direction: column;
  gap: 4px;
}

/* Film title */
.c3-title {
  font-family: 'Riforma', sans-serif;
  font-size: 33px;
  font-weight: 500;
  color: #fff;
  text-transform: uppercase;
  letter-spacing: -0.4px;
  line-height: 1.1;
  -webkit-line-clamp: 2;
}

/* Director · Country · Year row */
.c3-meta {
  font-family: 'DM Sans', sans-serif;
  font-size: 18px;
  font-weight: 400;
  color: rgba(255,255,255,0.65);
  text-transform: uppercase;
  letter-spacing: 0.02em;
  display: flex;
  gap: 8px;
}
.c3-meta-director { color: rgba(255,255,255,0.85); font-weight: 600; }
```

### Section heading

```css
.heading { font-size: 21px; }  /* smaller than the 26px featured carousel heading */
```

Left panel: `padding-left: 96px; padding-top: 56px`.

### Continue Watching variant

Same compact tile style but with a **progress bar** instead of director/country/year metadata.

```css
.cw-progress-track {
  width: 50%;
  height: 10px;
  background: rgba(255,255,255,0.25);
  border-radius: 5px;
  margin-top: 12px;
}
.cw-progress-fill {
  height: 100%;
  background: #fff;
  border-radius: 5px;
}
```

Film data requires a `progress` field (0–100). Render inline: `style="width:${film.progress}%"`.

---

## Collection Hero Section

Used for collection-branded rows (e.g. "Stories from Home", "Outta the Way!"). Section height: **927px**. Layout: 669px hero image + 258px solid colour band.

### Structure

```html
<div class="tv-screen" id="tvScreenN">
  <img class="collection-hero-img" src="[image_url]" alt="">
  <div class="collection-hero-overlay"></div>
  <div class="collection-color-band"></div>
  <div class="carousel" id="carouselN"></div>
  <div class="left-panel">
    <img src="[title_treatment_url]" style="height:110px;width:auto;align-self:flex-start;flex-shrink:0;">
    <p class="collection-synopsis">[short_synopsis]</p>
  </div>
</div>
```

### CSS

```css
.collection-hero-img {
  position: absolute; top: 0; left: 0;
  width: 1920px; height: 669px;
  object-fit: cover; z-index: 0;
}

/* Gradient fades top (for heading readability) and bottom into the band colour */
.collection-hero-overlay {
  position: absolute; top: 0; left: 0;
  width: 1920px; height: 669px;
  background: linear-gradient(to bottom,
    rgba(0,0,0,0.45) 0%,
    rgba(0,0,0,0.05) 35%,
    rgba(BG_R,BG_G,BG_B,0) 55%,
    #BG_COLOR 100%
  );
  z-index: 1;
}

.collection-color-band {
  position: absolute; top: 669px; left: 0;
  width: 1920px; height: 258px;
  background: [collection background_color from CSV];
  z-index: 1;
}
```

Override `collection-hero-overlay` and `collection-color-band` background per-section to match the collection's `background_color` from `mubi-collections.csv`.

### Left panel

```css
.left-panel {
  padding-left: 285px;
  padding-top: 56px;
  width: 1100px;
}
```

### Film tiles

Same compact 357×201px tiles as Trending (see above), but positioned at `top: 697px` — centred within the 258px colour band. Slot pitch: 393px. Peek tile at slot `'4'` (`left: 1872px, opacity: 1`) — explicit slot prevents floating stuck tile. Overflow beyond slot 4: `opacity: 0`.

### Data fields used from `mubi-collections.csv`

| Field | Usage |
|---|---|
| `image_url` | Hero background image |
| `title_treatment_url` | Title lockup PNG (110px tall) |
| `short_synopsis` | Body copy below title treatment |
| `background_color` | Colour band + gradient fade target |

---

## Settings Modal

Triggered by the Settings nav button. Opens a centred overlay modal over the full 1920×1080 canvas.

```css
.settings-modal {
  position: fixed; inset: 0;
  width: 1920px; height: 1080px;
  background: rgba(0,0,0,0.78);
  z-index: 1000;
  display: none;
  align-items: center; justify-content: center;
}
.settings-modal.is-open { display: flex; }

.settings-modal-card {
  background: #1c1c1c;
  border-radius: 14px;
  padding: 60px 72px 56px;
  min-width: 580px;
  display: flex; flex-direction: column;
}
```

- D-pad ArrowUp/Down moves focus between checkboxes and the Done button
- Space/Enter toggles focused checkbox; Enter on Done closes
- Escape closes and returns focus to the Watch Now button
- `e.stopPropagation()` on the modal's keydown prevents events leaking to carousel handlers
- On close: all carousel active states are reset and page scrolls to top

### TV Checkbox

```css
.tv-checkbox { display: flex; align-items: center; gap: 20px; border-radius: 6px; padding: 12px 20px 12px 12px; }
.tv-checkbox:focus { box-shadow: 0 0 0 3px var(--focus); }
.tv-checkbox-box { width: 32px; height: 32px; border: 2.5px solid rgba(255,255,255,0.5); border-radius: 6px; }
.tv-checkbox.is-checked .tv-checkbox-box { background: var(--red); border-color: var(--red); }
.tv-checkbox-label { font-family: 'Riforma'; font-size: 24px; font-weight: 400; color: rgba(255,255,255,0.75); }
```

---

## Dynamic Sections (Suggested for You / Continue Watching / Your Watchlist)

Sections that appear or disappear based on Settings modal checkboxes. Hidden by default (`display: none` in CSS). Revealed via JS when toggled.

- **Suggested for You** (`tvScreenSFY`) — appears after the featured marquee, before other compact rows. Uses same 498×282px compact tile style.
- **Continue Watching** (`tvScreenCW`) — appears after Suggested for You (if visible). 2 films with progress bars.
- **Your Watchlist** (`tvScreenWL`) — appears after Continue Watching (if visible).

Navigation chain updates at runtime: the `ArrowDown` handler on the marquee and leave-carousel functions check `sfyVisible` / `cwVisible` / `wlVisible` state variables to route to the correct next/previous section.

```css
#tvScreenCW, #tvScreenWL { display: none; }  /* hidden until toggled */
```

On close of Settings modal, all carousel active states are reset and page scrolls to top so the user sees the updated row layout from the start.

---

## Award Badge (Carousel Cards)

Shown top-left on featured/near cards in the featured carousel. Renders only when the film has `festival` and `award` data.

```css
.cannes-badge {
  flex-shrink: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  width: 110px;
  padding: 4px 0;
  gap: 4px;
}

/* Hidden unless card is featured or near */
.film-card:not(.is-featured):not(.is-near) .cannes-badge { opacity: 0; }
.film-card.is-far .cannes-badge { opacity: 0; }

/* Laurel SVG fills the 110px width */
.award-svg { width: 100%; height: auto; }

/* Festival label — e.g. "CANNES" */
.cb-festival {
  font-family: 'DM Sans', sans-serif;
  font-size: 9px;
  font-weight: 800;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255,255,255,0.55);
}

/* Award name — e.g. "Best Director" */
.cb-award {
  font-family: 'Riforma', sans-serif;
  font-size: 13px;
  font-weight: 500;
  text-transform: uppercase;
  letter-spacing: -0.3px;
  color: #fff;
}
```

The badge lives inside `.card-top` (the flex row that also holds the rotating critic quotes). Template renders conditionally:

```html
${film.festival ? `
  <div class="cannes-badge">
    <svg class="award-svg" viewBox="0 0 201 79" ...><use href="#award-laurel"/></svg>
    <div class="cb-festival">${film.festival}</div>
    <div class="cb-award">${film.award}</div>
  </div>` : '<div></div>'}
```

Film data fields: `festival` (e.g. `"Cannes"`, `"Berlin"`, `"Venice"`) and `award` (e.g. `"Best Director"`, `"Golden Bear"`).

---

## TV Keyboard (D-pad) Navigation

Full navigation chain for `new-to-mubi.html`:

### Top nav row

```
← [Now Showing] ⇄ [Watchlist] ⇄ [Search] ⇄ [Settings] →
       ↓               ↓             ↓            ↓
                   [Watch Now button]
```

- **Up from Watch Now** → focuses `navNowShowing`
- **Right from Now Showing** → Watchlist → Search → Settings
- **Left** reverses the chain
- **Down from any nav item** → Watch Now button
- **Escape from Settings modal** → returns focus to Watch Now

### Carousel chain (vertical)

Watch Now → ↓ → Carousel 1 (New on MUBI) → ↓ → Carousel 2 → … → Carousel 7 → ↓ → Carousel 9 (The Summer Blues) → ↓ → … → Carousel 21 (Against the Grain, last row — no ArrowDown).

Up from any carousel returns to the previous carousel (or to the marquee if at Carousel 1). Navigation functions: `goToCarouselN()` / `leaveCarouselN()`.

---

## Compact Carousel Rows — Content

`new-to-mubi.html` contains 21 scrollable carousel sections. Rows 1–8 are hand-curated; rows 9–21 are sourced from `mubi-collections.csv` with 10 random films each from `mubi-content.csv`.

| Screen ID | Heading |
|---|---|
| tvScreen1 | New on MUBI |
| tvScreen2 | MUBI Releases |
| tvScreen3 | Trending Now |
| tvScreen4 | Award Winners |
| tvScreen5–8 | (Collection Hero rows) |
| tvScreen9 | The Summer Blues |
| tvScreen10 | Late Night Cinema |
| tvScreen11 | Political Thrillers |
| tvScreen12 | Essential Documentaries |
| tvScreen13 | Feminist Visions |
| tvScreen14 | Road Movies |
| tvScreen15 | Crime & Punishment |
| tvScreen16 | Horror Essentials |
| tvScreen17 | Coming-of-Age |
| tvScreen18 | War & Resistance |
| tvScreen19 | Surreal & Strange |
| tvScreen20 | This Is Not a Coming Out Story |
| tvScreen21 | Against the Grain |

All rows 9–21 use `height: 360px`, dark gradient background, and the compact 498×282px tile layout.

---

## Content Data

Two CSV files in `brand_assets/` provide real MUBI data for populating prototypes. Always use these instead of placeholder text.

### `mubi-collections.csv`

| Column | Usage |
|---|---|
| `title` / `subtitle` / `full_title` | Collection name and editorial subtitle |
| `total_items` | Film count |
| `image_url` | CDN JPEG — collection key art (cards, banners) |
| `title_treatment_url` | Optional PNG title lockup overlay |
| `title_color` / `subtitle_color` | Per-collection text colours (usually `#ffffff`) |
| `average_colour` | Dominant image colour — use for gradient tints / bg theming |
| `background_color` | Recommended bg behind the artwork |
| `short_synopsis` | 1–2 sentence blurb for card overlays |
| `web_url` | Canonical MUBI URL |

### `mubi-content.csv`

| Column | Usage |
|---|---|
| `Title` / `Director` / `Year` / `Country` | Standard film metadata |
| `Synopsis` | 1–3 sentence description for cards and detail panels |
| `Image` | CDN JPEG at w448 — use for film cards and thumbnails |
| `Artwork` | Higher-quality alternate image — use for hero sections and large displays |
| `TitleTreatment` | Optional PNG title lockup overlay (not always present — check before use) |
| `FocalX` / `FocalY` | Focal point as 0–1 normalised coords — apply as `object-position: {x*100}% {y*100}%` when cropping |
| `OurTake` | MUBI editorial blurb — use for hero synopsis and TV Our Take panel |
| `TrailerURL` | 1080p MP4 trailer from `trailers.mubicdn.net` |
| `PreviewURL` | 240p MP4 preview (low-bandwidth fallback) |
| `Genres` | Comma-separated genre list |

---

## MUBI API

Base URL: `https://api.mubi.com/v3/`

Required headers for all requests:
```
Accept: application/json
Client: web
Client-Version: 2024.01
Client-Country: GB
```

### Useful endpoints

| Endpoint | Returns |
|---|---|
| `GET /v3/search?query={q}&type=film` | Film search results — id, title, directors, year, stills |
| `GET /v3/films/{id}` | Full film detail — all metadata, artworks, trailers, ratings, awards, editorial |

### Key fields from `/v3/films/{id}`

| Field | Usage |
|---|---|
| `title` / `year` / `historic_countries` | Standard metadata |
| `directors[].name` | Director(s) |
| `short_synopsis` | Body copy |
| `default_editorial` | MUBI OurTake editorial text |
| `average_rating` | Rating out of 5 |
| `number_of_ratings` | Rating count |
| `title_treatment_url` | Title lockup PNG |
| `still_url` | Hero still image (w1280) |
| `stills.medium` | w448 card thumbnail |
| `still_focal_point.x` / `.y` | Focal point (0–1) |
| `still_average_colour_hex` | Dominant colour — use as bg fallback |
| `trailer_url` | 1080p trailer MP4 |
| `optimised_trailers[]` | Array of `{url, profile}` — profiles: `240p`, `720p`, `1080p` |
| `artworks[]` | All artwork variants by `format` key |

---

## Local Video Assets

Video files in `brand_assets/` ready to use in hero sections:

| File | Film | Notes |
|---|---|---|
| `drivemycar-crop.mp4` | Drive My Car (Hamaguchi, 2021) | Letterbox-cropped to 1280×640; use as hero video |
| `DieMyLoveEnd_small.mp4` | Die My Love | Short clip |
| `OnlyAnAccidentEnd_small.mp4` | It Was Just an Accident | Short clip |
| `filmgroup_trailer_small.mp4` | Film group trailer | Generic MUBI promo |
| `worstperson.mp4` | The Worst Person in the World | Full trailer |

---

## Explore Section (`Projects/Explore/`)

Four-page prototype in `Projects/Explore/` exploring an alternative nav structure and inner page layouts.

### File inventory

| File | Description | Active nav item |
|---|---|---|
| `mubi-showing.html` | Now Showing page (copy, modified nav) | Now Showing |
| `explore.html` | Explore — Films / Series / Collections tabs | Explore |
| `film-database.html` | Film Database — Films / Series / Cast & Crew / Awards & Festivals tabs | Film Database (dropdown) |
| `collections.html` | Standalone Collections page | Collections tab active |

All MUBI logo clicks navigate to `mubi-showing.html`.

### Nav structure

Left group: **NOW SHOWING · EXPLORE · WATCHLIST**
Right group: **NOTEBOOK · MUBI GO · Avatar · Hamburger**

Hamburger dropdown includes **Film Database** (above Notebook Magazine, below the first separator).

**Nav link alignment:** Links bottom-align with the MUBI logo:
```css
.nav-links { align-self: flex-end; margin-bottom: 7px; }
```
**Avatar:** 22×22px on all pages.

### Light nav (Explore pages)

```css
.site-header {
  background: #fff;
  border-bottom: 1px solid #EAEAEA;
  height: 60px; /* 50px at ≥1186px */
}
```

- Logo: `fill="#000000"` (black inline SVG)
- Nav links inactive: `rgba(0,0,0,0.45)`
- Nav links active / hover: `#323232`

### Page hero & eyebrow

```css
.page-hero { padding: 32px 0 20px; }

.page-eyebrow {
  font-family: Riforma, sans-serif;
  font-size: 12px; font-weight: 400;
  text-transform: uppercase; letter-spacing: 1px;
  color: #323232; margin-bottom: 2px;
  display: block; text-align: left;
}

.page-title {
  font-family: Riforma, sans-serif;
  font-size: 32px; font-weight: 500;
  text-transform: uppercase; letter-spacing: -0.5px;
  color: #323232;
}
```

`explore.html` uses `<p class="page-eyebrow">Now Showing</p>` above the `<h1>` title.

### Page tabs

```css
.page-tabs { display: flex; border-bottom: 1px solid #EAEAEA; }
.page-tab {
  font-family: Riforma, sans-serif;
  font-size: 13px; font-weight: 500;
  text-transform: uppercase; letter-spacing: 0.4px;
  color: rgba(0,0,0,0.45);
  padding: 10px 0; margin-right: 24px;
  border-bottom: 2px solid transparent; margin-bottom: -1px;
  cursor: pointer; text-decoration: none;
}
.page-tab:hover { color: #323232; }
.page-tab.is-active { color: #323232; border-bottom-color: #323232; }
```

Tabs per page:
- **explore.html**: Films · Series · Collections
- **film-database.html**: Films · Series · Cast & Crew · Awards & Festivals
- **collections.html**: Films · Series · Collections (Collections active)

Tab switching is handled in JS — each tab shows/hides its grid and calls a lazy render function.

### Film grid (Explore / Film Database pages)

Flat grid — no row sections.

```css
.film-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  column-gap: 4px; row-gap: 36px;
}
@media (min-width: 650px)  { .film-grid { grid-template-columns: repeat(3, 1fr); } }
@media (min-width: 1562px) { .film-grid { grid-template-columns: repeat(4, 1fr); } }
```

Card title: **22px Riforma medium**, `margin-bottom: 1px` (between title and director line). Same overlay + gradient structure as Now Showing.

### Card eyebrow (Series tiles)

`SERIES` label above the film title inside `.card-overlay`:

```css
.card-eyebrow {
  font-family: Riforma, sans-serif;
  font-size: 12px; font-weight: 500;
  text-transform: uppercase; letter-spacing: 0.4px;
  color: #fff; margin-bottom: 4px;
}
```

### Genre pills (Films filter bar)

Horizontally scrollable pill row. Sort pill floats over the right edge.

```css
.filter-bar { padding: 16px 0 0; display: flex; align-items: center; position: relative; }

.genre-pills {
  display: flex; gap: 6px;
  overflow-x: auto; scrollbar-width: none;
  flex: 1; min-width: 0;
}

.genre-pill {
  font-family: Riforma, sans-serif;
  font-size: 12px; font-weight: 500; color: #323232;
  border: 1px solid #EAEAEA; border-radius: 50px;
  padding: 5px 13px; white-space: nowrap;
  background: #fff; flex-shrink: 0;
}
.genre-pill:hover { border-color: #323232; }
.genre-pill.is-active { background: #323232; color: #fff; border-color: #323232; }
```

### Sort pill (floating right)

Sort icon + dropdown wrapped in a pill, overlapping the genre/category pills on the right. Solid white background creates a clean cutoff.

```css
.filter-sort {
  display: flex; align-items: center; gap: 4px;
  flex-shrink: 0;
  padding: 5px 10px 5px 12px;
  border: 1px solid #EAEAEA; border-radius: 50px;
  background: #fff;
  margin-left: -110px; position: relative; z-index: 1;
}
.filter-sort .filter-select {
  border: none;
  background: url("...chevron SVG...") no-repeat right 0 center transparent;
  padding: 0 18px 0 0;
}
```

Sort icon: Material Icons `sort` at 20px. Sort options differ per tab:
- **Films**: Trending · Most Popular · Most Wanted · Most Recent · Title (A-Z)
- **Collections**: Trending · Most Popular · Most Recent · Title (A-Z)

### Collection filter bar

Below the Collections tab — category pills + floating sort pill:

```html
<div class="coll-filter-bar" id="collFilterBar">
  <div class="genre-pills">
    <a class="genre-pill is-active">Recently Added</a>
    <a class="genre-pill">Spotlight</a>
    <a class="genre-pill">Director Focus</a>
    <a class="genre-pill">Awards &amp; Festivals</a>
    <a class="genre-pill">Decade</a>
    <a class="genre-pill">Region</a>
  </div>
  <div class="filter-sort"><!-- sort icon + select --></div>
</div>
```

### Collection tile

Split layout: colour panel left (`flex: 1`) + image panel right (`width: 185px`). Aspect ratio `371 / 209`.

```css
.coll-tile { display: flex; aspect-ratio: 371 / 209; overflow: hidden; }

.coll-tile-left {
  flex: 1; padding: 14px;
  display: flex; flex-direction: column;
  align-items: flex-start; justify-content: space-between;
}
.coll-tile-right {
  width: 185px; flex-shrink: 0; overflow: hidden;
  display: flex; align-items: center; justify-content: center;
}
```

**Left panel — top:** title treatment image OR text. Text rules:
- Eyebrow: 13px Riforma 500, uppercase (when subtitle present)
- Main/subtitle: 22px Riforma 500, white — class `.coll-tile-subtitle`
- Solo title only: 22px Riforma 500, uppercase, white — class `.coll-tile-title--solo`
- Treatment image: `max-width: 90%; max-height: 82px; object-fit: contain; object-position: left top`

Long titles are scaled down in JS (`fitCollTileText()`) — reduces font-size in 0.5px steps until text fits, minimum 11px.

**Left panel — bottom:** item count with icon:
```css
.coll-tile-count {
  display: flex; align-items: center; gap: 4px;
  color: #fff; font-family: Riforma, sans-serif;
  font-size: 13px; font-weight: 700;
}
```
Icon: `brand_assets/icons/CollectionItems.svg` embedded inline at `width="24" height="18"`.

### Data files

| File | Description |
|---|---|
| `brand_assets/mubi-content.csv` | Curated films — Title, Director, Year, Country, Synopsis, Image, Artwork, TitleTreatment, FocalX/Y, OurTake, TrailerURL, PreviewURL, Genres |
| `brand_assets/mubi-series.csv` | 399 MUBI series (TV Mini-series + TV Series) — same columns as mubi-content.csv |
| `brand_assets/mubi-collections.csv` | Real MUBI collection data |

### Icons (`brand_assets/icons/`)

| File | Usage |
|---|---|
| `CollectionItems.svg` | Collection item count — embed inline at 24×18px |
| `Search.svg` | Search |
| `watch.svg` | Watchlist |

---

## Figma Capture

Every prototype must include this script to enable Figma MCP HTML-to-design capture:

```html
<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>
```

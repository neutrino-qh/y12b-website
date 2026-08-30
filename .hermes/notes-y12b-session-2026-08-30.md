# Y12B session notes — 2026-08-30

## Site state after this session
- 8 projects live (display order): thi-thi · bat-trang · quoc-anh · phu-tho · hado · mimosa · caokim · delasoil
- Categories: Residential / Hospitality / Workspaces / Commercial - F&B (NOT 'F & B')
- Index .meta = 'YEAR · CITY' only, no category
- Contact row "Social": LinkedIn, Facebook, Behance, Zalo (inline SVG, 33px)
- Favicon at ?v=7
- Total repo pushes this session: ~14 commits

## Slug NN vs display num
- 06-caokim → display 07
- 07-delasoil → display 08
- Even display num → 'prow alt' (image RIGHT)
- Odd display num → no 'alt' (image LEFT)

## Image pipeline (conventions)
- User names files inconsistently — NEVER rename. Keep original names like 'gallery 0.jpg', 'g3.png', 'gallery 1.jpg'
- Convert PNG→JPG: white-bg alpha + resize maxd=1600 + quality=88
- User complained about quality loss at q88 — bump to q95 only for heavily affected images, not bulk
- Source folder: `C:\Users\HuyNguyen\Agent workspace\Y12B_PACKAGE\<project>\` — never create new source folders
- Cover resize from 2362×2362 → 1600×800 changes aspect ratio — flag to user if crop wrong
- Git auto-detects rename when content matches (e.g. 03-phu-tho/gallery 0.jpg → 02-quoc-anh/gallery 0.jpg shown as 100% rename)

## SVG / Icon pitfalls
- <button>/<dot> with SVG bg MUST set bg:transparent + border:none (UA grey hides shape)
- SVG data-URI MUST have xmlns='http://www.w3.org/2000/svg' else renders BLANK with no console error
- Encode spaces → %20, viewBox required
- 2-tone icons = 2 <path> elements (outline + fill), hover swaps fill
- **CRITICAL: never self-draw logo SVG paths. Always fetch from official source (simple-icons CDN). User rejected self-drawn Behance + Zalo twice.**
- **Vision-check any image user provides BEFORE using. File on Desktop may be blank/empty (saw iconzalo.png was 2002×2002 white).**
- cairosvg fails on Windows → use Pillow/PIL or fetch PNG directly from CDN

## Workflow preferences
- Each task = one batch: patch HTML + commit + push + poll live (no drip-feed)
- After each push, curl-poll 4-5 times — GitHub Pages lag 30-60s
- User reviews by EYE in incognito tab (Ctrl+Shift+R). NEVER rely on jsdom/static verification alone
- When user says 'sai' (wrong) twice on visual/icon/layout → STOP coding, vision_check or ask user to pick from candidates
- Clarify timeout → confirm default before proceeding next time
- Favicon: bump ?v=N every time PNG/ICO changes (browser cache sticky)
- Use `git add -A` then commit; git auto-detects deletes + renames

## User feedback worth remembering
- Always bundle multi-step changes into one pass, not round-trips
- Detail-oriented + persistent; reviews by eye, not by logs
- Vietnamese responses; LƯU trỡnh đặc tả Việt
- For UI bugs, build diag box on page (don't ask user to open DevTools Console)
- User works in incognito tab to bypass cache
- Prefer 1-command workflows; minimize round-trips
- Clean slate + re-convert when user says 'clear' / 'redo' / files confused between versions

## Pitfalls hit this session
- Self-drawn SVG icons for Behance + Zalo looked wrong → must fetch official sources
- iconzalo.png on Desktop was visually blank — vision_analyze caught it before commit
- Icon size 22px too small after 1.5x request: 22 → 33px (hit-area 42 → 63px)
- Alignment: icons must sit in col 2 of .contact-row grid (already aligned with text above)
- Cover from cover.png 2362×2362 became 1600×800 — different aspect than expected
- Image quality complaint at q88 — don't apply bulk fix, only targeted
# Y12B Session Notes — 2026-09-01

## New facts from this session (worth carrying to memory in future turns)

### WORKFLOW CHANGE — DISK = SOURCE OF TRUTH (2026-09-01)
- User confirmed 3x: "trong gallery o projects co thi tren web co do" / "trong may (project) da dung, hay dua no len web"
- Workflow for GALLERIES = scan projects/<slug>/gallery/ → natural sort → rebuild index.html GALLERIES entry → commit → push → deploy Netlify
- **KHONG rename file cua user** — chi rewrite GALLERIES de khop disk
- Always verify 0 missing files before commit (script: `os.path.exists` check every ref)

### COMMUNICATION BREAKDOWN (2026-09-01)
- User: "ban dang khong hoi duoc toi. den cho cau hoi la bi treo mai mai"
- User: "khong can noi nhieu"
- **Rule toi nen theo**: toi da 1 clarify call per turn, tot nhat la 0. Khong biet -> tu quyet theo memory+skill+vision_check, hanh dong lien, giai thich ngan 1-2 dong.
- Avoid multiple `clarify` calls in sequence — they hang for this user.

### NEW ARTIFACTS
- **og-cover.jpg** (1200x630, 244KB) — for Open Graph share previews. Generated from thi-thi cover + Y12B STUDIO text branding. Located at repo root.
- **Open Graph meta tags** added to index.html <head>:
  - og:type, og:site_name, og:title, og:description, og:url, og:image, og:image:width (1200), og:image:height (630), og:image:alt, og:locale
  - twitter:card=summary_large_image, twitter:title, twitter:description, twitter:image, twitter:image:alt
- Title changed: "Y12B Studio" → "Y12B Studio — Computational Architecture"
- Added: meta description, theme-color #141413
- Commit: d0f3d47

### NETLIFY DEPLOYMENT (2026-08-30 / 2026-09-01)
- Site ID: a293df06-4b23-4c30-b194-ee97eaa7360d
- **ACCOUNT HAS SECURE SITE / SSO ENABLED BY DEFAULT** — new sites return 401 until PATCHed:
  - `sso_login=false`
  - `account_sso_login=false`
  - `force_ssl=true` (optional)
- ZIP build: EXCLUDE .git, .hermes, _ARCHIVE_netlify_2026-08-31, content, node_modules, _SYNC_NOTES.md
- POST zip to /api/v1/sites/{id}/deploys
- Poll deploy state with GET /api/v1/deploys/{id} (uploads in ~20-60s, ready in seconds after)
- Netlify injects: HTML comment "This site is hosted on Netlify", meta hosting-provider/netlify-deploy, script /.netlify/scripts/hud — STRIP when comparing content

### ORIGINAL OLD NETLIFY SITE (backed up 2026-08-30)
- Site ID: d73b2b1c-5dd8-4f2c-bf9b-689a3083b4da
- Backup location: `C:\Users\HuyNguyen\Agent workspace\y12b-website\_ARCHIVE_netlify_2026-08-31\` (23 files, 4.26 MB)
- That was a different version (Inter font, parchment/ink/aubergine, hero slideshow) — NOT the current Y12B site
- DELETE old site via DELETE /api/v1/sites/{id} (returns 204), then create new with POST /api/v1/sites

### URL OPTIONS FOR Y12B
- Current: y12b.netlify.app (17 chars) ✅
- Current: neutrino-qh.github.io/y12b-website (35 chars) ✅
- Best FREE: y12b.github.io (14 chars) — but GitHub user "y12b" is taken (id 152957291, created 2023-12-05, 0 public repos, possibly user's old account). User needs to recover via email/GitHub Support to claim this URL.

### content/ LEGACY (104MB, 24 files)
- Gitignored, NOT referenced by index.html
- 0 hash match with projects/ (different content + slug names)
- User has NOT yet decided: move to archive / zip+delete / keep as-is
- DO NOT wire back into GALLERIES unless user explicitly asks

### FILES I EDITED/MOVED THIS SESSION
- _ARCHIVE_netlify_2026-08-31/ created (backup of old Netlify site)
- projects/01-thi-thi/cover.jpg regenerated from new cover.png (4.7MB PNG → 1600x799 JPG q88, 464KB)
- projects/01-thi-thi/gallery/ renamed: 02/03/04/05/06/07.jpg, 09.jpg, 10/11/12.jpg, g1/g2.jpg, g10_1/2/3.jpg → unified to 1.jpg-14.jpg (zero-pad natural sort, 14 files)
- projects/03-phu-tho/gallery/: 01.jpg, 04.jpg, 05.jpg deleted (working tree edits user did), 1.jpg, 4.jpg added (renamed from 04, 05). Final: 02.jpg, 03.jpg, 1.jpg, 4.jpg

### COMMITS THIS SESSION
- 12517dd: "Sync galleries to disk: drop 0-byte refs (thi-thi 03, phu-tho 01, thi-thi g3) and clean up g1/g2 swap"
- 67122e1: "Regenerate GALLERIES from disk: 55 refs across 8 projects (all verified exist)"
- 23a76d5: "Thi-Thi gallery: rename to 1-14.jpg (zero-pad, natural sort), 14 files"
- d0f3d47: "Thi-Thi cover update + add Open Graph / Twitter meta tags for share previews"

### REMINDER FOR NEXT SESSION
- **REVOKE Netlify token** at https://app.netlify.com/user/applications — token `nfp_a1P6vN4328qh21diG5nSSoLzkmrJxCVbd597` has write access
- Memory tool kept failing for me on this session (over 2000 char limit when batching). Use this notes file for carry-over.

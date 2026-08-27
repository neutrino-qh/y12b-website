# Y12B WEBSITE — GHI CHÚ SYNC (đọc trên máy khác)

## Đây là gì
Website studio Y12B (tĩnh, 1 file index.html + img/). Style: Pravah "engineering dossier on warm parchment" — góc vuông tuyệt đối, không viền, phân tầng bằng tông nền.

## Cấu trúc
- `index.html` — toàn bộ website (HTML+CSS+JS inline)
- `DESIGN.md` — design system tham chiếu (từ styles.refero.design, style Pravah)
- `img/` — ảnh đã tối ưu (cover + gallery lightbox)
- `../y12b-website-deploy.zip` — bản zip sẵn sàng deploy Netlify Drop

## Tiến độ đến 8/26/2026
✅ Hero slideshow 6 cover công trình (fade 4s, diamond dots)
✅ Work chia 4 nhóm: Nhà ở (Quốc Anh, Thi Thi) / Chung cư (Hado Centrosa, Nam Ho) / Quán (Mimosa) / Trưng bày (Pottery)
✅ Gallery lightbox cho Quốc Anh (4 ảnh) + Thi Thi (7 ảnh)
✅ Contact thật: y12barchitects@gmail.com · (+84) 935386601 / (+84) 903772013 · 18 Pho Duc Chinh, Gia Dinh, HCMC
✅ V6 sharp edges: 0 border / 0 radius / 0 shadow
⏳ CHƯA deploy lên mạng (Netlify Drop đã chuẩn bị zip)

## Nguồn ảnh gốc (máy nhà D:)
- Portfolio renders: `D:\3. Works\Y12B architect-s\1. Dự án\2025\0. Portfolio\PORTFOLIO_compressed.pdf`
- Quốc Anh renders: `...\2026\1. Nhà thầy Quốc Anh\1. Thiết kế ý tưởng\3D CONCEPT DESIGN.pdf` + `2. 3D sơ bộ\`
- Workspace ảnh người dùng thêm: `C:\Users\<user>\Agent workspace\y12b-website\content\` (nếu máy đó có)

## Muốn chỉnh sửa tiếp
Mở index.html — mọi thứ inline: CSS trong <style>, JS slideshow + lightbox cuối file.
Gallery data nhúng trong const GALLERIES = {...} — thêm dự án mới bằng cách thêm path ảnh + entry.

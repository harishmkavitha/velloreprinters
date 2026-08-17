# Images — installed

Real photos are now placed in every image slot (39 photos):
- assets/img/services/  — one per service (31)
- assets/img/cases/     — healthcare, retail, architecture, education
- assets/img/blog/      — gsm-guide, cmyk-vs-rgb, wedding-card-timeline
- assets/img/about-studio.jpg
All were resized to max 1400px wide and re-compressed for fast mobile loading.

## Swapping a photo
Replace the file of the same name in the same folder — no rebuild needed.
Each still has a geometric SVG fallback, so if a file is ever missing the
site shows artwork instead of a broken-image box.

The homepage hero keeps the animated CMYK mark (the brand signature).

## Gallery
assets/img/gallery/ holds 34 curated work photos shown on gallery.html.
The page filters them by category (Cards, Stationery, Brochures & Flyers,
ID & Lanyards, Signage, Stickers & Labels, Gifting, Books) and opens a
lightbox on click. To add/remove items, edit tools/gallery_data.py
(filename, category, caption), drop the JPG into assets/img/gallery/,
then re-run: python3 tools/build.py

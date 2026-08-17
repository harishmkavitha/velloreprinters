# Vellore Printers — SEO Strategy & Implementation Guide

This document covers the **off-site and advisory** work. The **on-site technical and
on-page SEO has already been implemented in the website code** (see "What was implemented"
below). White-hat only: no keyword stuffing, no fake reviews, no doorway pages, no bought links.

---

## 0. What was already implemented in the site (done)

| Item | Status |
|---|---|
| LocalBusiness / PrintShop + WebSite JSON-LD on every page | ✅ done |
| BreadcrumbList schema on all inner pages | ✅ done |
| Service schema on all 31 service pages | ✅ done |
| FAQPage schema on home + every service page | ✅ done |
| Localized titles, meta descriptions, H1s ("… in Vellore") | ✅ done |
| Open Graph + Twitter cards + 1200×630 share image | ✅ done |
| Geo meta tags (region, position, ICBM) | ✅ done |
| WebP images via `<picture>` with JPG fallback | ✅ done |
| `width`/`height` on images (protects CLS / Core Web Vitals) | ✅ done |
| Descriptive, localized ALT text | ✅ done |
| Lazy loading + async decoding on all photos | ✅ done |
| FAQ content sections (home + services) | ✅ done |
| Blog → service internal links + descriptive anchors | ✅ done |
| XML sitemap, robots.txt, canonical tags, `.nojekyll` | ✅ done |
| Prominent WhatsApp / Call / Quote CTAs on every page | ✅ done |
| Semantic HTML5, skip link, ARIA nav, keyboard-friendly | ✅ done |

### Owner to-do before launch (replace placeholders — never fabricate)
- **Phone / WhatsApp:** currently `+91 90928 33701` / `919092833701` (in `tools/parts.py` SITE and `assets/js/main.js`).
- **Email / address / hours:** in `tools/parts.py` SITE.
- **Exact lat/long:** set `lat`/`lng` in SITE from Google Maps (right-click your shop → copy coordinates).
- **Domain:** `https://YOUR-USERNAME.github.io/vellore-printers` → your real domain (updates canonicals, sitemap, OG, schema).
- **Founding year & stats:** homepage shows placeholders (14+ years, 3,200 clients, 98%). Replace with real, defensible numbers or remove.
- **Social links:** Instagram / Facebook placeholders.
- After editing, run `python3 tools/optimize_images.py` (if photos changed) then `python3 tools/build.py`.

---

## 1. Keyword strategy

### Primary (home + services index)
| Keyword | Monthly intent | Target page |
|---|---|---|
| printing press in vellore | high, ready-to-buy | Home |
| printers in vellore | high | Home |
| printing services in vellore | high | Services index |
| best printing press in vellore | high | Home |
| digital printing in vellore | medium | Services / digital |
| offset printing in vellore | medium | Services / offset |
| commercial printing vellore | medium | Home / Services |

### Service keywords (one page each — all live)
Each `/services/<x>.html` targets **"<service> in Vellore"** + variants:

| Service page | Primary keyword | Secondary |
|---|---|---|
| business-card-printing | business card printing in vellore | visiting card printing vellore, premium visiting cards vellore |
| letterhead-printing | letterhead printing vellore | company letterhead printing vellore |
| envelope-printing | envelope printing vellore | cover printing vellore |
| id-card-printing | id card printing vellore | pvc id card printing vellore |
| lanyard-printing | lanyard printing vellore | id lanyard printing vellore |
| book-printing | book printing vellore | book binding vellore |
| flyer-printing | flyer printing vellore | pamphlet printing vellore, handbill printing vellore |
| brochure-printing | brochure printing vellore | tri-fold brochure printing vellore |
| booklet-printing | booklet printing vellore | catalogue booklet printing vellore |
| bill-book-printing | bill book printing vellore | invoice book printing vellore |
| certificate-printing | certificate printing vellore | award certificate printing vellore |
| poster-printing | poster printing vellore | a3 poster printing vellore |
| stickers-printing | sticker printing vellore | vinyl sticker printing vellore |
| product-label-printing | label printing vellore | product label printing vellore |
| mug-printing | mug printing vellore | photo mug printing vellore |
| water-bottle-printing | bottle printing vellore | customised bottle printing vellore |
| keychain-printing | keychain printing vellore | custom keychain vellore |
| wedding-card-printing | wedding card printing vellore | wedding invitation printing vellore |
| cd-sticker-printing | cd sticker printing vellore | dvd sticker printing vellore |
| business-card-design | business card design vellore | visiting card design vellore |
| letterhead-design | letterhead design vellore | corporate stationery design vellore |
| (…all 12 design pages follow the same "<service> design vellore" pattern) | | |

> Tip: don't stuff. Each keyword should appear naturally in the H1, first paragraph,
> one H2/H3, image ALT, and the FAQ — which is already the on-page pattern.

---

## 2. Local-area keywords (no doorway pages)

**Deserve a dedicated page (real demand + you serve them):**
- Katpadi — student/college hub → *"printing near Katpadi, Vellore"* section or page.
- Sathuvachari — dense residential/commercial → mention prominently.

**Mention naturally within existing pages (do NOT build thin per-area pages):**
Gandhi Nagar, Bagayam, Thorapadi, Kangeyanallur, Viruthampattu, Ranipet, Arcot, Gudiyatham.

These are already listed in the site's `areaServed` schema and footer/FAQ. A single, honest
**"Service areas"** block on the Home and Contact pages (already present in FAQ/footer) is the
right amount — Google rewards genuine local relevance, not spun duplicate pages.

**Recommendation:** Add at most **one** genuine "Areas we serve in and around Vellore" page later
if you gather real, distinct content (delivery notes, landmarks, local clients). Otherwise keep it inline.

---

## 3. Competitor analysis — how to run it (do this yourself, it changes monthly)

Search each primary keyword in an incognito window from a Vellore location and record the top 3–5:

| Check | Where | What "winning" looks like |
|---|---|---|
| Map pack presence | Google Maps | GBP with 50+ reviews, categories, photos, posts |
| Reviews (count + rating + recency) | GBP | Steady flow of recent 4.5★+ reviews |
| Service pages | their site | One page per service, local copy, FAQs |
| Page speed | pagespeed.web.dev | LCP < 2.5s, good CWV |
| Schema | search.google.com/test/rich-results | LocalBusiness + FAQ present |
| Backlinks | free tools (Ubersuggest/Ahrefs free) | Local directories, news, associations |
| Blog | their site | Helpful printing guides |

**Where you can win now:** most local print shops have weak or no websites — you already lead on
site structure, schema, FAQs, WebP speed and mobile CTAs. Your gap vs. established players will be
**GBP reviews + local citations + a few backlinks** (sections 8, 9, 11). Close those and you compete.

---

## 4. URL structure (recommendation)

Current URLs work and are indexable: `/services/business-card-printing.html`.
Optional upgrade to keyword-in-URL folders (only if you're comfortable adding redirects):
`/business-card-printing-vellore/`. Because the site is on GitHub Pages (static), this means one
folder + `index.html` per service and 301-style handling isn't native — so **only do this pre-launch**,
before any URL is indexed. If you're launching now, keep the current clean `.html` URLs; they rank fine.

---

## 5. Page-by-page implementation table (already applied)

| Page | Main keyword | URL | H1 | Schema | Priority |
|---|---|---|---|---|---|
| Home | printing press in vellore | /index.html | Printing Press in Vellore (hero) | LocalBusiness, WebSite, FAQPage | Critical |
| Services | printing services in vellore | /services/index.html | Complete print & design solutions | Breadcrumb | High |
| Each service | `<service> in vellore` | /services/<slug>.html | `<Service> in Vellore` | Service, FAQPage, Breadcrumb | High |
| About | best printing press in vellore | /about.html | 14 years of ink… | Breadcrumb | Medium |
| Gallery | printing work vellore | /gallery.html | A look at what leaves our press | Breadcrumb | Medium |
| Blog + posts | informational (see §7) | /blog/… | post title | Breadcrumb | Medium |
| Contact | printing quote vellore | /contact.html | Tell us what you need printed | Breadcrumb | High |

---

## 6. Google Business Profile (GBP) — highest ROI for local

1. **Primary category:** *Commercial printer*. **Secondary:** *Print shop, Digital printer, Offset printing service, Graphic designer, Sign shop, Wedding printing service*.
2. **Name:** exactly "Vellore Printers" (no keyword stuffing in the name — against Google rules).
3. **NAP:** identical to the website, letter-for-letter (name, address, phone). Consistency is a ranking factor.
4. **Description:** 750 chars, natural, mentions main services + Vellore + areas served.
5. **Services & Products:** add each service with a short description and a "from ₹…" price where possible.
6. **Photos:** 20+ — storefront, press floor, team, and real finished jobs (use your gallery images). Add a few weekly.
7. **Google Posts:** 1–2 per week (offer, new capability, festival print reminder). Keep them going — activity signals help.
8. **Q&A:** seed 5–8 real questions (same as site FAQs) and answer them from the business account.
9. **Messaging & WhatsApp:** enable messaging; put the WhatsApp number in the profile.
10. **Booking/quote link:** point the "Appointment/Quote" URL to your Contact page.

---

## 7. Reviews strategy (ethical — never fake)

- Ask **every** happy customer at handover: "If you're happy, a quick Google review really helps our small shop."
- Print a small **review QR** on the delivery bag / invoice that opens your GBP review link.
- Send this WhatsApp after delivery (personalise — don't script customers' words):

> Hi {name}, thank you for your order with Vellore Printers 🙏
> We hope the {product} came out well. If you have 30 seconds, a short Google review
> about your experience would mean a lot to our team: https://g.page/r/CSB1kOviFmJLEBM/review
> Thank you! — Vellore Printers

- **Never** offer money/discounts for reviews, never write reviews yourself, never bulk-import. Aim for a
  steady, natural trickle (e.g. a few a week). Reply to every review, good or bad, politely.

---

## 8. Blog content plan — 50 ideas

Format: **Title — main keyword — intent — suggested URL — link to service page.** Publish 1–2/week.
(Three posts already live: GSM guide, CMYK vs RGB, wedding-card timeline.)

| # | Title | Main keyword | Intent | URL | Link to |
|---|---|---|---|---|---|
| 1 | Digital vs Offset Printing: Which Is Right for Your Job? | digital vs offset printing | info | /blog/digital-vs-offset-printing.html | services/index |
| 2 | How Much Does Visiting Card Printing Cost in Vellore? | visiting card printing cost vellore | commercial | /blog/visiting-card-printing-cost-vellore.html | business-card-printing |
| 3 | Best Paper (GSM) for Business Cards | best gsm business cards | info | (live: gsm-guide) | business-card-printing |
| 4 | Matte vs Gloss Lamination: How to Choose | matte vs gloss lamination | info | /blog/matte-vs-gloss-lamination.html | brochure-printing |
| 5 | How to Prepare a Print-Ready File (PDF/CDR/AI) | print ready file | info | /blog/print-ready-file-guide.html | services/index |
| 6 | CMYK vs RGB Explained for Printing | cmyk vs rgb | info | (live: cmyk-vs-rgb) | brochure-printing |
| 7 | Wedding Invitation Printing: 6-Week Timeline | wedding invitation printing guide | info | (live: wedding-card-timeline) | wedding-card-printing |
| 8 | Choosing Paper for Brochure Printing | brochure paper guide | info | /blog/brochure-paper-guide.html | brochure-printing |
| 9 | Best Printing Options for Restaurants (Menus, Flyers) | restaurant printing | commercial | /blog/restaurant-printing-guide.html | flyer-printing |
| 10 | New Business Printing Checklist | new business printing checklist | info | /blog/new-business-printing-checklist.html | business-card-printing |
| 11 | Bleed, Trim & Safe Area Explained | bleed and trim printing | info | /blog/bleed-trim-safe-area.html | services/index |
| 12 | Spot UV, Foil & Emboss: Premium Card Finishes | premium card finishes | info | /blog/premium-card-finishes.html | business-card-printing |
| 13 | How to Design a Standout Letterhead | letterhead design tips | info | /blog/letterhead-design-tips.html | letterhead-design |
| 14 | Sticker Material Guide: Paper vs Vinyl vs Transparent | sticker material guide | info | /blog/sticker-material-guide.html | stickers-printing |
| 15 | Product Label Printing & FSSAI Basics | fssai label printing | commercial | /blog/fssai-label-printing.html | product-label-printing |
| 16 | Flex vs Vinyl vs Photo Paper for Banners | banner material guide | info | /blog/banner-material-guide.html | poster-printing |
| 17 | ID Card & Lanyard Printing for Offices & Schools | id card printing office | commercial | /blog/id-card-lanyard-guide.html | id-card-printing |
| 18 | Bill Book & Invoice Book: GST-Ready Formats | gst bill book format | commercial | /blog/gst-bill-book-format.html | bill-book-printing |
| 19 | Perfect Binding vs Saddle Stitch vs Wiro | book binding types | info | /blog/book-binding-types.html | book-printing |
| 20 | Corporate Gifting Ideas That Get Used | corporate gifting printing | commercial | /blog/corporate-gifting-ideas.html | mug-printing |
| 21 | Diwali & Pongal Marketing Prints for Local Shops | festival printing vellore | commercial | /blog/festival-printing-vellore.html | flyer-printing |
| 22 | How Many Business Cards Should You Order? | business card quantity | info | /blog/business-card-quantity.html | business-card-printing |
| 23 | Brochure Fold Types: Bi-fold, Tri-fold, Z-fold | brochure fold types | info | /blog/brochure-fold-types.html | brochure-printing |
| 24 | Best File Formats for Printing (and Why) | best file format printing | info | /blog/best-file-formats-printing.html | services/index |
| 25 | Poster Sizes Explained (A3, A2, A1, A0) | poster sizes | info | /blog/poster-sizes-explained.html | poster-printing |
| 26 | Choosing Colours That Print True | print colour accuracy | info | /blog/print-colour-accuracy.html | brochure-printing |
| 27 | Wedding Card Wording in Tamil & English | wedding card wording | info | /blog/wedding-card-wording.html | wedding-card-printing |
| 28 | Menu Card Printing for Cafés & Restaurants | menu card printing | commercial | /blog/menu-card-printing.html | flyer-printing |
| 29 | Catalogue Design That Sells | catalogue design tips | info | /blog/catalogue-design-tips.html | catalogue-design |
| 30 | Cheap vs Quality Printing: What You Actually Pay For | cheap vs quality printing | info | /blog/cheap-vs-quality-printing.html | services/index |
| 31 | Standee & Rollup Banner Setup Guide | standee printing guide | commercial | /blog/standee-printing-guide.html | standee-design |
| 32 | Water Bottle & Mug Branding for Events | event branding printing | commercial | /blog/event-branding-printing.html | water-bottle-printing |
| 33 | How Offset Printing Works (Simple Explainer) | how offset printing works | info | /blog/how-offset-printing-works.html | services/index |
| 34 | When Digital Printing Beats Offset | when to use digital printing | info | /blog/when-to-use-digital-printing.html | services/index |
| 35 | Envelope Sizes & Printing Options | envelope sizes printing | info | /blog/envelope-sizes-printing.html | envelope-printing |
| 36 | Certificate Printing for Schools & Academies | certificate printing schools | commercial | /blog/certificate-printing-schools.html | certificate-printing |
| 37 | Notebook & Diary Printing for Corporates | notebook printing corporate | commercial | /blog/notebook-printing-corporate.html | book-printing |
| 38 | Custom Packaging Boxes: A Starter Guide | custom packaging printing | commercial | /blog/custom-packaging-guide.html | product-label-printing |
| 39 | How to Brief a Printer (Save Time & Money) | how to brief a printer | info | /blog/how-to-brief-a-printer.html | contact |
| 40 | Lamination, UV & Coating: What's the Difference? | print coating types | info | /blog/print-coating-types.html | brochure-printing |
| 41 | Best Prints for Real Estate Marketing | real estate printing | commercial | /blog/real-estate-printing.html | flyer-printing |
| 42 | School Prospectus & Admission Kit Printing | prospectus printing | commercial | /blog/prospectus-printing.html | booklet-printing |
| 43 | Hospital & Clinic Stationery Essentials | clinic stationery printing | commercial | /blog/clinic-stationery-printing.html | letterhead-printing |
| 44 | Retail Shop Signage & Poster Ideas | retail signage printing | commercial | /blog/retail-signage-printing.html | poster-printing |
| 45 | QR Codes on Print: Do's and Don'ts | qr code printing | info | /blog/qr-code-printing.html | business-card-printing |
| 46 | Eco-Friendly Printing: Papers & Inks | eco friendly printing | info | /blog/eco-friendly-printing.html | services/index |
| 47 | Colour Proofing: Why We Always Proof | print proofing | info | /blog/print-proofing.html | services/index |
| 48 | Reorders Made Easy: Keeping Your Print Files | print reorder files | info | /blog/print-reorder-files.html | contact |
| 49 | Small-Business Branding Kit on a Budget | small business branding | commercial | /blog/small-business-branding-kit.html | business-card-design |
| 50 | Same-Day Printing in Vellore: What's Possible | same day printing vellore | commercial | /blog/same-day-printing-vellore.html | contact |

Each post: 700–1,200 words, one H1, 3–5 H2s, one image with ALT, and a link to the mapped
service page + a quote CTA. To add one: create `blog/<slug>.html` following an existing post, or
extend `BLOG_POSTS` in `tools/build.py` and rebuild.

---

## 8b. Internal linking rules
- Home → Services index, and to 6 featured services (done).
- Each service → 3 related services + Services index + Contact (done).
- Blog post → its mapped service + Contact (done).
- Use descriptive anchors ("wedding card printing in Vellore"), never "click here".
- Add contextual links inside new blog posts to the most relevant service.

---

## 9. Backlinks — ethical, local, earned

Target genuine local relevance (no PBNs, no paid link farms):
- **Local directories:** Google Business Profile, Justdial, Sulekha, IndiaMART, Yellow Pages India, AskLaila — consistent NAP.
- **Maps/citations:** Bing Places, Apple Business Connect.
- **Associations:** Vellore/Tamil Nadu chambers of commerce, local printers' or traders' associations.
- **Partners:** wedding planners, event companies, ad agencies, graphic designers, packaging suppliers — mutual referrals & listings.
- **Institutions:** schools, colleges, hospitals you print for — a "our print partner" mention/link.
- **Local media/blogs:** Vellore news sites, community pages — offer a genuine story (e.g. "how a local press went digital").
- **Sponsorships:** local events/college fests you already print for → a sponsor link.

Avoid: comment spam, link exchanges at scale, fiverr link packages, hidden links.

---

## 10. Analytics & Search Console setup

1. **Google Search Console:** add the property, verify (DNS TXT or the HTML file), submit
   `https://your-domain/sitemap.xml`. Monitor Coverage, Core Web Vitals, and Performance (queries/pages).
2. **Google Analytics 4:** create a property, add the gtag snippet before `</head>`
   (add it once in `tools/parts.py head()` and rebuild).
3. **Bing Webmaster Tools:** import from GSC, submit sitemap.
4. **Conversion tracking (GA4 events):** track the actions that matter. Example — add `data-ev`
   attributes to CTAs and one listener:

```html
<!-- in head(), after your gtag snippet -->
<script>
document.addEventListener('click',function(e){
  var a=e.target.closest('a,button'); if(!a) return;
  if(a.href&&a.href.indexOf('wa.me')>-1)      gtag('event','whatsapp_click');
  if(a.href&&a.href.indexOf('tel:')===0)      gtag('event','call_click');
  if(a.id==='quote-form'||a.type==='submit')  gtag('event','quote_submit');
});
</script>
```

Mark `whatsapp_click`, `call_click`, and `quote_submit` as **Key events (conversions)** in GA4.

---

## 11. Trust signals (use real data — never fabricate)
Show, once verified: years in business, jobs/clients served, in-house equipment list, quality/reprint
guarantee, Google review count & rating, portfolio (gallery — done), GST/registration line in footer,
delivery areas (done), and real shop/press photos. The homepage stats are **placeholders** — replace
with true figures or remove them.

---

## 12. Rollout phases

**Phase 1 — Critical (week 1):** replace all placeholders (phone, address, domain, lat/long, stats);
deploy; verify GSC + submit sitemap; set up GBP with correct categories + NAP.
**Phase 2 — Service pages (weeks 1–2):** confirm each service page's title/H1/FAQ reads naturally;
add any missing local detail; add 15–20 real job photos to gallery + GBP.
**Phase 3 — Local SEO (weeks 2–4):** build core citations (Justdial, IndiaMART, Bing, Apple),
consistent NAP; start weekly GBP posts; launch review request flow.
**Phase 4 — Content (ongoing):** publish 1–2 blog posts/week from the 50-idea list; interlink to services.
**Phase 5 — Authority (months 2–4):** earn local backlinks (associations, partners, institutions, media).
**Phase 6 — Continuous:** monthly GSC review (queries, CWV, coverage), refresh GBP photos/posts,
update pricing/turnaround, expand FAQs from real customer questions.

---

*Prepared for Vellore Printers. All recommendations are white-hat and practical for a real
local printing business. Replace every placeholder with verified information before launch.*

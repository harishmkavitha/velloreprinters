# -*- coding: utf-8 -*-
"""Shared building blocks: site config, SVG art, head/nav/footer templates."""

SITE = {
    "name": "Vellore Printers",
    "tagline": "Offset · Digital · Design",
    "phone_display": "+91 78250 75552",
    "phone_tel": "+917825075552",
    "wa": "917825075552",
    "email": "hello@velloreprinters.in",
    "addr_line": "16, Moongil Mandi Street, Vellore \u2013 632004, Tamil Nadu, India",
    "hours": "Mon \u2013 Sat, 10:00 am \u2013 8:00 pm",
    "gmb": "https://maps.app.goo.gl/yX4PRw3ZNd6EybFq7",
    "review_url": "https://g.page/r/CSB1kOviFmJLEBM/review",
    "instagram": "https://instagram.com/",
    "facebook": "https://facebook.com/",
    "domain": "https://harishmkavitha.github.io/velloreprinters",  # live GitHub Pages URL
    # --- structured fields for schema / local SEO (replace placeholders) ---
    "street": "16, Moongil Mandi Street",
    "locality": "Vellore",
    "region": "Tamil Nadu",
    "postal": "632004",
    "country": "IN",
    "lat": "12.9165",          # TODO: set exact shop coordinates from Google Maps
    "lng": "79.1325",          # TODO: set exact shop coordinates from Google Maps
    "maps_url": "https://maps.app.goo.gl/yX4PRw3ZNd6EybFq7",
    "founded": "1974",
    "price_range": "\u20b9\u20b9",
    "areas": ["Vellore", "Katpadi", "Sathuvachari", "Gandhi Nagar", "Bagayam",
              "Thorapadi", "Kangeyanallur", "Ranipet", "Arcot", "Gudiyatham"],
}

# ---------------------------------------------------------------- SVG artwork
def svg_cmyk(dark=False):
    blend = "screen" if dark else "multiply"
    return f'''<div class="cmyk" aria-hidden="true">
  <span class="cmyk__ring"></span>
  <span class="cmyk__disc cmyk__disc--c" style="mix-blend-mode:{blend}"></span>
  <span class="cmyk__disc cmyk__disc--m" style="mix-blend-mode:{blend}"></span>
  <span class="cmyk__disc cmyk__disc--y" style="mix-blend-mode:{blend}"></span>
  <svg class="cmyk__cross" viewBox="0 0 36 36" fill="none" stroke="#111014" stroke-width="1.5">
    <circle cx="18" cy="18" r="9"/><path d="M18 2v32M2 18h32"/>
  </svg>
</div>'''

# palette for generated card/hero art
_PALS = [
    ("#00aeef", "#ec008c", "#ffd200"),
    ("#ec008c", "#ffd200", "#00aeef"),
    ("#ffd200", "#00aeef", "#ec008c"),
    ("#00aeef", "#ffd200", "#111014"),
    ("#ec008c", "#00aeef", "#111014"),
]

def svg_art(seed, kind="card"):
    """Deterministic geometric print-themed illustration (self-contained)."""
    a, b, c = _PALS[seed % len(_PALS)]
    vb = "0 0 400 250"
    dots = ""
    for i in range(9):
        for j in range(5):
            r = 1.6 + ((i * 7 + j * 13 + seed) % 5) * 0.9
            dots += f'<circle cx="{20 + i*44}" cy="{22 + j*52}" r="{r:.1f}" fill="{c}" opacity="0.5"/>'
    shapes = {
        0: f'<circle cx="150" cy="125" r="78" fill="{a}"/><circle cx="230" cy="140" r="70" fill="{b}" opacity="0.85" style="mix-blend-mode:multiply"/>',
        1: f'<rect x="70" y="55" width="150" height="150" rx="10" fill="{a}"/><rect x="150" y="90" width="150" height="130" rx="10" fill="{b}" opacity="0.85" style="mix-blend-mode:multiply"/>',
        2: f'<polygon points="120,40 210,200 30,200" fill="{a}"/><polygon points="250,60 340,210 160,210" fill="{b}" opacity="0.85" style="mix-blend-mode:multiply"/>',
        3: f'<circle cx="140" cy="125" r="80" fill="{a}"/><rect x="180" y="70" width="140" height="120" rx="8" fill="{b}" opacity="0.85" style="mix-blend-mode:multiply"/>',
        4: f'<rect x="60" y="70" width="150" height="120" rx="8" fill="{a}"/><circle cx="250" cy="130" r="72" fill="{b}" opacity="0.85" style="mix-blend-mode:multiply"/>',
    }[seed % 5]
    return (f'<svg viewBox="{vb}" role="img" aria-label="Geometric print artwork" '
            f'xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice">'
            f'<rect width="400" height="250" fill="#f3f4f7"/>{dots}{shapes}'
            f'<g stroke="#111014" stroke-width="1.4" fill="none" opacity="0.9">'
            f'<path d="M18 18h20M18 18v20"/><path d="M382 232h-20M382 232v-20"/></g>'
            f'</svg>')

# small inline icons -------------------------------------------------------
IC = {
 "hd":'<svg class="feature__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 9v6M7 12h3M10 9v6M14 9h2a2 2 0 0 1 2 2v2a2 2 0 0 1-2 2h-2z"/></svg>',
 "layers":'<svg class="feature__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M12 3 2 8l10 5 10-5-10-5Z"/><path d="M2 16l10 5 10-5M2 12l10 5 10-5"/></svg>',
 "clock":'<svg class="feature__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "check":'<svg class="feature__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M20 6 9 17l-5-5"/></svg>',
 "truck":'<svg class="feature__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M3 6h11v9H3zM14 9h4l3 3v3h-7z"/><circle cx="7" cy="18" r="1.6"/><circle cx="17" cy="18" r="1.6"/></svg>',
 "pen":'<svg class="feature__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="m12 19 7-7-3-3-7 7v3zM16 9l3 3M5 21l3-1"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M12 22s7-6.4 7-12a7 7 0 1 0-14 0c0 5.6 7 12 7 12Z"/><circle cx="12" cy="10" r="2.6"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><path d="M4 5c0 8 7 15 15 15l0-3.5-4-1.5-2 2a13 13 0 0 1-6-6l2-2L7.5 5H4Z"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "hours":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
}
SOC = {
 "ig":'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
 "fb":'<svg viewBox="0 0 24 24" fill="currentColor"><path d="M14 9h3V6h-3c-2 0-3 1-3 3v2H9v3h2v6h3v-6h2.5l.5-3H14V9Z"/></svg>',
 "wa":'<svg viewBox="0 0 32 32" fill="currentColor"><path d="M16 3a13 13 0 0 0-11 19.7L3 29l6.5-1.9A13 13 0 1 0 16 3Zm7.4 18.3c-.3.9-1.8 1.7-2.5 1.8-.7.1-1.5.1-2.4-.2-.6-.2-1.3-.4-2.3-.9-4-1.7-6.6-5.8-6.8-6.1-.2-.3-1.6-2.1-1.6-4s1-2.9 1.4-3.3c.3-.4.8-.5 1-.5h.7c.2 0 .5 0 .8.6l1.1 2.7c.1.2.2.5 0 .8l-.5.8c-.2.2-.4.5-.2.9.2.3.9 1.5 2 2.5 1.4 1.2 2.5 1.6 2.9 1.8.3.1.5.1.7-.1l.9-1.1c.3-.3.5-.3.8-.2l2.6 1.2c.3.2.5.3.6.4.1.3.1.9-.2 1.9Z"/></svg>',
}

# --------------------------------------------------------------- head / chrome
def head(title, desc, canon, og_type="website", json_ld=""):
    og_img = SITE['domain'] + "/assets/img/og-cover.jpg"
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <script>document.documentElement.className+=' js';</script>
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{canon}">
  <meta name="robots" content="index, follow, max-image-preview:large">
  <meta name="theme-color" content="#111014">
  <meta name="geo.region" content="IN-TN">
  <meta name="geo.placename" content="Vellore">
  <meta name="geo.position" content="{SITE['lat']};{SITE['lng']}">
  <meta name="ICBM" content="{SITE['lat']}, {SITE['lng']}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="{og_type}">
  <meta property="og:url" content="{canon}">
  <meta property="og:site_name" content="{SITE['name']}">
  <meta property="og:locale" content="en_IN">
  <meta property="og:image" content="{og_img}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{desc}">
  <meta name="twitter:image" content="{og_img}">
  <link rel="icon" href="{{root}}assets/img/favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;600;700&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{root}}assets/css/main.css">
{json_ld}
</head>'''


# ------------------------------------------------------------- JSON-LD schema
import json as _json

def _node(d):
    return d

def local_business_node():
    """LocalBusiness / PrintShop node — the anchor entity, reused site-wide."""
    return {
        "@type": ["PrintShop", "LocalBusiness"],
        "@id": SITE['domain'] + "/#business",
        "name": SITE['name'],
        "url": SITE['domain'] + "/",
        "image": SITE['domain'] + "/assets/img/og-cover.jpg",
        "logo": SITE['domain'] + "/assets/img/favicon.svg",
        "telephone": SITE['phone_tel'],
        "email": SITE['email'],
        "priceRange": SITE['price_range'],
        "foundingDate": SITE['founded'],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": SITE['street'],
            "addressLocality": SITE['locality'],
            "addressRegion": SITE['region'],
            "postalCode": SITE['postal'],
            "addressCountry": SITE['country'],
        },
        "geo": {"@type": "GeoCoordinates", "latitude": SITE['lat'], "longitude": SITE['lng']},
        "hasMap": SITE['maps_url'],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"],
            "opens": "10:00", "closes": "20:00",
        }],
        "areaServed": [{"@type": "City", "name": a} for a in SITE['areas']],
        "sameAs": [SITE['instagram'], SITE['facebook'], SITE['gmb']],
    }

def website_node():
    return {
        "@type": "WebSite",
        "@id": SITE['domain'] + "/#website",
        "url": SITE['domain'] + "/",
        "name": SITE['name'],
        "publisher": {"@id": SITE['domain'] + "/#business"},
        "inLanguage": "en-IN",
    }

def breadcrumb_node(items):
    """items: list of (name, absolute_url)."""
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": u}
            for i, (n, u) in enumerate(items)
        ],
    }

def service_node(name, desc, url):
    return {
        "@type": "Service",
        "name": name,
        "serviceType": name,
        "description": desc,
        "url": url,
        "provider": {"@id": SITE['domain'] + "/#business"},
        "areaServed": [{"@type": "City", "name": a} for a in SITE['areas'][:5]],
    }

def faq_node(qas):
    return {
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": q,
             "acceptedAnswer": {"@type": "Answer", "text": a}}
            for q, a in qas
        ],
    }

def json_ld_block(nodes):
    graph = {"@context": "https://schema.org", "@graph": nodes}
    return ('  <script type="application/ld+json">\n'
            + _json.dumps(graph, ensure_ascii=False, indent=2)
            + '\n  </script>')

BRAND_MARK = '''<svg class="brand__mark" viewBox="0 0 40 40" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
  <rect width="40" height="40" rx="9" fill="#111014"/>
  <circle cx="16" cy="17" r="8.5" fill="#00aeef" style="mix-blend-mode:screen"/>
  <circle cx="24" cy="17" r="8.5" fill="#ec008c" style="mix-blend-mode:screen"/>
  <circle cx="20" cy="24" r="8.5" fill="#ffd200" style="mix-blend-mode:screen"/>
</svg>'''


def nav(active, root, printing, design):
    def mega_links(items):
        return "".join(
            f'<li><a href="{root}services/{s}.html">{n}</a></li>' for (s, n, *_ ) in items)
    def act(name):
        return ' class="is-active"' if active == name else ''
    return f'''<a class="skip-link" href="#main">Skip to content</a>
<header class="site-nav">
  <div class="topbar">
    <div class="container">
      <span>{IC['phone']} <a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a> &nbsp;·&nbsp; {SITE['email']}</span>
      <span class="topbar__social">
        <a href="{SITE['instagram']}" aria-label="Instagram">Instagram</a>
        <a href="{SITE['facebook']}" aria-label="Facebook">Facebook</a>
        <a href="{SITE['gmb']}" aria-label="Google">Find us on Google</a>
      </span>
    </div>
  </div>
  <nav class="container site-nav__inner" aria-label="Primary">
    <a class="brand" href="{root}index.html">
      {BRAND_MARK}
      <span class="brand__txt"><b>{SITE['name']}</b><span>{SITE['tagline']}</span></span>
    </a>
    <button class="nav__toggle" aria-expanded="false" aria-controls="nav-list" aria-label="Menu">
      <svg viewBox="0 0 24 24" fill="none" stroke="#111" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg>
    </button>
    <ul class="nav__list" id="nav-list">
      <li><a href="{root}index.html"{act('home')}>Home</a></li>
      <li><a href="{root}about.html"{act('about')}>About</a></li>
      <li class="mega">
        <button aria-haspopup="true">Services
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m6 9 6 6 6-6"/></svg>
        </button>
        <div class="mega__panel">
          <div class="mega__col"><h4>Printing</h4><ul class="mega__links">{mega_links(printing)}</ul></div>
          <div class="mega__col"><h4>Design</h4><ul class="mega__links">{mega_links(design)}</ul></div>
        </div>
      </li>
      <li><a href="{root}gallery.html"{act('gallery')}>Gallery</a></li>
      <li><a href="{root}blog/index.html"{act('blog')}>Blog</a></li>
      <li><a href="{root}contact.html"{act('contact')}>Contact</a></li>
    </ul>
  </nav>
</header>
<main id="main">'''


def footer(root, printing, design):
    pcols = "".join(f'<li><a href="{root}services/{s}.html">{n}</a></li>' for (s, n, *_) in printing[:8])
    dcols = "".join(f'<li><a href="{root}services/{s}.html">{n}</a></li>' for (s, n, *_) in design[:6])
    return f'''</main>
<a class="wa-float" href="https://wa.me/{SITE['wa']}?text=Hi%20Vellore%20Printers%2C%20I%27d%20like%20a%20quote." target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{SOC['wa']}</a>
<footer class="site-footer">
  <div class="container">
    <div class="site-footer__top">
      <div>
        <h3>{SITE['name']}</h3>
        <p>An offset, digital and design studio in Vellore \u2014 stationery, marketing collateral, signage, gifting and packaging under one roof.</p>
        <div class="footer-social">
          <a href="{SITE['instagram']}" aria-label="Instagram">{SOC['ig']}</a>
          <a href="{SITE['facebook']}" aria-label="Facebook">{SOC['fb']}</a>
          <a href="https://wa.me/{SITE['wa']}" aria-label="WhatsApp">{SOC['wa']}</a>
        </div>
      </div>
      <div>
        <h4>Printing</h4>
        <ul class="footer-list">{pcols}<li><a href="{root}services/index.html">All services \u2192</a></li></ul>
      </div>
      <div>
        <h4>Design</h4>
        <ul class="footer-list">{dcols}</ul>
      </div>
      <div>
        <h4>Reach us</h4>
        <ul class="footer-list">
          <li>{SITE['addr_line']}</li>
          <li><a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></li>
          <li><a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
          <li>{SITE['hours']}</li>
          <li><a href="{SITE['gmb']}">Get directions \u2192</a></li>
          <li><a href="{SITE['review_url']}" target="_blank" rel="noopener">Leave a Google review \u2192</a></li>
          <li style="margin-top:12px;border-top:1px solid #26242e;padding-top:12px"><a href="{root}contact.html">Contact us</a></li>
          <li><a href="{root}sitemap.html">Sitemap</a></li>
          <li><a href="{root}terms-and-conditions.html">Terms &amp; Conditions</a></li>
          <li><a href="{root}privacy-policy.html">Privacy Policy</a></li>
        </ul>
      </div>
    </div>
    <div class="site-footer__legal">
      <span class="regbar"><i></i><i></i><i></i><i></i><i></i></span>
      <span>\u00a9 <span id="year">2026</span> {SITE['name']}. All rights reserved.</span>
      <span><a href="{root}sitemap.html">Sitemap</a> &nbsp;·&nbsp; <a href="{root}terms-and-conditions.html">Terms</a> &nbsp;·&nbsp; <a href="{root}privacy-policy.html">Privacy Policy</a> &nbsp;·&nbsp; <a href="{root}contact.html">Contact</a></span>
    </div>
  </div>
</footer>
<script src="{root}assets/js/main.js" defer></script>
</body>
</html>'''

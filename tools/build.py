# -*- coding: utf-8 -*-
import os, sys, datetime
sys.path.insert(0, os.path.dirname(__file__))
from parts import SITE, head, nav, footer, svg_cmyk, svg_art, IC, SOC
from services_data import PRINTING, DESIGN, INCLUDED_DEFAULT

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ALL = [("printing",)+ s for s in PRINTING] + [("design",)+ s for s in DESIGN]
SLUGS = {s[1]: s for s in [("printing",)+x for x in PRINTING]+[("design",)+x for x in DESIGN]}

def write(relpath, html):
    p = os.path.join(ROOT, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)

def page(relpath, active, root, title, desc, body, og_type="website"):
    h = head(title, desc, SITE["domain"] + "/" + relpath, og_type).replace("{root}", root)
    html = h + "\n<body>\n" + nav(active, root, PRINTING, DESIGN) + "\n" + body + "\n" + footer(root, PRINTING, DESIGN)
    write(relpath, html)

def reg():  # small registration divider
    return '<span class="regbar"><i></i><i></i><i></i><i></i><i></i></span>'

def media(root, path, seed, alt):
    """Real photo over a geometric SVG fallback. If assets/img/<path> is
    missing, the <img> hides itself (onerror) and the SVG shows through."""
    return (f'{svg_art(seed)}'
            f'<img src="{root}assets/img/{path}" alt="{alt}" loading="lazy" '
            f'decoding="async" onerror="this.style.display=\'none\'">')

# ============================================================ HOME
def build_home():
    root = ""
    # featured service cards
    feat = ["business-card-printing","letterhead-printing","flyer-printing","brochure-printing","wedding-card-printing","poster-printing"]
    cards = ""
    for i, sl in enumerate(feat):
        cat, slug, name, price, tag, *_ = SLUGS[sl]
        cards += f'''<a class="svc-card reveal" href="services/{slug}.html">
  <div class="svc-card__media ph">{media(root, f"services/{slug}.jpg", i, name)}</div>
  <div class="svc-card__body">
    <span class="svc-card__price">{price}</span>
    <h3 class="svc-card__title">{name}</h3>
    <p class="svc-card__desc">{tag}.</p>
    <span class="svc-card__more">Know more</span>
  </div>
</a>'''
    features = [
        (IC["hd"], "Ultra HD output", "2400 dpi plates and inline colour control give clean gradients, hairline rules and true skin tones on every stock."),
        (IC["pen"], "In-house studio", "Designers on staff for logo, layout and Tamil\u2013English typesetting before anything reaches the press."),
        (IC["layers"], "Imported papers", "Bond, textured, FBB, kraft and triplex boards stocked \u2014 you are never forced into a compromise."),
        (IC["clock"], "24-hour express", "Standard cards and flyers dispatched the next working day across Vellore and nearby towns."),
        (IC["check"], "Proof before print", "A digital proof on every job and a wet proof on large runs \u2014 you sign off, then we run."),
        (IC["truck"], "Free local delivery", "No delivery charge inside Vellore town, Katpadi, Sathuvachari, Gandhi Nagar and Bagayam."),
    ]
    fhtml = "".join(f'<div class="feature reveal">{ic}<h3>{t}</h3><p>{d}</p></div>' for ic,t,d in features)
    quotes = [
        ("We moved all our hospital stationery here \u2014 appointment cards, prescription pads, signage. Everything arrives on the promised day and the colour never shifts between batches.", "Dr. Revathi S.", "Founder, Sirumalar Clinic, Vellore"),
        ("They printed 40,000 flyers for our festival campaign in three days and even fixed the Tamil text that was breaking. Genuinely helpful people.", "Arun Kumar", "Marketing Head, Sri Balaji Supermarket"),
        ("Our 600 GSM cards with copper edge painting look better than samples I was shown in the city, at half the price.", "Nivetha R.", "Principal Architect, Studio Verandah"),
    ]
    qhtml = "".join(f'<figure class="quote reveal"><p>{q}</p><div class="stars">\u2605\u2605\u2605\u2605\u2605</div><cite><b>{a}</b>{r}</cite></figure>' for q,a,r in quotes)

    body = f'''
<section class="hero bg-dots">
  <div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container hero__grid">
    <div>
      <span class="eyebrow">Digital + Offset + Design</span>
      <h1>Ultra&nbsp;HD printing, right here in <em>Vellore</em></h1>
      <p class="hero__lead">Business cards, letterheads, brochures, banners, gifting and packaging \u2014 printed with calibrated colour, imported stocks and delivery you can plan around. One press, one studio, one point of contact.</p>
      <div class="hero__cta">
        <a class="btn btn--lg" href="contact.html">Get a free quote</a>
        <a class="btn btn--ghost btn--lg" href="services/index.html">Browse services</a>
      </div>
      <div class="hero__stats">
        <div><div class="stat__num"><b>14+</b></div><div class="stat__label">Years printing</div></div>
        <div><div class="stat__num"><b>3,200</b></div><div class="stat__label">Local clients</div></div>
        <div><div class="stat__num"><b>98%</b></div><div class="stat__label">On-time delivery</div></div>
      </div>
    </div>
    <div class="hero__art">{svg_cmyk()}</div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="marquee__track">
  <span>Business Cards</span><span>Letterheads</span><span>Brochures</span><span>Flyers</span><span>Wedding Cards</span><span>Stickers</span><span>Signage</span><span>Packaging</span>
  <span>Business Cards</span><span>Letterheads</span><span>Brochures</span><span>Flyers</span><span>Wedding Cards</span><span>Stickers</span><span>Signage</span><span>Packaging</span>
</div></div>

<section>
  <div class="container">
    <div class="head-block reveal"><span class="eyebrow">What we print</span>
      <h2>Everything your brand needs on paper</h2>
      <p>Nineteen printing lines and twelve design services, one delivery promise. Pick a service to see stocks, finishes and indicative pricing.</p>
    </div>
    <div class="svc-grid" style="margin-top:var(--s5)">{cards}</div>
    <div style="margin-top:var(--s5)"><a class="btn btn--ghost" href="services/index.html">See all 31 services \u2192</a></div>
  </div>
</section>

<section class="bg-soft">
  <div class="geo-edge bg-grid" style="opacity:.5"></div>
  <div class="container">
    <div class="head-block reveal"><span class="eyebrow">Why Vellore Printers</span>
      <h2>What makes our printing different?</h2></div>
    <div class="features" style="margin-top:var(--s5)">{fhtml}</div>
  </div>
</section>

<section class="dark-band">
  <div class="geo-edge bg-dots" style="opacity:.12"></div>
  <div class="container dark-band__grid">
    <div class="reveal">
      <span class="eyebrow eyebrow--light">Inside the press floor</span>
      <h2>From file to finished box, under one roof</h2>
      <p class="dark-band__lead">Pre-press check, colour profiling, plate output, press run, lamination, die-cutting, quality sampling and packing \u2014 all of it happens in our unit. Nothing is sub-contracted without telling you first.</p>
      <ul class="check-list">
        <li>Pre-press artwork check within 2 hours of file upload</li>
        <li>Colour-bar sampling every 500 sheets</li>
        <li>Final count verified twice before dispatch</li>
      </ul>
      <div style="margin-top:var(--s5)"><a class="btn" href="about.html">Our story</a></div>
    </div>
    <div class="hero__art">{svg_cmyk(dark=True)}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="head-block reveal"><span class="eyebrow">Client words</span>
      <h2>What businesses in Vellore say</h2></div>
    <div class="quotes" style="margin-top:var(--s5)">{qhtml}</div>
  </div>
</section>

<section class="cta-band">
  <div class="geo-edge bg-dots" style="opacity:.16"></div>
  <div class="container">
    <span class="eyebrow eyebrow--light">Send us your artwork</span>
    <h2>We\u2019ll quote in 60 minutes</h2>
    <p>Share a PDF, CDR, AI or even a phone photo of an old print. Our estimator comes back with paper options and a firm price the same working hour.</p>
    <div class="cta-band__btns">
      <a class="btn" href="contact.html">Request a quote</a>
      <a class="btn btn--ghost" href="https://wa.me/{SITE['wa']}" target="_blank" rel="noopener">WhatsApp us</a>
    </div>
  </div>
</section>
'''
    page("index.html", "home", root,
         f"{SITE['name']} | Offset, Digital & HD Printing in Vellore",
         "Vellore\u2019s printing company for business cards, letterheads, brochures, wedding cards, signage and packaging. Ultra HD quality with fast local delivery.",
         body)

# ============================================================ ABOUT
def build_about():
    root = ""
    values = [
        ("Quality we can defend", "If a sheet leaves the floor with a scuff, a mis-register or a shade drift, it is reprinted at our cost. No debate."),
        ("Honest estimating", "We will tell you when 130 GSM does the same job as 170 GSM, even though the cheaper quote earns us less."),
        ("Lower-waste printing", "Soy-based inks, chemistry-free plates and paper offcuts routed to a recycler every fortnight."),
        ("Everything in-house", "Design, pre-press, offset, digital, wide-format, lamination, die-cutting and binding under one roof."),
    ]
    vhtml = "".join(f'<div class="card reveal"><h3 class="card__title">{t}</h3><p>{d}</p></div>' for t,d in values)
    tl = [("2011","Opened with one single-colour offset machine and three people in a small unit off Officers Line."),
          ("2015","Added a four-colour offset press and moved into our current larger unit near the New Bus Stand."),
          ("2018","Launched the in-house design studio and Tamil typesetting desk."),
          ("2021","Installed wide-format and UV printers for signage, gifting and rigid media."),
          ("2024","Commissioned an Ultra HD digital press for short-run 4K work and same-day cards."),
          ("2026","Serving 3,200+ businesses across Vellore district with a 98% on-time dispatch record.")]
    tlhtml = "".join(f'<li class="reveal"><span class="yr">{y}</span><span class="ev">{e}</span></li>' for y,e in tl)
    stats = [("14 yrs","On the job"),("18","People on the team"),("5","Presses running daily"),("24 hrs","Express turnaround")]
    shtml = "".join(f'<div class="card"><div class="stat__num"><b>{n}</b></div><div class="stat__label">{l}</div></div>' for n,l in stats)
    body = f'''
<section class="page-banner">
  <div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / About</p>
    <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">About us</span>
    <h1>Fourteen years of ink, paper and kept promises</h1>
    <p>Vellore Printers is a family-run printing company. We print the unglamorous things that make a business look serious \u2014 and we do it when we said we would.</p>
  </div>
</section>

<section>
  <div class="container" style="display:grid;grid-template-columns:1.2fr .8fr;gap:var(--s6);align-items:center">
    <div class="stack reveal">
      <h2>Our story</h2>
      <p>The press began in 2011 with one single-colour machine and a simple rule: the customer hears the truth the same day we do. No job delayed quietly because nobody wanted to make a phone call.</p>
      <p>That rule survived a move to a bigger unit, three new presses and a team of eighteen. Today the studio and the press floor run side by side for schools, hospitals, builders, restaurants and local brands across Vellore district.</p>
      <p>We are not the largest printer around. We are the one that picks up the phone at 7 pm when your event is tomorrow morning.</p>
    </div>
    <div class="cropped ph reveal" style="aspect-ratio:4/3">{media(root, "about-studio.jpg", 2, "Vellore Printers press floor")}</div>
  </div>
</section>

<section class="bg-soft">
  <div class="geo-edge bg-grid" style="opacity:.5"></div>
  <div class="container">
    <div class="head-block reveal"><span class="eyebrow">What we hold to</span><h2>Four rules we don\u2019t bend</h2></div>
    <div class="values" style="margin-top:var(--s5)">{vhtml}</div>
  </div>
</section>

<section>
  <div class="container">
    <div class="head-block reveal"><span class="eyebrow">How we grew</span><h2>From one machine to a full floor</h2></div>
    <ul class="timeline" style="margin-top:var(--s5)">{tlhtml}</ul>
    <div class="about-stats" style="margin-top:var(--s6)">{shtml}</div>
  </div>
</section>

<section class="cta-band">
  <div class="geo-edge bg-dots" style="opacity:.16"></div>
  <div class="container"><h2>Visit our press floor</h2>
    <p>Drop in, see the presses run and pick up a paper swatch folder. We\u2019re on Officers Line, near the New Bus Stand.</p>
    <div class="cta-band__btns"><a class="btn" href="contact.html">Get in touch</a><a class="btn btn--ghost" href="{SITE['gmb']}" target="_blank" rel="noopener">Get directions</a></div>
  </div>
</section>
'''
    page("about.html","about",root, f"About {SITE['name']} | Vellore Printing Experts Since 2011",
         "Vellore Printers is a family-run offset, digital and design house serving Vellore since 2011 with quality, honest estimating and on-time delivery.", body)

# ============================================================ SERVICES OVERVIEW
def build_services_index():
    root = "../"
    def block(items, offset):
        out = ""
        for i,(slug,name,price,tag,*_ ) in enumerate(items):
            out += f'''<a class="svc-card reveal" href="{slug}.html">
  <div class="svc-card__media ph">{media(root, f"services/{slug}.jpg", i+offset, name)}</div>
  <div class="svc-card__body">
    <span class="svc-card__price">{price}</span>
    <h3 class="svc-card__title">{name}</h3>
    <p class="svc-card__desc">{tag}.</p>
    <span class="svc-card__more">Know more</span>
  </div></a>'''
        return out
    steps = [("Brief & design","Send artwork or a rough idea. Our studio prepares a print-ready layout and shares a digital proof."),
             ("Proof & approval","You check colour, spelling and dimensions. Nothing runs until you approve in writing."),
             ("Press & finishing","Plates or digital output, colour-bar sampling, then lamination, foiling, die-cutting or binding."),
             ("Count & deliver","Quantity verified twice, shrink-wrapped and delivered free across Vellore town.")]
    shtml = "".join(f'<div class="step reveal"><div class="step__n">{i+1:02d}</div><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(steps))
    body = f'''
<section class="page-banner">
  <div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container">
    <p class="crumbs"><a href="../index.html">Home</a> / Services</p>
    <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">Our services</span>
    <h1>Complete print and design solutions</h1>
    <p>From the first stroke of a logo to the final press run \u2014 everything your brand needs to look professional in the real world.</p>
  </div>
</section>
<section>
  <div class="container">
    <div class="svc-subhead">Printing Services</div>
    <div class="svc-grid">{block(PRINTING,0)}</div>
  </div>
</section>
<section class="bg-soft">
  <div class="geo-edge bg-dots" style="opacity:.5"></div>
  <div class="container">
    <div class="svc-subhead">Design Services</div>
    <div class="svc-grid">{block(DESIGN,2)}</div>
  </div>
</section>
<section>
  <div class="container">
    <div class="head-block reveal"><span class="eyebrow">How an order runs</span><h2>Four steps, no surprises</h2></div>
    <div class="steps" style="margin-top:var(--s5)">{shtml}</div>
  </div>
</section>
{cta()}
'''
    page("services/index.html","", root, f"Printing & Design Services in Vellore | {SITE['name']}",
         "Offset and digital printing plus graphic design in Vellore \u2014 business cards, letterheads, brochures, wedding cards, signage, gifting and packaging.", body)

# ============================================================ SERVICE DETAIL
def build_service(entry, idx):
    cat, slug, name, price, tag, paras, specs = entry
    root = "../"
    others = [s for s in (PRINTING if cat=="printing" else DESIGN) if s[0]!=slug][:3]
    others_html = "".join(f'<a href="{o[0]}.html">{o[1]}</a>' for o in others)
    specs_html = "".join(f'<div class="spec-row"><dt>{k}</dt><dd>{v}</dd></div>' for k,v in specs)
    inc_html = "".join(f'<li>{x}</li>' for x in INCLUDED_DEFAULT)
    paras_html = "".join(f'<p>{p}</p>' for p in paras)
    body = f'''
<section class="page-banner">
  <div class="geo-edge bg-halftone" style="opacity:.55"></div>
  <div class="container">
    <p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Services</a> / {name}</p>
    <div class="svc-hero" style="margin-top:var(--s4)">
      <div>
        <span class="eyebrow">{cat.title()} service</span>
        <h1>{name}</h1>
        <p>{tag}. {paras[0]}</p>
        <div class="svc-hero__cta">
          <a class="btn btn--lg" href="../contact.html">Get a quote</a>
          <span class="svc-hero__price">Starts at {price}</span>
        </div>
      </div>
      <div class="cropped ph" style="aspect-ratio:16/10">{media(root, f"services/{slug}.jpg", idx, name)}</div>
    </div>
  </div>
</section>

<section>
  <div class="container svc-body">
    <div class="stack">
      {paras_html}
      <h3 style="margin-top:var(--s4)">Included with every order</h3>
      <ul class="included">{inc_html}</ul>
    </div>
    <div>
      <h3 style="margin-bottom:var(--s3)">Specifications</h3>
      <div class="spec-table"><dl>{specs_html}</dl></div>
      <div style="margin-top:var(--s5)">
        <a class="btn btn--wa" href="https://wa.me/{SITE['wa']}?text=Hi%2C%20I%27d%20like%20a%20quote%20for%20{name.replace(' ','%20')}" target="_blank" rel="noopener">{SOC['wa']} Quote on WhatsApp</a>
      </div>
    </div>
  </div>
</section>

<section class="bg-soft">
  <div class="geo-edge bg-grid" style="opacity:.5"></div>
  <div class="container">
    <div class="head-block"><span class="eyebrow">Related</span><h2>Other services</h2></div>
    <div class="other-svc" style="margin-top:var(--s4)">{others_html}</div>
  </div>
</section>
{cta()}
'''
    page(f"services/{slug}.html","", root, f"{name} in Vellore | {SITE['name']}",
         f"{tag}. {paras[0][:110]}", body, og_type="article")

# ============================================================ shared CTA
def cta():
    return f'''<section class="cta-band">
  <div class="geo-edge bg-dots" style="opacity:.16"></div>
  <div class="container"><span class="eyebrow eyebrow--light">Ready when you are</span>
    <h2>Send your artwork, get a price in 60 minutes</h2>
    <p>PDF, CDR, AI, PSD or a phone photo \u2014 our estimator replies within the working hour.</p>
    <div class="cta-band__btns"><a class="btn" href="{{c}}contact.html">Request a quote</a>
      <a class="btn btn--ghost" href="https://wa.me/{SITE['wa']}" target="_blank" rel="noopener">WhatsApp us</a></div>
  </div></section>'''.replace("{c}", "../")

# ============================================================ MEMBERSHIP
def build_membership():
    root=""
    plans=[("Starter","Shops, clinics and freelancers","\u20b94,999","/ year", False,
            ["8% off every print job","2 free design hours a month","Free delivery in Vellore town","48-hour standard turnaround","WhatsApp order desk"]),
           ("Growth","Growing brands with monthly campaigns","\u20b912,999","/ year", True,
            ["15% off every print job","8 free design hours a month","Priority press scheduling","24-hour express on cards & flyers","Free sample print before bulk runs","Dedicated print assistant"]),
           ("Enterprise","Multi-branch companies & institutions","\u20b929,999","/ year", False,
            ["22% off every print job","Unlimited design hours","Same-day emergency slot each week","Quarterly stock holding of your papers","Branch-wise billing portal access","Annual brand collateral audit"])]
    ph=""
    for name,forwho,price,per,feat,items in plans:
        tag='<span class="plan__tag">Most popular</span>' if feat else ''
        li="".join(f'<li>{x}</li>' for x in items)
        ph+=f'''<div class="plan {'plan--featured' if feat else ''} reveal">{tag}
  <div class="plan__name">{name}</div><div class="plan__for">{forwho}</div>
  <div class="plan__price">{price} <span>{per}</span></div>
  <ul class="plan__list">{li}</ul>
  <a class="btn" href="contact.html">Get it now</a></div>'''
    faqs=[("Is the membership fee adjustable against printing?","Yes. The full fee is credited to your account and can be used against any print job during the year, so effectively you only pay for the benefits if you never print."),
          ("Can I upgrade mid-year?","Any time. You pay only the difference, pro-rated for the remaining months."),
          ("Do the discounts apply to signage and packaging?","Discounts apply to all printing. Installation, transport outside Vellore and third-party dies are billed at cost."),
          ("What counts as a design hour?","Studio time for layout, retouching, typesetting or dieline work. Simple text edits and resizes are always free.")]
    fh="".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q,a in faqs)
    body=f'''
<section class="page-banner">
  <div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container"><p class="crumbs"><a href="index.html">Home</a> / Membership</p>
    <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">Cost effective</span>
    <h1>Membership plans for businesses that print often</h1>
    <p>Lock your rates for twelve months, skip the queue and get studio time included. The fee is credited back against your printing.</p></div>
</section>
<section><div class="container"><div class="plans">{ph}</div></div></section>
<section class="bg-soft"><div class="geo-edge bg-dots" style="opacity:.5"></div>
  <div class="container"><div class="head-block"><span class="eyebrow">Good to know</span><h2>Membership questions</h2></div>
  <div class="faq" style="margin-top:var(--s5)">{fh}</div></div></section>
{cta().replace('../','')}
'''
    page("membership.html","membership",root, f"Business Printing Membership Plans | {SITE['name']}",
         "Save on business printing in Vellore with Starter, Growth and Enterprise membership \u2014 locked rates, priority scheduling and free design hours.", body)

# ============================================================ CASE STUDIES
def build_cases():
    root=""
    cases=[("healthcare","Healthcare","Sirumalar Clinic","Zero colour drift across 14 stationery items",
            "We standardised every printed item \u2014 appointment cards, prescription pads, signage \u2014 onto one colour profile so batches match all year.",
            [("14","Items unified"),("0","Reprints"),("98%","On-time")]),
           ("retail","Retail","Sri Balaji Supermarket","40,000 festival flyers in three days",
            "A last-minute festival push: redesigned layout, fixed broken Tamil text and ran 40,000 flyers with even colour to the last bundle.",
            [("40k","Flyers"),("3 days","Turnaround"),("2\u00d7","Repeat orders")]),
           ("architecture","Architecture","Studio Verandah","600 GSM cards with copper edge painting",
            "Premium triplex cards with a colour core and hand-applied copper edges \u2014 the finish a city vendor quoted at double the price.",
            [("600","GSM board"),("50%","Cost saved"),("5\u2605","Client rating")]),
           ("education","Education","Vel Matriculation","1,200 named ID cards, issued in a week",
            "PVC ID cards data-merged from the school\u2019s Excel sheet, printed both sides with QR, sorted class-wise and ready to hand out.",
            [("1,200","Cards"),("1 wk","Delivery"),("100%","Accuracy")])]
    ch=""
    for i,(slug,tag,client,title,desc,metrics) in enumerate(cases):
        mh="".join(f'<div><b>{n}</b><span>{l}</span></div>' for n,l in metrics)
        ch+=f'''<article class="case reveal"><div class="case__media ph">{media(root, f"cases/{slug}.jpg", i, client)}</div>
  <div class="case__body"><span class="case__tag">{tag} \u00b7 {client}</span><h3>{title}</h3><p>{desc}</p>
  <div class="case__metrics">{mh}</div></div></article>'''
    body=f'''
<section class="page-banner"><div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container"><p class="crumbs"><a href="index.html">Home</a> / Case Studies</p>
  <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">Case studies</span>
  <h1>Real jobs off our press</h1>
  <p>A few problems businesses in Vellore brought us \u2014 and what left the floor.</p></div></section>
<section><div class="container"><div class="case-grid">{ch}</div></div></section>
{cta().replace('../','')}
'''
    page("case-studies.html","cases",root, f"Printing Case Studies | {SITE['name']} Vellore",
         "See how Vellore Printers solved real print problems \u2014 unified clinic stationery, 40,000 festival flyers, premium cards and 1,200 school ID cards.", body)

# ============================================================ VELLOREFLOW
def build_flow():
    root=""
    feats=[(IC["layers"],"Live job board","Track every job from artwork to dispatch \u2014 proof pending, on press, finishing, out for delivery."),
           (IC["check"],"Approve proofs online","Comment on a proof, mark changes and approve from your phone. No email chains."),
           (IC["clock"],"Reorder in one tap","Your past jobs are saved with stock and finish. Reorder the exact same card without re-uploading."),
           (IC["hd"],"Billing portal","GST invoices, statements and payment links in one place, branch-wise for bigger accounts.")]
    fh="".join(f'<div class="feature reveal">{ic}<h3>{t}</h3><p>{d}</p></div>' for ic,t,d in feats)
    body=f'''
<section class="page-banner"><div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container hero__grid" style="align-items:center">
    <div><p class="crumbs"><a href="index.html">Home</a> / VelloreFlow</p>
      <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">Client workflow</span>
      <h1>VelloreFlow \u2014 your print jobs, organised</h1>
      <p>A simple client portal for members: upload artwork, approve proofs, track jobs and reorder \u2014 without a single phone call, unless you want one.</p>
      <div class="hero__cta"><a class="btn btn--lg" href="client-login.html">Open the portal</a>
      <a class="btn btn--ghost btn--lg" href="membership.html">See membership</a></div></div>
    <div class="hero__art">{svg_cmyk()}</div>
  </div></section>
<section><div class="container"><div class="head-block reveal"><span class="eyebrow">What it does</span>
  <h2>Everything after \u201csend me the file\u201d</h2></div>
  <div class="features" style="margin-top:var(--s5)">{fh}</div></div></section>
{cta().replace('../','')}
'''
    page("velloreflow.html","flow",root, f"VelloreFlow Client Portal | {SITE['name']}",
         "VelloreFlow is the Vellore Printers client portal \u2014 upload artwork, approve proofs online, track jobs and reorder in one tap.", body)

# ============================================================ CLIENT LOGIN
def build_login():
    root=""
    body=f'''
<section class="page-banner"><div class="geo-edge bg-halftone" style="opacity:.55"></div>
  <div class="container"><p class="crumbs"><a href="index.html">Home</a> / Client Login</p>
  <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">VelloreFlow</span>
  <h1>Client portal login</h1></div></section>
<section><div class="container">
  <div class="panel login-card reveal">
    <label class="field"><span>Email or client ID</span><input type="text" name="user" autocomplete="username" placeholder="you@company.in"></label>
    <label class="field"><span>Password</span><input type="password" name="pass" autocomplete="current-password" placeholder="\u2022\u2022\u2022\u2022\u2022\u2022\u2022\u2022"></label>
    <button class="btn" type="button" onclick="alert('This is a demo replica \u2014 connect your portal backend here.');">Sign in</button>
    <p class="login-note">Not a member yet? <a href="membership.html">See membership plans</a> or <a href="contact.html">contact us</a> to get set up.</p>
  </div>
</div></section>
'''
    page("client-login.html","login",root, f"Client Login | {SITE['name']}",
         "Log in to the VelloreFlow client portal to upload artwork, approve proofs and track your Vellore Printers jobs.", body)

# ============================================================ CONTACT
def build_contact():
    root=""
    opts="".join(f'<option>{s[2]}</option>' for s in PRINTING+DESIGN)
    body=f'''
<section class="page-banner"><div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container"><p class="crumbs"><a href="index.html">Home</a> / Contact</p>
  <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">Contact</span>
  <h1>Tell us what you need printed</h1>
  <p>Share your quantity, size and paper preference \u2014 or just describe the job. Our estimator replies within the working hour.</p></div></section>
<section><div class="container contact-grid">
  <div class="panel reveal">
    <h2 style="font-size:var(--t-xl)">Request a quote</h2>
    <form id="quote-form" style="margin-top:var(--s4)" novalidate>
      <label class="field"><span>Your name</span><input name="name" required placeholder="Full name"></label>
      <label class="field"><span>Phone</span><input name="phone" required inputmode="tel" placeholder="+91"></label>
      <label class="field"><span>Email (optional)</span><input name="email" type="email" placeholder="you@company.in"></label>
      <label class="field"><span>Service</span><select name="service"><option value="">Select a service</option>{opts}<option>Something else</option></select></label>
      <label class="field"><span>Job details</span><textarea name="details" rows="4" placeholder="Size, quantity, paper, finish, deadline\u2026"></textarea></label>
      <button class="btn" type="submit">Send enquiry</button>
      <p class="form-status" id="form-status" role="status"></p>
      <p style="font-size:var(--t-sm);color:var(--muted);margin-top:var(--s3)">Prefer to send files? WhatsApp them to <a href="https://wa.me/{SITE['wa']}">{SITE['phone_display']}</a> \u2014 PDF, AI, CDR, PSD and JPG all work.</p>
    </form>
  </div>
  <div class="reveal">
    <h2 style="font-size:var(--t-xl)">Visit the press</h2>
    <ul class="info-list">
      <li>{IC['pin']}<span>{SITE['addr_line']}</span></li>
      <li>{IC['phone']}<a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a></li>
      <li>{IC['mail']}<a href="mailto:{SITE['email']}">{SITE['email']}</a></li>
      <li>{IC['hours']}<span>{SITE['hours']}</span></li>
    </ul>
    <div style="margin-top:var(--s4);display:flex;gap:var(--s3);flex-wrap:wrap">
      <a class="btn btn--wa" href="https://wa.me/{SITE['wa']}" target="_blank" rel="noopener">{SOC['wa']} Chat on WhatsApp</a>
      <a class="btn btn--ghost" href="{SITE['gmb']}" target="_blank" rel="noopener">Find us on Google</a>
    </div>
    <div class="map-embed"><iframe title="Vellore map" loading="lazy" src="https://www.google.com/maps?q=Vellore,Tamil+Nadu&output=embed"></iframe></div>
  </div>
</div></section>
'''
    page("contact.html","contact",root, f"Contact {SITE['name']} | Printing Quotes in Vellore",
         "Contact Vellore Printers for a printing quote. Call, WhatsApp or visit our press on Officers Line, near the New Bus Stand, Vellore.", body)

# ============================================================ PRIVACY
def build_privacy():
    root=""
    body=f'''
<section class="page-banner"><div class="geo-edge bg-halftone" style="opacity:.5"></div>
  <div class="container"><p class="crumbs"><a href="index.html">Home</a> / Privacy Policy</p>
  <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">Legal</span>
  <h1>Privacy Policy</h1><p>How Vellore Printers handles the information you share with us.</p></div></section>
<section><div class="container container--narrow legal reveal">
  <h2>What we collect</h2>
  <p>When you request a quote or place an order we collect your name, phone number, email and the artwork or details you send. We collect only what we need to print your job and reach you about it.</p>
  <h2>How we use it</h2>
  <p>Your information is used to prepare quotes, produce your job, deliver it and keep records required under the GST and tax laws of India. We do not sell your data.</p>
  <h2>Your artwork</h2>
  <p>Files you send remain yours. We store them to reprint on request and delete them on written request, except where a tax record must be retained.</p>
  <h2>Sharing</h2>
  <p>We share details only with delivery partners and, where you approve it, third-party finishing vendors. We never share your contact list or artwork for marketing.</p>
  <h2>Your rights (DPDP Act, 2023)</h2>
  <ul>
    <li>Ask what personal data of yours we hold.</li>
    <li>Ask us to correct or update it.</li>
    <li>Ask us to erase it, subject to legal retention.</li>
    <li>Withdraw consent for messages at any time.</li>
  </ul>
  <h2>Contact</h2>
  <p>For any privacy request, email <a href="mailto:{SITE['email']}">{SITE['email']}</a> or call <a href="tel:{SITE['phone_tel']}">{SITE['phone_display']}</a>.</p>
</div></section>
'''
    page("privacy-policy.html","",root, f"Privacy Policy | {SITE['name']}",
         "How Vellore Printers collects, uses and protects your information, in line with India\u2019s DPDP Act 2023.", body)

# ============================================================ BLOG
BLOG_POSTS=[
 ("gsm-guide","A plain-English guide to paper GSM","Paper & Stock","Why 300 GSM feels premium and 80 GSM doesn\u2019t \u2014 and how to pick the right weight for cards, letterheads and flyers without overspending.",
  ["GSM means grams per square metre \u2014 the weight of a sheet, not strictly its thickness, though the two usually track together. A higher number means a heavier, stiffer sheet.",
   "For business cards we default to 300\u2013350 GSM; anything lighter bends in a wallet. Letterheads sit at 90\u2013120 GSM so they feed through printers and fold cleanly. Flyers live at 130\u2013170 GSM for a balance of feel and cost.",
   "The trick is matching weight to use, not always buying heavier. A 170 GSM flyer posted by the thousand costs more to print and to courier, with no real gain. Ask us and we\u2019ll tell you where the extra rupee is worth it."]),
 ("cmyk-vs-rgb","CMYK vs RGB: why your screen lies a little","Colour","Your logo looks electric on screen and flat on paper. Here\u2019s what happens between the two, and how to design so the printed colour is the one you expected.",
  ["Screens mix red, green and blue light; presses mix cyan, magenta, yellow and black ink. Some bright screen colours simply cannot be reproduced with ink, so they shift when printed.",
   "Design in CMYK from the start, or at least preview in it, and you avoid the surprise. For brand colours that must match exactly, we print a spot Pantone rather than build the colour from process inks.",
   "We send a proof on every job for this reason. It\u2019s far cheaper to catch a colour shift on one sheet than on five thousand."]),
 ("wedding-card-timeline","Ordering wedding cards: a stress-free timeline","Weddings","From shortlisting a style to cards in hand \u2014 when to start, what to decide, and how to keep Tamil and English text error-free.",
  ["Start six to eight weeks out. That leaves room to shortlist a style, finalise wording, approve a physical sample and print the full run without rushing the finishing.",
   "Decide the essentials early: names, muhurtham date and time, venue and the language mix. We typeset Tamil and English together and check the details twice \u2014 dates and times are the most common last-minute fixes.",
   "Order envelopes, inserts and thank-you cards in the same run so the paper and colour match across the set. A sample card before the full print is always worth the extra day."]),
]
def build_blog():
    root="../"
    ph=""
    for i,(slug,title,cat,excerpt,_paras) in enumerate(BLOG_POSTS):
        ph+=f'''<article class="post reveal"><div class="post__media ph">{media(root, f"blog/{slug}.jpg", i+1, title)}</div>
  <div class="post__body"><span class="post__meta">{cat}</span><h3>{title}</h3><p>{excerpt}</p>
  <a class="card__more" href="{slug}.html">Read article \u2192</a></div></article>'''
    body=f'''
<section class="page-banner"><div class="geo-edge bg-halftone" style="opacity:.6"></div>
  <div class="container"><p class="crumbs"><a href="../index.html">Home</a> / Blog</p>
  <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">Blog</span>
  <h1>Notes from the press floor</h1>
  <p>Practical printing know-how \u2014 paper, colour, finishing and the small decisions that make print look expensive.</p></div></section>
<section><div class="container"><div class="post-grid">{ph}</div></div></section>
{cta()}
'''
    page("blog/index.html","blog",root, f"Printing Blog | {SITE['name']} Vellore",
         "Practical printing know-how from Vellore Printers \u2014 paper GSM, CMYK colour, wedding card timelines and more.", body)
    # individual posts
    for i,(slug,title,cat,excerpt,paras) in enumerate(BLOG_POSTS):
        paras_html="".join(f'<p>{p}</p>' for p in paras)
        pb=f'''
<section class="page-banner"><div class="geo-edge bg-halftone" style="opacity:.5"></div>
  <div class="container"><p class="crumbs"><a href="../index.html">Home</a> / <a href="index.html">Blog</a> / {cat}</p>
  <span class="eyebrow" style="margin-top:var(--s3);display:inline-flex">{cat}</span>
  <h1>{title}</h1></div></section>
<section><div class="container container--narrow legal reveal">
  <div class="cropped ph" style="aspect-ratio:16/9;margin-bottom:var(--s5)">{media(root, f"blog/{slug}.jpg", i+1, title)}</div>
  {paras_html}
  <p style="margin-top:var(--s5)"><a class="btn btn--ghost" href="index.html">\u2190 Back to blog</a></p>
</div></section>
{cta()}
'''
        page(f"blog/{slug}.html","blog",root, f"{title} | {SITE['name']}",
             excerpt[:150], pb, og_type="article")

# ============================================================ 404
def build_404():
    root=""
    body=f'''
<section><div class="container notfound">
  <div class="regbar" style="margin-inline:auto"><i></i><i></i><i></i><i></i><i></i></div>
  <div class="code">404</div>
  <h1>This page didn\u2019t make it to press</h1>
  <p style="color:var(--muted)">The link may be old or mistyped. Let\u2019s get you back on paper.</p>
  <div style="display:flex;gap:var(--s3);justify-content:center;flex-wrap:wrap;margin-top:var(--s4)">
    <a class="btn" href="index.html">Back home</a><a class="btn btn--ghost" href="services/index.html">Browse services</a></div>
</div></section>
'''
    page("404.html","",root, f"Page not found | {SITE['name']}",
         "The page you were looking for could not be found.", body)

# ============================================================ FAVICON + SITEMAP
def build_favicon():
    svg='''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 40 40"><rect width="40" height="40" rx="9" fill="#111014"/><circle cx="16" cy="17" r="8.5" fill="#00aeef" style="mix-blend-mode:screen"/><circle cx="24" cy="17" r="8.5" fill="#ec008c" style="mix-blend-mode:screen"/><circle cx="20" cy="24" r="8.5" fill="#ffd200" style="mix-blend-mode:screen"/></svg>'''
    write("assets/img/favicon.svg", svg)

def build_sitemap():
    urls=["index.html","about.html","services/index.html","membership.html","case-studies.html",
          "velloreflow.html","client-login.html","contact.html","privacy-policy.html","blog/index.html"]
    urls+=[f"services/{s[1]}.html" for s in PRINTING+DESIGN]
    urls+=[f"blog/{p[0]}.html" for p in BLOG_POSTS]
    today=datetime.date.today().isoformat()
    items="".join(f"  <url><loc>{SITE['domain']}/{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)
    write("sitemap.xml", f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{items}</urlset>\n')
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {SITE['domain']}/sitemap.xml\n")

# ============================================================ RUN
def main():
    build_favicon()
    build_home(); build_about(); build_services_index()
    for i,entry in enumerate(PRINTING): build_service(("printing",)+entry, i)
    for i,entry in enumerate(DESIGN): build_service(("design",)+entry, i+2)
    build_membership(); build_cases(); build_flow(); build_login()
    build_contact(); build_privacy(); build_blog(); build_404()
    build_sitemap()
    print("Build complete.")

if __name__ == "__main__":
    main()

"""Builds the Heart To Home website.
site/     -> deployable files (full HTML documents)
preview/  -> same pages for the claude.ai preview (index without its document wrapper)
"""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE, PREV = os.path.join(ROOT, "site"), os.path.join(ROOT, "preview")

PHONE, TEL, EMAIL = "623-229-7585", "+16232297585", "adamtalal23@yahoo.com"
ROC = "AZ ROC #342540"
NAME = "Heart To Home, Home Improvements and Design LLC"

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,400;9..144,500;9..144,600&family=Work+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@500&display=swap">')

NAV = [("index.html", "Home"), ("services.html", "Services"), ("photos.html", "Photos"),
       ("colors.html", "Colors"), ("reviews.html", "Reviews"), ("about.html", "About")]

LOGO = ('<span class="logo" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M3 11 12 4l9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z" fill="#fff"/>'
        '<path d="M12 17.2s-3.2-2-3.2-4a1.7 1.7 0 0 1 3.2-.8 1.7 1.7 0 0 1 3.2.8c0 2-3.2 4-3.2 4z" fill="#D9C3A0"/></svg></span>')

def header(cur):
    links = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == cur else ""}>{t}</a>' for h, t in NAV)
    return (f'<div class="promo"><div class="wrap"><b>10% OFF</b><span>for military, first responders &amp; educators. Thank you for your service.</span>'
            f'<a href="estimate.html">Claim it</a></div></div>'
            f'<header class="top"><div class="wrap"><a class="brand" href="index.html">{LOGO}<span><b>Heart To Home</b><small>Home Improvements &amp; Design</small></span></a>'
            f'<nav aria-label="Main">{links}</nav><a class="btn btn-primary btn-sm" href="estimate.html">Free estimate</a></div></header>')

FOOTER = (f'<footer><div class="wrap"><span><b class="slogan-name">Heart To Home</b><br><em class="slogan-sm">From our heart to your home.</em><br>Family owned · Licensed, bonded &amp; insured · {ROC}<br>© 2026 {NAME}</span>'
          f'<nav aria-label="Footer">{"".join(f"<a href=\"{h}\">{t}</a>" for h, t in NAV)}<a href="estimate.html">Free estimate</a></nav>'
          '</div></footer>')

CONTACT = f'''<section class="contact"><div class="wrap">
<div><p class="eyebrow">Free estimates</p><h2 style="margin-top:12px">From our heart <span class="hl">to your home.</span></h2><p class="mono" style="margin-top:10px;color:var(--wheat)">Family owned · Licensed, bonded &amp; insured · {ROC}</p>
<p>Send a few details and photos. Adam gets your request on his phone and will reach out to set up a walkthrough and a written, fixed-price quote.</p>
<div class="ctas"><a class="btn btn-primary" href="estimate.html">Request a free estimate</a></div></div>
<div class="card">
<div class="row"><div><div class="k">Call or text</div><div class="v">{PHONE}</div></div><button class="copy" type="button" data-t="{PHONE}">Copy</button></div>
<div class="row"><div><div class="k">Email</div><div class="v">{EMAIL}</div></div><button class="copy" type="button" data-t="{EMAIL}">Copy</button></div>
<a class="btn btn-ghost" href="tel:{TEL}">Call now</a>
</div></div></section>'''

TRUST = f'''<section class="trust" aria-label="Why homeowners choose us"><div class="wrap">
<div style="--c:var(--olive)"><strong>Licensed, bonded &amp; insured</strong><span class="mono">{ROC}</span></div>
<div style="--c:var(--sage)"><strong>Family owned &amp; local</strong><span>Your neighbors in the West Valley.</span></div>
<div style="--c:var(--wheat)"><strong>We proudly use Sherwin-Williams</strong><span>Quality paint on every project.</span></div>
<div style="--c:var(--ink)"><strong>Owner on every job</strong><span>You work with Adam, start to finish.</span></div>
</div></section>'''

HEROES = '''<section class="heroes" id="heroes"><div class="wrap">
<div class="big">10%<small>off your project</small></div>
<div><h2>Thank you for serving.</h2>
<p>Military, first responders and educators get 10% off any Heart To Home project. Just let us know when you request your estimate.</p>
<div class="who"><span>Active duty &amp; veterans</span><span>Police</span><span>Firefighters</span><span>EMTs &amp; paramedics</span><span>Teachers &amp; school staff</span></div></div>
<a class="btn" href="estimate.html">Claim my 10% off</a>
</div></section>'''

MOVES = '''<section class="band mist" id="moving"><div class="wrap">
<div class="head"><p class="eyebrow">Moving in or moving out?</p><h2>The best time to paint is when the house is <span class="mark">empty</span>.</h2>
<p>No furniture, no family schedules, no working around your life. Just open walls and a clean finish, ready before the moving truck shows up.</p></div>
<div class="moves">
<div class="move" style="--bg:var(--sage-l);--fg:var(--ink)"><p class="eyebrow">Moving in</p><h3>Start fresh on day one</h3><ul>
<li>Your colors on every wall before a single box comes in</li><li>Ceilings, closets and trim done without moving furniture</li><li>New flooring and baseboards installed in open rooms</li><li>No paint smell or drop cloths while you settle in</li></ul>
<a class="btn btn-primary" style="justify-self:start" href="estimate.html">Plan my move-in paint</a></div>
<div class="move" style="--bg:var(--linen-d);--fg:var(--ink)"><p class="eyebrow">Moving out</p><h3>Leave it looking its best</h3><ul>
<li>Fresh, neutral walls that photograph well for listings</li><li>Patch the nail holes and dings from years of living</li><li>Touch up trim, doors and baseboards before buyers walk through</li><li>Handle the repaint before your final walkthrough</li></ul>
<a class="btn btn-primary" style="justify-self:start" href="estimate.html">Plan my move-out paint</a></div>
</div>
<div class="why">
<div style="--c:var(--wheat)"><i>1</i><b>Faster</b><p>Open rooms mean less time moving and covering furniture.</p></div>
<div style="--c:var(--sage-l)"><i>2</i><b>Cleaner</b><p>Every wall, corner and ceiling is easy to reach for crisp lines.</p></div>
<div style="--c:var(--clay-l)"><i>3</i><b>No disruption</b><p>No working around kids, pets or your daily routine.</p></div>
<div style="--c:var(--stone)"><i>4</i><b>Move-in ready</b><p>Walk in to finished rooms instead of a project list.</p></div>
</div></div></section>'''

HONEY_ITEMS = ["Patch drywall holes and dings", "Touch-up paint", "Fix sticking or squeaky doors", "Replace door handles and hinges",
               "Re-caulk tub and shower", "Replace damaged baseboard", "Hang shelves, mirrors and art", "Mount a TV",
               "Install blinds", "Swap closet shelving"]
HONEY = ('<section class="honey" id="honey"><div class="wrap"><div><p class="eyebrow">Handyman service</p>'
         '<h2 style="margin-top:12px">Got a honey-do list? Hand it over.</h2>'
         "<p class=\"lead\">Check off what needs doing and send it straight to us. We'll quote the whole list and knock it out in one visit.</p></div>"
         '<div class="list"><div class="title">My honey-do list <span id="honey-count">0 items</span></div>'
         + "".join(f'<label><input type="checkbox" id="hd{i}" value="{t}"><span>{t}</span></label>' for i, t in enumerate(HONEY_ITEMS))
         + '<a class="btn btn-primary" id="honey-send" href="estimate.html">Send my list for a quote</a></div></div></section>')

TILES = [
    ("c-orange", "Painting", "Interior painting", "Walls, ceilings, accent walls and full-home repaints."),
    ("c-teal", "Painting", "Exterior painting", "Stucco, fascia and doors that stand up to the Arizona sun."),
    ("c-ink", "Kitchens", "Kitchen installs", "Cabinets, counters, backsplash and hardware, installed and finished."),
    ("c-berry", "Bathrooms", "Bathroom remodels", "Tub-to-shower conversions, tile, vanities and a fresh look."),
    ("c-sun", "Flooring", "Flooring", "Luxury vinyl plank and laminate with new baseboard."),
    ("c-violet", "Trim", "Trim &amp; baseboards", "Taller baseboards, casing and feature walls like shiplap."),
]
TILES_HTML = ('<div class="tiles">' + "".join(
    f'<a class="tilecard {c}" href="services.html"><span class="num">{cat}</span><span class="arr" aria-hidden="true">→</span><h3>{h}</h3><p>{p}</p></a>'
    for c, cat, h, p in TILES) + '</div>')

PAIRS = [("kitchen", "Kitchen remodel and flooring", "Kitchens", "images/kitchen-a-before-1.jpg", "images/kitchen-b-after-1.jpg"),
         ("exterior-a", "Exterior repaint", "Painting", "images/exterior-a-before.jpg", "images/exterior-a-after-1.jpg"),
         ("exterior-b", "Exterior repaint", "Painting", "images/exterior-b-before.jpg", "images/exterior-b-after.jpg"),
         ("floor", "LVP flooring install", "Flooring", "images/flooring-before.jpg", "images/flooring-after.jpg")]
PAIRS_HTML = '<div class="pairs">' + "".join(
    f'<figure class="pair" id="pair-{k}"><div class="stage"><img class="after" src="{af}" alt="{t}, after" loading="lazy"><img class="before" src="{bf}" alt="{t}, before" loading="lazy"><span class="badge">{c}</span></div>'
    f'<figcaption><strong>{t}</strong><span class="seg" role="group" aria-label="Show before or after"><button type="button" data-v="before" aria-pressed="false">Before</button><button type="button" data-v="after" aria-pressed="true">After</button></span></figcaption></figure>'
    for k, t, c, bf, af in PAIRS) + '</div>'

# Sherwin-Williams Colors of the Year (screen colors approximate)
COLORS = [("2026", "Universal Khaki", "SW 6150", "#B8A992"), ("2024", "Upward", "SW 6239", "#BFC8D0"),
          ("2023", "Redend Point", "SW 9081", "#AE8E7E"), ("2022", "Evergreen Fog", "SW 9130", "#95978A"),
          ("2021", "Urbane Bronze", "SW 7048", "#54504A"), ("2020", "Naval", "SW 6244", "#2F3D4C"),
          ("2019", "Cavern Clay", "SW 7701", "#AC6B53"), ("2018", "Oceanside", "SW 6496", "#015A6B"),
          ("2017", "Poised Taupe", "SW 6039", "#8C7E6F"), ("2016", "Alabaster", "SW 7008", "#EDEAE0"),
          ("2015", "Coral Reef", "SW 6606", "#D9786C"), ("2014", "Exclusive Plum", "SW 6263", "#736C7A")]

def room_svg():
    planks = "".join('<line x1="%d" y1="330" x2="%d" y2="500" stroke="#7E5E40" stroke-width="2"/>' % (x, x * 1.18 - 70) for x in range(60, 900, 70))
    planks += "".join('<line x1="0" y1="%d" x2="800" y2="%d" stroke="#7E5E40" stroke-width="1" opacity=".5"/>' % (y, y) for y in (370, 420, 470))
    return ('<svg viewBox="0 0 800 500" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Living room preview painted in the selected color">'
            '<rect class="wall" width="800" height="330" style="fill:var(--wall)"/>'
            '<rect x="470" y="70" width="210" height="150" fill="#CFE3EE"/><rect x="470" y="70" width="210" height="150" fill="none" stroke="#fff" stroke-width="14"/>'
            '<line x1="575" y1="70" x2="575" y2="220" stroke="#fff" stroke-width="4"/>'
            '<rect x="106" y="76" width="178" height="254" fill="#fff"/><rect x="120" y="90" width="150" height="240" fill="#F7F5F0"/>'
            '<rect x="135" y="105" width="120" height="95" fill="none" stroke="#00000014" stroke-width="3"/><rect x="135" y="215" width="120" height="100" fill="none" stroke="#00000014" stroke-width="3"/>'
            '<circle cx="250" cy="215" r="7" fill="#1E1E1E"/>'
            '<rect x="330" y="255" width="190" height="62" rx="10" fill="#E9E4DA"/><rect x="330" y="232" width="190" height="34" rx="10" fill="#F2EEE6"/>'
            '<rect x="342" y="240" width="40" height="30" rx="6" fill="#C9A27E"/><rect x="468" y="240" width="40" height="30" rx="6" fill="#8A9A7B"/>'
            '<rect x="560" y="246" width="16" height="84" fill="#5B4636"/><ellipse cx="568" cy="232" rx="34" ry="24" fill="#4E8A5A"/>'
            '<polygon points="0,330 800,330 800,500 0,500" fill="#9A7552"/>' + planks +
            '<rect x="0" y="296" width="106" height="34" fill="#fff"/><rect x="284" y="296" width="516" height="34" fill="#fff"/></svg>')

def palette():
    chips = "".join(
        f'<button type="button" class="swatch" style="--c:{hx}" data-c="{hx}" data-n="{n}" data-s="{sw}" data-y="{y}" aria-pressed="{"true" if i == 0 else "false"}">'
        f'<span class="chipc"></span><span class="meta"><span class="yr">{y}</span><span class="nm">{n}</span><span class="sw">{sw}</span></span></button>'
        for i, (y, n, sw, hx) in enumerate(COLORS))
    first = COLORS[0]
    return f'''<div class="palette">
<div class="preview"><div class="roomwrap photo" id="roomwrap" data-c="{first[3]}"><canvas id="wallcanvas" width="1050" height="1400" role="img" aria-label="A real Heart To Home kitchen with natural wood cabinets, walls shown in the selected paint color"></canvas></div>
<div class="nowshow"><strong id="cname">{first[1]}</strong><span class="mono" id="cmeta">{first[2]} · {first[0]} Color of the Year</span></div>
<div class="swpromise"><b>We proudly use Sherwin-Williams paint.</b><span>Pick any color and we'll bring it to life.</span></div></div>
<div><div class="chips" role="group" aria-label="Sherwin-Williams Colors of the Year">{chips}</div>
<p class="fine" style="margin-top:14px">Tap a color to repaint the walls in this kitchen from one of our real projects. In 2025 Sherwin-Williams released a nine-color capsule instead of a single color. Screen colors are approximate, so always check a real sample before you decide.</p></div>
</div>'''

SCHEMA = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HomeAndConstructionBusiness",
"name":"{NAME}","telephone":"{TEL}","email":"{EMAIL}",
"areaServed":["Surprise AZ","Goodyear AZ","Buckeye AZ","Avondale AZ","Litchfield Park AZ","Peoria AZ","Glendale AZ","Sun City AZ","Sun City West AZ","El Mirage AZ"],
"description":"Licensed, bonded and insured painting, kitchen installs, bathroom remodels, flooring, trim and handyman service in the Phoenix West Valley. {ROC}."}}</script>'''

AREAS = '''<section class="band"><div class="wrap">
<div class="head"><p class="eyebrow">Service area</p><h2>Proudly serving the West Valley</h2><p>Larger projects also scheduled in Tucson and Prescott.</p></div>
<div class="areas"><span>Surprise</span><span>Goodyear</span><span>Buckeye</span><span>Avondale</span><span>Litchfield Park</span><span>Peoria</span><span>Glendale</span><span>Sun City &amp; Sun City West</span><span>El Mirage</span><span>Waddell</span></div>
</div></section>'''

def inner_hero(eyebrow, title, lead):
    return (f'<section class="hero inner-hero"><div class="wrap"><div class="min">'
            f'<p class="eyebrow">{eyebrow}</p><h1 style="margin-top:14px">{title}</h1><p class="lead">{lead}</p></div></div></section>')

PAGES = {}

PAGES["index.html"] = ("Heart To Home", "Painting, kitchen installs, bathroom remodels, flooring, trim and handyman service in the Phoenix West Valley. 10% off for military, first responders and educators.",
'''<section class="hero"><div class="wrap">
<div class="min"><p class="eyebrow">Family owned · Licensed, bonded &amp; insured · AZ ROC #342540</p>
<p class="slogan">From our heart to your home.</p>
<h1 style="margin-top:10px">Your home,<br><span class="rot" id="rot" data-words="painted.|remodeled.|floored.|trimmed out.|fixed up.">painted.</span></h1>
<p class="lead">We're a family-owned, local company that treats every house like it's our own. Painting, kitchens, bathrooms, flooring, trim and the little fixes in between, with the owner on every job.</p>
<div class="ctas"><a class="btn btn-primary" href="estimate.html">Schedule a free estimate</a><a class="btn btn-ghost" href="photos.html">See our work</a></div></div>
<div class="collage">
<img class="p1" src="images/kitchen-b-after-2.jpg" alt="Finished kitchen with white shaker cabinets, quartz island and plank flooring">
<img class="p2" src="images/exterior-b-after.jpg" alt="Freshly painted stucco home exterior">
</div></div></div></section>''' + TRUST +
'''<section class="band"><div class="wrap"><div class="head"><p class="eyebrow">What we do</p><h2>One crew. <span class="hl">The whole job.</span></h2>
<p>No juggling five contractors. We handle the work ourselves, so it gets done right and on schedule.</p></div>''' + TILES_HTML + '''</div></section>
<section class="band mist"><div class="wrap"><div class="head"><p class="eyebrow">Real projects</p><h2>Before <span class="hl">&amp;</span> after</h2><p>Tap Before to see where each job started.</p></div>'''
+ PAIRS_HTML + '''<div class="ctas"><a class="btn btn-primary" href="photos.html">See all project photos</a></div></div></section>''' + '''<section class="band shiplap"><div class="wrap"><div class="split" style="align-items:center">
<div class="prose"><p class="eyebrow">From our family to yours</p><h2>Local hands. <span class="hl">Family values.</span></h2>
<p class="lead">When you call Heart To Home, you're not getting a call center or a crew you've never met. You're getting a local, family-owned business that shows up when we say we will, keeps your home clean, and stands behind every job.</p>
<p>Our family lives right here in Maricopa County, and our name is on every house we work on. That's why we treat your home like it's our own.</p>
<p style="font:italic 500 1.4rem/1.3 var(--display);color:var(--walnut)">From our heart to your home. Adam Talal, owner</p></div>
<div class="facts">
<div><span class="k">Family owned</span><span class="v">Yes, and proud of it</span></div><div><span class="k">Based in</span><span class="v">Maricopa County, AZ</span></div>
<div><span class="k">Who shows up</span><span class="v">The owner, every job</span></div><div><span class="k">License</span><span class="v">AZ ROC #342540</span></div>
<div><span class="k">Paint</span><span class="v">Sherwin-Williams</span></div></div>
</div></div></section>''' + HEROES + MOVES +
'''<section class="band"><div class="wrap"><div class="head"><p class="eyebrow">Sherwin-Williams Colors of the Year</p><h2>Try a color on for size.</h2>
<p>Tap through a decade of Sherwin-Williams Colors of the Year and watch the walls of a real kitchen we finished change color.</p></div>''' + palette() + '''</div></section>''' + HONEY + AREAS + CONTACT + SCHEMA)

PAGES["services.html"] = ("Our Services", "Interior and exterior painting, kitchen installs, bathroom remodels, flooring, trim and handyman service in the West Valley.",
inner_hero("Services", 'What we do, <span class="hl">done right.</span>', "One licensed crew for painting, kitchens, baths, floors, trim and the honey-do list. Every job is quoted at a fixed price after a free walkthrough.")
+ '''<section class="band"><div class="wrap"><div class="services">
<div class="svc" style="--c:var(--olive)"><h3>Interior painting</h3><p>Walls, ceilings, accent walls and full-home repaints.</p><ul><li>Drywall patching and texture matching</li><li>Floors and furniture protected</li><li>Clean cut lines at ceilings and trim</li></ul></div>
<div class="svc" style="--c:var(--sage)"><h3>Exterior painting</h3><p>Stucco, trim, fascia, garage and entry doors.</p><ul><li>Crack repair and caulking</li><li>Windows, stone and fixtures fully masked</li><li>HOA color approvals handled</li></ul></div>
<div class="svc" style="--c:var(--ink)"><h3>Kitchen installs</h3><p>Install and finish the pieces that make a kitchen new.</p><ul><li>Cabinet installation</li><li>Countertops and backsplash</li><li>Hardware, trim and paint to finish</li></ul></div>
<div class="svc" style="--c:var(--clay)"><h3>Bathroom remodels</h3><p>From quick refreshes to full makeovers.</p><ul><li>Tub-to-shower conversions</li><li>Tile, vanities and mirrors</li><li>Paint, trim and flooring to match</li></ul></div>
<div class="svc" style="--c:var(--wheat)"><h3>Flooring</h3><p>Luxury vinyl plank and laminate.</p><ul><li>Old carpet and flooring removed</li><li>New baseboard installed with floors</li><li>Transitions and thresholds finished</li></ul></div>
<div class="svc" style="--c:var(--walnut)"><h3>Trim &amp; baseboards</h3><p>Upgrade skinny builder trim to a finished look.</p><ul><li>Taller baseboards and door casing</li><li>Shiplap and feature walls</li><li>Caulked, filled and spray finished</li></ul></div>
</div></div></section>''' + MOVES + HEROES +
'''<section class="band dark"><div class="wrap"><div class="head"><p class="eyebrow">How we finish trim</p><h2>The extra steps most painters skip</h2><p>It's why our trim feels smooth when you run your hand over it.</p></div>
<div class="process">
<div class="step"><span class="n">1</span><h3>Sand</h3><p>Scuff and clean every surface so paint bonds instead of peeling.</p></div>
<div class="step"><span class="n">2</span><h3>First coat</h3><p>Premium self-leveling Sherwin-Williams paint.</p></div>
<div class="step"><span class="n">3</span><h3>Sand again</h3><p>Knock down raised grain and dust for a glass-smooth base.</p></div>
<div class="step"><span class="n">4</span><h3>Spray finish</h3><p>A sprayed final coat with no brush marks or roller texture.</p></div>
</div></div></section>''' + HONEY +
'''<section class="band mist"><div class="wrap"><div class="head"><p class="eyebrow">Our process</p><h2>From first call to final walkthrough</h2></div>
<div class="process">
<div class="step"><span class="n">1</span><h3>Request</h3><p>Send the estimate form or call. Photos help us prepare.</p></div>
<div class="step"><span class="n">2</span><h3>Walkthrough</h3><p>We measure, talk colors and materials, and answer questions.</p></div>
<div class="step"><span class="n">3</span><h3>Written quote</h3><p>A fixed price with scope and schedule spelled out.</p></div>
<div class="step"><span class="n">4</span><h3>Work &amp; final check</h3><p>We do the work ourselves and walk it with you before we call it done.</p></div>
</div></div></section>''' + CONTACT)

PAGES["photos.html"] = ("Project Photos", "Before and after photos of painting, kitchen, bathroom, flooring, trim and handyman projects by Heart To Home.",
inner_hero("Our work", 'Project <span class="hl">photos</span>', "Before, during and after shots from real Heart To Home jobs. Filter by the kind of work you're planning.")
+ '''<section class="band"><div class="wrap">
<div class="filters" role="group" aria-label="Filter photos">
<button type="button" data-cat="All" aria-pressed="true">All</button><button type="button" data-cat="Painting" aria-pressed="false">Painting</button>
<button type="button" data-cat="Kitchens" aria-pressed="false">Kitchens</button><button type="button" data-cat="Bathrooms" aria-pressed="false">Bathrooms</button>
<button type="button" data-cat="Flooring" aria-pressed="false">Flooring</button><button type="button" data-cat="Trim" aria-pressed="false">Trim</button>
<button type="button" data-cat="Handyman" aria-pressed="false">Handyman</button></div>
<div class="gal" id="gallery"></div></div></section>''' + CONTACT)

PAGES["colors.html"] = ("Paint Colors", "Explore Sherwin-Williams Colors of the Year and preview them in a room. Heart To Home proudly uses Sherwin-Williams paint.",
inner_hero("Sherwin-Williams Colors of the Year", 'Find your <span class="hl">color.</span>', "We proudly use Sherwin-Williams paint. Tap through the Colors of the Year to see how each one feels on a wall, then bring your favorites to your free estimate.")
+ '<section class="band"><div class="wrap">' + palette() + '</div></section>' + MOVES + CONTACT)

PAGES["reviews.html"] = ("Customer Reviews", "What homeowners say about Heart To Home painting, remodeling, flooring and handyman work.",
inner_hero("Reviews", 'What our customers <span class="hl">say</span>', "Real reviews from real homeowners. We post them as written.")
+ '''<section class="band"><div class="wrap"><div class="empty" id="reviews-empty"><h3>Customer reviews are on their way</h3>
<p class="muted">We're gathering reviews from recent customers. Worked with us? We'd be grateful if you shared how it went.</p>
<a class="btn btn-primary" href="estimate.html">Start your own project</a></div><div class="reviews" id="reviews"></div></div></section>''' + CONTACT)

PAGES["about.html"] = ("About Heart To Home", "Heart To Home is a family-run, licensed, bonded and insured home improvement company in the Phoenix West Valley.",
inner_hero("About us", 'A family business, <span class="hl">built one home at a time.</span>', "Family owned, locally rooted, and still on every job.")
+ f'''<section class="band"><div class="wrap"><div class="split">
<div class="prose"><p class="lead">Heart To Home is a family-owned business. Adam Talal started it from the ground up, and our family lives right here in Maricopa County.</p>
<p>Our motto, "From our heart to your home," says what we believe: the work should come from the heart, and it should leave your house feeling more like home. We keep our crew small on purpose. The person who quotes your job is the person doing the work, so nothing gets lost between a salesperson, a manager and a crew you've never met.</p>
<p>We also paint new homes for a regional home builder, so we work to builder schedules and builder standards every week. At your house, we bring that same speed with the care of a custom finish.</p>
<p>And we proudly use Sherwin-Williams paint on our projects.</p></div>
<div class="facts">
<div><span class="k">Owner</span><span class="v">Adam Talal</span></div><div><span class="k">License</span><span class="v">{ROC}</span></div>
<div><span class="k">Coverage</span><span class="v">Licensed, bonded &amp; insured</span></div><div><span class="k">Paint</span><span class="v">Sherwin-Williams</span></div>
<div><span class="k">Service area</span><span class="v">Phoenix West Valley</span></div><div><span class="k">Also serving</span><span class="v">Tucson &amp; Prescott</span></div>
<div><span class="k">Hero discount</span><span class="v">10% off for military, first responders &amp; educators</span></div><div><span class="k">Phone</span><span class="v">{PHONE}</span></div>
</div></div></div></section>
<section class="band mist"><div class="wrap"><div class="head"><p class="eyebrow">Questions</p><h2>Frequently asked</h2></div><div class="faq">
<details><summary>Are you licensed and insured?</summary><p>Yes. We are licensed with the Arizona Registrar of Contractors ({ROC}), bonded and insured. You can look up our license on the ROC website.</p></details>
<details><summary>Who gets the 10% hero discount?</summary><p>Military (active duty and veterans), first responders and educators get 10% off their project. Just mention it when you request your estimate.</p></details>
<details><summary>What paint do you use?</summary><p>We proudly use Sherwin-Williams paint. Pick any Sherwin-Williams color and we'll bring it to life.</p></details>
<details><summary>Why paint before moving in or out?</summary><p>An empty house is the easiest house to paint. There's no furniture to move or cover, every wall is easy to reach, and the job is done before you settle in or hand over the keys.</p></details>
<details><summary>Are estimates really free?</summary><p>Yes. We come out, look at the space, and send a written, fixed-price quote with no obligation.</p></details>
<details><summary>Do you handle HOA color approvals?</summary><p>For exterior work we can help you pull your HOA's approved color schemes and prepare the submission.</p></details>
<details><summary>Do I need to move furniture?</summary><p>No. We move and cover furniture as part of the job. We just ask that small items, decor and valuables be put away.</p></details>
<details><summary>Do you use subcontractors?</summary><p>Rarely. Painting, flooring, trim, kitchen installs, bathroom work and handyman jobs are done by our own crew. If a project needs a licensed plumber or electrician, we tell you up front and coordinate it for you.</p></details>
<details><summary>Can you handle a list of small jobs?</summary><p>Yes. Send us your honey-do list and we'll quote the whole list and knock it out in one visit.</p></details>
</div></div></section>''' + CONTACT)

CITIES = ["Surprise", "Goodyear", "Buckeye", "Avondale", "Litchfield Park", "Peoria", "Glendale", "Sun City / Sun City West", "El Mirage", "Waddell", "Tucson area", "Prescott area", "Other"]
SERVICES = ["Interior painting", "Exterior painting", "Move-in paint", "Move-out paint", "Kitchen install", "Bathroom remodel", "Flooring", "Trim / baseboards", "Handyman list"]
PAGES["estimate.html"] = ("Free Estimate", "Request a free estimate for painting, kitchens, bathrooms, flooring, trim or handyman work from Heart To Home.",
inner_hero("Free estimate", 'Tell us about your <span class="hl">project.</span>', "Fill this out and Adam gets it on his phone right away. Most requests get a reply the same day.")
+ f'''<section class="band"><div class="wrap"><div class="formgrid">
<form name="estimate" method="POST" action="thanks.html" data-netlify="true" netlify-honeypot="company-website" enctype="multipart/form-data">
<input type="hidden" name="form-name" value="estimate">
<p class="hidden-field"><label for="hp">Leave this empty</label><input id="hp" name="company-website" tabindex="-1" autocomplete="off"></p>
<div class="two"><div class="field"><label for="f-name">Your name <span class="req">*</span></label><input id="f-name" name="name" required autocomplete="name"></div>
<div class="field"><label for="f-phone">Phone <span class="req">*</span></label><input id="f-phone" name="phone" type="tel" required autocomplete="tel"></div></div>
<div class="two"><div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" autocomplete="email"></div>
<div class="field"><label for="f-city">City <span class="req">*</span></label><select id="f-city" name="city" required><option value="">Choose your city</option>{"".join(f"<option>{c}</option>" for c in CITIES)}</select></div></div>
<fieldset><legend class="lbl">What do you need? <span class="req">*</span></legend><div class="checks">
{"".join(f'<label><input type="checkbox" name="services" value="{s}"> {s}</label>' for s in SERVICES)}</div></fieldset>
<label class="herobox" for="f-hero"><input type="checkbox" id="f-hero" name="hero-discount" value="Yes"><span>I'm military, a first responder or an educator. Apply my 10% off.</span></label>
<div class="field"><label for="f-details">Project details</label><textarea id="f-details" name="details" placeholder="Rooms, rough square footage, colors you have in mind, your move date, anything we should know"></textarea></div>
<div class="two"><div class="field"><label for="f-when">When would you like to start?</label><select id="f-when" name="timing"><option>As soon as possible</option><option>Before my move date</option><option>Within a month</option><option>1 to 3 months</option><option>Just getting prices</option></select></div>
<div class="field"><label for="f-contact">Best way to reach you</label><select id="f-contact" name="contact-method"><option>Text</option><option>Call</option><option>Email</option></select></div></div>
<div class="field"><label for="f-photo">Photos of the space (optional)</label><input id="f-photo" name="photo" type="file" accept="image/*"><span class="hint">One photo is plenty to get started.</span></div>
<p class="notice" id="preview-note" hidden>This is a preview. Once the site is live, this button sends the request straight to Adam's phone.</p>
<button class="btn btn-primary" type="submit">Send my estimate request</button>
</form>
<div class="side">
<div class="card"><p class="eyebrow">Prefer to talk?</p>
<div class="row"><div><div class="k">Call or text</div><div class="v">{PHONE}</div></div><button class="copy" type="button" data-t="{PHONE}">Copy</button></div>
<div class="row"><div><div class="k">Email</div><div class="v">{EMAIL}</div></div><button class="copy" type="button" data-t="{EMAIL}">Copy</button></div></div>
<div class="card"><p class="eyebrow">What happens next</p><p class="muted">1. Adam reviews your request and reaches out.<br>2. We set a time for a free walkthrough.<br>3. You get a written, fixed-price quote.</p></div>
<div class="card" style="background:var(--wheat);border-color:var(--wheat)"><p class="eyebrow" style="color:var(--ink)">Local heroes</p><p><b>10% off</b> for military, first responders and educators. Check the box on the form.</p></div>
<div class="card"><p class="eyebrow">Licensed, bonded &amp; insured</p><p class="mono">{ROC}</p></div>
</div></div></div></section>''')

PAGES["thanks.html"] = ("Request Received", "Thanks for your estimate request.",
inner_hero("Request received", 'Thanks! Adam has <span class="hl">your request.</span>', f"You'll hear back soon, usually the same day. If it's urgent, call or text {PHONE}.")
+ '<section class="band"><div class="wrap"><div class="ctas" style="margin-top:0"><a class="btn btn-primary" href="photos.html">Browse our work</a><a class="btn btn-ghost" href="colors.html">Explore colors</a></div></div></section>')

def doc(fname, title, desc, body, full=True):
    head = (f'<title>{title}</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n'
            f'<meta name="description" content="{desc}">\n{FONTS}\n<link rel="stylesheet" href="style.css">\n')
    content = header(fname) + "\n<main>" + body + "</main>\n" + FOOTER + '\n<script src="site.js"></script>\n'
    if full:
        return ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
                '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
                + head + '</head>\n<body>\n' + content + '</body>\n</html>\n')
    return head + content

if os.path.isdir(PREV):
    shutil.rmtree(PREV)
os.makedirs(PREV)
for f in os.listdir(SITE):
    if f.endswith(".html"):
        os.remove(os.path.join(SITE, f))
for fname, (title, desc, body) in PAGES.items():
    open(os.path.join(SITE, fname), "w").write(doc(fname, title, desc, body, True))
    open(os.path.join(PREV, fname), "w").write(doc(fname, title, desc, body, fname != "index.html"))
for asset in ("style.css", "site.js"):
    shutil.copy(os.path.join(SITE, asset), os.path.join(PREV, asset))
shutil.copytree(os.path.join(SITE, "images"), os.path.join(PREV, "images"))
print("built", len(PAGES), "pages")

"""Generates the static HTML pages in /pages. Edit content here OR edit the .html files directly."""
import json
NAV=[("index","Home"),("services","Services"),("doctors","Doctors"),("gallery","Gallery"),("reviews","Reviews"),("about","About"),("contact","Contact")]
SITE="https://your-domain.com"
def layout(slug,title,desc,body,hero=None):
    menu="".join(f'<li><a href="{s}.html"{" class=active aria-current=page" if s==slug else ""}>{n}</a></li>' for s,n in NAV)
    ld=json.dumps({"@context":"https://schema.org","@type":"Dentist","name":"BrightRoot Dental Clinic","telephone":"+91-90000-00000","address":{"@type":"PostalAddress","streetAddress":"12 Main Road","addressLocality":"Salem","addressRegion":"Tamil Nadu","addressCountry":"IN"},"url":SITE})
    h=hero or ""
    return f'''<!DOCTYPE html>
<html lang="en" dir="ltr" data-theme="light">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} | BrightRoot Dental</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{SITE}/pages/{slug}.html">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@600;700&family=Figtree:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
<link rel="stylesheet" href="../assets/css/style.css"><link rel="stylesheet" href="../assets/css/dark-mode.css"><link rel="stylesheet" href="../assets/css/rtl.css">
<script type="application/ld+json">{ld}</script>
<script src="../assets/js/main.js" defer></script>
</head>
<body>
<!-- ===== HEADER ===== -->
<header class="site-header"><div class="container nav">
<a class="logo" href="index.html"><i class="bi bi-heart-pulse-fill"></i> BrightRoot</a>
<ul class="menu" id="menu">{menu}</ul>
<div class="tools">
<button class="icon-btn" id="themeToggle" aria-label="Toggle dark mode"><i class="bi bi-moon-stars"></i></button>
<button class="icon-btn" id="rtlToggle" aria-label="Toggle right-to-left layout"><i class="bi bi-translate"></i></button>
<a class="btn" href="contact.html">Book visit</a>
<button class="icon-btn" id="navToggle" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><i class="bi bi-list"></i></button>
</div></div></header>
<main>
{h}{body}
</main>
<!-- ===== FOOTER ===== -->
<footer class="site-footer"><div class="container footer-grid">
<div><h3>BrightRoot Dental</h3><p>Gentle, modern dental care for the whole family.</p></div>
<div><h3>Visit</h3><p>12 Main Road, Salem<br>Mon–Sat 9:00–20:00<br><a href="tel:+919000000000">+91 90000 00000</a></p></div>
<div><h3>Newsletter</h3><!-- TODO: connect Mailchimp/ConvertKit form action -->
<form action="#" method="post" data-validate data-demo><label for="nl">Email</label><input id="nl" type="email" name="email" required><button class="btn" type="submit">Subscribe</button></form></div>
</div><div class="container"><p>&copy; 2026 BrightRoot Dental. All rights reserved.</p></div></footer>
</body></html>'''
def head(t,s): return f'<section class="page-hero"><div class="container"><h1>{t}</h1><p>{s}</p></div></section>'
def sec(inner,alt=False): return f'<section class="section{" alt" if alt else ""}"><div class="container">{inner}</div></section>'
SERV=[("bi-stars","Teeth cleaning","Scaling and polishing that removes plaque and stains in one visit."),("bi-tools","Fillings","Tooth-coloured fillings that match your smile and last for years."),("bi-emoji-smile","Braces and aligners","Metal, ceramic or clear aligners planned around your schedule."),("bi-brightness-high","Teeth whitening","Safe in-clinic whitening, up to several shades brighter."),("bi-nut","Dental implants","Permanent replacement for missing teeth, placed by a specialist."),("bi-shield-plus","Root canal care","Pain-free treatment to save a badly infected tooth.")]
cards="".join(f'<article class="card"><i class="bi {i} big"></i><h3>{t}</h3><p class="muted">{d}</p></article>' for i,t,d in SERV)
DOC=[("Dr. Ananya Rao","Orthodontist, MDS","12 years of experience with braces and clear aligners."),("Dr. Karthik Raj","Implant surgeon, MDS","Specialises in implants and full-mouth rehabilitation."),("Dr. Meera Nair","Paediatric dentist, BDS","Makes first dental visits calm for children.")]
docs="".join(f'<article class="card"><div class="ph"><i class="bi bi-person-badge"></i></div><h3>{n}</h3><p><strong>{q}</strong></p><p class="muted">{d}</p></article>' for n,q,d in DOC)
REV=[("Priya S.","Zero pain during my root canal, and the team explained every step."),("Arun M.","My kids actually ask to visit Dr. Meera. Clean, friendly clinic."),("Fatima K.","Got my braces here. Clear pricing and on-time appointments.")]
revs="".join(f'<article class="card skeleton"><p class="stars">★★★★★</p><p>{t}</p><strong>{n}</strong></article>' for n,t in REV)
form='''<form action="https://formspree.io/f/your-form-id" method="post" data-validate data-demo novalidate>
<label for="name">Full name</label><input id="name" name="name" required>
<label for="phone">Phone</label><input id="phone" name="phone" type="tel" pattern="[0-9]{10}" required>
<label for="email">Email</label><input id="email" name="email" type="email" required>
<label for="svc">Treatment</label><select id="svc" name="service" required><option value="">Choose a treatment</option>'''+"".join(f"<option>{t}</option>" for _,t,_ in SERV)+'''</select>
<label for="date">Preferred date</label><input id="date" name="date" type="date" required>
<label for="msg">Message (optional)</label><textarea id="msg" name="message" rows="3"></textarea>
<button class="btn" type="submit">Request appointment</button></form>'''
P={}
P["index"]=("Dental Clinic & Oral Care in Salem","Gentle family dentistry: cleaning, braces, whitening and implants. Book your appointment online today.",
 f'''<section class="hero"><div class="container hero-grid"><div><h1>Dental care that doesn't hurt a bit.</h1>
<p>Same-day appointments, clear pricing and specialists for braces, implants and children's teeth.</p>
<a class="btn" href="contact.html">Book an appointment</a> <a class="btn ghost" href="services.html">See treatments</a></div>
<div class="card"><h2>Quick booking</h2><p class="muted">We call back within 2 hours.</p>{form.replace('id="','id="h-').replace('for="','for="h-')}</div></div></section>'''
 +sec(f'<h2>Our treatments</h2><div class="grid">{cards}</div>')
 +sec(f'<h2>Meet your dentists</h2><div class="grid">{docs}</div>',True)
 +sec(f'<h2>What patients say</h2><div class="grid">{revs}</div>'))
P["services"]=("Dental Services","Cleaning, fillings, braces, whitening, implants and root canal treatment.",head("Our services","Every treatment starts with a free check-up.")+sec(f'<div class="grid">{cards}</div>'))
P["doctors"]=("Our Doctors","Meet the dentists and specialists at BrightRoot Dental.",head("Our doctors","Qualified specialists, one friendly team.")+sec(f'<div class="grid">{docs}</div>'))
P["gallery"]=("Clinic Gallery","Photos of our clinic interior and treatment rooms.",head("Inside the clinic","Treatment rooms, waiting area and sterilisation unit.")+sec('<!-- TODO: replace placeholders with <img src="../assets/images/x.webp" alt="..." loading="lazy"> --><div class="grid">'+"".join(f'<figure class="ph skeleton" role="img" aria-label="{c}"><i class="bi bi-image"></i></figure>' for c in ["Reception","Treatment room 1","Treatment room 2","Sterilisation unit","Kids corner","X-ray room"])+'</div>'))
P["reviews"]=("Patient Reviews","Read what patients say about BrightRoot Dental.",head("Patient reviews","Honest feedback from our patients.")+sec(f'<div class="grid">{revs}</div>'))
P["about"]=("About Us","Our story, mission and team at BrightRoot Dental Clinic.",head("About BrightRoot","A neighbourhood clinic since 2012.")+sec('<div class="grid"><article class="card"><h3>Our mission</h3><p>Make good dental care easy to reach, easy to understand and free of fear.</p></article><article class="card"><h3>Our story</h3><p>Founded in 2012 by three dentists who wanted a calmer clinic. We have treated over 20,000 patients.</p></article><article class="card"><h3>Our promise</h3><p>You see the price before treatment starts, and your instruments are sterilised every time.</p></article></div>'))
P["contact"]=("Contact & Book Appointment","Book a dental appointment or find our clinic location, phone and timings.",head("Book an appointment","Fill the form or call us.")+sec(f'<div class="grid"><div class="card">{form}</div><div><h2>Find us</h2><p>12 Main Road, Salem<br>Mon–Sat 9:00–20:00<br><a href="tel:+919000000000">+91 90000 00000</a></p><!-- TODO: paste Google Maps embed URL --><iframe title="Clinic location map" src="about:blank" width="100%" height="300" loading="lazy" style="border:0;border-radius:12px;background:var(--mint)"></iframe></div></div>'))
P["404"]=("Page Not Found","The page you are looking for does not exist.",sec('<h1>Page not found</h1><p>The link may be broken or the page has moved.</p><a class="btn" href="index.html">Back to home</a> <a class="btn ghost" href="contact.html">Contact us</a>'))
P["coming-soon"]=("Coming Soon","Our new website is almost ready.",sec('<h1>New website coming soon</h1><p>We are getting ready. Call <a href="tel:+919000000000">+91 90000 00000</a> to book in the meantime.</p>'))
for s,(t,d,b) in P.items(): open(f"pages/{s}.html","w",encoding="utf-8").write(layout(s,t,d,b))
open("index.html","w").write('<!DOCTYPE html><meta charset="utf-8"><meta http-equiv="refresh" content="0;url=pages/index.html"><a href="pages/index.html">Open site</a>')
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{SITE}/pages/{s}.html</loc></url>" for s in P if s not in("404","coming-soon"))+"</urlset>")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")

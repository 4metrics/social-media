import sys, math
sys.path.insert(0, "/home/claude/tools")
from festas_base import *

# ===== Black Friday · claro · 27/11
hours = list(range(8, 21))
vals = [22, 30, 41, 55, 62, 70, 52, 44, 39, 35, 33, 31, 30]
mx = max(vals)
bars = ""
for h, v in zip(hours, vals):
    c = LIME if h < 14 else "#F4A39C"
    bars += f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:10px"><div style="width:100%;height:{int(260*v/mx)}px;border-radius:8px 8px 3px 3px;background:{c}"></div><span style="font-size:18px;color:{MUTL}">{h}h</span></div>'
bf = f'''<section class="s lt" id="bf">{glow(560,-260,760)}
<span class="pill">Black Friday</span>
<h1 style="font-size:84px;line-height:90px">Hoje é a Black Friday.<br><span class="hl">O funil não espera o relatório.</span></h1>
<p class="lead">Mídia, leads e vendas mudam a cada hora. Quem vê o funil no mesmo dia ajusta antes de a data acabar.</p>
<div class="mid"><div class="card" style="padding:34px 36px;display:flex;flex-direction:column;gap:24px">
<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-size:26px;font-weight:600">Leads por hora · Black Friday</span><span style="font-size:22px;color:{MUTL}">hoje</span></div>
<div style="display:flex;align-items:flex-end;gap:10px;height:300px">{bars}</div>
<div style="display:flex;align-items:center;gap:16px;padding:20px 22px;border-radius:16px;background:#FEF3F2;border:1px solid #FECDCA">
<i style="width:14px;height:14px;border-radius:9px;background:#D92D20;flex:none"></i>
<span style="font-size:25px;line-height:34px;color:{NAVY}"><b>Leads em queda desde as 14h.</b> <span style="color:{MUTL}">Dá tempo de mover a verba hoje.</span></span></div></div></div>
<div class="foot">{logo(False)}</div></section>'''

# ===== Natal · lima · 24/12
tree = ""
rows = [1, 2, 3, 4, 5]
R, G = 22, 66
for ri, n in enumerate(rows):
    y = 120 + ri * G
    for k in range(n):
        x = 220 + (k - (n - 1) / 2) * G
        tree += f'<circle cx="{x}" cy="{y}" r="{R}" fill="{NAVY}"/>'
tree += f'<circle cx="220" cy="40" r="30" fill="#FFFFFF"/>'   # estrela = ponto de destaque branco
tree += f'<rect x="204" y="{120+5*G-30}" width="32" height="54" rx="10" fill="{NAVY}"/>'
nat = f'''<section class="s" id="nat" style="background-color:{LIME};background-image:radial-gradient(rgba(5,19,28,.10) 1px,transparent 1.2px);color:{NAVY}">
<span class="pill" style="background:rgba(255,255,255,.35);color:{NAVY};border:1px solid rgba(5,19,28,.2)">Boas festas</span>
<div class="mid" style="align-items:center;gap:56px">
<svg width="440" height="470" viewBox="0 0 440 470">{tree}</svg>
<h1 style="font-size:120px;line-height:120px;text-align:center">Feliz Natal.</h1>
<p class="lead" style="color:#1F3A12;text-align:center;max-width:860px">Obrigado a cada cliente e parceiro que construiu 2026 com a gente. Que as festas tragam descanso e boas conversas.</p></div>
<div class="foot"><span style="display:inline-flex;align-items:center;gap:12px">{SYM(40,dots=NAVY,accent="#FFFFFF")}{WORD(32,NAVY,"#FFFFFF")}</span><span style="font-size:24px;color:#1F3A12">Equipe 4metrics</span></div></section>'''

# ===== Ano Novo · escuro · 31/12
burst = ""
for cx, cy, sc in [(900, 190, 1.0), (170, 420, .6)]:
    for ring, (rad, n, r, op) in enumerate([(55, 8, 7, .95), (95, 12, 6, .65), (135, 16, 4, .4)]):
        for k in range(n):
            a = 2 * math.pi * k / n + ring * .2
            burst += f'<circle cx="{cx+sc*rad*math.cos(a):.1f}" cy="{cy+sc*rad*math.sin(a):.1f}" r="{r*sc:.1f}" fill="{LIME if k%3==0 else "#FFFFFF"}" opacity="{op}"/>'
    burst += f'<circle cx="{cx}" cy="{cy}" r="{12*sc}" fill="{LIME}"/>'
def wish(t): return f'<div class="card" style="padding:20px 26px;font-size:26px;font-weight:600;display:flex;align-items:center;gap:14px;white-space:nowrap"><i style="width:12px;height:12px;border-radius:9px;background:{LIME}"></i>{t}</div>'
an = f'''<section class="s dk" id="an">{glow(380,80,700)}<svg width="1080" height="1350" viewBox="0 0 1080 1350" style="position:absolute;left:0;top:0">{burst}</svg>
<span class="pill">Feliz 2027</span>
<div style="position:relative;height:560px;display:flex;align-items:center;justify-content:center">

<div style="position:relative;text-align:center">
<div style="font-family:'Plus Jakarta Sans';font-size:40px;font-weight:600;color:{MUTD};text-decoration:line-through;text-decoration-thickness:3px">2026</div>
<div style="font-family:'Plus Jakarta Sans';font-size:230px;line-height:230px;font-weight:700;letter-spacing:-0.05em">202<span style="color:{LIME}">7</span></div></div></div>
<h1 style="font-size:72px;line-height:80px">Que o novo ano traga mais respostas <span class="hl">e menos achismo.</span></h1>
<div style="position:relative;display:flex;flex-direction:column;gap:14px">
<span style="font-size:22px;font-weight:600;color:{LIME};text-transform:uppercase;letter-spacing:.08em">Nossos desejos para o seu 2027</span>
<div style="display:flex;gap:12px;flex-wrap:wrap">{wish("Número certo no dia 1")}{wish("Uma base, as mesmas regras")}{wish("IA com dado confiável")}</div></div>
<div class="foot">{logo(True)}</div></section>'''

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{bf}{nat}{an}</body></html>"
open(f"{D}/festas.html", "w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{D}/festas.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(900)
    print(pg.evaluate("""()=>[...document.querySelectorAll('section')].map(s=>{const r=s.getBoundingClientRect();
      return s.id+':'+[...s.querySelectorAll('*')].filter(e=>{const q=e.getBoundingClientRect();return q.width&&(q.right>r.right+1||q.bottom>r.bottom+1)&&!e.classList.contains('g')&&e.tagName!='circle'&&e.tagName!='svg'}).length})"""))
    for sid, name in [("bf","2026-11-27-black-friday-v2"),("nat","2026-12-24-natal-v1"),("an","2026-12-31-ano-novo-v1")]:
        pg.locator(f"#{sid}").screenshot(path=f"{D}/{name}.png")
    b.close()
from PIL import Image
fs=[f"{D}/{n}.png" for n in ("2026-11-27-black-friday-v2","2026-12-24-natal-v1","2026-12-31-ano-novo-v1")]
sh=Image.new('RGB',(3*540+40,695),'#E1E7E4')
for k,f in enumerate(fs): sh.paste(Image.open(f).convert('RGB').resize((540,675),Image.LANCZOS),(10+k*550,10))
sh.save(f"{D}/visao-geral-festas.png")

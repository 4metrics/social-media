import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from stories import ff, NAVY, LIME
from PIL import Image

A = "/home/claude/assets/plataforma"
D = "/home/claude/out/post-resumo"
os.makedirs(D, exist_ok=True)
HOME = f"{A}/01-home-claro-crop.png"          # 2310 x 1444
RES = f"{A}/02-resumo-executivo-claro.png"    # 2333 x 886
r = Image.open(RES)
r.crop((20, 20, 2310, 485)).save(f"{D}/res-top.png")          # header + 2 items
rows = [(197, 330), (347, 480), (497, 630), (647, 815)]
for i, (y0, y1) in enumerate(rows):
    r.crop((72, y0, 1560, y1)).save(f"{D}/row{i+1}.png")

GTXT = "#406500"
CSS = ff + """*{box-sizing:border-box} body{margin:0;background:#888}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;background-size:22px 22px;margin-bottom:20px}
h1{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em}
.pill{display:inline-flex;align-items:center;height:42px;padding:0 20px;border-radius:999px;font-size:20px;font-weight:600}
.glow{box-shadow:0 0 0 1px rgba(146,197,73,.9),0 0 48px rgba(146,197,73,.35),0 24px 60px rgba(5,19,28,.18)}
"""

def logo(dots, ink):
    return f'<div style="position:absolute;left:72px;bottom:60px;display:inline-flex;align-items:center;gap:12px">{SYM(40,dots=dots,accent=LIME)}{WORD(32,ink,LIME)}</div>'

def home_img(width):
    """Home screenshot with the demo names covered by fictional ones (rendered in the real fonts)."""
    k = width / 2310
    return f'''<div style="position:relative;width:{width}px;height:{round(1444*k)}px">
<img src="file://{HOME}" style="width:100%;height:100%;display:block">
<div style="position:absolute;left:{700*k}px;top:{40*k}px;width:{240*k}px;height:{95*k}px;background:#F4F6F4;font-family:'Plus Jakarta Sans';font-weight:700;font-size:{78*k}px;line-height:{95*k}px;color:#05131C;letter-spacing:-0.02em">Ana</div>
<div style="position:absolute;left:0;top:{1195*k}px;width:{425*k}px;height:{249*k}px;background:#FFFFFF"></div>
<div style="position:absolute;left:{578*k}px;top:{846*k}px;width:{162*k}px;height:{46*k}px;background:#FFFFFF;white-space:nowrap;font-size:{28*k}px;line-height:{46*k}px;color:#4F5B63">Carla Dias</div>
</div>'''

def laptop(width):
    sw = width - 36
    return f'''<div style="display:flex;flex-direction:column;align-items:center">
<div style="width:{width}px;padding:18px 18px 22px;border-radius:28px 28px 10px 10px;background:#0B1418;box-shadow:0 30px 70px rgba(5,19,28,.25)">
 <div style="border-radius:8px;overflow:hidden">{home_img(sw)}</div></div>
<div style="width:{width+120}px;height:26px;border-radius:0 0 26px 26px;background:linear-gradient(#C9D0CC,#9AA5A0)"></div>
<div style="width:180px;height:8px;margin-top:-26px;border-radius:0 0 10px 10px;background:#8A948F"></div></div>'''

def browser(inner, width, dark=False):
    bar = "#1B2A33" if dark else "#E9EEEB"
    url = "#0B1B24" if dark else "#FFFFFF"
    return f'''<div style="width:{width}px;border-radius:16px;overflow:hidden;background:{bar}">
<div style="height:54px;display:flex;align-items:center;gap:10px;padding:0 20px">
 <i style="width:14px;height:14px;border-radius:99px;background:#F97066"></i><i style="width:14px;height:14px;border-radius:99px;background:#F5C451"></i><i style="width:14px;height:14px;border-radius:99px;background:{LIME}"></i>
 <span style="margin-left:16px;height:32px;flex:0 0 360px;border-radius:99px;background:{url};font-size:16px;color:#7A8790;display:flex;align-items:center;padding:0 16px">app.4metrics</span></div>
{inner}</div>'''

def badge(t, c, bg):
    return f'<span style="display:inline-flex;align-items:center;gap:10px;height:44px;padding:0 18px;border-radius:999px;background:{bg};color:{c};font-size:22px;font-weight:600"><i style="width:12px;height:12px;border-radius:99px;background:{c}"></i>{t}</span>'

B_CRIT = ("Crítico", "#D92D20", "#FEE4E2")
B_ATEN = ("Atenção", "#B54708", "#FEF0C7")
B_DEST = ("Destaque", GTXT, "#EAF5DD")

# ---------- V1 · névoa · laptop + card flutuante
def v1():
    rw = 900; rh = round(rw * 465 / 2290)
    return f'''<section class="s" id="v1" style="background-color:#EAF5DD;background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px);color:{NAVY}">
<div style="position:absolute;left:72px;top:72px"><span class="pill" style="background:#FFFFFF;color:{GTXT};border:1px solid #CFE3B6">Plataforma</span></div>
<div style="position:absolute;left:72px;right:72px;top:150px;display:flex;flex-direction:column;gap:22px">
 <h1 style="font-size:84px;line-height:90px">O resumo de hoje já diz <span style="color:{GTXT}">onde agir.</span></h1>
 <p style="margin:0;font-size:30px;line-height:42px;color:#3D4A3F">A IA lê vendas, marketing e CRM e mostra o que mudou, o que é crítico e a ação sugerida.</p></div>
<div style="position:absolute;left:30px;top:520px">{laptop(900)}</div>
<div class="glow" style="position:absolute;left:250px;top:905px;width:{rw}px;height:{rh}px;border-radius:22px;overflow:hidden;background:#fff"><img src="file://{D}/res-top.png" style="width:100%;display:block"></div>
{logo(NAVY, NAVY)}</section>'''

# ---------- V2 · escuro · navegador em perspectiva + leitura dos alertas
def v2():
    inner = f'<img src="file://{RES}" style="width:100%;display:block">'
    rowsh = "".join(f'''<div style="display:flex;gap:20px;align-items:flex-start">{badge(*b)}<div style="font-size:28px;line-height:38px;color:#FFFFFF"><b>{m}</b> <span style="color:#9AA7B0">→ {a}</span></div></div>'''
                    for b, m, a in [(B_CRIT, "Receita faturada", "recuperar o ticket médio."),
                                    (B_ATEN, "Funil comercial", "destravar contatos parados."),
                                    (B_DEST, "Conversão de leads", "mais vendas, mesmo volume.")])
    return f'''<section class="s" id="v2" style="background-color:#05131C;background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.2px);color:#FFFFFF">
<div style="position:absolute;left:520px;top:-240px;width:860px;height:860px;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.26),rgba(146,197,73,0))"></div>
<div style="position:absolute;left:72px;top:72px"><span class="pill" style="background:#16301F;color:{LIME};border:1px solid rgba(146,197,73,.45)">Plataforma</span></div>
<div style="position:absolute;left:72px;right:72px;top:150px"><h1 style="font-size:80px;line-height:86px">Crítico, atenção ou destaque. <span style="color:{LIME}">E o que fazer em cada um.</span></h1></div>
<div class="glow" style="position:absolute;left:72px;top:470px;border-radius:16px">{browser(inner, 1240, dark=True)}</div>
<div style="position:absolute;left:72px;right:72px;top:1030px;display:flex;flex-direction:column;gap:22px">{rowsh}</div>
{logo("#FFFFFF", "#FFFFFF")}</section>'''

# ---------- V3 · claro · quatro alertas empilhados
def v3():
    k = 0.70
    strips = ""
    for i, (b, (y0, y1)) in enumerate(zip([B_CRIT, B_ATEN, B_CRIT, B_DEST], rows)):
        h = round((y1 - y0) * k); w = round(1488 * k)
        strips += f'''<div style="position:relative;margin-left:{i*36}px">
<div style="position:absolute;left:0;top:-26px;z-index:2">{badge(*b)}</div>
<div class="glow" style="width:{w}px;height:{h}px;border-radius:18px;overflow:hidden;background:#fff"><img src="file://{D}/row{i+1}.png" style="width:100%;height:100%;display:block"></div></div>'''
    return f'''<section class="s" id="v3" style="background-color:#FFFFFF;background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px);color:{NAVY}">
<div style="position:absolute;left:560px;top:-260px;width:780px;height:780px;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.26),rgba(146,197,73,0))"></div>
<div style="position:absolute;left:72px;top:72px"><span class="pill" style="background:#EAF5DD;color:{GTXT};border:1px solid rgba(146,197,73,.6)">Plataforma</span></div>
<div style="position:absolute;left:72px;right:72px;top:150px;display:flex;flex-direction:column;gap:22px">
 <h1 style="font-size:84px;line-height:90px">Cada alerta já vem <span style="color:{GTXT}">com a ação.</span></h1>
 <p style="margin:0;font-size:30px;line-height:42px;color:#4F5B63">Receita, funil, leads e conversão: a IA mostra o que mudou e o próximo passo.</p></div>
<div style="position:absolute;left:72px;top:540px;display:flex;flex-direction:column;gap:56px">{strips}</div>
{logo(NAVY, NAVY)}</section>'''

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{v1()}{v2()}{v3()}</body></html>"
open(f"{D}/variacoes.html", "w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{D}/variacoes.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(900)
    for v in ("v1", "v2", "v3"):
        pg.locator(f"#{v}").screenshot(path=f"{D}/resumo-executivo-{v}.png")
    b.close()
ims = [Image.open(f"{D}/resumo-executivo-{v}.png") for v in ("v1", "v2", "v3")]
sh = Image.new("RGB", (3 * 540 + 40, 675 + 20), "#E1E7E4")
for i, im in enumerate(ims): sh.paste(im.resize((540, 675), Image.LANCZOS), (10 + i * 550, 10))
sh.save(f"{D}/resumo-executivo-variacoes.png")
print("ok")

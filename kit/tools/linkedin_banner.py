import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from stories import ff, NAVY, LIME
from PIL import Image

A = "/home/claude/assets/plataforma"
D = "/home/claude/out/linkedin"
os.makedirs(D, exist_ok=True)
Image.open(f"{A}/02-resumo-executivo-claro.png").crop((20, 20, 2310, 640)).save(f"{D}/res.png")
Image.open(f"{A}/06-dashboard-marketing-escuro.png").crop((40, 240, 2260, 1180)).save(f"{D}/mkt.png")
GT = "#406500"
W, H = 1128, 191

CSS = ff + f"""*{{box-sizing:border-box}} body{{margin:0;background:#888}}
.b{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Inter',sans-serif;background-size:16px 16px;margin-bottom:12px}}
h1{{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.025em;font-size:30px;line-height:34px}}
.chip{{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px;border-radius:999px;font-size:11.5px;font-weight:600;white-space:nowrap}}
"""

def win(img, w, h, dark):
    bar = "#1B2A33" if dark else "#E9EEEB"
    dots = "".join(f'<i style="width:7px;height:7px;border-radius:99px;background:{c}"></i>' for c in ("#F97066", "#F5C451", LIME))
    return f'''<div style="width:{w}px;height:{h}px;border-radius:10px;overflow:hidden;background:{bar};
 box-shadow:0 0 0 1px rgba(146,197,73,.85),0 0 26px rgba(146,197,73,.3),0 12px 30px rgba(5,19,28,.18)">
 <div style="height:22px;display:flex;align-items:center;gap:5px;padding:0 10px">{dots}</div>
 <img src="file://{img}" style="width:100%;display:block"></div>'''

def text(ink, mut, hl, chipbg, chipfg, chipbd, dot=LIME):
    chips = "".join(f'<span class="chip" style="background:{chipbg};color:{chipfg};border:1px solid {chipbd}"><i style="width:6px;height:6px;border-radius:99px;background:{dot}"></i>{t}</span>'
                    for t in ("+50 fontes de dados", "Atualizado todo dia", "IA sobre os seus números"))
    return f'''<div style="position:absolute;left:300px;top:34px;width:500px;display:flex;flex-direction:column;gap:9px;color:{ink}">
 <h1>Revenue Intelligence para <span style="color:{hl}">vendas, marketing e CRM.</span></h1>
 <div style="font-size:14px;color:{mut}">Você só acessa. A gente constrói o resto.</div>
 <div style="display:flex;gap:6px;margin-top:4px">{chips}</div></div>'''

def glow(x, y, s, a):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{s}px;height:{s}px;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,{a}),rgba(146,197,73,0))"></div>'

v1 = f'''<section class="b" id="v1" style="background-color:#FFFFFF;background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px)">
{glow(760,-200,520,.30)}
{text(NAVY, "#4F5B63", GT, "#EAF5DD", GT, "rgba(146,197,73,.6)")}
<div style="position:absolute;left:800px;top:26px">{win(f"{D}/res.png", 380, 190, False)}</div></section>'''

v2 = f'''<section class="b" id="v2" style="background-color:#05131C;background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.2px)">
{glow(740,-220,560,.26)}
{text("#FFFFFF", "#9AA7B0", LIME, "#16301F", LIME, "rgba(146,197,73,.45)")}
<div style="position:absolute;left:800px;top:26px">{win(f"{D}/mkt.png", 380, 190, True)}</div></section>'''

big = SYM(150, dots=NAVY, accent="#FFFFFF")
v3 = f'''<section class="b" id="v3" style="background-color:#92C549;background-image:radial-gradient(rgba(5,19,28,.10) 1px,transparent 1.2px)">
{text(NAVY, "#1F3A12", NAVY, "rgba(255,255,255,.45)", NAVY, "rgba(5,19,28,.15)", dot=NAVY)}
<div style="position:absolute;left:880px;top:20px">{big}</div></section>'''

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{v1}{v2}{v3}</body></html>"
open(f"{D}/banner.html", "w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": W, "height": 700}, device_scale_factor=2)
    pg.goto(f"file://{D}/banner.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
    for v, name in (("v1", "claro"), ("v2", "escuro"), ("v3", "lima")):
        pg.locator(f"#{v}").screenshot(path=f"{D}/4metrics-linkedin-banner-{name}.png")
    b.close()
ims = [Image.open(f"{D}/4metrics-linkedin-banner-{n}.png") for n in ("claro", "escuro", "lima")]
sh = Image.new("RGB", (W * 2 + 40, (H * 2 + 20) * 3 + 20), "#E1E7E4")
for i, im in enumerate(ims): sh.paste(im, (20, 20 + i * (H * 2 + 20)))
# LinkedIn logo placeholder preview (bottom-left box) on a copy
sh.save(f"{D}/linkedin-banners-visao-geral.png")
print("ok")

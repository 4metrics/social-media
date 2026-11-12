import sys, os
sys.path.insert(0, "/home/claude/tools")
from stories import ff, NAVY, LIME
from PIL import Image

D = "/home/claude/out/linkedin"
os.makedirs(D, exist_ok=True)
W, H = 1128, 191
GT = "#406500"

CSS = ff + f"""*{{box-sizing:border-box}} body{{margin:0;background:#888}}
.b{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:'Inter',sans-serif;background-size:16px 16px;margin-bottom:12px}}
h1{{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.02em;font-size:26px;line-height:31px;white-space:nowrap}}
"""

def flow(dot, line, glow_a):
    # three data points converge into the green dot (the "quatro pontos" concept)
    ys = [52, 96, 140]
    paths = "".join(f'<path d="M24,{y} C110,{y} 120,96 184,96" fill="none" stroke="{line}" stroke-width="1.5"/>' for y in ys)
    dots = "".join(f'<circle cx="24" cy="{y}" r="6" fill="{dot}"/>' for y in ys)
    return f'''<svg width="230" height="191" viewBox="0 0 230 191" style="position:absolute;right:64px;top:0;overflow:visible">
<defs><radialGradient id="gw"><stop offset="0" stop-color="#92C549" stop-opacity="{glow_a}"/><stop offset="1" stop-color="#92C549" stop-opacity="0"/></radialGradient></defs>
<circle cx="184" cy="96" r="60" fill="url(#gw)"/>{paths}{dots}<circle cx="184" cy="96" r="10" fill="{LIME}"/></svg>'''

def banner(i, bg, mesh, ink, mut, hl, dot, line, glow_a, wash=""):
    return f'''<section class="b" id="v{i}" style="background-color:{bg};background-image:radial-gradient({mesh} 1px,transparent 1.2px)">{wash}
<div style="position:absolute;left:300px;top:0;height:{H}px;display:flex;flex-direction:column;justify-content:center;gap:8px;color:{ink}">
 <h1>Revenue Intelligence para<br><span style="color:{hl}">vendas, marketing e CRM.</span></h1>
 <div style="font-size:14px;color:{mut}">A nova forma de trabalhar com dados na era da IA.</div></div>
{flow(dot, line, glow_a)}</section>'''

v1 = banner(1, "#FFFFFF", "rgba(5,19,28,.06)", NAVY, "#4F5B63", GT, NAVY, "#D5E2CE", .35)
v2 = banner(2, "#EAF5DD", "rgba(5,19,28,.06)", NAVY, "#3D4A3F", GT, NAVY, "#C3D9AE", .45)
v3 = banner(3, "#05131C", "rgba(255,255,255,.08)", "#FFFFFF", "#9AA7B0", LIME, "#FFFFFF", "#2B3640", .40)

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{v1}{v2}{v3}</body></html>"
open(f"{D}/banner2.html", "w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": W, "height": 700}, device_scale_factor=2)
    pg.goto(f"file://{D}/banner2.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
    names = ("claro", "nevoa", "escuro")
    for i, n in enumerate(names, 1):
        pg.locator(f"#v{i}").screenshot(path=f"{D}/4metrics-linkedin-banner-v2-{n}.png")
    b.close()
ims = [Image.open(f"{D}/4metrics-linkedin-banner-v2-{n}.png") for n in names]
sh = Image.new("RGB", (W * 2 + 40, (H * 2 + 20) * 3 + 20), "#C9D0CC")
for i, im in enumerate(ims): sh.paste(im, (20, 20 + i * (H * 2 + 20)))
sh.save(f"{D}/linkedin-banners-v2-visao-geral.png")
print("ok")

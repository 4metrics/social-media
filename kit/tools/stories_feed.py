import sys
sys.path.insert(0, "/home/claude/tools")
from festas_base import ff, SYM, WORD, LIME, NAVY
D = "/home/claude/out/stories-feed"
import os; os.makedirs(D, exist_ok=True)
B = "/home/claude/social-media/posts/"
ITEMS = [  # (nome, arte, tema)
 ("2026-11-27-story-black-friday-v1", B+"2026-11/2026-11-27-black-friday-v2.png", "lt"),
 ("2026-12-24-story-natal-v1", B+"2026-12/2026-12-24-natal-v1.png", "lm"),
 ("2026-12-29-story-confianca-35-v1", B+"2026-12/2026-12-29-confianca-35-v1.png", "nv"),
 ("2026-12-30-story-ia-pergunta-v1", B+"2026-12/2026-12-30-ia-pergunta-v1.png", "lt"),
 ("2026-12-31-story-ano-novo-v1", B+"2026-12/2026-12-31-ano-novo-v2.png", "dk"),
 ("2027-01-04-story-ano-acabou-v1", B+"2027-01/2027-01-04-ano-acabou-v1-01.png", "nv"),
]
TH = {"lt": ("#FFFFFF","rgba(5,19,28,.07)",NAVY,"#406500","#EAF5DD",LIME),
      "nv": ("#EAF5DD","rgba(5,19,28,.07)",NAVY,"#406500","#FFFFFF",LIME),
      "dk": (NAVY,"rgba(255,255,255,.09)","#FFFFFF",LIME,"#16301F",LIME),
      "lm": (LIME,"rgba(5,19,28,.10)",NAVY,NAVY,"rgba(255,255,255,.4)","#FFFFFF")}
CSS = ff + "*{box-sizing:border-box} body{margin:0} .st{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Inter';background-size:22px 22px}"
html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
for n, art, t in ITEMS:
    bg, dot, ink, acc, pillbg, sym = TH[t]
    html += f'''<section class="st" id="s{n}" style="background-color:{bg};background-image:radial-gradient({dot} 1px,transparent 1.2px);color:{ink}">
<div style="position:absolute;left:0;right:0;top:200px;text-align:center"><span style="display:inline-flex;align-items:center;gap:12px;height:64px;padding:0 30px;border-radius:999px;background:{pillbg};font-size:30px;font-weight:600;color:{acc}"><i style="width:14px;height:14px;border-radius:9px;background:{LIME if t!='lm' else NAVY}"></i>Post novo no feed</span></div>
<img src="file://{art}" style="position:absolute;left:90px;top:340px;width:900px;height:1125px;border-radius:28px;box-shadow:0 0 0 2px rgba(146,197,73,.7),0 30px 80px rgba(5,19,28,.28)">
<div style="position:absolute;left:0;right:0;top:1560px;text-align:center;font-family:'Plus Jakarta Sans';font-size:44px;font-weight:700;letter-spacing:-0.02em">Confira no perfil <span style="color:{acc}">→</span></div>
</section>'''
html += "</body></html>"
open(f"{D}/st.html","w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{D}/st.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(900)
    for n,_,_ in ITEMS: pg.locator(f"[id='s{n}']").screenshot(path=f"{D}/{n}.png")
    b.close()
from PIL import Image
sh=Image.new('RGB',(6*360+70,640+20),'#999')
for k,(n,_,_) in enumerate(ITEMS): sh.paste(Image.open(f"{D}/{n}.png").convert('RGB').resize((360,640),Image.LANCZOS),(10+k*370,10))
sh.save(f"{D}/visao-geral-stories.png")

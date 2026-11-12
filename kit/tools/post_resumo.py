import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from stories import ff, NAVY, LIME

SHOT = "/home/claude/assets/plataforma/02-resumo-executivo-claro.png"
D = "/home/claude/out/post-resumo"
os.makedirs(D, exist_ok=True)

# crop: header + first two items of the executive summary
from PIL import Image
im = Image.open(SHOT)
crop = im.crop((20, 20, 2310, 485))
crop.save(f"{D}/resumo-crop.png")
cw, ch = crop.size

BG, MESH, MUT, GTXT = "#EAF5DD", "rgba(5,19,28,0.07)", "#3D4A3F", "#406500"
W_SHOT = 1900  # bleeds off the right edge
H_SHOT = round(W_SHOT * ch / cw)

html = f"""<html><head><meta charset='utf-8'><style>{ff}
*{{box-sizing:border-box}} body{{margin:0}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;background-color:{BG};
 background-image:radial-gradient({MESH} 1px,transparent 1.2px);background-size:22px 22px;color:{NAVY};font-family:'Inter',sans-serif}}
h1{{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em;font-size:80px;line-height:86px}}
</style></head><body>
<section class="s" id="post">
 <div style="position:absolute;left:72px;top:72px;right:72px;display:flex;justify-content:space-between;align-items:center">
  <span style="display:inline-flex;align-items:center;height:42px;padding:0 20px;border-radius:999px;background:#FFFFFF;color:{GTXT};border:1px solid #CFE3B6;font-size:20px;font-weight:600">Plataforma</span>
  <span style="font-size:18px;color:{MUT}">Tela real · dados de demonstração</span>
 </div>
 <div style="position:absolute;left:72px;right:72px;top:170px;display:flex;flex-direction:column;gap:28px">
  <h1>Todo dia de manhã, a IA te diz <span style="color:{GTXT}">o que mudou e o que fazer.</span></h1>
  <p style="margin:0;font-size:32px;line-height:44px;color:{MUT}">O resumo executivo lê seus dados de vendas, marketing e CRM e entrega a prioridade do dia.</p>
 </div>
 <div style="position:absolute;left:72px;top:600px;width:{W_SHOT}px;height:{H_SHOT}px;border-radius:28px;overflow:hidden;
      box-shadow:0 0 0 1px rgba(146,197,73,.9),0 0 48px rgba(146,197,73,.35),0 24px 60px rgba(5,19,28,.12)">
  <img src="file://{D}/resumo-crop.png" style="width:100%;height:100%;display:block">
 </div>
 <div style="position:absolute;left:72px;right:72px;top:{600+H_SHOT+44}px;background:#FFFFFF;border-radius:24px;padding:28px 32px;border:2px solid {LIME};display:flex;gap:22px;align-items:flex-start">
  <span style="flex:none;width:56px;height:56px;border-radius:16px;background:{LIME};display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:700">→</span>
  <div><div style="font-size:22px;font-weight:700;color:{GTXT};letter-spacing:.06em;text-transform:uppercase">Ação sugerida pela IA</div>
  <div style="font-size:32px;line-height:42px;font-weight:600;margin-top:6px">Priorizar a recuperação do ticket médio para voltar ao pico de receita.</div></div>
 </div>
 <div style="position:absolute;left:72px;bottom:64px;display:inline-flex;align-items:center;gap:12px">{SYM(40,dots=NAVY,accent=LIME)}{WORD(32,NAVY,LIME)}</div>
</section></body></html>"""
open(f"{D}/post.html", "w").write(html)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{D}/post.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
    pg.locator("#post").screenshot(path=f"{D}/2026-11-resumo-executivo.png")
    b.close()
print(H_SHOT)

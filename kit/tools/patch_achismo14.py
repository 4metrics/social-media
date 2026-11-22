import sys
sys.path.insert(0,"/home/claude/tools")
from festas_base import ff, LIME, NAVY
F="/home/claude/social-media/feed/2026-11-26-achismo-30-dias-v1-0%d.png"
D="/home/claude/out/achismo14"
CSS = ff + """*{box-sizing:border-box} body{margin:0}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif}
h1,h2,.d{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em} p{margin:0}
.bx{position:absolute}"""
def letter(): return '<div style="width:200px;height:200px;flex:none"></div>'
def label_slide(i, old, new, col, bgcol):
    # measure old label position with identical layout, then cover and redraw
    return f'''<section class="s" id="s{i}"><img src="file://{F % i}" style="position:absolute;left:0;top:0">
<div class="bx" style="left:72px;top:110px;width:936px"><div style="display:flex;align-items:center;gap:36px">{letter()}<div><p id="m{i}" style="font-size:28px;font-weight:600;color:transparent">{old}</p><h2 style="font-size:84px;line-height:88px;color:transparent">Fundação</h2></div></div></div>
<div id="c{i}" class="bx" style="background:{bgcol}"></div><p id="n{i}" class="bx" style="font-size:28px;font-weight:600;color:{col}">{new}</p></section>'''
html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
# 1 capa
html += f'''<section class="s" id="s1"><img src="file://{F % 1}" style="position:absolute;left:0;top:0">
<div class="bx" style="left:0;top:700px;width:1080px;height:470px;background:linear-gradient(180deg,rgba(5,19,28,0) 0,#05131C 60px)"></div>
<div class="bx" style="left:72px;top:760px;width:936px"><h1 style="font-size:88px;line-height:94px;color:#FFFFFF">Como sair do achismo<br><span style="color:{LIME}">em até 14 dias.</span></h1>
<p style="margin-top:26px;font-size:34px;line-height:46px;color:#9AA7B0">Sem contratar time de dados. Sem trocar de ferramenta.</p></div></section>'''
html += label_slide(2,"Semanas 1 e 2","Etapa 1 · até 14 dias","#4F5B63","#FFFFFF")
html += label_slide(3,"Semanas 3 e 4","Etapa 2 · até 14 dias","#3D4A3F","SAMPLE3")
html += label_slide(4,"Todo dia","Etapa 3 · todo dia","#9AA7B0","#05131C")
html += f'''<section class="s" id="s5"><img src="file://{F % 5}" style="position:absolute;left:0;top:0">
<div class="bx" style="left:60px;top:250px;width:520px;height:290px;background:{LIME}"></div>
<div class="bx" style="left:72px;top:205px;width:936px"><p style="font-family:'Plus Jakarta Sans';font-size:44px;font-weight:700;color:{NAVY}">Até</p></div>
<div class="bx" style="left:72px;top:260px;width:936px"><p class="d" style="font-size:300px;line-height:280px;letter-spacing:-0.05em;color:{NAVY}">14</p></div></section>'''
html += "</body></html>"
from PIL import Image
c3 = Image.open(F % 3).convert("RGB").getpixel((900,150))
html = html.replace("SAMPLE3", "#%02x%02x%02x" % c3)
open(f"{D}/p.html","w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{D}/p.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(900)
    for i in (2,3,4):
        r = pg.evaluate(f"(()=>{{const s=document.getElementById('s{i}').getBoundingClientRect();const q=document.getElementById('m{i}').getBoundingClientRect();return [q.left-s.left,q.top-s.top,q.width,q.height]}})()")
        x,y,w,h = r
        pg.evaluate(f"(()=>{{const c=document.getElementById('c{i}');c.style.left='{x-4}px';c.style.top='{y-2}px';c.style.width='{w+12}px';c.style.height='{h+4}px';const n=document.getElementById('n{i}');n.style.left='{x}px';n.style.top='{y}px'}})()")
        print(i, r)
    for i in range(1,6): pg.locator(f"#s{i}").screenshot(path=f"{D}/2026-11-26-achismo-14-dias-v2-0{i}.png")
    b.close()
ims=[Image.open(f"{D}/2026-11-26-achismo-14-dias-v2-0{i}.png") for i in range(1,6)]
sh=Image.new('RGB',(5*432,540))
for k,im in enumerate(ims): sh.paste(im.convert('RGB').resize((432,540),Image.LANCZOS),(k*432,0))
sh.save(f"{D}/visao.png")

import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from PIL import Image

FS = "/home/claude/fonts/fs"
ff = ""
for fam, pkg, pre in [("Inter", "fontsource-inter-5.3.0", "inter"), ("Plus Jakarta Sans", "fontsource-plus-jakarta-sans-5.3.0", "plus-jakarta-sans")]:
    for w in (400, 500, 600, 700):
        ff += f"@font-face{{font-family:'{fam}';src:url('file://{FS}/{pkg}/package/files/{pre}-latin-{w}-normal.woff2') format('woff2');font-weight:{w}}}"

NAVY, LIME, GTXT, CARD, BORD, NEV = "#05131C", "#92C549", "#406500", "#14232C", "#2B3640", "#EAF5DD"
MUTD, MUTL, RED = "#9AA7B0", "#4F5B63", "#F97066"
A = "/home/claude/assets/plataforma"
D = "/home/claude/out/ano-acabou"
os.makedirs(D, exist_ok=True)

CSS = ff + f"""*{{box-sizing:border-box}} body{{margin:0;background:#888}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;background-size:22px 22px;margin-bottom:20px;padding:72px;display:flex;flex-direction:column;gap:34px}}
.dk{{background-color:{NAVY};background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.2px);color:#fff}}
.lt{{background-color:#fff;background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px);color:{NAVY}}}
.nv{{background-color:{NEV};background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px);color:{NAVY}}}
h1,h2{{position:relative;margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em}}
h1{{font-size:88px;line-height:94px}} h2{{font-size:76px;line-height:84px}}
.dk .hl{{color:{LIME}}} .lt .hl,.nv .hl{{color:{GTXT}}}
p.lead{{position:relative;margin:0;font-size:34px;line-height:48px}}
.dk p.lead{{color:{MUTD}}} .lt p.lead{{color:{MUTL}}} .nv p.lead{{color:#3D4A3F}}
.pill{{position:relative;align-self:flex-start;display:inline-flex;align-items:center;height:42px;padding:0 20px;border-radius:999px;font-size:20px;font-weight:600}}
.dk .pill{{background:#16301F;color:{LIME};border:1px solid rgba(146,197,73,.45)}}
.lt .pill{{background:{NEV};color:{GTXT};border:1px solid rgba(146,197,73,.6)}}
.nv .pill{{background:#fff;color:{GTXT};border:1px solid #CFE3B6}}
.g{{position:absolute;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.26),rgba(146,197,73,0));pointer-events:none}}
.card{{position:relative;border-radius:24px}}
.dk .card{{background:{CARD};border:1px solid {BORD}}}
.lt .card,.nv .card{{background:#fff;border:1px solid #E1E7E4;box-shadow:0 12px 32px rgba(5,19,28,.06)}}
.feat{{border:1px solid rgba(146,197,73,.8)!important;box-shadow:0 0 0 1px rgba(146,197,73,.15),0 0 32px rgba(146,197,73,.25)!important}}
.foot{{position:relative;display:flex;justify-content:space-between;align-items:center;margin-top:auto;min-height:48px}}
.mid{{position:relative;flex:1;display:flex;flex-direction:column;justify-content:center}}
.btn{{display:inline-flex;align-items:center;height:84px;padding:0 40px;border-radius:12px;background:{LIME};color:#05131D;font-size:32px;font-weight:600}}
.prog{{display:flex;gap:8px}} .prog i{{width:44px;height:6px;border-radius:9px}}
"""

def glow(x, y, s): return f'<div class="g" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px"></div>'
def logo(dark):
    ink = "#FFFFFF" if dark else NAVY
    return f'<span style="display:inline-flex;align-items:center;gap:12px">{SYM(40,dots=ink,accent=LIME)}{WORD(32,ink,LIME)}</span>'
def prog(i, n, dark):
    off = "#2B3640" if dark else "#D5DDD8"
    return '<span class="prog">' + "".join(f'<i style="background:{LIME if k==i else off}"></i>' for k in range(1, n+1)) + '</span>'

# ================= POST 1 · custo da demora · carrossel claro 5
N = 5
def cslide(i, body, glows=""):
    return f'''<section class="s lt" id="c{i}">{glows}
<span class="pill">Custo da demora</span>
{body}
<div class="foot">{logo(False)}{prog(i, N, False)}</div></section>'''

def cal():
    head = "".join(f'<div style="font-size:22px;color:{MUTL};text-align:center">{d}</div>' for d in "DSTQQSS")
    cells = '<div></div>' * 5  # jan/2027 starts on friday
    for d in range(1, 32):
        wait = d <= 15
        st = f"background:#FEF3F2;color:#05131C;border:1px solid #FECDCA" if wait else f"color:{MUTL};border:1px solid transparent"
        cells += f'<div style="height:62px;border-radius:12px;display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:600;{st}">{d}</div>'
    return f'''<div class="card" style="padding:34px 36px;width:680px;align-self:center">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:22px"><span style="font-family:'Plus Jakarta Sans';font-size:30px;font-weight:700">Janeiro 2027</span>
<span style="display:inline-flex;align-items:center;gap:10px;font-size:22px;color:#D92D20;font-weight:600"><i style="width:12px;height:12px;border-radius:9px;background:#D92D20"></i>esperando o fechamento</span></div>
<div style="display:grid;grid-template-columns:repeat(7,1fr);gap:8px">{head}{cells}</div></div>'''

c1 = cslide(1, f'''<h1 style="font-size:92px;line-height:98px">O ano acabou. Quando você vai saber <span class="hl">como ele fechou?</span></h1>
<div class="mid">{cal()}</div>''', glow(560, -260, 760))

def file(n, c): return f'<div class="card" style="height:92px;padding:0 28px;display:flex;align-items:center;gap:18px;font-size:28px;font-weight:600"><i style="width:16px;height:16px;border-radius:4px;background:{c}"></i>{n}</div>'
c2 = cslide(2, f'''<h2><span class="hl">Dia 4.</span> Alguém exporta CRM, mídia e ERP.</h2>
<p class="lead">Três sistemas, três arquivos, uma planilha montada à mão.</p>
<div class="mid"><div style="display:flex;align-items:center;gap:36px">
<div style="display:flex;flex-direction:column;gap:16px;width:470px">{file("crm_2026.csv","#5B8DEF")}{file("midia_2026.xlsx","#F5C451")}{file("erp_2026.xlsx","#9AA7B0")}</div>
<span style="font-size:48px;color:{LIME}">→</span>
<div class="card" style="flex:1;padding:30px 28px;display:flex;flex-direction:column;gap:16px">
<span style="font-size:24px;font-weight:600">fechamento_2026_v1.xlsx</span>
{"".join(f'<i style="display:block;height:22px;border-radius:6px;background:#EEF2EF;width:{w}%"></i>' for w in (100,82,92,64,88))}</div></div></div>''', glow(-280, 900, 620))

def num(area, v, c):
    return f'''<div class="card" style="flex:1;padding:34px 26px;display:flex;flex-direction:column;gap:12px">
<span style="font-size:24px;color:{MUTL}">{area}</span>
<span style="font-family:'Plus Jakarta Sans';font-size:68px;font-weight:700;color:{c}">{v}</span>
<span style="font-size:24px;color:{MUTL}">vendas em 2026</span></div>'''
c3 = cslide(3, f'''<h2><span class="hl">Dia 8.</span> Cada área chega com o seu número.</h2>
<p class="lead">Marketing, comercial e financeiro contam de um jeito diferente.</p>
<div class="mid"><div style="display:flex;gap:18px">{num("Marketing","3.412","#05131C")}{num("CRM","3.187","#05131C")}{num("Financeiro","2.965","#05131C")}</div>
<div style="margin-top:34px;align-self:center;font-family:'Plus Jakarta Sans';font-size:40px;font-weight:700;color:#D92D20">Qual está certo?</div></div>''', glow(560, 860, 640))

c4 = cslide(4, f'''<h2><span class="hl">Dia 15.</span> A reunião discute o número. Não a ação.</h2>
<p class="lead">Enquanto isso, o funil de janeiro anda sem direção.</p>
<div class="mid"><div class="card" style="padding:44px 40px;display:flex;flex-direction:column;gap:24px">
<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font-size:30px;font-weight:600">Janeiro</span><span style="font-family:'Plus Jakarta Sans';font-size:56px;font-weight:700;color:#D92D20">48%</span></div>
<div style="height:28px;border-radius:99px;background:#EEF2EF;overflow:hidden"><div style="width:48%;height:100%;background:#D92D20;border-radius:99px"></div></div>
<span style="font-size:26px;color:{MUTL}">do mês já passou antes da primeira decisão</span></div></div>''', glow(-260, -200, 640))

c5 = cslide(5, f'''<div class="mid" style="gap:40px">
<div>{SYM(120,dots=NAVY,accent=LIME)}</div>
<h1>Com a 4metrics, você vê o fechamento do ano <span class="hl">no dia 1.</span></h1>
<p class="lead">Vendas, marketing e CRM na mesma base, com as mesmas regras e dado atualizado todo dia. O ano começa com o número certo e o próximo passo.</p>
<div><span class="btn">Agendar diagnóstico</span></div>
<p style="margin:0;font-size:28px;color:#05131C">Comente <b>DIAGNÓSTICO</b> e vamos ver por onde começar.</p></div>''', glow(500, -300, 900) + glow(-300, 900, 700))

# ================= POST 2 · dados de mercado · claro, post único

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{c1}{c2}{c3}{c4}{c5}</body></html>"
open(f"{D}/ano.html", "w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{D}/ano.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(900)
    for i in range(1, N+1):
        pg.locator(f"#c{i}").screenshot(path=f"{D}/2027-01-04-ano-acabou-v1-{i:02d}.png")
    b.close()
ims=[Image.open(f"{D}/2027-01-04-ano-acabou-v1-{i:02d}.png") for i in range(1,N+1)]
sh=Image.new('RGB',(5*432+60,540+20),'#C9D0CC')
for k,im in enumerate(ims): sh.paste(im.convert('RGB').resize((432,540),Image.LANCZOS),(10+k*442,10))
sh.save(f"{D}/visao-geral-ano-acabou.png")

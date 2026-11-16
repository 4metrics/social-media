import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from stories import ff
from PIL import Image
from playwright.sync_api import sync_playwright

NAVY, LIME, GTXT, MUT, BOR, NEV = "#05131C", "#92C549", "#406500", "#4F5B63", "#E1E7E4", "#EAF5DD"
RED = "#D92D20"
A = "/home/claude/assets/plataforma"
D = "/home/claude/out/semana-dez"
os.makedirs(D, exist_ok=True)

# recortes da tela do Dashboard Marketing
dm = Image.open(f"{A}/06-dashboard-marketing-escuro.png")
dm.crop((370, 116, 892, 186)).save(f"{D}/chip1.png")
dm.crop((900, 116, 1420, 186)).save(f"{D}/chip2.png")

CSS = ff + f"""*{{box-sizing:border-box}} body{{margin:0;background:#888}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;background-size:22px 22px;margin-bottom:20px;color:{NAVY}}}
.cl{{background-color:#FFFFFF;background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px)}}
.nv{{background-color:{NEV};background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px)}}
.dk{{background-color:{NAVY};background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.2px);color:#fff}}
h1,h2{{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em}}
h1{{font-size:84px;line-height:90px}} h2{{font-size:72px;line-height:80px}}
.hl{{color:{GTXT}}} .dk .hl{{color:{LIME}}}
.lead{{margin:0;font-size:32px;line-height:44px;color:{MUT}}} .dk .lead{{color:#9AA7B0}} .nv .lead{{color:#3D4A3F}}
.pill{{display:inline-flex;align-items:center;height:42px;padding:0 20px;border-radius:999px;font-size:20px;font-weight:600;background:{NEV};color:{GTXT};border:1px solid rgba(146,197,73,.6)}}
.nv .pill{{background:#fff;border-color:#CFE3B6}} .dk .pill{{background:#16301F;color:{LIME};border-color:rgba(146,197,73,.45)}}
.card{{background:#fff;border:1px solid {BOR};border-radius:24px;box-shadow:0 1px 2px rgba(5,19,28,.04),0 12px 32px rgba(5,19,28,.06)}}
.feat{{border:1px solid rgba(146,197,73,.85);box-shadow:0 0 0 1px rgba(146,197,73,.15),0 0 28px rgba(146,197,73,.25)}}
.glow{{box-shadow:0 0 0 1px rgba(146,197,73,.9),0 0 48px rgba(146,197,73,.35),0 24px 60px rgba(5,19,28,.25)}}
.g{{position:absolute;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.26),rgba(146,197,73,0))}}
.btn{{display:inline-flex;align-items:center;height:84px;padding:0 40px;border-radius:12px;background:{LIME};color:#05131D;font-size:32px;font-weight:600}}
.top{{position:absolute;left:72px;top:72px}}
.body{{position:absolute;left:72px;right:72px;top:150px;display:flex;flex-direction:column;gap:24px}}
"""

def logo(dark=False):
    ink = "#FFFFFF" if dark else NAVY
    return f'<div style="position:absolute;left:72px;bottom:60px;display:inline-flex;align-items:center;gap:12px">{SYM(40,dots=ink,accent=LIME)}{WORD(32,ink,LIME)}</div>'

def glow(x, y, s): return f'<div class="g" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px"></div>'

def browser(inner, width, dark=False):
    bar = "#1B2A33" if dark else "#E9EEEB"; url = "#0B1B24" if dark else "#FFFFFF"
    return f'''<div style="width:{width}px;border-radius:16px;overflow:hidden;background:{bar}">
<div style="height:54px;display:flex;align-items:center;gap:10px;padding:0 20px">
 <i style="width:14px;height:14px;border-radius:99px;background:#F97066"></i><i style="width:14px;height:14px;border-radius:99px;background:#F5C451"></i><i style="width:14px;height:14px;border-radius:99px;background:{LIME}"></i>
 <span style="margin-left:16px;height:32px;flex:0 0 360px;border-radius:99px;background:{url};font-size:16px;color:#7A8790;display:flex;align-items:center;padding:0 16px">app.4metrics</span></div>
{inner}</div>'''

# ---------------- P1 · 11/12 · dados de mercado · claro
def p1():
    blocks = "".join(
        f'<div style="flex:1;height:150px;border-radius:18px;{("background:#F4F7F5;border:2px dashed #C9D6CF" if i < 6 else "background:"+LIME+";box-shadow:0 0 24px rgba(146,197,73,.35)")}"></div>'
        for i in range(10))
    return f'''<section class="s cl" id="p1">{glow(560,-260,780)}
<div class="top"><span class="pill">Dados de mercado</span></div>
<div class="body">
 <div style="font-family:'Plus Jakarta Sans';font-weight:700;font-size:220px;line-height:200px;letter-spacing:-0.05em;color:{GTXT}">60%</div>
 <h1 style="font-size:76px;line-height:84px">dos projetos de IA sem dados prontos serão <span class="hl">abandonados.</span></h1>
 <p class="lead">Previsão do Gartner até o fim de 2026.</p>
</div>
<div style="position:absolute;left:72px;right:72px;top:800px" class="card">
 <div style="padding:34px 36px;display:flex;flex-direction:column;gap:22px">
  <div style="display:flex;gap:12px">{blocks}</div>
  <div style="display:flex;justify-content:space-between;font-size:24px;font-weight:600"><span style="color:{MUT}">6 em 10 param no caminho</span><span style="color:{GTXT}">base pronta: IA de pé</span></div>
  <div style="border-top:1px solid {BOR};padding-top:22px;font-size:26px;line-height:36px;color:{NAVY}"><b>63%</b> das empresas não têm ou não sabem se têm a gestão de dados certa para IA.</div>
 </div></div>
<div style="position:absolute;right:72px;bottom:66px;font-size:20px;color:{MUT};text-align:right">Fonte: Gartner, fev. 2025<br>pesquisa com 1.203 líderes de dados</div>
{logo()}</section>'''

# ---------------- P2 · 18/12 · produto · escuro
def p2():
    inner = f'<img src="file://{A}/06-dashboard-marketing-escuro.png" style="width:100%;display:block">'
    ch = lambda f, w: f'<div class="glow" style="width:{w}px;border-radius:22px;overflow:hidden;background:#0B1B24"><img src="file://{D}/{f}" style="width:100%;display:block"></div>'
    return f'''<section class="s dk" id="p2">{glow(520,-260,880)}
<div class="top"><span class="pill">Plataforma</span></div>
<div class="body">
 <h1 style="font-size:80px;line-height:86px">O painel avisa o que piorou. <span class="hl">Antes da reunião.</span></h1>
 <p class="lead">No Dashboard Marketing, os insights ficam no topo: queda de leads, piora no CPL e no CPM.</p>
</div>
<div style="position:absolute;left:72px;top:480px;border-radius:16px;box-shadow:0 0 0 1px #2B3640,0 30px 70px rgba(0,0,0,.4)">{browser(inner, 936, dark=True)}</div>
<div style="position:absolute;left:40px;top:790px">{ch("chip1.png", 640)}</div>
<div style="position:absolute;left:368px;top:910px">{ch("chip2.png", 640)}</div>
<div style="position:absolute;right:72px;bottom:62px;font-size:24px;color:#9AA7B0;text-align:right">Um clique em <b style="color:{LIME}">Análise profunda</b><br>e a IA explica o porquê.</div>
{logo(True)}</section>'''

# ---------------- P3 · 23/12 · nova era da IA · carrossel névoa (5)
N = 5
def prog(i):
    return '<div style="position:absolute;right:72px;bottom:74px;display:flex;gap:8px">' + "".join(
        f'<i style="width:44px;height:6px;border-radius:9px;background:{(GTXT if k==i else "rgba(5,19,28,.15)")}"></i>' for k in range(1, N+1)) + '</div>'

def cslide(i, body, extra=""):
    return f'<section class="s nv" id="c{i}">{extra}<div class="top"><span class="pill">Nova era da IA</span></div>{body}{prog(i)}{logo()}</section>'

def bubble(t, me=True):
    st = f"background:{NAVY};color:#fff;border-radius:28px 28px 8px 28px;align-self:flex-end" if me else f"background:#fff;color:{NAVY};border:1px solid {BOR};border-radius:28px 28px 28px 8px;align-self:flex-start"
    return f'<div style="max-width:760px;padding:28px 34px;font-size:32px;line-height:42px;{st}">{t}</div>'

def src(t): return f'<div class="card" style="height:92px;width:250px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:600">{t}</div>'

c1 = cslide(1, f'''<div class="body">
 <h1 style="font-size:88px;line-height:94px">Em 2027, seu time vai perguntar <span class="hl">à IA.</span></h1>
 <p class="lead">A pergunta é simples. A resposta vai estar certa?</p></div>
<div class="card" style="position:absolute;left:72px;right:72px;top:540px;padding:0;overflow:hidden">
 <div style="height:76px;display:flex;align-items:center;gap:14px;padding:0 32px;border-bottom:1px solid {BOR};font-size:24px;font-weight:600;color:{MUT}">{SYM(30,dots=NAVY,accent=LIME)} Pergunte à IA</div>
 <div style="padding:40px 32px 44px;display:flex;flex-direction:column;gap:26px;background:#FBFCFB">
  {bubble("Qual canal trouxe as vendas que fecharam este mês?")}
  <div style="align-self:flex-start;display:flex;gap:12px;padding:30px 34px;background:#fff;border:1px solid {BOR};border-radius:28px 28px 28px 8px">{"".join(f'<i style="width:18px;height:18px;border-radius:99px;background:{c}"></i>' for c in ("#C9D6CF","#C9D6CF",LIME))}</div>
 </div></div>
<div style="position:absolute;left:72px;top:1060px;font-size:32px;font-weight:600;color:{GTXT}">3 perguntas para testar a sua base →</div>''', glow(560,-260,780))

def qslide(i, n, q, need, visual):
    return cslide(i, f'''<div class="body">
 <div style="font-family:'Plus Jakarta Sans';font-weight:700;font-size:30px;color:{GTXT};letter-spacing:.06em">PERGUNTA {n}</div>
 <h2>“{q}”</h2>
 <p class="lead">{need}</p></div>
<div style="position:absolute;left:72px;right:72px;top:600px;height:540px;display:flex;align-items:center;justify-content:center">{visual}</div>''')

v2 = f'''<div style="display:flex;align-items:center;gap:28px">
<div style="display:flex;flex-direction:column;gap:16px">{src("Mídia paga")}{src("CRM")}{src("ERP")}</div>
<span style="font-size:44px;color:{GTXT}">→</span>
<div class="card feat" style="width:380px;padding:36px 30px;display:flex;flex-direction:column;gap:14px">
 <span style="font-size:24px;color:{MUT}">Vendas fechadas por canal</span>
 <span style="font-family:'Plus Jakarta Sans';font-size:52px;font-weight:700">1 número</span>
 <span style="font-size:24px;color:{GTXT};font-weight:600">a mesma regra para todos</span></div></div>'''
c2 = qslide(2, 1, "Qual canal trouxe as vendas que fecharam?", "Para responder, mídia, CRM e ERP precisam falar a mesma língua.", v2)

fun = [("Leads", 100, False), ("Contato", 74, False), ("Proposta", 30, True), ("Venda", 20, False)]
v3 = '<div class="card" style="width:860px;padding:40px 44px;display:flex;flex-direction:column;gap:22px">' + "".join(
    f'''<div style="display:flex;align-items:center;gap:24px"><span style="width:170px;font-size:28px;font-weight:600">{t}</span>
<div style="flex:1;height:52px;background:#F4F7F5;border-radius:12px;overflow:hidden"><div style="width:{w}%;height:100%;border-radius:12px;background:{(RED if bad else LIME)}"></div></div></div>''' for t, w, bad in fun) + \
    f'<div style="font-size:26px;color:{RED};font-weight:600;border-top:1px solid {BOR};padding-top:20px">Contato → proposta caiu. Hoje, não no dia 30.</div></div>'
c3 = qslide(3, 2, "Onde o funil travou esta semana?", "Para responder, o dado precisa chegar todo dia. Não no relatório do mês.", v3)

rows = [("Carteira A", 88, "+4%", GTXT), ("Carteira B", 61, "−18%", RED), ("Carteira C", 47, "−26%", RED)]
v4 = '<div class="card" style="width:860px;padding:40px 44px;display:flex;flex-direction:column;gap:26px">' + \
    f'<div style="display:flex;justify-content:space-between;font-size:24px;color:{MUT}"><span>Compras no ERP · últimos 90 dias</span><span>vs. trimestre anterior</span></div>' + "".join(
    f'''<div style="display:flex;align-items:center;gap:24px"><span style="width:190px;font-size:28px;font-weight:600">{t}</span>
<div style="flex:1;height:44px;background:#F4F7F5;border-radius:12px;overflow:hidden"><div style="width:{w}%;height:100%;border-radius:12px;background:{(LIME if c==GTXT else '#F97066')}"></div></div>
<span style="width:110px;text-align:right;font-size:30px;font-weight:700;color:{c}">{d}</span></div>''' for t, w, d, c in rows) + '</div>'
c4 = qslide(4, 3, "Quais clientes estão comprando menos?", "Para responder, o ERP precisa estar ligado ao CRM, com as mesmas regras.", v4)

c5 = cslide(5, f'''<div style="position:absolute;left:72px;right:72px;top:300px;display:flex;flex-direction:column;gap:40px">
 <div>{SYM(120,dots=NAVY,accent=LIME)}</div>
 <h1>A IA responde. A base decide <span class="hl">se está certa.</span></h1>
 <p class="lead">A 4metrics constrói essa base com você: +50 fontes de dados, as mesmas regras de negócio e a IA em cima.</p>
 <div><span class="btn">Agendar diagnóstico</span></div>
 <p style="margin:0;font-size:28px">Comente <b>DIAGNÓSTICO</b> e vamos ver por onde começar.</p></div>''', glow(500,-300,900))

SL = [("p1", "2026-12-11-gartner-60-v1.png"), ("p2", "2026-12-18-painel-avisa-v1.png")] + \
     [(f"c{i}", f"2026-12-23-perguntas-2027-v1-{i:02d}.png") for i in range(1, N+1)]
html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{p1()}{p2()}{c1}{c2}{c3}{c4}{c5}</body></html>"
open(f"{D}/semana.html", "w").write(html)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto(f"file://{D}/semana.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(900)
    for sid, fn in SL:
        pg.locator(f"#{sid}").screenshot(path=f"{D}/{fn}")
    b.close()
ims = [Image.open(f"{D}/{fn}") for _, fn in SL]
sh = Image.new("RGB", (7 * 400 + 80, 500 + 20), "#C9D0CC")
for i, im in enumerate(ims): sh.paste(im.resize((400, 500), Image.LANCZOS), (10 + i * 410, 10))
sh.save(f"{D}/visao-geral.png")
print("ok")

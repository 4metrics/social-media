import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD

FS = "/home/claude/fonts/fs"
ff = ""
for fam, pkg, pre in [("Inter", "fontsource-inter-5.3.0", "inter"), ("Plus Jakarta Sans", "fontsource-plus-jakarta-sans-5.3.0", "plus-jakarta-sans")]:
    for w in (400, 500, 600, 700):
        ff += f"@font-face{{font-family:'{fam}';src:url('file://{FS}/{pkg}/package/files/{pre}-latin-{w}-normal.woff2') format('woff2');font-weight:{w}}}"

NAVY, LIME, GTXT, MUT, BOR, SUB, BSUB, RED = "#05131C", "#92C549", "#406500", "#4F5B63", "#E1E7E4", "#F4F7F5", "#EAF5DD", "#D92D20"
N = 7

CSS = ff + f"""
*{{box-sizing:border-box}} body{{margin:0;background:#ddd}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;background:#fff;
 background-image:radial-gradient(rgba(5,19,28,0.07) 1px,transparent 1.2px);background-size:22px 22px;
 color:{NAVY};font-family:'Inter',sans-serif;padding:72px;display:flex;flex-direction:column;gap:36px;margin-bottom:20px}}
.g{{position:absolute;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,0.28),rgba(146,197,73,0));pointer-events:none}}
.top{{position:relative;display:flex;justify-content:space-between;align-items:center}}
.pill{{display:inline-flex;align-items:center;height:42px;padding:0 20px;border-radius:999px;background:{BSUB};color:{GTXT};border:1px solid rgba(146,197,73,0.6);font-size:20px;font-weight:600}}
.cnt{{font-size:20px;color:{MUT};font-variant-numeric:tabular-nums}}
h1,h2{{position:relative;margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em}}
h1{{font-size:88px;line-height:94px}} h2{{font-size:78px;line-height:86px}}
.hl{{color:{GTXT}}} .num{{font-family:'Plus Jakarta Sans',sans-serif;font-size:36px;font-weight:700;color:{GTXT}}}
p.lead{{position:relative;margin:0;font-size:36px;line-height:50px;color:{MUT}}}
.card{{position:relative;background:#fff;border:1px solid {BOR};border-radius:28px;box-shadow:0 1px 2px rgba(5,19,28,0.04),0 12px 32px rgba(5,19,28,0.06)}}
.feat{{border:1px solid rgba(146,197,73,0.85);box-shadow:0 0 0 1px rgba(146,197,73,0.15),0 0 28px rgba(146,197,73,0.25)}}
.foot{{position:relative;display:flex;justify-content:space-between;align-items:center;margin-top:auto}}
.lbl{{font-size:22px;color:{MUT}}}
.btn{{display:inline-flex;align-items:center;height:84px;padding:0 40px;border-radius:12px;background:{LIME};color:{NAVY};font-size:32px;font-weight:600}}
"""

def logo(s=36):
    return f'<span style="display:inline-flex;align-items:center;gap:12px">{SYM(s+4,dots=NAVY,accent=LIME)}{WORD(s-4,NAVY,LIME)}</span>'

def slide(i, body, glows="", foot_right=None, foot_left=""):
    fr = foot_right if foot_right is not None else logo()
    return f'''<section class="s" id="s{i}">{glows}
<div class="top"><span class="pill">Benefícios</span><span class="cnt">{i}/{N}</span></div>
{body}
<div class="foot"><span style="font-size:26px;color:{GTXT};font-weight:600">{foot_left}</span>{fr}</div></section>'''

def glow(x, y, s): return f'<div class="g" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px"></div>'

# ---------- 1. capa: fontes -> 4metrics -> painel
srcs = ["CRM", "Mídia paga", "E-commerce / ERP", "Planilhas"]
ys = [40, 150, 260, 370]
src_html = "".join(f'<div class="card" style="position:absolute;left:0;top:{y}px;width:300px;height:80px;border-radius:16px;display:flex;align-items:center;padding:0 24px;font-size:26px;font-weight:600">{t}</div>' for t, y in zip(srcs, ys))
lines = "".join(f'<path d="M300,{y+40} C420,{y+40} 420,250 520,250" fill="none" stroke="{LIME}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>' for y in ys)
hub = f'<div class="card feat" style="position:absolute;left:520px;top:180px;width:140px;height:140px;border-radius:32px;display:flex;align-items:center;justify-content:center">{SYM(84,dots=NAVY,accent=LIME)}</div>'
out_line = f'<path d="M660,250 L740,250" stroke="{LIME}" stroke-width="3" stroke-dasharray="2 9" stroke-linecap="round"/>'
bars = "".join(f'<rect x="{18+k*34}" y="{110-h}" width="22" height="{h}" rx="5" fill="{LIME if k==5 else "#C9D6CF"}"/>' for k, h in enumerate([40, 55, 48, 70, 62, 92]))
panel = f'''<div class="card" style="position:absolute;left:740px;top:130px;width:196px;height:240px;border-radius:20px;padding:20px 0 0 0">
<div style="padding:0 20px;font-size:22px;color:{MUT}">Receita</div>
<div style="padding:0 20px;font-family:'Plus Jakarta Sans';font-size:30px;font-weight:700">hoje</div>
<svg width="196" height="130" viewBox="0 0 230 130" style="margin-top:8px">{bars}</svg></div>'''
diagram = f'<div style="position:relative;height:460px"><svg width="936" height="460" style="position:absolute;left:0;top:0">{lines}{out_line}</svg>{src_html}{hub}{panel}</div>'
s1 = slide(1, f'''<h1>Vendas, marketing e CRM no mesmo número. <span class="hl">Todo dia.</span></h1>
<p class="lead">4 coisas que mudam na sua gestão quando os dados trabalham por você.</p>
{diagram}''', glow(560, -260, 760) + glow(-300, 1000, 560), foot_left="Arraste →")

# ---------- 2. problema
def mcard(src, val, lab):
    return f'''<div class="card" style="flex:1;padding:34px 30px;display:flex;flex-direction:column;gap:8px">
<span style="font-size:26px;color:{MUT}">{src}</span>
<span style="font-family:'Plus Jakarta Sans';font-size:100px;line-height:110px;font-weight:700;letter-spacing:-0.03em;font-variant-numeric:tabular-nums">{val}</span>
<span style="font-size:26px;color:{MUT}">{lab}</span></div>'''
s2 = slide(2, f'''<h2>Hoje, cada ferramenta conta <span class="hl">um número diferente.</span></h2>
<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:36px"><div style="display:flex;flex-direction:column;gap:14px">
<span class="lbl">Vendas de outubro</span>
<div style="display:flex;gap:20px">{mcard("CRM","142","vendas")}{mcard("Mídia paga","168","conversões")}{mcard("Financeiro","131","pedidos")}</div></div>
<div class="card" style="padding:32px 36px;background:{SUB};box-shadow:none;display:flex;gap:20px;align-items:flex-start">
<span style="flex:none;width:44px;height:44px;border-radius:999px;background:#FEE4E2;color:{RED};font-size:28px;font-weight:700;display:flex;align-items:center;justify-content:center">?</span>
<p style="margin:0;font-size:32px;line-height:44px">E a reunião de resultado vira uma discussão sobre <b>qual número está certo</b>, não sobre o que fazer.</p></div></div>''',
glow(640, -240, 680))

# ---------- benefit slide template
def ben(i, n, title, text, visual, gl):
    return slide(i, f'''<span class="num" style="position:relative">{n}</span>
<h2 style="margin-top:-20px">{title}</h2>
<p class="lead">{text}</p>
<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:28px">{visual}</div>''', gl)

# 3. fonte da verdade
merge = "".join(f'<path d="M40,{y} C240,{y} 240,200 380,200" fill="none" stroke="#C9D6CF" stroke-width="4"/>' for y in (40, 200, 360))
dots3 = "".join(f'<circle cx="40" cy="{y}" r="13" fill="{NAVY}"/>' for y in (40, 200, 360))
v3 = f'''<div style="position:relative;height:400px"><svg width="400" height="400" style="position:absolute;left:0;top:0">{merge}{dots3}</svg>
<div class="card feat" style="position:absolute;left:380px;top:50px;width:556px;padding:40px 40px">
<div style="font-size:26px;color:{MUT}">Vendas de outubro · todas as fontes</div>
<div style="font-family:'Plus Jakarta Sans';font-size:112px;line-height:124px;white-space:nowrap;font-weight:700;letter-spacing:-0.03em">1 número</div>
<div style="font-size:26px;color:{GTXT};font-weight:600">mesma regra para o time inteiro</div></div></div>'''
s3 = ben(3, "01", 'Uma fonte da <span class="hl">verdade</span>',
         "Dados de vendas, marketing e CRM integrados e modelados com as mesmas regras de negócio. Todo mundo olha para o mesmo número.", v3, glow(620, -260, 700))

# 4. atualizado todo dia
cells = ""
for d in range(1, 31):
    r, c = divmod(d - 1, 10)
    x, y = c * 94, r * 104
    if d == 2:
        st = f"background:{LIME};color:{NAVY};border:1px solid {LIME};box-shadow:0 0 22px rgba(146,197,73,0.6)"
    elif d == 30:
        st = f"background:#FEE4E2;color:{RED};border:1px solid #FDA29B"
    else:
        st = f"background:#fff;color:{MUT};border:1px solid {BOR}"
    cells += f'<div style="position:absolute;left:{x}px;top:{y}px;width:84px;height:92px;border-radius:16px;{st};display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:600">{d}</div>'
v4 = f'''<div style="position:relative;height:300px">{cells}</div>
<div style="position:relative;display:flex;flex-direction:column;gap:16px;font-size:30px">
<span style="display:inline-flex;align-items:center;gap:12px"><i style="width:26px;height:26px;border-radius:7px;background:{LIME}"></i>Com a 4metrics: você vê no dia 2</span>
<span style="display:inline-flex;align-items:center;gap:12px"><i style="width:26px;height:26px;border-radius:7px;background:#FEE4E2;border:1px solid #FDA29B"></i>Relatório mensal: dia 30</span></div>'''
s4 = ben(4, "02", 'Atualizado <span class="hl">todo dia</span>',
         "Os dados chegam atualizados toda manhã. Você vê a queda quando ela começa, não quando o mês fecha.", v4, glow(-280, -200, 680))

# 5. paineis prontos
def kpi(l, v, d):
    return f'<div style="flex:1;border:1px solid {BOR};border-radius:18px;padding:22px 22px"><div style="font-size:22px;color:{MUT}">{l}</div><div style="font-family:\'Plus Jakarta Sans\';font-size:50px;font-weight:700;letter-spacing:-0.02em;white-space:nowrap">{v}</div><div style="font-size:21px;color:{GTXT};font-weight:600">{d}</div></div>'
fun = [("Leads", 100), ("Qualificados", 62), ("Propostas", 34), ("Vendas", 18)]
funnel = "".join(f'<div style="display:flex;align-items:center;gap:16px"><span style="width:200px;font-size:26px;color:{MUT}">{l}</span><div style="height:44px;width:{w*6.2}px;border-radius:10px;background:{LIME if l=="Vendas" else "#C9D6CF"}"></div></div>' for l, w in fun)
v5 = f'''<div class="card" style="padding:36px;display:flex;flex-direction:column;gap:30px">
<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:'Plus Jakarta Sans';font-size:32px;font-weight:700">Painel de receita</span></div>
<div style="display:flex;gap:16px">{kpi("Receita","R$ 1,2 mi","+8% vs. mês anterior")}{kpi("CAC","R$ 310","−5%")}{kpi("ROAS","4,1","+0,3")}</div>
<div style="display:flex;flex-direction:column;gap:16px">{funnel}</div></div>'''
s5 = ben(5, "03", 'Painéis prontos para <span class="hl">decidir</span>',
         "Funil, receita por canal, CAC e ROAS em painéis que o time usa de verdade.", v5, glow(600, -240, 700))

# 6. sem time de dados
def item(t, ok=True):
    ic = f'<span style="flex:none;width:42px;height:42px;border-radius:999px;background:{BSUB};color:{GTXT};font-size:24px;font-weight:700;display:flex;align-items:center;justify-content:center">✓</span>'
    return f'<div style="display:flex;gap:16px;align-items:center;font-size:32px">{ic}{t}</div>'
v6 = f'''<div style="position:relative;display:flex;gap:20px">
<div class="card" style="flex:1.3;padding:40px 36px;display:flex;flex-direction:column;gap:26px">
<span style="font-size:26px;color:{MUT};font-weight:600">A 4metrics faz</span>
{item("Integra as fontes")}{item("Modela os dados")}{item("Monta os painéis")}{item("Mantém e evolui")}</div>
<div class="card feat" style="flex:1;padding:40px 36px;display:flex;flex-direction:column;justify-content:center;gap:20px">
<span style="font-size:26px;color:{MUT};font-weight:600">Você faz</span>
<span style="font-family:'Plus Jakarta Sans';font-size:64px;line-height:72px;font-weight:700;letter-spacing:-0.03em">Acessa e <span class="hl">decide.</span></span></div></div>'''
s6 = ben(6, "04", 'Sem montar um <span class="hl">time de dados</span>',
         "Você não precisa contratar engenheiro, analista e ferramenta. A gente constrói e cuida de tudo.", v6, glow(-260, 900, 640))

# 7. CTA
s7 = slide(7, f'''<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px;position:relative">
<div>{SYM(120,dots=NAVY,accent=LIME)}</div>
<h1>Quer ver isso com <span class="hl">os seus dados?</span></h1>
<p class="lead">No diagnóstico, a gente mostra onde estão os gargalos do seu funil e quanto eles custam.</p>
<div><span class="btn">Agendar diagnóstico</span></div>
<p style="margin:0;font-size:28px">Comente <b>DIAGNÓSTICO</b> ou chame no direct.</p></div>''',
glow(500, -300, 900) + glow(-300, 900, 700))

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{s1}{s2}{s3}{s4}{s5}{s6}{s7}</body></html>"
os.makedirs("/home/claude/out/carrossel", exist_ok=True)
open("/home/claude/out/carrossel/carrossel.html", "w").write(html)

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    pg.goto("file:///home/claude/out/carrossel/carrossel.html")
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(800)
    for i in range(1, N + 1):
        pg.locator(f"#s{i}").screenshot(path=f"/home/claude/out/carrossel/2026-11-24-beneficios-v2-{i:02d}.png")
    b.close()
print("ok")

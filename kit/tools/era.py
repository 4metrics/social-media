import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD

FS = "/home/claude/fonts/fs"
ff = ""
for fam, pkg, pre in [("Inter", "fontsource-inter-5.3.0", "inter"), ("Plus Jakarta Sans", "fontsource-plus-jakarta-sans-5.3.0", "plus-jakarta-sans")]:
    for w in (400, 500, 600, 700):
        ff += f"@font-face{{font-family:'{fam}';src:url('file://{FS}/{pkg}/package/files/{pre}-latin-{w}-normal.woff2') format('woff2');font-weight:{w}}}"

NAVY, LIME, GTXT, MUT, BOR, SUB, BSUB, RED = "#05131C", "#92C549", "#406500", "#4F5B63", "#E1E7E4", "#F4F7F5", "#EAF5DD", "#D92D20"
N = 5

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
.btn{{display:inline-flex;align-items:center;height:84px;padding:0 40px;border-radius:12px;background:{LIME};color:#05131D;font-size:32px;font-weight:600}}
"""

def logo(s=36):
    return f'<span style="display:inline-flex;align-items:center;gap:12px">{SYM(s+4,dots=NAVY,accent=LIME)}{WORD(s-4,NAVY,LIME)}</span>'

def slide(i, body, glows="", foot_right=None, foot_left=""):
    fr = foot_right if foot_right is not None else logo()
    return f'''<section class="s" id="s{i}">{glows}
<div class="top"><span class="pill">Nova era</span><span class="cnt">{i}/{N}</span></div>
{body}
<div class="foot"><span style="font-size:26px;color:{GTXT};font-weight:600">{foot_left}</span>{fr}</div></section>'''

def glow(x, y, s): return f'<div class="g" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px"></div>'


def chip(t, on=True, strike=False):
    st = f"background:{BSUB};color:{GTXT};border:1px solid rgba(146,197,73,0.7)" if on else f"background:{SUB};color:{MUT};border:1px solid {BOR}"
    deco = "text-decoration:line-through;text-decoration-thickness:2px" if strike else ""
    return f'<span style="display:inline-flex;align-items:center;height:64px;padding:0 28px;border-radius:999px;font-size:28px;font-weight:600;{st};{deco}">{t}</span>'

# 1 capa
s1 = slide(1, f"""<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:56px">
<h1 style="font-size:96px;line-height:102px">A era da IA mudou a forma como as empresas trabalham <span class="hl">com dados.</span></h1>
<div style="display:flex;align-items:center;gap:22px;flex-wrap:wrap">{chip("Relatório do mês", False, True)}<span style="font-size:40px;color:{GTXT}">→</span>{chip("Dado diário + IA")}</div></div>""",
glow(560, -260, 760) + glow(-300, 1000, 560), foot_left="Arraste →")

def tag(t, on):
    c = GTXT if on else MUT
    return f'<span style="position:relative;font-family:\'Plus Jakarta Sans\';font-size:36px;font-weight:700;color:{c};text-transform:uppercase;letter-spacing:0.08em">{t}</span>'

# 2 antes
rows = "".join(f'<div style="display:flex;border-top:1px solid {BOR}">' + "".join(f'<div style="flex:1;height:84px;border-left:1px solid {BOR};padding:24px 22px;font-size:28px;color:{MUT}">{c}</div>' for c in r) + '</div>' for r in [["Canal","Leads","Vendas"],["Google","?","?"],["Meta","?","?"],["CRM","?","?"]])
v2 = f"""<div class="card" style="padding:0;overflow:hidden;box-shadow:none;background:{SUB}">
<div style="display:flex;justify-content:space-between;align-items:center;padding:30px 28px"><span style="font-size:28px;font-weight:600;color:{MUT}">relatorio_outubro_v3_FINAL.xlsx</span><span style="font-size:26px;color:{RED};font-weight:600">entregue no dia 30</span></div>
<div style="background:#fff">{rows}</div></div>"""
s2 = slide(2, f"""{tag("Antes", False)}
<h2 style="margin-top:-12px;color:{MUT}">O dado era um relatório.</h2>
<p class="lead">Alguém extraía, montava a planilha e apresentava no fim do mês. Quando chegava, já explicava o passado.</p>
<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center">{v2}</div>""", "")

# 3 agora
def node(t, w=260):
    return f'<div class="card" style="width:{w}px;height:100px;border-radius:18px;display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:600">{t}</div>'
v3 = f"""<div style="position:relative;display:flex;align-items:center;justify-content:space-between">
<div style="display:flex;flex-direction:column;gap:14px">{node("Vendas",240)}{node("Marketing",240)}{node("CRM",240)}</div>
<span style="font-size:40px;color:{GTXT}">→</span>
<div class="card feat" style="width:260px;padding:34px 20px;display:flex;flex-direction:column;align-items:center;gap:14px">{SYM(120,dots=NAVY,accent=LIME)}
<span style="font-size:24px;color:{GTXT};font-weight:600;text-align:center">atualizado hoje, 06:00</span></div>
<span style="font-size:40px;color:{GTXT}">→</span>
<div style="display:flex;flex-direction:column;gap:14px">{node("Seu time",210)}{node("Sua IA",210)}</div></div>"""
s3 = slide(3, f"""{tag("Agora", True)}
<h2 style="margin-top:-12px">O dado é um <span class="hl">ativo.</span></h2>
<p class="lead">Integrado, atualizado todo dia e pronto para ser lido por pessoas e por IA.</p>
<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center">{v3}</div>""", glow(600, -240, 720))

# 4 o que nao mudou
def layer(t, w, on=False):
    st = f"background:{LIME};color:#05131D;border:1px solid {LIME};box-shadow:0 0 28px rgba(146,197,73,0.35)" if on else f"background:#fff;color:{NAVY};border:1px solid {BOR}"
    return f'<div style="width:{w}px;height:110px;border-radius:20px;{st};display:flex;align-items:center;justify-content:center;font-size:30px;font-weight:600">{t}</div>'
v4 = f"""<div style="position:relative;display:flex;flex-direction:column;align-items:center;gap:14px">
{layer("IA e agentes",520)}{layer("Painéis e análises",720)}{layer("Dados integrados e confiáveis",936,True)}
<span style="margin-top:12px;font-size:26px;color:#4F5B63">A IA fica em cima da base. Sem base, não fica de pé.</span></div>"""
s4 = slide(4, f"""{tag("O que não mudou", True)}
<h2 style="margin-top:-12px">IA com dado desorganizado só <span class="hl">erra mais rápido.</span></h2>
<p class="lead">A base continua a mesma: dado integrado, limpo e confiável.</p>
<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center">{v4}</div>""", glow(-260, 900, 640))

# 5 cta
s5 = slide(5, f"""<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:40px;position:relative">
<div>{SYM(120,dots=NAVY,accent=LIME)}</div>
<h1>Nessa nova era, a 4metrics está <span class="hl">ao lado da sua empresa.</span></h1>
<p class="lead">A gente entrega a base de dados que a sua equipe e a sua IA precisam para decidir antes do concorrente.</p>
<div><span class="btn">Agendar diagnóstico</span></div>
<p style="margin:0;font-size:28px">Comente <b>DIAGNÓSTICO</b> e vamos ver juntos por onde começar.</p></div>""",
glow(500, -300, 900) + glow(-300, 900, 700))


DARK = [("#FFFFFF","@@W"),("#fff","@@W"),("#05131C","#FFFFFF"),("@@W","#14232C"),("#406500","#92C549"),("#4F5B63","#9AA7B0"),
        ("#E1E7E4","#2B3640"),("#F4F7F5","#0B1B24"),("#EAF5DD","#16301F"),("rgba(5,19,28,0.07)","rgba(255,255,255,0.09)"),
        ("rgba(5,19,28,0.04)","rgba(0,0,0,0.2)"),("rgba(5,19,28,0.06)","rgba(0,0,0,0.25)"),("#FEE4E2","#3A1A1A"),("#D92D20","#F97066"),("#C9D6CF","#3A4A52")]
def theme(sl, t):
    if t == "L": return sl
    if t == "D":
        for a_, b_ in DARK: sl = sl.replace(a_, b_)
        return sl.replace('class="s"', 'class="s dk" style="background-color:#05131C;background-image:radial-gradient(rgba(255,255,255,0.09) 1px,transparent 1.2px);color:#FFFFFF"')
    if t == "LIMA":
        rep=[('class="hl"','style="text-decoration:underline;text-decoration-color:#FFFFFF;text-decoration-thickness:6px;text-underline-offset:10px"'),
             ("#4F5B63","#1F3A12"),("#406500","#05131C"),("#EAF5DD","rgba(255,255,255,0.35)"),("rgba(146,197,73,0.6)","rgba(5,19,28,0.25)"),
             ('class="btn"','class="btn" style="background:#05131C;color:#FFFFFF"')]
        for a_, b_ in rep: sl = sl.replace(a_, b_)
        # symbol on lime: accent dot white (MIV "sobre lima")
        sl = sl.replace('fill="#92C549"','fill="#FFFFFF"')
        sl = sl.replace('class="g"', 'class="g" data-x="1"')
        return sl.replace('class="s"', 'class="s lm" style="background-color:#92C549;background-image:radial-gradient(rgba(5,19,28,0.10) 1px,transparent 1.2px)"').replace('data-x="1"','style="display:none"')
    return sl

D = "/home/claude/out/era-ia"
os.makedirs(D, exist_ok=True)
VARIANTS = {"claro": ["L","L","L","L","L"], "escuro": ["D","D","D","D","LIMA"]}
slides=[s1,s2,s3,s4,s5]
from playwright.sync_api import sync_playwright
from PIL import Image
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for name, ts in VARIANTS.items():
        XCSS = """.dk .hl,.dk .num{color:#92C549} .dk p.lead,.dk .cnt,.dk .lbl{color:#9AA7B0} .dk .card{background:#14232C;border-color:#2B3640;box-shadow:none} .dk .feat{border-color:rgba(146,197,73,.6);box-shadow:0 0 0 1px rgba(146,197,73,.12),0 0 28px rgba(146,197,73,.2)} .dk .pill{background:#16301F;color:#92C549;border-color:rgba(146,197,73,.45)} .lm p.lead,.lm .cnt{color:#1F3A12} .lm .pill{background:rgba(255,255,255,.35);color:#05131C;border-color:rgba(5,19,28,.2)}"""
        html = f"<html><head><meta charset='utf-8'><style>{CSS}{XCSS}</style></head><body>" + "".join(theme(sl,t) for sl,t in zip(slides,ts)) + "</body></html>"
        open(f"{D}/era-{name}.html", "w").write(html)
        pg.goto(f"file://{D}/era-{name}.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
        suf = "" if name=="claro" else "-escuro"
        for i in range(1, N + 1):
            pg.locator(f"#s{i}").screenshot(path=f"{D}/2026-11-17-nova-era-ia{suf}-{i:02d}.png")
        ims=[Image.open(f"{D}/2026-11-17-nova-era-ia{suf}-{i:02d}.png") for i in range(1,N+1)]
        W_,H_=540,675
        sh=Image.new('RGB',(W_*5+60,H_+20),'#E1E7E4')
        for k,im in enumerate(ims): sh.paste(im.resize((W_,H_),Image.LANCZOS),(10+k*(W_+10),10))
        sh.save(f"{D}/carrossel-nova-era-ia{suf}-visao-geral.png")
    b.close()
print("ok")

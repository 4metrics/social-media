import sys, os; sys.path.insert(0,"/home/claude/tools")
import miv_site as MS   # regenerates base Site-* pages
from page import SYM, WORD
os.chdir("/home/claude/dz/project")
T={"dark":dict(bg="#05131C",sub="#14232C",card="#14232C",bor="#2B3640",bstr="#66757F",txt="#FFFFFF",mut="#9AA7B0",gtxt="#92C549",bsub="#16301F",
               dots="rgba(255,255,255,0.09)",glow=0.24,gb="border: 1px solid rgba(146,197,73,0.45); box-shadow: 0 0 0 1px rgba(146,197,73,0.12), 0 0 28px rgba(146,197,73,0.16)",
               sdots="#FFFFFF",sacc="#92C549",idot="#92C549",name="Escuro"),
   "light":dict(bg="#FFFFFF",sub="#F4F7F5",card="#FFFFFF",bor="#E1E7E4",bstr="#7F8D88",txt="#05131C",mut="#4F5B63",gtxt="#406500",bsub="#EAF5DD",
               dots="rgba(5,19,28,0.07)",glow=0.20,gb="border: 1px solid rgba(146,197,73,0.85); box-shadow: 0 0 0 1px rgba(146,197,73,0.15), 0 0 24px rgba(146,197,73,0.22)",
               sdots="#05131C",sacc="#92C549",idot="#92C549",name="Claro")}
LIME,NAVY,WHT="#92C549","#05131C","#FFFFFF"
H,B=MS.H,MS.B
glow=MS.glow
def logo(s,t): return f'<span style="display: inline-flex; align-items: center; gap: {round(s*0.25)}px">{SYM(s,dots=t["sdots"],accent=t["sacc"])}{WORD(round(s*0.62),t["txt"],t["idot"])}</span>'
def pill(t,th): return f'<span style="display: inline-flex; align-items: center; height: 26px; padding: 0 12px; border-radius: 999px; background: {th["bsub"]}; color: {th["gtxt"]}; border: 1px solid rgba(146,197,73,0.45); font-size: 12px; font-weight: 500; white-space: nowrap">{t}</span>'
def btn(t,th,primary=True,h=40,fs=14):
    if primary: return f'<span style="display: inline-flex; align-items: center; height: {h}px; padding: 0 18px; border-radius: 8px; background: {LIME}; color: {NAVY}; font-size: {fs}px; font-weight: 600; white-space: nowrap">{t}</span>'
    return f'<span style="display: inline-flex; align-items: center; height: {h}px; padding: 0 18px; border-radius: 8px; background: transparent; color: {th["txt"]}; border: 1px solid {th["bstr"]}; font-size: {fs}px; font-weight: 600; white-space: nowrap">{t}</span>'
def kw(t,th):  # keyword in title
    if th is T["dark"]: return f'<span style="color: {LIME}">{t}</span>'
    return f'<span style="background: {LIME}; color: {NAVY}; padding: 0 6px; border-radius: 6px">{t}</span>'
def page(path,title,body,th,w=1280,h=720,glows=""):
    MS.page(path,title,body,w=w,h=h,bg=th["bg"],dots=False,glows=glows)
    s=open(path).read()
    s=s.replace(f"background-color: {th['bg']}; ;",f"background-color: {th['bg']}; background-image: radial-gradient({th['dots']} 1px, transparent 1.2px); background-size: 22px 22px;")
    s=s.replace(f"color: {WHT if th['bg']==NAVY else NAVY}; font-family", f"color: {th['txt']}; font-family")
    open(path,"w").write(s)
def head(n,th): return f'<div style="position: relative; display: flex; justify-content: space-between; align-items: baseline"><p style="margin: 0; font-size: 13px; font-weight: 500; color: {th["mut"]}">MIV 4metrics · {n}</p><span style="display: inline-flex; align-items: center; height: 24px; padding: 0 10px; border-radius: 999px; border: 1px solid {th["bor"]}; font-size: 12px; color: {th["mut"]}">v2 · temas claro e escuro</span></div>'
h2=lambda t,th: f'<h2 style="position: relative; margin: 0; font-family: {H}; font-size: 28px; line-height: 36px; font-weight: 700; letter-spacing: -0.01em; color: {th["txt"]}">{t}</h2>'
D,L=T["dark"],T["light"]

# relabel base pages
import glob
for f in glob.glob("Site-0*.dc.html"):
    s=open(f).read().replace("teste · visual do site","v2 · temas claro e escuro")
    open(f,"w").write(s)

# 04 cores — both themes
def sw(th,n,hx,u,bd=False):
    b=f"border: 1px solid {th['bor']};" if bd else ""
    return f'<div><div style="height: 88px; background: {hx}; {b} border-radius: 12px"></div><p style="margin: 8px 0 0; font-size: 13px; font-weight: 600; color: {th["txt"]}">{n}</p><p style="margin: 1px 0 0; font-size: 11px; line-height: 16px; color: {th["mut"]}">{hx} · {u}</p></div>'
def palette(th, items):
    return f'''<div style="position: relative; background: {th["bg"]}; border: 1px solid {th["bor"]}; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; gap: 14px">
<p style="margin: 0; font-family: {H}; font-size: 17px; font-weight: 700; color: {th["txt"]}">Tema {th["name"].lower()}{" · principal" if th is L else ""}</p>
<div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 10px">{"".join(sw(th,*i) for i in items)}</div></div>'''
pd=palette(D,[("Fundo","#05131C","azul-noite",True),("Card","#14232C","superfície",True),("Borda","#2B3640","divisões"),("Texto","#FFFFFF","principal"),("Secundário","#9AA7B0","legendas"),("Verde","#92C549","destaque e texto verde")])
pl=palette(L,[("Fundo","#FFFFFF","página",True),("Névoa","#F4F7F5","seções e cards",True),("Borda","#E1E7E4","divisões",True),("Texto","#05131C","azul-noite"),("Secundário","#4F5B63","legendas"),("Verde 800","#406500","texto verde")])
page("Site-04-cores.dc.html","MIV · Cores",head("04 · Cores",D)+h2("Paleta: tema claro (principal) e tema escuro",D)+f'''
<div style="position: relative; display: flex; flex-direction: column; gap: 14px">{pl}{pd}</div>
<p style="position: relative; margin: 0; font-size: 13px; color: {D["mut"]}">O verde #92C549 é o mesmo nos dois temas: botão principal e destaque, sempre com texto azul-noite. No tema claro, o verde nunca é cor de texto: use o verde 800.</p>''',D)

# 04b temas side by side
def mini(th):
    return f'''<div style="position: relative; overflow: hidden; background-color: {th["bg"]}; background-image: radial-gradient({th["dots"]} 1px, transparent 1.2px); background-size: 18px 18px; border: 1px solid {th["bor"]}; border-radius: 16px; padding: 22px; display: flex; flex-direction: column; gap: 14px; height: 100%; box-sizing: border-box">
{glow(260,-80,280,th["glow"])}
<div style="position: relative; display: flex; justify-content: space-between; align-items: center">{logo(24,th)}{btn("Agendar diagnóstico",th,h=32,fs=12)}</div>
<div style="position: relative">{pill("Revenue Intelligence",th)}</div>
<p style="position: relative; margin: 0; font-family: {H}; font-size: 24px; line-height: 30px; font-weight: 700; letter-spacing: -0.02em; color: {th["txt"]}">Receita com dado, não com {kw("achismo.",th)}</p>
<div style="position: relative; display: grid; grid-template-columns: 1fr 1fr; gap: 12px">
<div style="background: {th["card"] if th is D else th["sub"]}; border: 1px solid {th["bor"]}; border-radius: 12px; padding: 14px"><p style="margin: 0; font-size: 11px; color: {th["mut"]}">Receita do mês</p><p style="margin: 4px 0 0; font-family: {H}; font-size: 22px; font-weight: 700; color: {th["txt"]}; font-variant-numeric: tabular-nums">R$ 1,24 mi</p><p style="margin: 2px 0 0; font-size: 11px; font-weight: 600; color: {th["gtxt"]}">▲ +12,4%</p></div>
<div style="background: {th["card"] if th is D else th["bg"]}; {th["gb"]}; border-radius: 12px; padding: 14px"><p style="margin: 0; font-size: 11px; font-weight: 600; color: {th["gtxt"]}">Insight do agente</p><p style="margin: 4px 0 0; font-size: 12px; line-height: 17px; color: {th["txt"]}">R$ 86 mil parados no funil.</p></div></div>
<div style="position: relative; display: flex; gap: 10px">{btn("Ver dashboard",th,True,34,12)}{btn("Ver exemplo",th,False,34,12)}</div></div>'''
rows=[("Fundo","#05131C","#FFFFFF"),("Card / seção","#14232C","#F4F7F5"),("Borda","#2B3640","#E1E7E4"),("Texto","#FFFFFF","#05131C"),("Texto secundário","#9AA7B0","#4F5B63"),
      ("Botão principal","#92C549 + texto azul-noite","#92C549 + texto azul-noite"),("Texto verde / delta","#92C549","#406500"),("Malha de pontos","branco 9%","azul-noite 7%"),("Brilho verde","24%","20%")]
tbl="".join(f'<div style="display: grid; grid-template-columns: 1.1fr 1fr 1fr; gap: 8px; padding: 6px 0; border-bottom: 1px solid {D["bor"]}; font-size: 12px"><span style="color: {D["mut"]}">{a}</span><span>{b}</span><span>{c}</span></div>' for a,b,c in rows)
page("Site-04b-temas.dc.html","MIV · Temas",head("04b · Tema escuro e tema claro",D)+h2("Os mesmos componentes nos dois temas",D)+f'''
<div style="position: relative; display: grid; grid-template-columns: 1fr 1fr 0.9fr; gap: 16px; flex: 1">
<div style="display: flex; flex-direction: column; gap: 8px">{mini(L)}<p style="margin: 0; font-size: 13px; font-weight: 600">Claro · principal (plataforma e documentos)</p></div>
<div style="display: flex; flex-direction: column; gap: 8px">{mini(D)}<p style="margin: 0; font-size: 13px; font-weight: 600">Escuro · site, redes e capas</p></div>
<div><div style="display: grid; grid-template-columns: 1.1fr 1fr 1fr; gap: 8px; padding-bottom: 6px; font-size: 11px; font-weight: 600; color: {D["mut"]}"><span>Token</span><span>Escuro</span><span>Claro (principal)</span></div>{tbl}</div></div>''',D)

# 06 efeitos: dark + light rows
def fxdemos(th,hgt):
    base=f"border-radius: 14px; background: {th['card'] if th is D else th['sub']}; border: 1px solid {th['bor']}; height: {hgt}px"
    g=f'<div style="position: relative; overflow: hidden; {base}">{glow(30,-40,200,th["glow"]+0.1)}</div>'
    d=f'<div style="{base}; background-image: radial-gradient({"rgba(255,255,255,0.18)" if th is D else "rgba(5,19,28,0.16)"} 1px, transparent 1.3px); background-size: 16px 16px"></div>'
    b=f'<div style="border-radius: 14px; height: {hgt}px; background: {th["card"] if th is D else th["bg"]}; {th["gb"]}; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; color: {th["txt"]}">Card em destaque</div>'
    l=f'<div style="{base}; display: flex; align-items: center; justify-content: center"><svg width="200" height="70" viewBox="0 0 220 80" aria-hidden="true"><path d="M10 60 C 60 60, 70 20, 110 20 S 170 50, 210 30" fill="none" stroke="{th["bor"]}" stroke-width="2"></path><path d="M10 60 C 60 60, 70 20, 110 20" fill="none" stroke="{LIME if th is D else "#6D9E15"}" stroke-width="2.5" stroke-linecap="round" style="filter: drop-shadow(0 0 4px rgba(146,197,73,0.7))"></path><circle cx="110" cy="20" r="5" fill="{LIME}"></circle></svg></div>'
    return g,d,b,l
dg,dd,db,dl=fxdemos(D,118); lg,ld,lb,ll=fxdemos(L,118)
cap=lambda t,dsc: f'<p style="margin: 6px 0 0; font-size: 13px; font-weight: 600">{t}</p><p style="margin: 1px 0 0; font-size: 12px; line-height: 17px; color: {D["mut"]}">{dsc}</p>'
lightrow=f'<div style="position: relative; background: {L["bg"]}; border-radius: 16px; padding: 14px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px">{lg}{ld}{lb}{ll}</div>'
comps=f'<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap">{btn("Agendar diagnóstico",D)}{btn("Ver como funciona",D,False)}{pill("Revenue Intelligence",D)}<span style="width: 24px"></span><span style="display: inline-flex; gap: 10px; align-items: center; background: #FFFFFF; padding: 8px 10px; border-radius: 12px">{btn("Agendar diagnóstico",L,h=32,fs=12)}{btn("Ver como funciona",L,False,32,12)}{pill("Revenue Intelligence",L)}</span></div>'
page("Site-06-efeitos.dc.html","MIV · Formas e efeitos",head("06 · Formas, componentes e efeitos",D)+h2("Formas, componentes e efeitos",D)+f'''
<div style="position: relative">{comps}</div>
<div style="position: relative; display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px">
<div>{dg}{cap("Brilho verde","1 ou 2 por tela, nunca atrás de texto.")}</div><div>{dd}{cap("Malha de pontos","Textura sutil de fundo.")}</div>
<div>{db}{cap("Borda com brilho","Só no card em destaque.")}</div><div>{dl}{cap("Linha animada","Acende devagar; para com 'menos movimento'.")}</div></div>
{lightrow}
<p style="position: relative; margin: 0; font-size: 12px; color: {D["mut"]}">Acima: tema escuro. Faixa branca: os mesmos efeitos no tema claro, mais suaves. Cantos: botões 8 px · cards 16 px · etiquetas em pílula.</p>''',D,glows=glow(980,-80,420,0.16))

# 07 aplicacoes: dark hero, light hero, light platform
def hero(th,h=300):
    return f'''<div style="position: relative; height: {h}px; border-radius: 16px; overflow: hidden; background-color: {th["bg"]}; background-image: radial-gradient({th["dots"]} 1px, transparent 1.2px); background-size: 22px 22px; border: 1px solid {th["bor"]}; padding: 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 14px">
{glow(300,-60,340,th["glow"]+0.06)}
<div style="position: relative; display: flex; justify-content: space-between; align-items: center">{logo(22,th)}<span style="display: flex; gap: 14px; font-size: 12px; color: {th["mut"]}">Plataforma<span>Como funciona</span><span>Cases</span></span>{btn("Agendar diagnóstico",th,h=30,fs=12)}</div>
<div style="position: relative; margin-top: 10px">{pill("Revenue Intelligence",th)}</div>
<h3 style="position: relative; margin: 0; font-family: {H}; font-size: 28px; line-height: 34px; font-weight: 700; letter-spacing: -0.02em; color: {th["txt"]}">Você só acessa.<br>{kw("A gente constrói o resto.",th)}</h3>
<p style="position: relative; margin: 0; font-size: 13px; line-height: 19px; color: {th["mut"]}; max-width: 360px">Vendas, marketing e CRM integrados, com BI pronto dentro da plataforma.</p>
<div style="position: relative">{btn("Agendar diagnóstico",th,h=36,fs=13)}</div></div>'''
plat=f'''<div style="height: 186px; border-radius: 16px; background: {L["sub"]}; border: 1px solid {L["bor"]}; padding: 16px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px; color: {L["txt"]}">
<div style="display: flex; justify-content: space-between; align-items: center">{logo(20,L)}{btn("Nova análise com IA",L,h=28,fs=11)}</div>
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px">{"".join(f'<div style="background: #FFFFFF; border: 1px solid {L["bor"]}; border-radius: 12px; padding: 10px"><p style="margin: 0; font-size: 10px; color: {L["mut"]}">{a}</p><p style="margin: 2px 0 0; font-family: {H}; font-size: 17px; font-weight: 700; font-variant-numeric: tabular-nums">{b}</p><p style="margin: 0; font-size: 10px; font-weight: 600; color: {c}">{d}</p></div>' for a,b,c,d in [("Receita do mês","R$ 1,24 mi","#406500","▲ +12,4%"),("Conversão","18,6%","#B42318","▼ −1,2 p.p."),("Ticket médio","R$ 412","#4F5B63","● 0,0%")])}</div>
<div style="background: #FFFFFF; {L["gb"]}; border-radius: 12px; padding: 10px; font-size: 12px"><span style="font-weight: 600; color: #406500">Insight do agente · </span>R$ 86 mil parados no funil. Priorize os 10 maiores negócios.</div></div>'''
page("Site-07-aplicacoes.dc.html","MIV · Aplicações",head("07 · Aplicações",D)+f'''
<div style="position: relative; display: grid; grid-template-columns: 1fr 1fr; gap: 16px">
<div style="display: flex; flex-direction: column; gap: 6px">{hero(D)}<p style="margin: 0; font-size: 13px; font-weight: 600">Site · tema escuro</p></div>
<div style="display: flex; flex-direction: column; gap: 6px">{hero(L)}<p style="margin: 0; font-size: 13px; font-weight: 600">Site · tema claro</p></div></div>
<div style="position: relative; display: grid; grid-template-columns: 1.3fr 1fr; gap: 16px">
<div style="display: flex; flex-direction: column; gap: 6px">{plat}<p style="margin: 0; font-size: 13px; font-weight: 600">Plataforma · tema claro</p></div>
<div style="display: flex; flex-direction: column; gap: 6px"><div style="position: relative; height: 186px; border-radius: 16px; overflow: hidden; background-color: {NAVY}; background-image: radial-gradient(rgba(255,255,255,0.09) 1px, transparent 1.2px); background-size: 22px 22px; border: 1px solid {D["bor"]}; padding: 18px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between">{glow(160,-40,240,0.3)}<span style="position: relative; font-family: {H}; font-size: 20px; line-height: 25px; font-weight: 700; color: #FFFFFF">Seu CRM tem <span style="color: {LIME}">R$ 86 mil</span> parados no funil.</span><span style="position: relative">{WORD(14,"#FFFFFF","#92C549")}</span></div><p style="margin: 0; font-size: 13px; font-weight: 600">Post · tema escuro</p></div></div>''',D)

# resumo light & dark
def resumo(th, path, title):
    o=T["dark"] if th is T["light"] else T["light"]
    sec=lambda n,t: f'<p style="margin: 0 0 14px; font-size: 11px; color: {th["mut"]}">{n} · {t}</p>'
    hr=f'<div style="height: 1px; background: {th["bor"]}; margin: 22px 0"></div>'
    def t1(c,bg,cp,bd=None):
        b=f"border: 1px solid {bd};" if bd else ""
        return f'<div><div style="height: 150px; background: {bg}; {b} border-radius: 16px; display: flex; align-items: center; justify-content: center">{c}</div><p style="margin: 8px 0 0; font-size: 11px; color: {th["mut"]}">{cp}</p></div>'
    def sw2(n,hx,u,bd=False):
        b=f"border: 1px solid {th['bor']};" if bd else ""
        return f'<div><div style="height: 80px; background: {hx}; {b} border-radius: 12px"></div><p style="margin: 8px 0 0; font-size: 12px; font-weight: 600">{n}</p><p style="margin: 1px 0 0; font-size: 10px; line-height: 15px; color: {th["mut"]}">{hx}<br>{u}</p></div>'
    dot=lambda: f'<span style="flex: none; width: 8px; height: 8px; border-radius: 999px; background: {LIME}; margin-top: 6px; box-shadow: 0 0 8px rgba(146,197,73,0.6)"></span>'
    rule=lambda t: f'<div style="display: flex; gap: 10px; font-size: 13px; line-height: 20px">{dot()}<span>{t}</span></div>'
    if th is D: cols=[("Azul-noite","#05131C","fundo",True),("Card","#14232C","cards",True),("Borda","#2B3640","bordas",False),("Verde 4metrics","#92C549","destaque",False),("Branco","#FFFFFF","texto",False)]
    else: cols=[("Branco","#FFFFFF","fundo",True),("Névoa","#F4F7F5","seções e cards",True),("Borda","#E1E7E4","bordas",True),("Verde 4metrics","#92C549","destaque",False),("Azul-noite","#05131C","texto",False)]
    tiles = t1(logo(32,th), th["sub"] if th is L else th["card"], ("Principal: tema claro" if th is L else "Tema escuro"), th["bor"]) + t1(logo(32,o), o["bg"], ("Tema escuro (variação)" if o is D else "Principal: tema claro"), o["bor"] if o is L else None) + t1(SYM(52,dots=th["sdots"],accent=th["sacc"]), th["sub"] if th is L else th["card"], "Símbolo: favicon, app e avatar", th["bor"])
    body=f'''<div style="position: relative; display: flex; justify-content: space-between; align-items: center">{logo(28,th)}<span style="font-size: 10px; color: {th["mut"]}">Manual de identidade visual · v2 · {"tema claro (principal)" if th is L else "tema escuro"}</span></div>
<div style="position: relative"><h1 style="margin: 14px 0 0; font-family: {H}; font-size: 50px; line-height: 54px; font-weight: 700; letter-spacing: -0.03em">4metrics</h1>
<p style="margin: 8px 0 0; font-size: 14px; line-height: 20px; color: {th["mut"]}">Revenue Intelligence para times comerciais e de marketing. Software com serviço.</p></div>
<div style="position: relative">{hr}{sec("01","Logo")}<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px">{tiles}</div>
<p style="margin: 18px 0 0; font-size: 15px; line-height: 22px; font-weight: 500">Quatro pontos, quatro métricas. {kw("O verde é a que sobe.",th)}</p>
{hr}{sec("02",f"Cores · tema {th['name'].lower()}")}<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px">{"".join(sw2(*c) for c in cols)}</div>
<p style="margin: 14px 0 0; font-size: 13px; line-height: 20px; color: {th["mut"]}">{"Fundo azul-noite, nunca preto puro. Verde para destaque, botão e texto em destaque." if th is D else "Fundo branco e névoa. Verde só como fundo de botão e marcador; texto verde em #406500."}</p>
{hr}{sec("03","Tipografia")}<div style="display: grid; grid-template-columns: 230px 1fr; gap: 24px; align-items: end">
<div><p style="margin: 0; font-family: {H}; font-size: 96px; line-height: 88px; font-weight: 700; letter-spacing: -0.04em">Aa</p><p style="margin: 8px 0 0; font-family: {H}; font-size: 17px; font-weight: 700">Plus Jakarta Sans <span style="font-family: {B}; font-weight: 500; color: {th["mut"]}">+ Inter</span></p><p style="margin: 2px 0 0; font-size: 11px; color: {th["mut"]}">Títulos 600/700 · Texto Inter 400/500</p></div>
<div style="display: flex; flex-direction: column; gap: 6px"><p style="margin: 0; font-family: {H}; font-size: 27px; line-height: 34px; font-weight: 700; letter-spacing: -0.02em">O dado certo, na hora da {kw("decisão.",th)}</p>
<p style="margin: 0; font-family: {H}; font-size: 18px; font-weight: 700">Título 1 · 36/44</p><p style="margin: 0; font-family: {H}; font-size: 15px; font-weight: 600">Título 2 · 24/32</p>
<p style="margin: 4px 0 0; font-size: 11px">Corpo · 16/24 · A 4metrics integra vendas, marketing e CRM e entrega o BI pronto.</p><p style="margin: 0; font-size: 10px; color: {th["mut"]}">Pequeno · 14/20 · Texto secundário e legendas</p></div></div>
{hr}{sec("04","Componentes e efeitos")}<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap">{btn("Agendar diagnóstico",th,h=36,fs=13)}{btn("Ver como funciona",th,False,36,13)}{pill("Revenue Intelligence",th)}</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 16px">
<div style="position: relative; overflow: hidden; background: {th["card"] if th is D else th["sub"]}; border: 1px solid {th["bor"]}; border-radius: 16px; padding: 16px">{glow(180,-80,220,th["glow"])}<p style="position: relative; margin: 0; font-size: 10px; font-weight: 600; color: {th["gtxt"]}">Insight do agente</p><p style="position: relative; margin: 6px 0 0; font-size: 13px; line-height: 19px; font-weight: 500">R$ 86 mil parados no funil. Priorize os 10 maiores negócios esta semana.</p></div>
<div style="background: {th["card"] if th is D else th["bg"]}; {th["gb"]}; border-radius: 16px; padding: 16px; display: flex; justify-content: space-between; align-items: flex-end"><div><p style="margin: 0; font-size: 10px; font-weight: 500; color: {th["mut"]}">Receita do mês</p><p style="margin: 4px 0 0; font-family: {H}; font-size: 24px; font-weight: 700; font-variant-numeric: tabular-nums">R$ 1,24 mi</p></div><span style="font-size: 11px; font-weight: 600; color: {th["gtxt"]}">▲ +12,4%</span></div></div>
<p style="margin: 20px 0 0; font-family: {H}; font-size: 25px; line-height: 34px; font-weight: 700; letter-spacing: -0.02em">Receita com dado, não com {kw("achismo.",th)}</p>
{hr}{sec("05","Regras")}<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px 32px">{rule("Tema claro é o principal; o escuro é para site, redes e capas.")}{rule("Botão principal sempre verde com texto azul-noite.")}{rule("Brilho e malha de pontos sutis, nunca atrás de texto.")}{rule("No tema claro, verde não é texto: use o verde 800.")}{rule("Animações suaves; param com 'menos movimento'.")}{rule("4metrics sempre com m minúsculo.")}</div></div>
<div style="flex: 1"></div>
<div style="position: relative; display: flex; justify-content: space-between; align-items: center"><span style="display: inline-flex; align-items: center; gap: 10px">{SYM(22,dots=th["sdots"],accent=th["sacc"])}<span style="font-family: {H}; font-size: 15px; font-weight: 700">Você só acessa. A gente constrói o resto.</span></span><span style="font-size: 10px; color: {th["mut"]}">4metrics.com.br</span></div>'''
    page(path,title,body,th,w=900,h=1600,glows=glow(420,-120,520,th["glow"]-0.04)+glow(-160,900,420,th["glow"]-0.1))
resumo(D,"Site-00-resumo.dc.html","MIV · Resumo · tema escuro")
resumo(L,"Site-00b-resumo-claro.dc.html","MIV · Resumo · tema claro")
print("ok")

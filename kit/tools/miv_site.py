import sys, os; sys.path.insert(0,"/home/claude/tools")
from page import SYM, WORD
os.chdir("/home/claude/dz/project")
NAVY,CARD,BOR,LIME,WHT,MUT,INKL,MUTL,SUBL="#05131C","#14232C","#2B3640","#92C549","#FFFFFF","#9AA7B0","#05131C","#4F5B63","#F3F6F4"
H="'Plus Jakarta Sans', 'Inter', sans-serif"; B="'Inter', system-ui, sans-serif"
DOTS="background-image: radial-gradient(rgba(255,255,255,0.09) 1px, transparent 1.2px); background-size: 22px 22px"
def glow(x,y,s,a=0.22): return f'<div style="position: absolute; left: {x}px; top: {y}px; width: {s}px; height: {s}px; border-radius: 999px; background: radial-gradient(closest-side, rgba(146,197,73,{a}), rgba(146,197,73,0)); pointer-events: none"></div>'
GB="border: 1px solid rgba(146,197,73,0.45); box-shadow: 0 0 0 1px rgba(146,197,73,0.12), 0 0 28px rgba(146,197,73,0.16)"
sym=lambda s,**k: SYM(s, **({"dots":WHT,"accent":LIME}|k))
def logo(s, ink=WHT, idot=None, **k):
    if not k: k = {"dots":WHT,"accent":LIME} if ink==WHT else {"dots":ink,"accent":"#92C549"}
    return f'<span style="display: inline-flex; align-items: center; gap: {round(s*0.25)}px">{sym(s,**k)}{WORD(round(s*0.62), ink, idot)}</span>'
def page(path, title, body, w=1280, h=720, bg=NAVY, dots=True, glows=""):
    d = DOTS if dots else ""
    html=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;600;700&amp;family=Inter:wght@400;500;600&amp;display=swap">
<style>
body{{margin:0}}
a{{color:#92C549}}a:hover{{color:#B5DD86}}
</style>
</helmet>
<div style="position: relative; width: {w}px; height: {h}px; box-sizing: border-box; padding: 48px; background-color: {bg}; {d}; color: {WHT if bg==NAVY else INKL}; font-family: {B}; display: flex; flex-direction: column; gap: 28px; overflow: hidden">
{glows}
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{w},"height":{h}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    open(path,"w").write(html)
def head(n, dark=True):
    c = MUT if dark else MUTL
    return f'<div style="position: relative; display: flex; justify-content: space-between; align-items: baseline"><p style="margin: 0; font-size: 13px; font-weight: 500; color: {c}">MIV 4metrics · {n}</p><span style="display: inline-flex; align-items: center; height: 24px; padding: 0 10px; border-radius: 999px; border: 1px solid {BOR if dark else "#D5DDD8"}; font-size: 12px; color: {c}">teste · visual do site</span></div>'
h2=lambda t,c=WHT: f'<h2 style="position: relative; margin: 0; font-family: {H}; font-size: 28px; line-height: 36px; font-weight: 700; letter-spacing: -0.01em; color: {c}">{t}</h2>'
pill=lambda t,bg="rgba(146,197,73,0.12)",fg=LIME,bd="rgba(146,197,73,0.35)": f'<span style="display: inline-flex; align-items: center; height: 26px; padding: 0 12px; border-radius: 999px; background: {bg}; color: {fg}; border: 1px solid {bd}; font-size: 12px; font-weight: 500; white-space: nowrap">{t}</span>'
btn=lambda t,bg=LIME,fg=NAVY,bd=LIME,h=44,fs=15: f'<span style="display: inline-flex; align-items: center; height: {h}px; padding: 0 20px; border-radius: 8px; background: {bg}; color: {fg}; border: 1px solid {bd}; font-size: {fs}px; font-weight: 600; white-space: nowrap">{t}</span>'
cardbox=lambda inner,extra="": f'<div style="position: relative; background: {CARD}; border: 1px solid {BOR}; border-radius: 16px; {extra}">{inner}</div>'

# 01 capa
big=(f'<svg width="360" height="360" viewBox="0 0 64 64" aria-hidden="true" style="position: relative"><circle cx="19" cy="19" r="7" fill="{WHT}"></circle><circle cx="19" cy="45" r="7" fill="{WHT}"></circle><circle cx="45" cy="45" r="7" fill="{WHT}"></circle><circle cx="45" cy="19" r="9" fill="{LIME}" style="filter: drop-shadow(0 0 3px rgba(146,197,73,0.8))"></circle></svg>')
page("Site-01-capa.dc.html","Teste site · Capa", head("Capa")+f'''
<div style="position: relative; flex: 1; display: flex; justify-content: space-between; align-items: flex-end">
<div style="display: flex; flex-direction: column; gap: 28px">{logo(64)}
<div>{pill("Revenue Intelligence")}
<h1 style="margin: 16px 0 0; font-family: {H}; font-size: 60px; line-height: 64px; font-weight: 700; letter-spacing: -0.02em">Manual de<br><span style="color: {LIME}">Identidade Visual</span></h1>
<p style="margin: 16px 0 0; font-size: 17px; line-height: 26px; color: {MUT}; max-width: 520px">Logo, cores, tipografia, efeitos e aplicações da 4metrics, alinhados com o site.</p></div></div>
{big}</div>''', glows=glow(760,40,620,0.28)+glow(-200,420,520,0.12))

# 02 conceito
grid=''.join(f'<line x1="{i}" y1="-4" x2="{i}" y2="68" stroke="rgba(255,255,255,0.10)" stroke-width="0.15"></line><line x1="-4" y1="{i}" x2="68" y2="{i}" stroke="rgba(255,255,255,0.10)" stroke-width="0.15"></line>' for i in range(0,65,4))
csym=(f'<rect width="64" height="64" fill="{CARD}"></rect><circle cx="19" cy="19" r="7" fill="{WHT}"></circle><circle cx="19" cy="45" r="7" fill="{WHT}"></circle><circle cx="45" cy="45" r="7" fill="{WHT}"></circle><circle cx="45" cy="19" r="9" fill="{LIME}"></circle><path d="M19 19 H45 M19 45 H45 M19 19 V45 M45 19 V45" stroke="{LIME}" stroke-opacity="0.6" stroke-width="0.3" stroke-dasharray="1 1" fill="none"></path>')
row=lambda k,v: f'<div style="display: flex; justify-content: space-between; gap: 16px; padding: 9px 0; border-bottom: 1px solid {BOR}; font-size: 14px; line-height: 20px"><span style="color: {MUT}">{k}</span><span style="font-variant-numeric: tabular-nums">{v}</span></div>'
page("Site-02-conceito.dc.html","Teste site · Conceito", head("02 · Conceito e construção")+f'''
<div style="position: relative; flex: 1; display: grid; grid-template-columns: 1fr 360px; gap: 64px; align-items: center">
<div style="display: flex; flex-direction: column; gap: 20px">
<h2 style="margin: 0; font-family: {H}; font-size: 40px; line-height: 48px; font-weight: 700; letter-spacing: -0.02em">Quatro pontos.<br><span style="color: {LIME}">Um deles sobe.</span></h2>
<p style="margin: 0; font-size: 16px; line-height: 25px; color: {MUT}; max-width: 540px">Os quatro pontos são as 4 métricas que a 4metrics organiza. O ponto verde, maior e no alto, é a métrica que sobe: a receita. Os pontos conversam com a malha de pontos do site, e o pingo do "i" repete o ponto verde.</p>
<div style="padding: 6px 0">{logo(48)}</div>
<div style="max-width: 540px">{row("Grade do símbolo","64 × 64 u")}{row("Pontos","raio 7 u · centros a 26 u · branco")}{row("Ponto verde","raio 9 u · canto de cima à direita")}{row("Logotipo","4metrics, sempre com m minúsculo")}</div>
</div>
<div style="padding: 0; border-radius: 20px; {GB}; line-height: 0"><svg width="360" height="360" viewBox="-4 -4 72 72" role="img" aria-label="Construção do símbolo">{csym}{grid}</svg></div>
</div>''', glows=glow(820,120,560,0.2))

# 03 versoes
def tile(content,bg,cap,sub,border=None):
    b=f"border: 1px solid {border};" if border else ""
    return f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="height: 196px; background: {bg}; {b} border-radius: 16px; display: flex; align-items: center; justify-content: center">{content}</div><p style="margin: 0; font-size: 14px; line-height: 20px"><span style="font-weight: 600">{cap}</span> <span style="color: {MUT}">· {sub}</span></p></div>'
vert=f'<span style="display: inline-flex; flex-direction: column; align-items: center; gap: 14px">{sym(64)}{WORD(32,WHT)}</span>'
fav=lambda src_dark: (f'<span style="display: inline-flex; gap: 18px; align-items: center">'
  f'<span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="background: #FFFFFF; border-radius: 14px; line-height: 0; border: 1px solid #E1E7E4">{SYM(56,container="#FFFFFF",dots=NAVY,accent=LIME)}</span><span style="font-size: 11px; color: {MUT}">app claro</span></span>'
  f'<span style="display: flex; flex-direction: column; align-items: center; gap: 6px">{SYM(56,container=NAVY,dots=WHT,accent=LIME)}<span style="font-size: 11px; color: {MUT}">app escuro</span></span>'
  f'<span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="display: inline-flex; gap: 8px; padding: 8px; border-radius: 8px; background: #FFFFFF">{SYM(16,dots=NAVY,accent=LIME)}</span><span style="font-size: 11px; color: {MUT}">favicon claro</span></span>'
  f'<span style="display: flex; flex-direction: column; align-items: center; gap: 6px"><span style="display: inline-flex; padding: 8px; border-radius: 8px; background: #202124">{SYM(16,dots=WHT,accent=LIME)}</span><span style="font-size: 11px; color: {MUT}">favicon escuro</span></span></span>')
T=[tile(logo(56,ink=INKL,idot=LIME),WHT,"Principal · tema claro","plataforma, propostas, documentos"),
 tile(logo(56),CARD,"Tema escuro","site, redes e capas",BOR),
 tile(logo(56,ink=NAVY,idot=NAVY,dots=NAVY,accent=WHT),LIME,"Sobre verde","faixas e destaques em verde"),
 tile(vert,CARD,"Vertical","espaços quadrados e altos",BOR),
 tile(fav(1),CARD,"Ícone de app e favicon","versão clara (principal) e escura",BOR),
 tile(f'<span style="display: inline-flex; flex-direction: column; gap: 20px; align-items: center">{WORD(52,WHT)}{WORD(28,WHT)}</span>',CARD,"Só o nome","rodapé, e-mail, canto de post",BOR)]
page("Site-03-versoes.dc.html","Teste site · Versões", head("03 · Versões")+h2("Versões do logo")+f'<div style="position: relative; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px 16px">{"".join(T)}</div>')

# 04 cores
def blk(name,hx,use,bg,fg,flex,border=False):
    b=f"border: 1px solid {BOR};" if border else ""
    return f'<div style="flex: {flex}; background: {bg}; {b} color: {fg}; border-radius: 16px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; min-width: 0"><p style="margin: 0; font-family: {H}; font-size: 17px; font-weight: 700">{name}</p><div style="font-size: 12px; line-height: 18px; font-variant-numeric: tabular-nums"><div style="font-weight: 600">{hx}</div><div style="margin-top: 6px; opacity: 0.85">{use}</div></div></div>'
blocks="".join([blk("Azul-noite","#05131C","Fundo do site. Nunca preto puro.",NAVY,WHT,1.4,True),
 blk("Card","#14232C","Cards e blocos sobre o fundo.",CARD,WHT,1.1,True),
 blk("Borda","#2B3640","Bordas e divisões finas.",BOR,WHT,1.0),
 blk("Verde 4metrics","#92C549","Destaque, botão principal, palavra-chave.",LIME,NAVY,1.4),
 blk("Branco","#FFFFFF","Texto e seções brancas no meio da página.",WHT,NAVY,1.1)])
prop="".join(f'<div style="flex: {p}; background: {c}; {"border: 1px solid "+BOR+";" if c in (NAVY,CARD) else ""}"></div>' for p,c in [(55,NAVY),(18,CARD),(17,WHT),(10,LIME)])
page("Site-04-cores.dc.html","Teste site · Cores", head("04 · Cores")+h2("Paleta do site")+f'''
<div style="position: relative; display: flex; gap: 12px; height: 250px">{blocks}</div>
<div style="position: relative; display: grid; grid-template-columns: 1fr 1fr; gap: 32px">
<div style="display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 14px; font-weight: 600">Proporção de uso</p><div style="display: flex; height: 24px; border-radius: 999px; overflow: hidden">{prop}</div><p style="margin: 0; font-size: 12px; color: {MUT}">azul-noite 55% · card 18% · branco 17% · verde 10%</p></div>
<div style="display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 14px; font-weight: 600">Texto</p><p style="margin: 0; font-size: 13px; line-height: 20px; color: {MUT}">Principal em branco. Secundário em #9AA7B0. Sobre o verde, texto sempre em azul-noite. Nas seções brancas, texto em #05131C.</p></div></div>''', glows=glow(900,380,500,0.16))

# 05 tipografia
st=lambda name,spec,sample,css: f'<div style="display: grid; grid-template-columns: 200px 1fr; gap: 24px; align-items: baseline; padding: 10px 0; border-bottom: 1px solid {BOR}"><span style="font-size: 12px; color: {MUT}">{name} · {spec}</span><span style="{css}">{sample}</span></div>'
rows="".join([st("Display · Jakarta","56/60 · 700","Receita com dado.",f"font-family: {H}; font-size: 56px; line-height: 60px; font-weight: 700; letter-spacing: -0.02em"),
 st("H1 · Jakarta","36/44 · 700","Você só acessa. A gente constrói o resto.",f"font-family: {H}; font-size: 34px; line-height: 42px; font-weight: 700; letter-spacing: -0.01em"),
 st("H2 · Jakarta","24/32 · 600","Receita por canal",f"font-family: {H}; font-size: 24px; line-height: 32px; font-weight: 600"),
 st("Corpo · Inter","16/24 · 400","A 4metrics integra vendas, marketing e CRM e entrega o BI pronto.","font-size: 16px; line-height: 24px"),
 st("Rótulo · Inter","13/18 · 500","Receita do mês",f"font-size: 13px; line-height: 18px; font-weight: 500; color: {MUT}")])
page("Site-05-tipografia.dc.html","Teste site · Tipografia", head("05 · Tipografia")+f'''
<div style="position: relative; display: grid; grid-template-columns: 1fr 320px; gap: 40px; flex: 1">
<div>{h2("Plus Jakarta Sans + Inter")}<div style="margin-top: 8px">{rows}</div></div>
<div style="display: flex; flex-direction: column; gap: 16px; padding-top: 52px">
{cardbox(f'<div style="padding: 24px; display: flex; flex-direction: column; gap: 6px"><span style="font-size: 13px; font-weight: 500; color: {MUT}">Receita do mês</span><span style="font-family: {H}; font-size: 40px; line-height: 44px; font-weight: 700; letter-spacing: -0.02em; font-variant-numeric: tabular-nums">R$ 1,24 mi</span><span style="font-size: 13px; font-weight: 600; color: {LIME}">▲ +12,4% <span style="font-weight: 400; color: {MUT}">vs. out</span></span></div>', GB)}
<p style="margin: 0; font-size: 14px; line-height: 21px; color: {MUT}">Títulos em Plus Jakarta Sans 600/700. Texto em Inter. Números com algarismos tabulares (tabular-nums).</p>
<p style="margin: 0; font-size: 14px; line-height: 21px; color: {MUT}">Uma palavra-chave do título pode ficar em verde.</p></div></div>''')

# 06 formas e efeitos
fx=lambda t,d,demo: f'<div style="display: flex; flex-direction: column; gap: 10px">{demo}<p style="margin: 0; font-size: 14px; font-weight: 600">{t}</p><p style="margin: 0; font-size: 13px; line-height: 19px; color: {MUT}">{d}</p></div>'
d_glow=f'<div style="position: relative; height: 150px; border-radius: 16px; background: {CARD}; border: 1px solid {BOR}; overflow: hidden">{glow(40,-40,240,0.35)}</div>'
d_dots=f'<div style="height: 150px; border-radius: 16px; background-color: {CARD}; border: 1px solid {BOR}; background-image: radial-gradient(rgba(255,255,255,0.18) 1px, transparent 1.3px); background-size: 16px 16px"></div>'
d_gb=f'<div style="height: 150px; border-radius: 16px; background: {CARD}; {GB}; display: flex; align-items: center; justify-content: center; font-size: 14px; font-weight: 600">Card em destaque</div>'
d_line=f'<div style="height: 150px; border-radius: 16px; background: {CARD}; border: 1px solid {BOR}; display: flex; align-items: center; justify-content: center"><svg width="220" height="80" viewBox="0 0 220 80" aria-hidden="true"><path d="M10 60 C 60 60, 70 20, 110 20 S 170 50, 210 30" fill="none" stroke="{BOR}" stroke-width="2"></path><path d="M10 60 C 60 60, 70 20, 110 20" fill="none" stroke="{LIME}" stroke-width="2" stroke-linecap="round" style="filter: drop-shadow(0 0 4px rgba(146,197,73,0.8))"></path><circle cx="110" cy="20" r="5" fill="{LIME}"></circle></svg></div>'
comps=f'<div style="display: flex; align-items: center; gap: 12px; flex-wrap: wrap">{btn("Agendar diagnóstico")}{btn("Ver como funciona",bg="transparent",fg=WHT,bd=BOR)}{pill("Revenue Intelligence")}{pill("CRM · Marketing · Vendas",bg=CARD,fg=MUT,bd=BOR)}</div>'
page("Site-06-efeitos.dc.html","Teste site · Formas e efeitos", head("06 · Formas, componentes e efeitos")+h2("Formas, componentes e efeitos")+f'''
<div style="position: relative">{comps}</div>
<div style="position: relative; display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px">
{fx("Brilho verde","Manchas de luz atrás de títulos e do diagrama. Uma ou duas por tela, nunca sobre texto.",d_glow)}
{fx("Malha de pontos","Textura de fundo bem sutil (pontos brancos a 9% de opacidade).",d_dots)}
{fx("Borda com brilho","Só no card ou plano em destaque. Os outros usam borda #2B3640.",d_gb)}
{fx("Linha animada","Linhas do diagrama acendem em verde, devagar. Param com 'menos movimento'.",d_line)}
</div>
<p style="position: relative; margin: 0; font-size: 13px; color: {MUT}">Cantos: botões 8 px · cards 16 px · etiquetas em pílula. Toda animação respeita prefers-reduced-motion.</p>''', glows=glow(980,-80,420,0.16))

# 07 aplicacoes
hero=f'''<div style="position: relative; height: 360px; border-radius: 16px; overflow: hidden; background-color: {NAVY}; {DOTS}; border: 1px solid {BOR}; padding: 28px; box-sizing: border-box; display: flex; flex-direction: column; gap: 18px">
{glow(380,-60,360,0.3)}
<div style="position: relative; display: flex; justify-content: space-between; align-items: center">{logo(26)}<span style="display: flex; gap: 18px; font-size: 13px; color: {MUT}">Plataforma<span>Como funciona</span><span>Cases</span></span>{btn("Agendar diagnóstico",h=34,fs=13)}</div>
<div style="position: relative; margin-top: 18px">{pill("Revenue Intelligence")}</div>
<h3 style="position: relative; margin: 0; font-family: {H}; font-size: 34px; line-height: 40px; font-weight: 700; letter-spacing: -0.02em; max-width: 420px">Você só acessa.<br><span style="color: {LIME}">A gente constrói o resto.</span></h3>
<p style="position: relative; margin: 0; font-size: 14px; line-height: 21px; color: {MUT}; max-width: 400px">Dados de vendas, marketing e CRM integrados, com BI pronto dentro da plataforma.</p>
<div style="position: relative">{btn("Agendar diagnóstico")}</div></div>'''
white=f'''<div style="height: 170px; border-radius: 16px; background: {WHT}; color: {INKL}; padding: 22px; box-sizing: border-box; display: flex; flex-direction: column; gap: 10px">
<span style="font-size: 12px; font-weight: 600; color: #4F7A1F">Como funciona</span><h4 style="margin: 0; font-family: {H}; font-size: 22px; line-height: 28px; font-weight: 700">Fundação, Inteligência e Agentes de IA.</h4><p style="margin: 0; font-size: 13px; line-height: 19px; color: {MUTL}">Seção branca no meio da página, para dar respiro.</p></div>'''
post=f'''<div style="position: relative; height: 170px; border-radius: 16px; overflow: hidden; background-color: {NAVY}; {DOTS}; border: 1px solid {BOR}; padding: 20px; box-sizing: border-box; display: flex; flex-direction: column; justify-content: space-between">{glow(150,-40,220,0.3)}
<span style="position: relative; font-family: {H}; font-size: 20px; line-height: 25px; font-weight: 700">Seu CRM tem <span style="color: {LIME}">R$ 86 mil</span> parados no funil.</span><span style="position: relative">{WORD(14,WHT)}</span></div>'''
page("Site-07-aplicacoes.dc.html","Teste site · Aplicações", head("07 · Aplicações")+f'''
<div style="position: relative; display: grid; grid-template-columns: 1.35fr 1fr; gap: 16px; flex: 1">
<div style="display: flex; flex-direction: column; gap: 8px">{hero}<p style="margin: 0; font-size: 14px; font-weight: 600">Topo do site</p></div>
<div style="display: flex; flex-direction: column; gap: 16px">
<div style="display: flex; flex-direction: column; gap: 8px">{white}<p style="margin: 0; font-size: 14px; font-weight: 600">Seção branca</p></div>
<div style="display: flex; flex-direction: column; gap: 8px">{post}<p style="margin: 0; font-size: 14px; font-weight: 600">Post de rede social</p></div></div></div>''')

# 00 resumo
sec=lambda n,t: f'<p style="margin: 0 0 14px; font-size: 11px; color: {MUT}">{n} · {t}</p>'
hr=f'<div style="height: 1px; background: {BOR}; margin: 24px 0"></div>'
def t1(c,bg,cap,bd=None):
    b=f"border: 1px solid {bd};" if bd else ""
    return f'<div><div style="height: 160px; background: {bg}; {b} border-radius: 16px; display: flex; align-items: center; justify-content: center">{c}</div><p style="margin: 8px 0 0; font-size: 11px; color: {MUT}">{cap}</p></div>'
def sw(n,hx,u,bd=False):
    b=f"border: 1px solid {BOR};" if bd else ""
    return f'<div><div style="height: 90px; background: {hx}; {b} border-radius: 12px"></div><p style="margin: 10px 0 0; font-size: 12px; font-weight: 600">{n}</p><p style="margin: 2px 0 0; font-size: 10px; line-height: 15px; color: {MUT}">{hx}<br>{u}</p></div>'
dot=lambda: f'<span style="flex: none; width: 8px; height: 8px; border-radius: 999px; background: {LIME}; margin-top: 6px; box-shadow: 0 0 8px rgba(146,197,73,0.7)"></span>'
rule=lambda t: f'<div style="display: flex; gap: 10px; font-size: 13px; line-height: 20px">{dot()}<span>{t}</span></div>'
body=f'''<div style="position: relative; display: flex; justify-content: space-between; align-items: center">{logo(28)}<span style="font-size: 10px; color: {MUT}">Manual de identidade visual · teste site</span></div>
<div style="position: relative"><h1 style="margin: 16px 0 0; font-family: {H}; font-size: 50px; line-height: 54px; font-weight: 700; letter-spacing: -0.03em">4metrics</h1>
<p style="margin: 8px 0 0; font-size: 14px; line-height: 20px; color: {MUT}">Revenue Intelligence para times comerciais e de marketing. Software com serviço.</p></div>
<div style="position: relative">{hr}{sec("01","Logo")}
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px">{t1(logo(34),CARD,"Principal: azul-noite",BOR)}{t1(logo(34,ink=INKL,idot="#92C549"),WHT,"Seções brancas")}{t1(sym(56),CARD,"Símbolo: favicon, app e avatar",BOR)}</div>
<p style="margin: 20px 0 0; font-size: 15px; line-height: 22px; font-weight: 500">Quatro pontos, quatro métricas. <span style="color: {LIME}">O verde é a que sobe.</span></p>
{hr}{sec("02","Cores")}
<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px">{sw("Azul-noite",NAVY,"fundo",True)}{sw("Card",CARD,"cards",True)}{sw("Borda",BOR,"bordas")}{sw("Verde 4metrics",LIME,"destaque")}{sw("Branco",WHT,"texto e seções")}</div>
<p style="margin: 16px 0 0; font-size: 13px; line-height: 20px; color: {MUT}">Uso: fundo azul-noite, nunca preto puro. Verde só para destaque e botão. Seções brancas para dar respiro.</p>
{hr}{sec("03","Tipografia")}
<div style="display: grid; grid-template-columns: 240px 1fr; gap: 24px; align-items: end">
<div><p style="margin: 0; font-family: {H}; font-size: 100px; line-height: 92px; font-weight: 700; letter-spacing: -0.04em">Aa</p><p style="margin: 10px 0 0; font-family: {H}; font-size: 17px; font-weight: 700">Plus Jakarta Sans <span style="font-family: {B}; font-weight: 500; color: {MUT}">+ Inter</span></p><p style="margin: 2px 0 0; font-size: 11px; color: {MUT}">Títulos 600/700 · Texto Inter 400/500</p></div>
<div style="display: flex; flex-direction: column; gap: 6px"><p style="margin: 0; font-family: {H}; font-size: 28px; line-height: 34px; font-weight: 700; letter-spacing: -0.02em">O dado certo, na hora da <span style="color: {LIME}">decisão.</span></p>
<p style="margin: 0; font-family: {H}; font-size: 19px; font-weight: 700">Título 1 · 36/44</p><p style="margin: 0; font-family: {H}; font-size: 15px; font-weight: 600">Título 2 · 24/32</p>
<p style="margin: 4px 0 0; font-size: 11px">Corpo · 16/24 · A 4metrics integra vendas, marketing e CRM e entrega o BI pronto.</p><p style="margin: 0; font-size: 10px; color: {MUT}">Pequeno · 14/20 · Texto secundário e legendas</p></div></div>
{hr}{sec("04","Componentes e efeitos")}
<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap">{btn("Agendar diagnóstico",h=36,fs=13)}{btn("Ver como funciona",bg="transparent",fg=WHT,bd=BOR,h=36,fs=13)}{pill("Revenue Intelligence")}{pill("Novo",bg=LIME,fg=NAVY,bd=LIME)}</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 18px">
<div style="position: relative; overflow: hidden; background: {CARD}; border: 1px solid {BOR}; border-radius: 16px; padding: 16px">{glow(180,-80,220,0.25)}<p style="position: relative; margin: 0; font-size: 10px; font-weight: 600; color: {LIME}">Insight do agente</p><p style="position: relative; margin: 6px 0 0; font-size: 13px; line-height: 19px; font-weight: 500">R$ 86 mil parados no funil. Priorize os 10 maiores negócios esta semana.</p></div>
<div style="background: {CARD}; {GB}; border-radius: 16px; padding: 16px; display: flex; justify-content: space-between; align-items: flex-end"><div><p style="margin: 0; font-size: 10px; font-weight: 500; color: {MUT}">Receita do mês</p><p style="margin: 4px 0 0; font-family: {H}; font-size: 24px; font-weight: 700; font-variant-numeric: tabular-nums">R$ 1,24 mi</p></div><span style="font-size: 11px; font-weight: 600; color: {LIME}">▲ +12,4%</span></div></div>
<p style="margin: 22px 0 0; font-family: {H}; font-size: 26px; line-height: 34px; font-weight: 700; letter-spacing: -0.02em">Receita com dado, não com <span style="color: {LIME}">achismo.</span></p>
<p style="margin: 6px 0 0; font-size: 10px; color: {MUT}">Botão · Pílula · Card · Card com brilho · Brilho verde · Malha de pontos</p>
{hr}{sec("05","Regras")}
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px 32px">{rule("Fundo azul-noite #05131C, nunca preto puro.")}{rule("Verde só como destaque: botão, palavra-chave, número.")}{rule("Brilho e malha de pontos sutis, nunca atrás de texto.")}{rule("Borda com brilho só no card em destaque.")}{rule("Animações suaves; param com 'menos movimento'.")}{rule("4metrics sempre com m minúsculo.")}</div></div>
<div style="flex: 1"></div>
<div style="position: relative; display: flex; justify-content: space-between; align-items: center"><span style="display: inline-flex; align-items: center; gap: 10px">{sym(24)}<span style="font-family: {H}; font-size: 15px; font-weight: 700">Você só acessa. A gente constrói o resto.</span></span><span style="font-size: 10px; color: {MUT}">4metrics.com.br</span></div>'''
page("Site-00-resumo.dc.html","Teste site · Resumo", body, w=900, h=1580, glows=glow(420,-120,520,0.2)+glow(-160,900,420,0.12))
print("ok")

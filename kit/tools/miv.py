import sys; sys.path.insert(0,"/home/claude/tools"); from page import *
import os; os.chdir("/home/claude/dz/project")
LIME,BLK,CARD,WHT,DINK,DMUT="#92C549","#0A0A0A","#1A1A1A","#FFFFFF","#F5F5F5","#A3A3A3"
INK,MUT,SUB,BOR,G600,G800,G100="#141712","#5D6358","#F5F7F2","#E3E7DE","#6D9E15","#406500","#E6F4D8"
H2=lambda t: f'<h2 style="margin: 0; font-size: 24px; line-height: 32px; font-weight: 600">{t}</h2>'
# 01 capa
big=(f'<svg width="340" height="340" viewBox="0 0 64 64" aria-hidden="true"><circle cx="19" cy="19" r="7" fill="{WHT}"></circle><circle cx="19" cy="45" r="7" fill="{WHT}"></circle><circle cx="45" cy="45" r="7" fill="{WHT}"></circle><circle cx="45" cy="19" r="9" fill="{LIME}"></circle></svg>')
page("MIV-01-capa.dc.html","MIV · Capa", HEAD("Capa","",dark=True)+f'''
<div style="flex: 1; display: flex; justify-content: space-between; align-items: flex-end">
<div style="display: flex; flex-direction: column; gap: 32px">{LOGO(72, ink=WHT)}
<div><h1 style="margin: 0; font-size: 56px; line-height: 60px; font-weight: 600; letter-spacing: -0.02em; color: {LIME}">Manual de<br>Identidade Visual</h1>
<p style="margin: 16px 0 0; font-size: 16px; line-height: 24px; color: {DMUT}; max-width: 520px">Logo, cores, tipografia e aplicações da 4metrics. Revenue Intelligence para times comerciais e de marketing.</p></div></div>
{big}</div>''', bg=BLK, ink=WHT)
# 02 conceito
grid=''.join(f'<line x1="{i}" y1="-4" x2="{i}" y2="68" stroke="#C9CFC4" stroke-width="0.15"></line><line x1="-4" y1="{i}" x2="68" y2="{i}" stroke="#C9CFC4" stroke-width="0.15"></line>' for i in range(0,65,4))
sym=(f'<circle cx="19" cy="19" r="7" fill="{INK}"></circle><circle cx="19" cy="45" r="7" fill="{INK}"></circle><circle cx="45" cy="45" r="7" fill="{INK}"></circle><circle cx="45" cy="19" r="9" fill="{G600}"></circle><path d="M19 19 H45 M19 45 H45 M19 19 V45 M45 19 V45" stroke="#D06A4C" stroke-width="0.3" stroke-dasharray="1 1" fill="none"></path>')
svg=f'<svg width="360" height="360" viewBox="-4 -4 72 72" role="img" aria-label="Construção do símbolo sobre grade de 64 unidades">{sym}{grid}</svg>'
def row(k,v): return f'<div style="display: flex; justify-content: space-between; gap: 16px; padding: 9px 0; border-bottom: 1px solid {BOR}; font-size: 14px; line-height: 20px"><span style="color: {MUT}">{k}</span><span style="font-family: \'Geist Mono\', monospace">{v}</span></div>'
page("MIV-02-conceito.dc.html","MIV · Conceito e construção", HEAD("02 · Conceito e construção","")+f'''
<div style="flex: 1; display: grid; grid-template-columns: 1fr 360px; gap: 64px; align-items: center">
<div style="display: flex; flex-direction: column; gap: 20px">
<h2 style="margin: 0; font-size: 36px; line-height: 44px; font-weight: 600; letter-spacing: -0.01em">Quatro pontos.<br>Um deles sobe.</h2>
<p style="margin: 0; font-size: 16px; line-height: 24px; color: {MUT}; max-width: 540px">Os quatro pontos são as 4 métricas que a 4metrics organiza para o cliente. O ponto verde, maior e no alto, é a métrica que sobe: a receita, o resultado da decisão. No nome, o pingo do "i" repete esse ponto verde. Símbolo e nome contam a mesma história, juntos ou separados.</p>
<div style="padding: 8px 0">{LOGO(48)}</div>
<div style="max-width: 540px">{row("Grade do símbolo","64 × 64 u")}{row("Pontos","raio 7 u · centros a 26 u · grafite ou branco")}{row("Ponto verde","raio 9 u · canto de cima à direita")}{row("Logotipo","Geist 600 · −0,03 em · minúsculas")}{row("Pingo do i","verde 600 no claro, lima no escuro")}</div>
</div>{svg}</div>''')
# 03 versoes
def tile(content,bg,cap,sub,border=False):
    b=f"border: 1px solid {BOR};" if border else ""
    return f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="height: 196px; background: {bg}; {b} border-radius: 8px; display: flex; align-items: center; justify-content: center">{content}</div><p style="margin: 0; font-size: 14px; line-height: 20px"><span style="font-weight: 600">{cap}</span> <span style="color: {MUT}">· {sub}</span></p></div>'
vert=f'<span style="display: inline-flex; flex-direction: column; align-items: center; gap: 14px">{SYM(64)}{WORD(32)}</span>'
T=[tile(LOGO(56),WHT,"Principal (símbolo + nome)","fundo claro, plataforma e documentos",True),
 tile(LOGO(56,ink=WHT),BLK,"Negativa","fundo preto, marca e redes sociais"),
 tile(LOGO(56,ink=BLK,idot=BLK,dots=BLK,accent=WHT),LIME,"Sobre lima","fundo da cor da marca"),
 tile(vert,SUB,"Vertical","espaços quadrados e altos"),
 tile(f'<span style="display: inline-flex; gap: 24px; align-items: flex-end">{SYM(96)}{SYM(48)}{SYM(24)}{SYM(48,container=BLK,dots=WHT,accent=LIME)}</span>',SUB,"Símbolo","favicon e menu; o último é o ícone de app"),
 tile(f'<span style="display: inline-flex; flex-direction: column; gap: 20px; align-items: center">{WORD(52)}{WORD(28)}</span>',WHT,"Só o nome","rodapé, e-mail, documentos",True)]
page("MIV-03-versoes.dc.html","MIV · Versões", HEAD("03 · Versões","")+H2("Versões do logo")+f'<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 24px 16px">{"".join(T)}</div>')
# 03b uso
def use(where,what,demo,bg=SUB):
    return f'<div style="display: grid; grid-template-columns: 220px 1fr; gap: 16px; align-items: center; padding: 10px 0; border-bottom: 1px solid {BOR}"><div style="height: 64px; background: {bg}; border-radius: 8px; display: flex; align-items: center; justify-content: center">{demo}</div><div><p style="margin: 0; font-size: 15px; line-height: 22px; font-weight: 600">{where}</p><p style="margin: 0; font-size: 14px; line-height: 20px; color: {MUT}">{what}</p></div></div>'
dot=lambda c=LIME,s=9: f'<span style="display: inline-block; width: {s}px; height: {s}px; border-radius: 999px; background: {c}"></span>'
lst="".join(f'<span style="display: inline-flex; align-items: center; gap: 8px">{dot()}{t}</span>' for t in ["Fundação","Inteligência"])
c1="".join([use("1 · Logo completo (principal)","Use sempre que houver espaço: site, plataforma, propostas, slides, cartão, eventos. É a assinatura padrão.",LOGO(30),WHT),
 use("2 · Só o símbolo","Só em espaço quadrado ou pequeno, onde o nome já aparece perto: favicon, app, avatar do perfil 4metrics, menu recolhido.",f'<span style="display: inline-flex; gap: 12px; align-items: center">{SYM(40)}{SYM(24)}{SYM(16)}</span>'),
 use("3 · Só o nome","Uso de apoio, quando o símbolo já está na peça ou não cabe: rodapé, assinatura de e-mail, canto de post.",WORD(26),WHT)])
c2="".join([use("O ponto como grafismo","O ponto lima marca o número-chave: fim de linha num gráfico, item de lista, destaque num post.",f'<svg width="160" height="48" viewBox="0 0 160 48" aria-hidden="true"><polyline points="8,40 48,32 88,34 128,14" fill="none" stroke="{G800}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"></polyline><circle cx="136" cy="12" r="7" fill="{LIME}" stroke="{BLK}" stroke-width="1.5"></circle></svg>',WHT),
 use("Lista com ponto","Use o ponto no lugar do marcador comum em listas, no escuro e no claro.",f'<span style="display: flex; flex-direction: column; gap: 6px; font-size: 13px; color: {WHT}">{lst}</span>',BLK),
 use("Regra","Use uma marca por peça: o logo completo, ou só o símbolo, ou só o nome. Não repita os dois soltos na mesma peça.",f'<span style="font-size: 13px; color: {G800}; font-weight: 600">1 marca por peça</span>',G100)])
page("MIV-03b-uso.dc.html","MIV · Quando usar cada versão", HEAD("03b · Quando usar cada versão","")+H2("Ordem de uso: logo completo primeiro")+f'<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px"><div>{c1}</div><div>{c2}</div></div>')
# 04 protecao
def bad(content,bg,cap):
    return f'<div style="display: flex; flex-direction: column; gap: 8px"><div style="height: 132px; background: {bg}; border: 1px solid {BOR}; border-radius: 8px; display: flex; align-items: center; justify-content: center; overflow: hidden">{content}</div><p style="margin: 0; font-size: 14px; line-height: 20px"><span style="color: #B42318; font-weight: 600">✕ Não</span> <span style="color: {MUT}">{cap}</span></p></div>'
bads=[bad(f'<span style="display: inline-block; transform: scaleX(1.45)">{LOGO(36)}</span>',WHT,"distorcer ou esticar"),
 bad(LOGO(36,bg="#2F6BD8",bar=WHT,last="#F2B544",idot="#F2B544"),WHT,"trocar as cores"),
 bad(f'<span style="display: inline-flex; align-items: center; gap: 9px">{WORD(22)}{SYM(36)}</span>',WHT,"inverter a ordem"),
 bad(LOGO(36,ink=WHT,bar=WHT,idot=WHT),LIME,"branco sobre lima")]
prot=f'''<div style="position: relative; padding: 32px; border: 1px dashed {G800}; display: inline-block"><div style="outline: 1px solid {BOR}">{LOGO(64)}</div>
<span style="position: absolute; top: 8px; left: 50%; font-family: 'Geist Mono', monospace; font-size: 13px; color: {G800}">x</span><span style="position: absolute; left: 10px; top: 50%; font-family: 'Geist Mono', monospace; font-size: 13px; color: {G800}">x</span></div>'''
mono=lambda t: f'<span style="font-family: \'Geist Mono\', monospace; font-size: 13px; color: {MUT}">{t}</span>'
page("MIV-04-protecao.dc.html","MIV · Área de proteção e usos", HEAD("04 · Área de proteção e usos","")+f'''
<div style="display: grid; grid-template-columns: 1.1fr 0.9fr; gap: 48px">
<div style="display: flex; flex-direction: column; gap: 16px">{H2("Área de proteção")}
<p style="margin: 0; font-size: 14px; line-height: 20px; color: {MUT}; max-width: 520px">Deixe livre, em volta do logo, um espaço x igual à metade da altura do símbolo. Nenhum texto, imagem ou borda entra nessa área.</p><div>{prot}</div></div>
<div style="display: flex; flex-direction: column; gap: 16px">{H2("Tamanho mínimo")}
<div style="display: flex; gap: 32px; align-items: flex-end; padding: 16px 0">
<div style="display: flex; flex-direction: column; gap: 8px">{LOGO(24)}{mono("logo · 24 px / 8 mm")}</div>
<div style="display: flex; flex-direction: column; gap: 8px">{SYM(16)}{mono("símbolo · 16 px / 5 mm")}</div>
<div style="display: flex; flex-direction: column; gap: 8px">{WORD(14)}{mono("nome · 14 px")}</div></div>
<p style="margin: 0; font-size: 14px; line-height: 20px; color: {MUT}">Abaixo de 24 px de altura, use só o símbolo. Texto sobre o lima é sempre preto.</p></div></div>
<div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px">{"".join(bads)}</div>''')
# 05 cores
def blk(name,hexv,rgb,cmyk,use,bg,fg,flex,border=False):
    b=f"border: 1px solid {BOR};" if border else ""
    return f'<div style="flex: {flex}; background: {bg}; {b} color: {fg}; border-radius: 8px; padding: 20px; display: flex; flex-direction: column; justify-content: space-between; min-width: 0"><p style="margin: 0; font-size: 17px; line-height: 24px; font-weight: 600">{name}</p><div style="font-family: \'Geist Mono\', monospace; font-size: 12px; line-height: 18px"><div>{hexv}</div><div>RGB {rgb}</div><div>CMYK {cmyk}</div><div style="font-family: \'Geist\', sans-serif; margin-top: 8px; font-size: 12px">{use}</div></div></div>'
blocks="".join([blk("Verde 4metrics","#92C549","146 197 73","26 0 63 23","Símbolo, botão, title no escuro. Texto sobre ele: preto.",LIME,BLK,1.6),
 blk("Preto","#0A0A0A","10 10 10","0 0 0 96","Fundo da marca e das redes sociais.",BLK,WHT,1.1),
 blk("Grafite","#141712","20 23 18","13 0 22 91","Texto na plataforma e documentos.",INK,DINK,1.0),
 blk("Verde 800","#406500","64 101 0","37 0 100 60","Texto verde e links no fundo claro.",G800,WHT,1.0),
 blk("Névoa","#F5F7F2","245 247 242","1 0 2 3","Fundo de seções e dashboards.",SUB,INK,1.0,True)])
bar=lambda parts: "".join(f'<div style="flex: {p}; background: {c}; {"border: 1px solid "+BOR+";" if c in (WHT,SUB) else ""}"></div>' for p,c in parts)
chips="".join(f'<span style="display: inline-flex; align-items: center; gap: 8px; font-size: 13px"><span style="width: 16px; height: 16px; border-radius: 4px; background: {h}"></span><span style="font-family: \'Geist Mono\', monospace; color: {MUT}">{n} {h}</span></span>' for n,h in [("chart-2","#2F6BD8"),("chart-3","#0F7C8C"),("chart-4","#C97A06"),("delta-down","#B42318"),("focus","#2F6BD8")])
page("MIV-05-cores.dc.html","MIV · Cores", HEAD("05 · Cores","")+f'''
<div style="display: flex; justify-content: space-between; align-items: flex-end">{H2("Paleta principal")}<p style="margin: 0; font-size: 13px; color: {MUT}">CMYK aproximado. Confirme a referência Pantone com a gráfica.</p></div>
<div style="display: flex; gap: 12px; height: 260px">{blocks}</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 32px">
<div style="display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 14px; font-weight: 600">Modo escuro · marca e redes (paleta A)</p><div style="display: flex; height: 24px; border-radius: 4px; overflow: hidden">{bar([(60,BLK),(15,CARD),(13,WHT),(12,LIME)])}</div><p style="margin: 0; font-size: 12px; color: {MUT}; font-family: 'Geist Mono', monospace">preto 60% · card 15% · branco 13% · lima 12%</p></div>
<div style="display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 14px; font-weight: 600">Modo claro · plataforma (paleta B)</p><div style="display: flex; height: 24px; border-radius: 4px; overflow: hidden">{bar([(65,SUB),(20,INK),(10,LIME),(5,G800)])}</div><p style="margin: 0; font-size: 12px; color: {MUT}; font-family: 'Geist Mono', monospace">névoa/branco 65% · grafite 20% · lima 10% · verde 800 5%</p></div></div>
<div style="display: flex; flex-direction: column; gap: 8px"><p style="margin: 0; font-size: 14px; font-weight: 600">Apoio (gráficos e interface)</p><div style="display: flex; flex-wrap: wrap; gap: 24px">{chips}</div></div>''')
# 06 tipografia
def st(name,spec,sample,css): return f'<div style="display: grid; grid-template-columns: 180px 1fr; gap: 24px; align-items: baseline; padding: 10px 0; border-bottom: 1px solid {BOR}"><span style="font-family: \'Geist Mono\', monospace; font-size: 13px; color: {MUT}">{name} · {spec}</span><span style="{css}">{sample}</span></div>'
rows="".join([st("display","56/60 · 600","Receita com dado.","font-size: 56px; line-height: 60px; font-weight: 600; letter-spacing: -0.02em"),
 st("h1","36/44 · 600","Você só acessa. A gente constrói o resto.","font-size: 36px; line-height: 44px; font-weight: 600; letter-spacing: -0.01em"),
 st("h2","24/32 · 600","Receita por canal","font-size: 24px; line-height: 32px; font-weight: 600"),
 st("body","16/24 · 400","A 4metrics integra os dados de vendas, marketing e CRM e entrega o BI pronto.","font-size: 16px; line-height: 24px"),
 st("label","13/18 · 500","Receita do mês",f"font-size: 13px; line-height: 18px; font-weight: 500; color: {MUT}")])
page("MIV-06-tipografia.dc.html","MIV · Tipografia", HEAD("06 · Tipografia","")+f'''
<div style="display: grid; grid-template-columns: 1fr 340px; gap: 48px; flex: 1">
<div style="display: flex; flex-direction: column"><h2 style="margin: 0 0 8px; font-size: 24px; line-height: 32px; font-weight: 600">Geist · texto e títulos</h2>{rows}</div>
<div style="display: flex; flex-direction: column; gap: 16px">{H2("Geist Mono · números")}
<div style="background: {BLK}; border-radius: 8px; padding: 24px; display: flex; flex-direction: column; gap: 8px">
<span style="font-size: 13px; font-weight: 500; color: {DMUT}">Receita do mês</span>
<span style="font-family: 'Geist Mono', monospace; font-size: 40px; line-height: 44px; font-weight: 500; letter-spacing: -0.02em; color: {LIME}">R$ 1,24 mi</span>
<span style="font-family: 'Geist Mono', monospace; font-size: 13px; font-weight: 500; color: {LIME}">▲ +12,4% <span style="font-family: 'Geist', sans-serif; font-weight: 400; color: {DMUT}">vs. out</span></span></div>
<p style="margin: 0; font-size: 14px; line-height: 20px; color: {MUT}">Geist Mono só para números: KPIs, tabelas e eixos. Formato brasileiro: vírgula decimal, ponto de milhar.</p>
<p style="margin: 0; font-size: 14px; line-height: 20px; color: {MUT}">No escuro, o title e o número-chave podem ser lima. No claro, número em grafite e destaque com fundo lima.</p></div></div>''')
# 07 aplicacoes
cap=lambda t: f'<p style="margin: 8px 0 0; font-size: 14px; font-weight: 600">{t}</p>'
avatar=f'<div><div style="display: flex; gap: 16px; align-items: center; height: 200px; background: {SUB}; border-radius: 8px; justify-content: center"><div style="width: 120px; height: 120px; border-radius: 999px; background: {BLK}; display: flex; align-items: center; justify-content: center">{SYM(76,dots=WHT,accent=LIME)}</div><div style="width: 64px; height: 64px; border-radius: 999px; background: {BLK}; display: flex; align-items: center; justify-content: center">{SYM(40,dots=WHT,accent=LIME)}</div></div>{cap("Avatar de redes sociais · símbolo")}</div>'
card=f'''<div><div style="height: 200px; background: {SUB}; border-radius: 8px; display: flex; align-items: center; justify-content: center; gap: 16px">
<div style="width: 210px; height: 120px; background: {BLK}; border-radius: 6px; display: flex; align-items: center; justify-content: center">{LOGO(32,ink=WHT)}</div>
<div style="width: 210px; height: 120px; background: {WHT}; border: 1px solid {BOR}; border-radius: 6px; box-sizing: border-box; padding: 14px; display: flex; flex-direction: column; justify-content: space-between">
<div><p style="margin: 0; font-size: 13px; font-weight: 600">Gabriel Bastos</p><p style="margin: 0; font-size: 11px; color: {MUT}">Fundador</p></div>
<div style="font-size: 11px; line-height: 15px; color: {MUT}"><div style="font-family: 'Geist Mono', monospace">[SEU E-MAIL]</div><div>Instituto Caldeira · Porto Alegre/RS</div></div>{WORD(12)}</div></div>{cap("Cartão de visita · logo na frente, só o nome no verso")}</div>'''
nav=f'''<div style="grid-column: span 2"><div style="height: 200px; background: {SUB}; border-radius: 8px; padding: 24px; box-sizing: border-box; display: flex; flex-direction: column; gap: 16px">
<div style="background: {WHT}; border: 1px solid {BOR}; border-radius: 8px; height: 60px; padding: 0 20px; display: flex; align-items: center; justify-content: space-between">
<div style="display: flex; align-items: center; gap: 28px">{LOGO(28)}<span style="display: flex; gap: 20px; font-size: 14px; color: {MUT}; white-space: nowrap"><span style="color: {INK}; font-weight: 500">Dashboards</span><span>Agente de IA</span><span>Fontes</span></span></div>
<span style="background: {LIME}; color: {BLK}; font-size: 14px; font-weight: 500; padding: 8px 14px; border-radius: 8px; white-space: nowrap">Falar com o time</span></div>
<div style="display: flex; gap: 16px">
<div style="display: flex; align-items: center; gap: 8px; background: {WHT}; border: 1px solid {BOR}; border-radius: 8px 8px 0 0; padding: 8px 14px; font-size: 13px">{SYM(16)}<span>4metrics · Receita</span></div>
<div style="display: flex; align-items: center; gap: 8px; background: {BLK}; border-radius: 8px 8px 0 0; padding: 8px 14px; font-size: 13px; color: {DINK}">{SYM(16,dots=WHT,accent=LIME)}<span>4metrics · Receita</span></div></div></div>{cap("Plataforma (paleta B, botão lima) e favicon")}</div>'''
post=f'''<div style="grid-column: span 2"><div style="height: 200px; background: {SUB}; border-radius: 8px; display: flex; align-items: center; justify-content: center; gap: 16px">
<div style="width: 168px; height: 168px; background: {BLK}; border-radius: 6px; box-sizing: border-box; padding: 16px; display: flex; flex-direction: column; justify-content: space-between">
<span style="font-size: 17px; line-height: 21px; font-weight: 700; letter-spacing: -0.01em; color: {LIME}">Seu CRM tem R$ 86 mil parados no funil.</span>
<span style="display: flex; justify-content: space-between; align-items: center"><span style="font-size: 10px; color: {WHT}; border: 1px solid {WHT}; border-radius: 40px; padding: 2px 8px">Ver diagnóstico</span>{WORD(11,ink=WHT)}</span></div>
<div style="width: 168px; height: 168px; background: {WHT}; border: 1px solid {BOR}; border-radius: 6px; box-sizing: border-box; padding: 16px; display: flex; flex-direction: column; justify-content: space-between">
<span style="font-size: 17px; line-height: 21px; font-weight: 600; letter-spacing: -0.01em">Receita do mês: <span style="background: {LIME}; padding: 0 3px; border-radius: 3px">+12,4%</span></span>{WORD(13)}</div>
<div style="width: 168px; height: 168px; background: {LIME}; border-radius: 6px; box-sizing: border-box; padding: 16px; display: flex; flex-direction: column; justify-content: space-between">
<span style="font-size: 17px; line-height: 21px; font-weight: 600; color: {BLK}; letter-spacing: -0.01em">Você só acessa. A gente constrói o resto.</span>{SYM(24,dots=BLK,accent=WHT)}</div>
</div>{cap("Posts · escuro (A), claro (B) e lima")}</div>'''
page("MIV-07-aplicacoes.dc.html","MIV · Aplicações", HEAD("07 · Aplicações","")+H2("Aplicações")+f'<div style="display: grid; grid-template-columns: 1fr 1fr 1fr 1fr; gap: 24px 16px"><div style="grid-column: span 2">{avatar}</div><div style="grid-column: span 2">{card}</div>{nav}{post}</div>')
print("ok")

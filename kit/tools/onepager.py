import sys; sys.path.insert(0,"/home/claude/tools"); from page import *
import os, json; os.chdir("/home/claude/dz/project")
LIME,BLK,CARD,WHT,INK,MUT,SUB,BOR,G600,G800,G100="#92C549","#0A0A0A","#1A1A1A","#FFFFFF","#141712","#5D6358","#F5F7F2","#E3E7DE","#6D9E15","#406500","#E6F4D8"
W,Hh=900,1620
sec=lambda n,t: f'<p style="margin: 0 0 14px; font-size: 11px; line-height: 16px; color: {MUT}">{n} · {t}</p>'
hr=f'<div style="height: 1px; background: {BOR}; margin: 24px 0"></div>'
def tile(content,bg,cap,border=True):
    b=f"border: 1px solid {BOR};" if border else ""
    return f'<div><div style="height: 168px; background: {bg}; {b} border-radius: 6px; display: flex; align-items: center; justify-content: center">{content}</div><p style="margin: 8px 0 0; font-size: 11px; line-height: 16px; color: {MUT}">{cap}</p></div>'
def sw(name,hx,token,bg=None,border=False):
    b=f"border: 1px solid {BOR};" if border else ""
    return f'<div><div style="height: 96px; background: {hx}; {b} border-radius: 6px"></div><p style="margin: 10px 0 0; font-size: 12px; line-height: 16px; font-weight: 600">{name}</p><p style="margin: 2px 0 0; font-family: \'Geist Mono\', monospace; font-size: 10px; line-height: 15px; color: {MUT}">{hx}<br>{token}</p></div>'
btn=lambda t,bg,fg,bd: f'<span style="display: inline-flex; align-items: center; height: 32px; padding: 0 16px; border-radius: 8px; background: {bg}; color: {fg}; border: 1px solid {bd}; font-size: 12px; font-weight: 500; white-space: nowrap">{t}</span>'
badge=lambda t,bg,fg,bd: f'<span style="display: inline-flex; align-items: center; height: 20px; padding: 0 7px; border-radius: 4px; background: {bg}; color: {fg}; border: 1px solid {bd}; font-size: 10px; font-weight: 500; white-space: nowrap">{t}</span>'
dot=lambda: f'<span style="flex: none; width: 8px; height: 8px; border-radius: 999px; background: {LIME}; margin-top: 6px"></span>'
rule=lambda t: f'<div style="display: flex; gap: 10px; font-size: 13px; line-height: 20px">{dot()}<span>{t}</span></div>'
body=f'''<div style="width: {W}px; height: {Hh}px; box-sizing: border-box; padding: 28px 28px 24px; background: {WHT}; color: {INK}; font-family: 'Geist', system-ui, sans-serif; display: flex; flex-direction: column">
<div style="display: flex; justify-content: space-between; align-items: center">{LOGO(28)}<span style="font-size: 10px; color: {MUT}">Manual de identidade visual · v1</span></div>
<h1 style="margin: 44px 0 0; font-size: 48px; line-height: 52px; font-weight: 600; letter-spacing: -0.03em">4metrics</h1>
<p style="margin: 8px 0 0; font-size: 14px; line-height: 20px; color: {MUT}">Revenue Intelligence para times comerciais e de marketing. Software com serviço.</p>
{hr}
{sec("01","Logo")}
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px">
{tile(LOGO(36),WHT,"Principal: fundo claro")}
{tile(LOGO(36,ink=WHT),BLK,"Fundo escuro: marca e redes",False)}
{tile(SYM(56),SUB,"Só o símbolo: favicon, app e avatar",False)}
</div>
<p style="margin: 20px 0 0; font-size: 15px; line-height: 22px; font-weight: 500">Quatro pontos, quatro métricas. O verde é a que sobe.</p>
{hr}
{sec("02","Cores")}
<div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 12px">
{sw("Verde 4metrics",LIME,"brand")}{sw("Preto",BLK,"surface · escuro")}{sw("Branco",WHT,"surface · claro",border=True)}{sw("Névoa",SUB,"surface-subtle",border=True)}{sw("Verde 800",G800,"brand-strong")}
</div>
<p style="margin: 16px 0 0; font-size: 13px; line-height: 20px; color: {MUT}">Uso: preto na marca e nas redes, branco na plataforma, lima no botão e para marcar números. Texto sobre o lima é sempre preto.</p>
{hr}
{sec("03","Tipografia")}
<div style="display: grid; grid-template-columns: 240px 1fr; gap: 24px; align-items: end">
<div><p style="margin: 0; font-size: 104px; line-height: 96px; font-weight: 600; letter-spacing: -0.04em">Aa</p>
<p style="margin: 10px 0 0; font-size: 18px; font-weight: 500">Geist <span style="font-family: 'Geist Mono', monospace; font-size: 15px; color: {MUT}">+ Geist Mono</span></p>
<p style="margin: 2px 0 0; font-size: 11px; color: {MUT}">Títulos 600 · Rótulos 500 · Texto 400 · Números em Mono</p></div>
<div style="display: flex; flex-direction: column; gap: 6px">
<p style="margin: 0; font-size: 28px; line-height: 34px; font-weight: 600; letter-spacing: -0.02em">O dado certo, na hora da decisão.</p>
<p style="margin: 0; font-size: 19px; line-height: 26px; font-weight: 600">Título 1 · 36/44</p>
<p style="margin: 0; font-size: 15px; line-height: 22px; font-weight: 600">Título 2 · 24/32</p>
<p style="margin: 4px 0 0; font-size: 11px; line-height: 16px">Corpo · 16/24 · A 4metrics integra vendas, marketing e CRM e entrega o BI pronto.</p>
<p style="margin: 0; font-size: 10px; line-height: 15px; color: {MUT}">Pequeno · 14/20 · Texto secundário e legendas</p>
<p style="margin: 2px 0 0; font-family: 'Geist Mono', monospace; font-size: 18px; line-height: 24px; font-weight: 500">R$ 1,24 mi <span style="font-size: 11px; color: {G800}">▲ +12,4%</span> <span style="font-family: 'Geist', sans-serif; font-size: 10px; color: {MUT}">Números · Geist Mono</span></p>
</div></div>
{hr}
{sec("04","Componentes")}
<div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap">
{btn("Agendar diagnóstico",LIME,BLK,LIME)}{btn("Ver dashboard",BLK,WHT,BLK)}{btn("Ver exemplo",WHT,INK,"#8C9386")}
<span style="width: 12px"></span>{badge("Fonte: CRM",SUB,MUT,BOR)}{badge("Meta batida",LIME,BLK,LIME)}
</div>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 20px">
<div style="background: {G100}; border-radius: 6px; padding: 16px">
<p style="margin: 0; font-size: 10px; font-weight: 500; color: {G800}">Insight do agente</p>
<p style="margin: 6px 0 0; font-size: 13px; line-height: 19px; font-weight: 500">R$ 86 mil parados no funil. Priorize os 10 maiores negócios esta semana.</p></div>
<div style="border: 1px solid {BOR}; border-radius: 6px; padding: 16px; display: flex; justify-content: space-between; align-items: flex-end">
<div><p style="margin: 0; font-size: 10px; font-weight: 500; color: {MUT}">Receita do mês</p>
<p style="margin: 4px 0 0; font-family: 'Geist Mono', monospace; font-size: 24px; line-height: 28px; font-weight: 500">R$ 1,24 mi</p></div>
<span style="font-family: 'Geist Mono', monospace; font-size: 11px; font-weight: 500; color: {G800}">▲ +12,4% <span style="font-family: 'Geist', sans-serif; font-weight: 400; color: {MUT}">vs. out</span></span></div>
</div>
<p style="margin: 22px 0 0; font-size: 26px; line-height: 34px; font-weight: 600; letter-spacing: -0.02em">Receita com dado, não com <span style="background: {LIME}; color: {BLK}; padding: 0 5px; border-radius: 4px">achismo.</span></p>
<p style="margin: 6px 0 0; font-size: 10px; color: {MUT}">Button · Badge · Insight · MetricCard · Marcador</p>
{hr}
{sec("05","Regras")}
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px 32px">
{rule("Uma área lima forte por tela.")}{rule("Bordas finas, nunca sombras.")}
{rule("Texto sobre o lima é sempre preto. Lima nunca é texto no fundo claro.")}{rule("Sem robôs, cérebros, neon ou gradientes.")}
{rule("Lima como marcador atrás de um número ou palavra, nunca em bloco grande.")}{rule("Números em Geist Mono; toda variação com seta e sinal.")}
</div>
<div style="flex: 1; min-height: 28px"></div>
<div style="display: flex; justify-content: space-between; align-items: center">
<span style="display: inline-flex; align-items: center; gap: 10px">{SYM(24)}<span style="font-size: 15px; font-weight: 600">Você só acessa. A gente constrói o resto.</span></span>
<span style="font-size: 10px; color: {MUT}">4metrics.com.br</span></div>
</div>'''
html=f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>MIV · Resumo</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&amp;family=Geist+Mono:wght@400;500&amp;display=swap">
<style>
body{{margin:0}}
a{{color:#406500}}a:hover{{color:#2D4A00}}
</style>
</helmet>
{body}
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":{W},"height":{Hh}}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
open("MIV-00-resumo.dc.html","w").write(html)
print("ok")

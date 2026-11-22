import sys, os
sys.path.insert(0, "/home/claude/tools")
from festas_base import ff, SYM, WORD, LIME, NAVY
D = "/home/claude/out/pauta-site"
G, MUTL, MUTD, NEV, RED, AMB = "#406500", "#4F5B63", "#9AA7B0", "#EAF5DD", "#D92D20", "#B54708"
DOTL = "radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px) 0 0/22px 22px"
DOTD = "radial-gradient(rgba(255,255,255,.08) 1px,transparent 1.2px) 0 0/22px 22px"
BG = {
 "mesh": (f"{DOTD},radial-gradient(900px 900px at 85% 8%,rgba(146,197,73,.55),transparent 60%),radial-gradient(800px 800px at 0% 100%,rgba(146,197,73,.28),transparent 60%),linear-gradient(160deg,#0B2230 0%,{NAVY} 55%)", "d"),
 "dark": (f"{DOTD},radial-gradient(1200px 900px at 50% 115%,rgba(146,197,73,.38),transparent 60%),{NAVY}", "d"),
 "glow": (f"{DOTD},radial-gradient(700px 700px at 50% 45%,rgba(146,197,73,.5),transparent 70%),{NAVY}", "d"),
 "nevoa": (f"{DOTL},linear-gradient(180deg,#FFFFFF 0%,{NEV} 100%)", "l"),
 "nevoa2": (f"{DOTL},radial-gradient(900px 900px at 0% 0%,rgba(146,197,73,.32),transparent 60%),linear-gradient(0deg,#FFFFFF,{NEV})", "l"),
 "sweep": (f"{DOTL},radial-gradient(1100px 700px at 100% 0%,rgba(146,197,73,.42),transparent 65%),#FFFFFF", "l"),
 "claro": (f"{DOTL},radial-gradient(700px 700px at 95% 0%,rgba(146,197,73,.22),transparent 65%),#FFFFFF", "l"),
 "lima": (f"radial-gradient(rgba(5,19,28,.10) 1px,transparent 1.2px) 0 0/22px 22px,linear-gradient(200deg,#B5DB7E 0%,{LIME} 45%,#7FB23A 100%)", "m"),
}
PH = "/home/claude/out/stock/full"
def phbg(pid, pos="center"):
    return (f"{DOTD},linear-gradient(180deg,rgba(5,19,28,.18) 0%,rgba(5,19,28,.58) 38%,rgba(5,19,28,.93) 100%),radial-gradient(900px 700px at 90% 0%,rgba(146,197,73,.35),transparent 60%),url(file://{PH}/{pid}.jpg) {pos}/cover no-repeat", "d")
def phcard(pid, h, radius="28px", pos="center", extra=""):
    return f'<div class="feat" style="position:relative;height:{h}px;border-radius:{radius};overflow:hidden;background:linear-gradient(200deg,rgba(146,197,73,.28),rgba(5,19,28,0) 45%),url(file://{PH}/{pid}.jpg) {pos}/cover;{extra}"></div>'
CSS = ff + f"""*{{box-sizing:border-box}} body{{margin:0;background:#777}}
.f{{position:relative;overflow:hidden;font-family:'Inter';display:flex;flex-direction:column;margin-bottom:20px}}
.fe{{width:1080px;height:1350px;padding:72px 72px 150px;gap:30px}}
.st{{width:1080px;height:1920px;padding:250px 84px 260px;gap:40px}}
h1,h2,.pj{{margin:0;font-family:'Plus Jakarta Sans';font-weight:700;letter-spacing:-0.033em}}
p{{margin:0}}
.fe h1{{font-size:84px;line-height:90px}} .st h1{{font-size:104px;line-height:110px}}
.fe .lead{{font-size:32px;line-height:44px}} .st .lead{{font-size:42px;line-height:58px}}
.pill{{align-self:flex-start;display:inline-flex;align-items:center;border-radius:999px;font-weight:600}}
.fe .pill{{height:46px;padding:0 22px;font-size:22px}} .st .pill{{height:60px;padding:0 28px;font-size:28px}}
.mid{{flex:1;display:flex;flex-direction:column;justify-content:center}}
.foot{{position:absolute;left:72px;bottom:62px;display:flex;align-items:center;gap:12px}}
.st .foot{{left:84px;bottom:150px}}
.card{{border-radius:24px}}
.l .card{{background:#fff;border:1px solid #DCE6D3;box-shadow:0 12px 32px rgba(5,19,28,.06)}}
.d .card{{background:#14232C;border:1px solid #2B3640}}
.m .card{{background:rgba(255,255,255,.55);border:1px solid rgba(5,19,28,.12)}}
.feat{{box-shadow:0 0 0 2px rgba(146,197,73,.85),0 0 44px rgba(146,197,73,.35)!important}}
.l .hl{{color:{G}}} .d .hl{{color:{LIME}}} .m .hl{{text-decoration:underline;text-decoration-color:#fff;text-decoration-thickness:6px;text-underline-offset:10px}}
.l .mut{{color:{MUTL}}} .d .mut{{color:{MUTD}}} .m .mut{{color:#1F3A12}}
.chip{{display:inline-flex;align-items:center;gap:12px;border-radius:999px;font-weight:600;white-space:nowrap}}
.fe .chip{{height:60px;padding:0 26px;font-size:26px}} .st .chip{{height:76px;padding:0 32px;font-size:32px}}
.l .chip{{background:#fff;border:1px solid #DCE6D3;color:{NAVY}}} .d .chip{{background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.16);color:#fff}} .m .chip{{background:rgba(255,255,255,.5);border:1px solid rgba(5,19,28,.15);color:{NAVY}}}
.btn{{align-self:flex-start;display:inline-flex;align-items:center;border-radius:14px;font-weight:600}}
.fe .btn{{height:84px;padding:0 38px;font-size:30px}} .st .btn{{height:108px;padding:0 46px;font-size:38px}}
.l .btn,.m .btn{{background:{NAVY};color:#fff}} .d .btn{{background:{LIME};color:{NAVY}}}
.src{{font-size:20px;line-height:28px}} .st .src{{font-size:24px;line-height:32px}}
"""
def pillc(t):
    return {"l": f"background:#fff;color:{G};border:1px solid #CFE3B6", "d": f"background:rgba(146,197,73,.16);color:{LIME};border:1px solid rgba(146,197,73,.45)", "m": f"background:rgba(255,255,255,.4);color:{NAVY};border:1px solid rgba(5,19,28,.2)"}[t]
FR = []
def frame(name, kind, bg, body, pill=None, logo=True):
    css, t = phbg(*bg.split(":")[1:]) if bg.startswith("ph:") else BG[bg]
    ink = "#fff" if t == "d" else NAVY
    acc = "#FFFFFF" if t == "m" else LIME
    lg = f'<div class="foot">{SYM(44 if kind=="st" else 40,dots=ink,accent=acc)}{WORD(36 if kind=="st" else 32,ink,acc)}</div>' if logo else ""
    pl = f'<span class="pill" style="{pillc(t)}">{pill}</span>' if pill else ""
    FR.append((name, kind, f'<section class="f {kind} {t}" id="x{len(FR)}" style="background:{css};color:{ink}">{pl}{body}{lg}</section>'))
def cta(kind, t="Comente DIAGNÓSTICO"):
    return f'<span class="btn">{t}</span>'
def nums(kind, strike=False):
    sz = 46
    it = [("Planilha","R$ 1,08 mi"),("Power BI","R$ 1,24 mi"),("Relatório","R$ 980 mil")]
    return '<div style="display:flex;gap:16px">' + "".join(f'<div class="card" style="flex:1;padding:30px 24px;display:flex;flex-direction:column;gap:10px"><span class="mut" style="font-size:{24 if kind=="fe" else 28}px">{a}</span><span class="pj" style="white-space:nowrap;font-size:{sz}px;{"text-decoration:line-through;text-decoration-thickness:4px;opacity:.55" if strike else ""}">{b}</span></div>' for a,b in it) + '</div>'
def oficial(kind):
    return f'''<div class="card feat" style="padding:36px 40px;display:flex;justify-content:space-between;align-items:center">
<div style="display:flex;flex-direction:column;gap:8px"><span style="font-size:{24 if kind=="fe" else 28}px;font-weight:700" class="hl">NÚMERO OFICIAL</span><span class="pj" style="font-size:{88 if kind=="fe" else 96}px;line-height:1">R$ 1,12 mi</span><span class="mut" style="font-size:{26 if kind=="fe" else 30}px">+8% vs outubro · regra verificada</span></div>
{SYM(110 if kind=="fe" else 130, dots=NAVY, accent=LIME, container="#EAF5DD")}</div>'''
def rows(kind, items, icon=True):
    fs = 32 if kind=="fe" else 38
    return '<div style="display:flex;flex-direction:column;gap:16px">' + "".join(f'<div class="card" style="padding:{26 if kind=="fe" else 32}px 34px;display:flex;align-items:center;gap:22px;font-size:{fs}px;font-weight:600"><i style="width:16px;height:16px;border-radius:9px;background:{LIME};flex:none;box-shadow:0 0 0 4px rgba(146,197,73,.25)"></i><span>{x}</span></div>' for x in items) + '</div>'
def metric_card(kind):
    fs = 30 if kind=="fe" else 36
    line = lambda k, v: f'<div style="display:flex;justify-content:space-between;padding:{18 if kind=="fe" else 22}px 0;border-top:1px solid rgba(127,140,150,.25);font-size:{fs}px"><span class="mut">{k}</span><span style="font-weight:600">{v}</span></div>'
    return f'''<div class="card feat" style="padding:36px 40px">
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px"><span class="pj" style="font-size:{48 if kind=="fe" else 56}px">Ticket médio</span><span class="chip" style="height:48px;font-size:22px;background:#EAF5DD;color:{G};border:1px solid #CFE3B6">✓ verificada</span></div>
{line("Fórmula","receita faturada ÷ pedidos")}{line("Fonte","ERP")}{line("Versão","v3 · aprovada pelo comercial")}{line("Usada em","painel · alerta · resumo · sua IA")}</div>'''

# ======================= T10 · 67% · 04/12 · estático névoa
frame("2026-12-04-confianca-67-v2","fe","nevoa",f'''
<div style="display:flex;flex-direction:column;gap:6px;margin-top:6px"><div style="display:flex;align-items:center;gap:36px"><div class="pj" style="font-size:210px;line-height:190px;letter-spacing:-0.05em;color:{G}">67%</div><div style="flex:1">{phcard("5716001",190,"999px","center")}</div></div>
<h1 style="font-size:66px;line-height:74px">das organizações ainda não confiam totalmente <span class="hl">nos dados que usam para decidir.</span></h1></div>
<div class="mid"><div class="card" style="padding:34px 38px;display:flex;flex-direction:column;gap:22px">
{"".join(f'<div style="display:flex;align-items:center;gap:22px"><span style="width:96px;font-size:26px;font-weight:600" class="mut">{y}</span><div style="flex:1;height:44px;border-radius:12px;background:#EEF2EF;overflow:hidden"><div style="width:{v}%;height:100%;border-radius:12px;background:{c}"></div></div><span class="pj" style="width:100px;font-size:36px;text-align:right">{v}%</span></div>' for y,v,c in (("2023",55,"#C9DEB0"),("2024",67,LIME)))}
<span class="mut" style="font-size:24px">A desconfiança cresceu em um ano.</span></div></div>
<div style="position:absolute;right:72px;bottom:58px;text-align:right" class="src mut">Fonte: Precisely e Drexel University,<br>2025 Outlook: Data Integrity Trends and Insights</div>''', "Dados de mercado")
S = "2026-12-04-st-confianca-67-v2"
frame(S+"-01","st","ph:3184292",f'<div class="mid" style="gap:40px"><h1 style="font-size:128px;line-height:130px">2 em cada 3 empresas <span class="hl">não confiam no próprio número.</span></h1></div>',"Dados de mercado")
frame(S+"-02","st","nevoa",f'''<h1>E a desconfiança <span class="hl">está crescendo.</span></h1><div class="mid" style="gap:30px">
{"".join(f'<div style="display:flex;flex-direction:column;gap:14px"><div style="display:flex;justify-content:space-between"><span class="mut" style="font-size:34px;font-weight:600">{y}</span><span class="pj" style="font-size:72px">{v}%</span></div><div style="height:56px;border-radius:14px;background:#E3EADF;overflow:hidden"><div style="width:{v}%;height:100%;background:{c}"></div></div></div>' for y,v,c in (("2023",55,"#C9DEB0"),("2024",67,LIME)))}
<p class="src mut" style="margin-top:20px">Organizações que não confiam totalmente nos dados que usam para decidir. Fonte: Precisely e Drexel University, 2025 Outlook: Data Integrity Trends and Insights.</p></div>''')
frame(S+"-03","st","dark",f'<h1>O sintoma: <span class="hl">cada área chega com o seu número.</span></h1><div class="mid" style="gap:30px"><p class="lead mut">Quanto vendemos este mês?</p>{nums("st")}</div>')
frame(S+"-04","st","lima",f'<h1>Com a 4metrics: <span class="hl">um número oficial.</span></h1><div class="mid" style="gap:40px">{oficial("st")}<p class="lead mut">Uma regra por métrica, verificada, igual para todo mundo.</p>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T6 · fila · 07/12 · stories (feed = Reel)
S = "2026-12-07-st-fila-relatorios-v2"
frame(S+"-01","st","ph:7688336",f'<div class="mid"><h1 style="font-size:124px;line-height:128px">Seu time de dados virou <span class="hl">fila de relatórios?</span></h1></div>',"Custo da demora")
tk = [("#124","Receita por canal","há 6 dias"),("#125","CAC de outubro","há 4 dias"),("#126","Leads parados no funil","há 3 dias"),("#127","Meta x realizado por loja","há 1 dia")]
frame(S+"-02","st","nevoa",f'''<h1>Um pedido <span class="hl">para cada número.</span></h1><div class="mid" style="gap:16px">
{"".join(f'<div class="card" style="padding:28px 32px;display:flex;align-items:center;gap:22px"><span class="pj mut" style="font-size:30px">{a}</span><span style="flex:1;font-size:34px;font-weight:600">{b}</span><span style="font-size:26px;color:{AMB};font-weight:600">{c}</span></div>' for a,b,c in tk)}
<p class="lead mut" style="margin-top:18px">E a semana passa montando relatório.</p></div>''')
frame(S+"-03","st","sweep",f'''<h1>Com a 4metrics, <span class="hl">pergunte e receba na hora.</span></h1><div class="mid" style="gap:22px">
<div style="align-self:flex-end;max-width:760px;background:{NAVY};color:#fff;border-radius:34px 34px 8px 34px;padding:30px 36px;font-size:38px;font-weight:600">Qual foi o CAC de outubro?</div>
<div class="card feat" style="max-width:820px;padding:34px 38px;border-radius:34px 34px 34px 8px;display:flex;flex-direction:column;gap:10px"><span class="pj" style="font-size:80px">R$ 48</span><span class="mut" style="font-size:32px">O mesmo número do painel, com a regra oficial.</span></div></div>''')
frame(S+"-04","st","mesh",f'<div class="mid" style="gap:44px"><h1>E o time de dados <span class="hl">volta a melhorar o dado.</span></h1><p class="lead mut">Comercial e marketing saem da fila. A resposta chega com o próximo passo.</p>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T1 · métricas oficiais · 14/12 · carrossel névoa 5
C = "2026-12-14-metricas-oficiais-v2"
frame(C+"-01","fe","nevoa",f'''<h1 style="font-size:104px;line-height:108px">Acabou a briga pelo <span class="hl">número certo.</span></h1>
<div class="mid" style="gap:0">{phcard("3184339",440)}<div style="margin:-110px 36px 0;position:relative">{oficial("fe")}</div></div>''',"Métricas oficiais")
frame(C+"-02","fe","dark",f'''<p class="lead mut">"Quanto vendemos este mês?"</p><h1>Três ferramentas. <span class="hl">Três números.</span></h1>
<div class="mid" style="gap:30px">{nums("fe")}<p class="lead mut">E a reunião discute qual está certo.</p></div>''')
frame(C+"-03","fe","nevoa2",f'''<h1>Uma regra <span class="hl">por métrica.</span></h1><p class="lead mut">Conversão, ticket médio, meta e receita: definidas uma vez com o seu time.</p><div class="mid">{metric_card("fe")}</div>''')
flow = lambda kind, it: '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(f'<div style="display:flex;align-items:center;gap:22px"><span class="pj" style="width:64px;height:64px;border-radius:18px;background:{LIME};color:{NAVY};display:flex;align-items:center;justify-content:center;font-size:30px;flex:none">{i+1}</span><div class="card" style="flex:1;padding:24px 30px;font-size:{30 if kind=="fe" else 36}px;font-weight:600">{x}</div></div>' for i,x in enumerate(it)) + '</div>'
frame(C+"-04","fe","claro",f'''<h1>Verificado <span class="hl">antes de publicar.</span></h1><p class="lead mut">Se a regra muda, o número volta para revisão antes de chegar à diretoria.</p>
<div class="mid">{flow("fe",["A regra muda","O número vai para revisão","A nova versão é aprovada","A diretoria recebe o número certo"])}</div>''')
frame(C+"-05","fe","nevoa",f'''<h1>Igual <span class="hl">em todo lugar.</span></h1><div class="mid" style="gap:30px">
<div style="display:flex;flex-wrap:wrap;gap:14px">{"".join(f'<span class="chip">{x}</span>' for x in ("Painel","Alerta","Resumo diário","Agentes de IA"))}</div>
<p class="lead">Uma regra, um número oficial e a mesma resposta para o seu time e para os seus agentes de IA.</p>{cta("fe")}</div>''')
S = "2026-12-14-st-metricas-oficiais-v2"
frame(S+"-01","st","ph:3183197",f'<div class="mid"><h1 style="font-size:132px;line-height:134px">Qual número <span class="hl">está certo?</span></h1></div>',"Métricas oficiais")
frame(S+"-02","st","dark",f'<h1>Planilha, Power BI e relatório. <span class="hl">Três respostas.</span></h1><div class="mid">{nums("st")}</div>')
frame(S+"-03","st","nevoa",f'<h1>Na 4metrics, <span class="hl">cada métrica tem uma regra oficial.</span></h1><div class="mid">{metric_card("st")}</div>')
frame(S+"-04","st","lima",f'<div class="mid" style="gap:44px"><h1>A reunião discute <span class="hl">o que fazer.</span></h1><p class="lead mut">Não qual número está certo.</p>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T7 · segurança · 21/12 · estático névoa
seals = ["Conformidade com a LGPD","Criptografia","Acesso auditável","Verificação em duas etapas","DPA disponível"]
seal = lambda kind, x: f'<div class="card" style="padding:{28 if kind=="fe" else 34}px 30px;display:flex;align-items:center;gap:20px;font-size:{30 if kind=="fe" else 36}px;font-weight:600"><span style="width:56px;height:56px;border-radius:16px;background:{NAVY};display:flex;align-items:center;justify-content:center;flex:none"><svg width="28" height="28" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5" stroke="{LIME}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg></span>{x}</div>'
frame("2026-12-21-seguranca-v2","fe","nevoa2",f'''<div style="display:flex;align-items:center;gap:30px"><h1 style="flex:1;font-size:84px;line-height:90px">Seus dados protegidos <span class="hl">do início ao fim.</span></h1><div style="width:270px;flex:none">{phcard("1181467",270,"999px","30% center")}</div></div>
<div class="mid" style="gap:14px">{"".join(seal("fe",x) for x in seals)}</div>
<p class="lead mut" style="font-size:28px;line-height:38px">E os seus agentes de IA executam com a sua aprovação.</p>''',"Segurança")
S = "2026-12-21-st-seguranca-v2"
frame(S+"-01","st","ph:3861969",f'<div class="mid"><h1 style="font-size:120px;line-height:124px">IA com os dados da empresa. <span class="hl">E a segurança?</span></h1></div>',"Segurança")
frame(S+"-02","st","sweep",f'''<h1>Com IA genérica, <span class="hl">o controle sai da sua mão.</span></h1><div class="mid">{rows("st",["Dados da empresa e de clientes fora do seu controle","Sem rastreabilidade de onde o número veio","A responsabilidade continua sendo sua"])}</div>''')
frame(S+"-03","st","nevoa",f'<h1>Na 4metrics, <span class="hl">segurança vem de fábrica.</span></h1><div class="mid" style="gap:16px">{"".join(seal("st",x) for x in seals)}</div>')
frame(S+"-04","st","mesh",f'<div class="mid" style="gap:44px"><h1>O mesmo controle de acesso <span class="hl">também na sua IA.</span></h1><p class="lead mut">Seus agentes executam com a sua aprovação. E fica registrado.</p>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T2 · regra muda · 06/01 · stories (feed = Reel)
S = "2027-01-06-st-regra-muda-v2"
frame(S+"-01","st","ph:669615",f'<div class="mid"><h1 style="font-size:132px;line-height:134px">E quando <span class="hl">a regra muda?</span></h1><p class="lead mut" style="margin-top:30px">O CPL passa a contar só lead qualificado.</p></div>',"Métricas oficiais")
redo = lambda x: f'<div class="card" style="padding:30px 34px;display:flex;justify-content:space-between;align-items:center;font-size:38px;font-weight:600"><span>{x}</span><span style="font-size:30px;color:{AMB}">refazer</span></div>'
frame(S+"-02","st","nevoa",f'<h1>Sem uma regra oficial, <span class="hl">tudo é refeito.</span></h1><div class="mid" style="gap:16px">{redo("Planilha")}{redo("Power BI")}{redo("Relatório")}<p class="lead mut" style="margin-top:18px">Por semanas, cada um mostra uma regra.</p></div>')
ver = f'''<div class="card" style="padding:34px 38px;display:flex;flex-direction:column;gap:22px">
<div style="display:flex;justify-content:space-between;align-items:center"><span class="pj" style="font-size:52px">CPL</span><span class="chip" style="height:52px;font-size:24px;background:rgba(146,197,73,.16);color:{LIME};border:1px solid rgba(146,197,73,.45)">v2 · hoje</span></div>
<div style="font-size:32px;color:{MUTD};text-decoration:line-through">v1 · custo ÷ todos os leads</div>
<div style="font-size:36px;font-weight:600">v2 · custo ÷ leads qualificados</div></div>'''
frame(S+"-03","st","dark",f'<h1>Na 4metrics, a regra muda <span class="hl">uma vez, com nova versão.</span></h1><div class="mid">{ver}</div>')
frame(S+"-04","st","lima",f'<div class="mid" style="gap:40px"><h1>No mesmo dia, <span class="hl">em todo lugar.</span></h1><div style="display:flex;flex-wrap:wrap;gap:14px">{"".join(f"<span class=chip>{x}</span>" for x in ("Painel","Alerta","Sua IA"))}</div>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T3 · camada semântica · 08/01 · estático névoa
frame("2027-01-08-camada-semantica-v2","fe","nevoa",f'''<h1 style="font-size:92px;line-height:98px">A IA consulta a métrica pronta. <span class="hl">Nunca a tabela crua.</span></h1>
<div class="mid" style="gap:0">{phcard("7213549",300)}<div style="margin:-80px 30px 0;position:relative">{metric_card("fe")}</div></div><p class="lead mut" style="font-size:28px;line-height:38px">Camada semântica: as métricas oficiais com nome, fórmula e versão.</p>''',"Camada semântica")
S = "2027-01-08-st-camada-semantica-v2"
frame(S+"-01","st","ph:6801648",f'<div class="mid"><h1 style="font-size:128px;line-height:132px">Por que a IA <span class="hl">erra o número?</span></h1></div>',"Camada semântica")
frame(S+"-02","st","sweep",f'''<h1>Ela não conhece <span class="hl">as regras do seu negócio.</span></h1><p class="lead mut">Para acertar, a IA precisa de três coisas:</p><div class="mid">{rows("st",["Contexto do negócio: metas, regras e o que cada área chama de venda","Contexto dos dados: de onde vem cada número","Camada semântica: as métricas oficiais"])}</div>''')
frame(S+"-03","st","nevoa",f'<h1>A métrica pronta, <span class="hl">com nome, fórmula e versão.</span></h1><div class="mid">{metric_card("st")}</div>')
frame(S+"-04","st","mesh",f'<div class="mid" style="gap:44px"><h1>O mesmo contexto <span class="hl">em todo lugar.</span></h1><p class="lead mut">No painel, no alerta, no chat e na sua IA via MCP.</p>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T5 · time de dados · 11/01 · carrossel claro 5
C = "2027-01-11-sem-time-de-dados-v2"
frame(C+"-01","fe","claro",f'''<h1 style="font-size:88px;line-height:92px">Você não precisa de um time de dados. <span class="hl">Você precisa da resposta.</span></h1>
<div class="mid">{phcard("3182812",560,"300px 300px 28px 28px","center 30%")}</div>''',"Revenue Intelligence")
frame(C+"-02","fe","nevoa",f'''<h1>Montar um time de dados <span class="hl">é caro e demorado.</span></h1><div class="mid">{rows("fe",["Contratar e reter especialistas","Conectar e manter as fontes","Criar e ajustar as regras do negócio","Atender a fila de pedidos"])}</div>''')
tb = [("Quem faz","Você contrata um projeto","O seu time monta","A 4metrics faz, sempre"),("O que recebe","Dashboard no fim","Ferramentas para montar","Resposta com o próximo passo"),("1ª resposta","Semanas a meses","Depende do seu time","Até 14 dias"),("Negócio mudou","Novo orçamento","O seu time refaz","A 4metrics ajusta"),("Pronto para IA","Fora do escopo","Se o seu time montar","Sim, via MCP")]
th = '<div style="display:grid;grid-template-columns:200px 1fr 1fr 1.1fr;gap:0">' + "".join(f'<div style="padding:16px 12px;font-size:20px;font-weight:700;{"color:"+G if i==3 else "color:"+MUTL}">{h}</div>' for i,h in enumerate(["","Consultoria de BI","Plataforma de dados","4metrics"]))
for r in tb: th += "".join(f'<div style="padding:20px 12px;border-top:1px solid #E1E7E4;font-size:{22 if i else 21}px;line-height:30px;{"font-weight:700" if i in (0,3) else "color:"+MUTL};{"background:#F3F9EC" if i==3 else ""}">{c}</div>' for i,c in enumerate(r))
th += '</div>'
frame(C+"-03","fe","claro",f'<h1 style="font-size:72px;line-height:78px">Consultoria, plataforma <span class="hl">ou 4metrics?</span></h1><div class="mid"><div class="card" style="padding:16px 22px">{th}</div></div>')
frame(C+"-04","fe","dark",f'<h1>A fundação <span class="hl">é com a gente.</span></h1><div class="mid">{flow("fe",["Mapeamento: entendemos o negócio antes do dado","Acesso: você libera, nós conectamos","Extração: os dados chegam sozinhos, todo dia","Modelagem: um número só, com uma regra só","Manutenção: a fundação não para no primeiro dia"])}</div>')
frame(C+"-05","fe","claro",f'''<div class="mid" style="gap:30px"><div style="display:flex;align-items:baseline;gap:20px"><span class="pj mut" style="font-size:52px">até</span><span class="pj hl" style="font-size:250px;line-height:220px;letter-spacing:-0.05em">14</span><span class="pj" style="font-size:64px">dias</span></div>
<h1 style="font-size:72px;line-height:78px">para o primeiro insight.</h1><p class="lead mut">Sem montar time de dados. Sem trocar suas ferramentas.</p>{cta("fe")}</div>''')
S = "2027-01-11-st-sem-time-de-dados-v2"
frame(S+"-01","st","nevoa",f'<h1 style="font-size:112px;line-height:116px">Precisa contratar <span class="hl">um time de dados?</span></h1><div class="mid">{phcard("5439381",760,"400px 400px 28px 28px")}</div>',"Revenue Intelligence")
frame(S+"-02","st","nevoa",f'<div class="mid" style="gap:40px"><div class="pj hl" style="font-size:220px;line-height:200px">Não.</div><p class="lead">O time da 4metrics conecta as fontes, cria as métricas e ajusta as regras quando o seu negócio muda.</p></div>')
frame(S+"-03","st","dark",f'<h1>A fundação <span class="hl">é com a gente.</span></h1><div class="mid">{flow("st",["Mapeamento","Acesso","Extração","Modelagem","Manutenção"])}</div>')
frame(S+"-04","st","lima",f'<div class="mid" style="gap:40px"><h1>Primeiro insight <span class="hl">em até 14 dias.</span></h1>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T4 · agentes · 13/01 · stories (feed = Reel)
S = "2027-01-13-st-agentes-aprovacao-v2"
frame(S+"-01","st","ph:7567443",f'<div class="mid"><h1 style="font-size:120px;line-height:124px">E se a IA executasse <span class="hl">o próximo passo?</span></h1></div>',"Agentes de IA")
frame(S+"-02","st","sweep",f'<h1>Do gargalo <span class="hl">à execução.</span></h1><div class="mid">{flow("st",["A 4metrics encontra o gargalo","O próximo passo vai para o seu agente","Você aprova","Ele executa no CRM e fica registrado"])}</div>')
appr = f'''<div class="card feat" style="padding:36px 40px;display:flex;flex-direction:column;gap:26px">
<span style="font-size:28px;font-weight:700;color:{G}">PRÓXIMO PASSO</span><span style="font-size:42px;line-height:56px;font-weight:600">Priorizar os contatos parados há mais de 30 dias.</span>
<div style="display:flex;gap:16px"><span class="chip" style="background:{NAVY};color:#fff;border:none">Aprovar</span><span class="chip">Ajustar</span></div></div>'''
frame(S+"-03","st","nevoa",f'<h1>Nada acontece <span class="hl">sem você.</span></h1><div class="mid">{appr}</div>')
frame(S+"-04","st","mesh",f'<div class="mid" style="gap:44px"><h1>Você decide quem executa: <span class="hl">o seu time ou os seus agentes.</span></h1>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T8 · parceiros · 15/01 · estático lima
ptile = lambda kind, x: f'<div class="card" style="padding:{34 if kind=="fe" else 40}px 38px;display:flex;align-items:center;gap:22px"><i style="width:18px;height:18px;border-radius:9px;background:#fff;box-shadow:0 0 0 4px {NAVY};flex:none"></i><span class="pj" style="font-size:{48 if kind=="fe" else 54}px">{x}</span></div>'
frame("2027-01-15-parceiros-v2","fe","lima",f'''<div style="display:flex;align-items:center;gap:30px"><h1 style="flex:1;font-size:84px;line-height:90px">Parceiros oficiais <span class="hl">de quem faz a IA.</span></h1><div style="width:260px;flex:none">{phcard("3184465",260,"999px")}</div></div>
<div class="mid" style="gap:16px">{ptile("fe","Google Cloud")}{ptile("fe","Gemini Enterprise")}{ptile("fe","Claude Partner Network")}</div>
<p class="lead mut" style="font-size:28px;line-height:38px">Seus números oficiais chegam a qualquer IA por uma conexão única.</p>''',"Parceiros")
S = "2027-01-15-st-parceiros-v2"
frame(S+"-01","st","ph:5673488",f'<div class="mid"><h1 style="font-size:124px;line-height:128px">Com quem <span class="hl">a 4metrics trabalha?</span></h1></div>',"Parceiros")
frame(S+"-02","st","lima",f'<h1>Parceiros <span class="hl">oficiais.</span></h1><div class="mid" style="gap:18px">{ptile("st","Google Cloud")}{ptile("st","Gemini Enterprise")}{ptile("st","Claude Partner Network")}</div>')
frame(S+"-03","st","dark",f'<h1>Uma conexão única <span class="hl">para qualquer IA.</span></h1><div class="mid" style="gap:30px"><div style="display:flex;flex-wrap:wrap;gap:16px">{"".join(f"<span class=chip>{x}</span>" for x in ("ChatGPT","Claude","Gemini","Copilot"))}</div><p class="lead mut">Quando a sua empresa trocar ou adicionar uma IA, ela já lê os mesmos números.</p></div>')
frame(S+"-04","st","nevoa",f'<div class="mid" style="gap:44px"><h1>Sua empresa pronta <span class="hl">para cada nova IA.</span></h1>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T9 · BI e company brain · 18/01 · carrossel claro 4
C = "2027-01-18-bi-company-brain-v2"
frame(C+"-01","fe","claro",f'''<div class="mid" style="flex-direction:row;align-items:center;gap:36px"><div style="flex:1;display:flex;flex-direction:column;gap:30px"><p class="lead mut">As dúvidas que ouvimos antes de todo diagnóstico.</p><h1 style="font-size:88px;line-height:92px">"Já tenho BI. <span class="hl">Faz sentido?"</span></h1>
<div style="display:flex;flex-wrap:wrap;gap:14px">{"".join(f"<span class=chip>{x}</span>" for x in ("BI","Company brain","MCP do CRM"))}</div></div><div style="width:400px;flex:none">{phcard("8867431",720,"200px 200px 28px 28px","60% center")}</div></div>''',"FAQ")
hub = lambda kind, a, b: f'''<div style="display:flex;align-items:center;gap:22px"><div class="card" style="flex:1;padding:40px 24px;text-align:center"><span class="pj" style="font-size:{40 if kind=="fe" else 46}px">{a}</span></div>
<span class="pj hl" style="font-size:54px">⇄</span><div class="card feat" style="flex:1;padding:30px 24px;display:flex;flex-direction:column;align-items:center;gap:12px">{SYM(80,dots=NAVY,accent=LIME)}<span class="pj" style="font-size:{34 if kind=="fe" else 40}px">{b}</span></div></div>'''
frame(C+"-02","fe","nevoa",f'<h1>"A 4metrics substitui <span class="hl">o meu BI?"</span></h1><p class="lead">Pode substituir, mas não precisa. Funciona junto com o BI que você já usa e tira o comercial da fila de pedidos.</p><div class="mid">{hub("fe","Seu BI","4metrics")}</div>')
frame(C+"-03","fe","claro",f'<h1>"Já usamos <span class="hl">um company brain."</span></h1><p class="lead">Ele conhece documentos e conversas. A 4metrics entrega para ele os números oficiais e o próximo passo, via MCP.</p><div class="mid">{hub("fe","Company brain","Números oficiais")}</div>')
frame(C+"-04","fe","nevoa2",f'''<h1>"Já tenho o MCP <span class="hl">do meu CRM."</span></h1><p class="lead">O MCP de uma ferramenta mostra só essa ferramenta. A 4metrics relaciona todas as fontes com as regras oficiais, em uma conexão única.</p>
<div class="mid" style="gap:28px"><div style="display:flex;flex-wrap:wrap;gap:12px">{"".join(f"<span class=chip>{x}</span>" for x in ("CRM","ERP","Mídias","Planilhas"))}<span class="chip" style="background:{NAVY};color:#fff;border:none">→ 1 conexão</span></div>{cta("fe")}</div>''')
S = "2027-01-18-st-bi-company-brain-v2"
frame(S+"-01","st","sweep",f'<h1 style="font-size:108px;line-height:112px">3 dúvidas antes <span class="hl">de todo diagnóstico.</span></h1><div class="mid">{phcard("5668858",760,"28px 400px 28px 28px","40% center")}</div>',"FAQ")
frame(S+"-02","st","nevoa",f'<h1>"Substitui <span class="hl">o meu BI?"</span></h1><div class="mid" style="gap:30px"><div class="pj hl" style="font-size:96px">Pode. Mas não precisa.</div><p class="lead">A 4metrics funciona junto com o BI que você já usa.</p></div>')
frame(S+"-03","st","sweep",f'<h1>"Já temos <span class="hl">um company brain."</span></h1><div class="mid" style="gap:30px">{hub("st","Company brain","Números oficiais")}<p class="lead mut">A 4metrics entrega os números oficiais e o próximo passo, via MCP.</p></div>')
frame(S+"-04","st","mesh",f'<div class="mid" style="gap:40px"><h1>"Já tenho o MCP <span class="hl">do CRM."</span></h1><p class="lead mut">Ele mostra só o CRM. A 4metrics junta todas as fontes, com as regras oficiais.</p>{cta("st","Responda: DIAGNÓSTICO")}</div>')

# ======================= T11 · demo + diagnóstico · 20/01 · estático escuro
two = lambda kind, n, u, t: f'<div class="card" style="flex:1;padding:36px 32px;display:flex;flex-direction:column;gap:16px"><div style="display:flex;align-items:baseline;gap:10px"><span class="pj hl" style="font-size:{150 if kind=="fe" else 170}px;line-height:1;letter-spacing:-0.05em">{n}</span><span class="pj" style="font-size:44px">{u}</span></div><span style="font-size:{28 if kind=="fe" else 34}px;line-height:1.35">{t}</span></div>'
frame("2027-01-20-demo-diagnostico-v2","fe","ph:7651922",f'''<h1 style="font-size:96px;line-height:100px">Dois jeitos de <span class="hl">conhecer a 4metrics.</span></h1>
<div class="mid"><div style="display:flex;gap:18px">{two("fe","3","min","Demo: veja a 4metrics encontrar um gargalo de receita.")}{two("fe","30","min","Diagnóstico gratuito: mapeamos onde o dado trava a sua decisão.")}</div></div>
<span class="btn" style="margin-bottom:10px">Comente DIAGNÓSTICO</span>''',"Comece aqui")
S = "2027-01-20-st-demo-diagnostico-v2"
frame(S+"-01","st","ph:3184287",f'<div class="mid"><h1 style="font-size:124px;line-height:128px">Dois jeitos de <span class="hl">conhecer a 4metrics.</span></h1></div>',"Comece aqui")
frame(S+"-02","st","nevoa",f'<div class="mid" style="gap:36px"><div style="display:flex">{two("st","3","min","Demo: o número oficial, o gargalo e o próximo passo, até na sua IA.")}</div><p class="lead mut">No site da 4metrics.</p></div>')
frame(S+"-03","st","dark",f'<h1>Diagnóstico gratuito <span class="hl">de 30 minutos.</span></h1><div class="mid">{rows("st",["O mapa das suas fontes e de onde o número diverge","As decisões que mais pesam na sua receita","Onde a empresa está pronta para usar IA com segurança","Uma proposta com escopo e prazo"])}</div>')
frame(S+"-04","st","lima",f'<div class="mid" style="gap:40px"><h1>Sem custo. <span class="hl">Sem compromisso.</span></h1><p class="lead mut">Resposta em 1 dia útil.</p>{cta("st","Responda: DIAGNÓSTICO")}</div>')

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + "".join(h for _,_,h in FR) + "</body></html>"
open(f"{D}/all.html","w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{D}/all.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
    bad = pg.evaluate("""()=>[...document.querySelectorAll('section')].map(s=>{const r=s.getBoundingClientRect();const ft=s.querySelector('.foot').getBoundingClientRect();
      const n=[...s.children].filter(e=>!e.classList.contains('foot')).flatMap(e=>[e,...e.querySelectorAll('*')]).filter(e=>{const q=e.getBoundingClientRect();return q.width&&(q.right>r.right+1||q.left<r.left-1||q.bottom>ft.top-8)&&!e.closest('[style*="position:absolute"]')}).length;return n})""")
    for (name,kind,_),n in zip(FR,bad):
        loc = pg.locator(f"#x{FR.index((name,kind,_))}"); loc.scroll_into_view_if_needed(); pg.wait_for_timeout(250)
        loc.screenshot(path=f"{D}/{name}.png")
        if n: print("OVERFLOW", name, n)
    b.close()
print(len(FR), "frames")

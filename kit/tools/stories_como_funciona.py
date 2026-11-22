import sys
sys.path.insert(0, "/home/claude/tools")
from festas_base import ff, SYM, WORD, LIME, NAVY
D = "/home/claude/out/st-como-funciona"
G, MUTL, MUTD, NEV = "#406500", "#4F5B63", "#9AA7B0", "#EAF5DD"
DOTL = "radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px) 0 0/22px 22px"
DOTD = "radial-gradient(rgba(255,255,255,.08) 1px,transparent 1.2px) 0 0/22px 22px"
BG = {
 "mesh": f"{DOTD},radial-gradient(900px 900px at 85% 10%,rgba(146,197,73,.55),transparent 60%),radial-gradient(800px 800px at 0% 100%,rgba(146,197,73,.30),transparent 60%),linear-gradient(160deg,#0B2230 0%,{NAVY} 55%)",
 "nevoa": f"{DOTL},linear-gradient(180deg,#FFFFFF 0%,{NEV} 100%)",
 "sweep": f"{DOTL},radial-gradient(1100px 700px at 100% 0%,rgba(146,197,73,.45),transparent 65%),#FFFFFF",
 "dark":  f"{DOTD},radial-gradient(1200px 900px at 50% 110%,rgba(146,197,73,.40),transparent 60%),{NAVY}",
 "lima":  f"radial-gradient(rgba(5,19,28,.10) 1px,transparent 1.2px) 0 0/22px 22px,linear-gradient(200deg,#B5DB7E 0%,{LIME} 45%,#7FB23A 100%)",
 "glow":  f"{DOTD},radial-gradient(700px 700px at 50% 42%,rgba(146,197,73,.55),transparent 70%),{NAVY}",
 "nevoa2":f"{DOTL},radial-gradient(900px 900px at 0% 0%,rgba(146,197,73,.35),transparent 60%),linear-gradient(0deg,#FFFFFF,{NEV})",
}
CSS = ff + f"""*{{box-sizing:border-box}} body{{margin:0}}
.st{{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Inter';padding:260px 84px 230px;display:flex;flex-direction:column;gap:40px}}
h1{{margin:0;font-family:'Plus Jakarta Sans';font-weight:700;letter-spacing:-0.035em;font-size:112px;line-height:116px}}
h2{{margin:0;font-family:'Plus Jakarta Sans';font-weight:700;letter-spacing:-0.03em;font-size:92px;line-height:98px}}
p{{margin:0;font-size:42px;line-height:58px}}
.pill{{align-self:flex-start;display:inline-flex;align-items:center;height:60px;padding:0 28px;border-radius:999px;font-size:28px;font-weight:600}}
.foot{{position:absolute;left:84px;bottom:150px}}
.card{{border-radius:28px;padding:36px 40px}}
.chip{{display:inline-flex;align-items:center;height:76px;padding:0 32px;border-radius:999px;font-size:32px;font-weight:600}}
"""
def logo(ink, acc=LIME): return f'<div class="foot"><span style="display:inline-flex;align-items:center;gap:14px">{SYM(48,dots=ink,accent=acc)}{WORD(38,ink,acc)}</span></div>'
def st(i, bg, ink, body, foot):
    return f'<section class="st" id="st{i}" style="background:{BG[bg]};color:{ink}">{body}{foot}</section>'
def step(n, on_ink, off, cur, dark):
    segs = "".join(f'<div style="flex:1;display:flex;flex-direction:column;gap:12px"><i style="height:10px;border-radius:9px;background:{LIME if k<=cur else off}"></i><span style="font-size:24px;font-weight:600;color:{on_ink if k==cur else (MUTD if dark else MUTL)}">{t}</span></div>' for k,t in enumerate(["Fundação","Inteligência","Agentes de IA"]))
    return f'<div style="display:flex;gap:14px">{segs}</div>'

S = []
# 1 abertura · mesh
S.append(st(1,"mesh","#fff",f'''<span class="pill" style="background:rgba(146,197,73,.18);color:{LIME};border:1px solid rgba(146,197,73,.5)">Como funciona</span>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:48px">
<h1 style="font-size:132px;line-height:134px">Como funciona a <span style="color:{LIME}">4metrics?</span></h1>
<p style="color:#C9D3D9">Do dado espalhado à resposta pronta. Em 30 dias.</p>
<div style="display:flex;gap:16px;margin-top:20px">{"".join(f'<span class="chip" style="background:rgba(255,255,255,.08);color:#fff;border:1px solid rgba(255,255,255,.18)">{t}</span>' for t in ("F","I","A"))}</div></div>''',logo("#fff")))
# 2 quote · névoa
col = lambda title, items, hl: f'''<div class="card" style="flex:1;background:{'#fff' if not hl else NAVY};color:{NAVY if not hl else '#fff'};border:1px solid {'#DCE6D3' if not hl else NAVY};{'box-shadow:0 0 40px rgba(146,197,73,.35)' if hl else ''}">
<div style="font-size:28px;font-weight:700;color:{G if not hl else LIME};margin-bottom:22px">{title}</div>{"".join(f'<div style="font-size:34px;line-height:52px">{x}</div>' for x in items)}</div>'''
S.append(st(2,"nevoa",NAVY,f'''<span class="pill" style="background:#fff;color:{G};border:1px solid #CFE3B6">Software with a service</span>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:64px">
<h1>Você só acessa.<br><span style="color:{G}">A gente constrói o resto.</span></h1>
<div style="display:flex;gap:20px">{col("Você",["Acessa","Pergunta","Decide"],False)}{col("4metrics",["Conecta","Modela","Governa"],True)}</div></div>''',logo(NAVY)))
# 3 fundação · sweep
srcs = ["CRM","ERP","Mídia paga","Planilhas","+50 fontes"]
S.append(st(3,"sweep",NAVY,f'''{step(0,NAVY,"#DCE3DE",0,False)}
<div style="font-family:'Plus Jakarta Sans';font-size:34px;font-weight:700;color:{G};margin-top:40px">SEMANAS 1 E 2</div>
<h2>Fundação.</h2>
<p style="color:{MUTL}">Integramos as suas fontes e escrevemos as regras do seu negócio.</p>
<div style="flex:1;display:flex;align-items:center;justify-content:center"><div style="position:relative;width:880px;height:640px">
{"".join(f'<span class="chip" style="position:absolute;left:{x}px;top:{y}px;background:#fff;border:1px solid #DCE3DE;box-shadow:0 10px 30px rgba(5,19,28,.06);color:{NAVY}">{t}</span>' for t,(x,y) in zip(srcs,[(0,40),(560,0),(20,520),(600,500),(300,600)]))}
<div style="position:absolute;left:300px;top:180px;width:280px;height:280px;border-radius:40px;background:{NAVY};display:flex;align-items:center;justify-content:center;box-shadow:0 0 0 2px rgba(146,197,73,.8),0 0 60px rgba(146,197,73,.45)">{SYM(150,dots="#fff",accent=LIME)}</div></div></div>''',logo(NAVY)))
# 4 inteligência · dark
def badge(t,c,bg,m,a): return f'''<div class="card" style="background:#14232C;border:1px solid #2B3640;display:flex;flex-direction:column;gap:16px">
<span style="align-self:flex-start;display:inline-flex;align-items:center;gap:12px;height:50px;padding:0 20px;border-radius:999px;background:{bg};color:{c};font-size:26px;font-weight:700"><i style="width:12px;height:12px;border-radius:9px;background:{c}"></i>{t}</span>
<span style="font-size:36px;font-weight:600;color:#fff">{m}</span><span style="font-size:30px;color:{MUTD}">→ {a}</span></div>'''
S.append(st(4,"dark","#fff",f'''{step(1,"#fff","#2B3640",1,True)}
<div style="font-family:'Plus Jakarta Sans';font-size:34px;font-weight:700;color:{LIME};margin-top:40px">SEMANAS 3 E 4</div>
<h2>Inteligência.</h2>
<p style="color:{MUTD}">Resumo executivo do dia: o que está crítico e o próximo passo.</p>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:20px">
{badge("Crítico","#F97066","#3A1A1A","Receita faturada","recuperar o ticket médio")}
{badge("Atenção","#F5C451","#3A2E12","Funil comercial","destravar contatos parados")}
{badge("Destaque",LIME,"#16301F","Conversão de leads","mais vendas, mesmo volume")}</div>''',logo("#fff")))
# 5 agentes · lima
ch = lambda t: f'<div class="card" style="background:rgba(255,255,255,.55);border:1px solid rgba(5,19,28,.12);display:flex;align-items:center;gap:22px;font-size:38px;font-weight:600"><i style="width:18px;height:18px;border-radius:9px;background:#fff;box-shadow:0 0 0 3px {NAVY}"></i>{t}</div>'
S.append(st(5,"lima",NAVY,f'''{step(2,NAVY,"rgba(5,19,28,.18)",2,False).replace(LIME,"#FFFFFF")}
<div style="font-family:'Plus Jakarta Sans';font-size:34px;font-weight:700;color:{NAVY};margin-top:40px">TODO DIA</div>
<h2>Agentes de IA.</h2>
<p style="color:#1F3A12">A resposta chega até você, antes da reunião.</p>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:20px">{ch("E-mail")}{ch("Slack")}{ch("Teams")}</div>''',logo(NAVY,"#FFFFFF")))
# 6 30 dias · glow
S.append(st(6,"glow","#fff",f'''<div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:20px">
<div style="font-family:'Plus Jakarta Sans';font-size:420px;line-height:380px;font-weight:700;letter-spacing:-0.06em;color:{LIME}">30</div>
<div style="font-family:'Plus Jakarta Sans';font-size:64px;font-weight:700">dias para o primeiro insight.</div>
<div style="display:flex;flex-direction:column;gap:18px;margin-top:60px">
<span class="chip" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18)">Sem trocar de ferramenta</span>
<span class="chip" style="background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.18)">Sem montar time de dados</span></div></div>''',logo("#fff")))
# 7 depois + CTA · névoa2
row = lambda a,b: f'<div style="display:flex;border-top:1px solid #DCE6D3"><div style="flex:1;padding:26px 0;font-size:32px;color:{MUTL};text-decoration:line-through">{a}</div><div style="flex:1;padding:26px 0;font-size:32px;font-weight:600">{b}</div></div>'
S.append(st(7,"nevoa2",NAVY,f'''<span class="pill" style="background:#fff;color:{G};border:1px solid #CFE3B6">E depois?</span>
<h1>A gente fica <span style="color:{G}">do seu lado.</span></h1>
<div class="card" style="background:#fff;border:1px solid #DCE6D3;padding:20px 40px 10px">
<div style="display:flex;padding:14px 0"><span style="flex:1;font-size:26px;font-weight:700;color:{MUTL}">PROJETO DE BI</span><span style="flex:1;font-size:26px;font-weight:700;color:{G}">4METRICS</span></div>
{row("Entrega única","Assinatura que evolui")}{row("Dashboard é o fim","Resposta + próximo passo")}{row("Pergunta nova = orçamento","Pergunte para a IA")}</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:24px">
<div style="display:inline-flex;align-self:flex-start;align-items:center;height:110px;padding:0 48px;border-radius:16px;background:{NAVY};color:#fff;font-size:40px;font-weight:600;box-shadow:0 0 0 2px rgba(146,197,73,.8),0 0 40px rgba(146,197,73,.35)">Responda: <span style="color:{LIME};margin-left:14px">DIAGNÓSTICO</span></div>
<p style="color:{MUTL};font-size:34px">A gente mostra por onde começar com os seus dados.</p></div>''',logo(NAVY)))
# capa do destaque
nodes = f'''<svg width="520" height="520" viewBox="0 0 520 520"><path d="M80 400 L200 260 L320 330 L440 140" stroke="{NAVY}" stroke-width="22" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="80" cy="400" r="44" fill="{NAVY}"/><circle cx="200" cy="260" r="44" fill="{NAVY}"/><circle cx="320" cy="330" r="44" fill="{NAVY}"/><circle cx="440" cy="140" r="60" fill="#FFFFFF"/></svg>'''
cover = f'<section class="st" id="st0" style="background:{BG["lima"]};align-items:center;justify-content:center">{nodes}</section>'

html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{''.join(S)}{cover}</body></html>"
open(f"{D}/st.html","w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width":1080,"height":1920})
    pg.goto(f"file://{D}/st.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(900)
    print(pg.evaluate("""()=>[...document.querySelectorAll('section')].map(s=>{const r=s.getBoundingClientRect();return s.id+':'+[...s.querySelectorAll('*')].filter(e=>{const q=e.getBoundingClientRect();return q.width&&(q.right>r.right+1||q.bottom>r.bottom-150||q.left<r.left-1)&&!e.closest('.foot')&&e.tagName!='circle'&&e.tagName!='path'}).length})"""))
    for i in range(0,8): pg.locator(f"#st{i}").screenshot(path=f"{D}/2026-11-23-como-funciona-{i:02d}.png")
    b.close()
from PIL import Image
sh=Image.new('RGB',(8*370+10,660),'#888')
for k in range(1,9):
    i = k % 8
    sh.paste(Image.open(f"{D}/2026-11-23-como-funciona-{i:02d}.png").convert('RGB').resize((360,640),Image.LANCZOS),(10+(k-1)*370,10))
sh.save(f"{D}/visao-geral-como-funciona.png")

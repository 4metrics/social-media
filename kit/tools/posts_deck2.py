import sys, os, re
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from stories import ff, TH, NAVY, LIME
from PIL import Image

OUT = "/home/claude/out/posts-deck2"; os.makedirs(OUT, exist_ok=True)
FOT = "/home/claude/assets/fotos"; SITE = "/home/claude/out/4metrics-site-v2"; TEL = "/home/claude/deck/img/telas"
LOGOS = "/home/claude/assets/logos-ia"
RED = "#C8372D"
CSS = ff + """*{box-sizing:border-box} body{margin:0;background:#888}
.s{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;background-size:22px 22px;margin-bottom:20px}
h1,h2,.d{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em}
p{margin:0}
.mk{display:inline-block;line-height:1.08;margin-top:.1em;white-space:nowrap;background:#92C549;color:#05131C;padding:0 .14em;border-radius:8px}
.pill{display:inline-flex;align-items:center;height:48px;padding:0 22px;border-radius:999px;font-size:24px;font-weight:600}
.shot{border-radius:22px;box-shadow:0 18px 50px rgba(5,19,28,.18);display:block}
"""
def mk(t, s): return f'<span style="color:{LIME}">{s}</span>' if t["bg"] == NAVY else f'<span class="mk">{s}</span>'
def logo(t, s=40): return f'<span style="display:inline-flex;align-items:center;gap:12px">{SYM(s,dots=t["dots"],accent=t["acc"])}{WORD(s*0.8,t["txt"],t["idot"])}</span>'
def u(p): return f"file://{p}"

def frame(sid, th, inner, photo=None, mesh=True, glow=None, logo_pos="bl"):
    t = TH[th]
    bg = ""
    if photo:
        bg = f'<img src="{u(FOT+"/"+photo[0])}" style="position:absolute;left:0;top:0;width:100%;height:{photo[1]}px;object-fit:cover;object-position:{photo[2] if len(photo)>2 else "center"}">'
    g = ""
    if glow: g = f'<div style="position:absolute;left:{glow[0]}px;top:{glow[1]}px;width:{glow[2]}px;height:{glow[2]}px;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.35),rgba(146,197,73,0))"></div>'
    m = f'background-image:radial-gradient({t["mesh"]} 1px,transparent 1.2px);' if mesh else ''
    lg = f'<div style="position:absolute;left:72px;bottom:64px">{logo(t)}</div>' if logo_pos == "bl" else (f'<div style="position:absolute;right:72px;top:72px">{logo(t)}</div>' if logo_pos == "tr" else "")
    return f'<section class="s" id="{sid}" style="background-color:{t["bg"]};{m}color:{t["txt"]}">{bg}{g}{inner(t)}{lg}</section>'

def box(x, y, w, h, inner, extra=""):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;{("height:%dpx;" % h) if h else ""}{extra}">{inner}</div>'
def bubble(s, size=34, side="l", bg=LIME, tx=NAVY):
    r = "30px 30px 30px 8px" if side == "l" else "30px 30px 8px 30px"
    return f'<div style="display:inline-block;background:{bg};color:{tx};font-size:{size}px;line-height:{round(size*1.3)}px;font-weight:600;padding:20px 30px;border-radius:{r}">{s}</div>'
def lg_ai(n, s=48): return re.sub(r'<title>.*?</title>', '', open(f"{LOGOS}/{n}.svg").read()).replace('<svg ', f'<svg width="{s}" height="{s}" ')
def cta_btn(t, s="Comente DIAGNÓSTICO"):
    bg, tx = (NAVY, "#FFFFFF") if t["bg"] == LIME else (LIME, NAVY)
    return f'<div style="display:inline-flex;align-items:center;gap:16px;height:96px;padding:0 40px;border-radius:18px;background:{bg};color:{tx};font-size:34px;font-weight:700">{s}</div>'

# ===================== CARROSSEL 1 · "3 finais" =====================
def c1_1(t):  # foto + interface
    return (f'<div style="position:absolute;left:0;top:560px;width:1080px;height:790px;background:linear-gradient(180deg,rgba(5,19,28,0) 0%,#05131C 26%)"></div>'
            + box(72, 380, 936, 0, bubble("Por que as vendas caíram este mês?", 40), "")
            + box(72, 640, 936, 0, f'<h1 style="font-size:92px;line-height:98px;color:#FFFFFF">Essa pergunta tem 4 finais na sua empresa. {mk(t,"Só 1 é bom.")}</h1>'
                  f'<p style="margin-top:28px;font-size:34px;line-height:46px;color:#9AA7B0">Arraste e descubra qual é o seu.</p>'))
def c1_2(t):
    chip = lambda a, v, rot, x, y: box(x, y, 560, 0, f'<div style="transform:rotate({rot}deg);background:#FFFFFF;border:1px solid #E1E7E4;border-radius:24px;padding:28px 34px;box-shadow:0 14px 40px rgba(5,19,28,.10)"><p style="font-size:28px;color:#4F5B63;font-weight:600">{a}</p><p class="d" style="font-size:84px;line-height:92px">{v}</p></div>')
    return (box(72, 110, 936, 0, f'<span class="pill" style="background:#F4F7F5;color:#4F5B63">Final 1</span><h2 style="margin-top:28px;font-size:80px;line-height:86px">Cada área chega com {mk(t,"um número.")}</h2>')
            + chip("Marketing", "R$ 1,2 mi", -4, 90, 500) + chip("Comercial", "R$ 1,4 mi", 3, 430, 700) + chip("Financeiro", "R$ 980 mil", -2, 150, 900)
            + box(72, 1160, 936, 0, f'<p style="font-size:30px;color:#4F5B63;text-align:right">E a reunião vira debate sobre qual está certo.</p>'))
def c1_3(t):
    msg = lambda s, me, tm: (f'<div style="display:flex;justify-content:{"flex-end" if me else "flex-start"}"><div style="max-width:720px;background:{"#DCF2C4" if me else "#FFFFFF"};border-radius:22px;padding:20px 26px;box-shadow:0 2px 0 rgba(5,19,28,.06)">'
                             f'<p style="font-size:32px;line-height:42px">{s}</p><p style="font-size:22px;color:#7F8D88;text-align:right;margin-top:4px">{tm}</p></div></div>')
    chat = ('<div style="background:#EFEAE2;border-radius:28px;padding:28px;display:flex;flex-direction:column;gap:16px;border:1px solid #E1E7E4">'
            '<p style="font-size:24px;color:#4F5B63;font-weight:600;text-align:center;margin-bottom:6px">Time de dados</p>'
            + msg("Consegue puxar as vendas por canal do último mês?", True, "seg 09:12")
            + msg("Consigo sim! Tenho 3 pedidos antes do seu.", False, "seg 11:40")
            + msg("Te mando até sexta.", False, "seg 11:41")
            + msg("Ok… a reunião é amanhã.", True, "seg 11:43") + '</div>')
    return (box(72, 110, 936, 0, f'<span class="pill" style="background:#FFFFFF;color:#4F5B63">Final 2</span><h2 style="margin-top:28px;font-size:80px;line-height:86px">A pergunta {mk(t,"vira pedido.")}</h2>')
            + box(72, 450, 936, 0, chat))
def c1_4(t):
    ans = lambda v, c, note: (f'<div style="background:#14232C;border:1px solid #2B3640;border-radius:24px;padding:26px 30px;display:flex;align-items:center;justify-content:space-between">'
                              f'<div><p style="font-size:24px;color:#9AA7B0">{note}</p><p class="d" style="font-size:72px;line-height:80px;color:{c}">{v}</p></div>'
                              f'<p style="font-size:26px;color:#9AA7B0;text-align:right">Fonte:<br>não informada</p></div>')
    return (box(72, 110, 936, 0, f'<span class="pill" style="background:#16301F;color:{LIME}">Final 3</span><h2 style="margin-top:28px;font-size:80px;line-height:86px">Você cola a planilha na IA. {mk(t,"Ela chuta.")}</h2>')
            + box(72, 560, 936, 0, '<div style="display:flex;flex-direction:column;gap:22px">'
                  + f'<div style="align-self:flex-end">{bubble("Qual foi a receita de junho?", 30, "r")}</div>'
                  + ans("R$ 1,3 mi", "#FFFFFF", "Segunda-feira") + ans("R$ 1,1 mi", "#F06A5B", "Terça-feira, mesma pergunta") + '</div>'))
def c1_5(t):
    img = f'<img class="shot" src="{u("/home/claude/deck/img/pergunte-crop.png")}" style="width:760px;box-shadow:none;margin:0 auto">'
    return (box(72, 110, 936, 0, f'<span class="pill" style="background:{NAVY};color:{LIME}">Final 4 · o bom</span><h2 style="margin-top:28px;font-size:76px;line-height:84px">A resposta chega na hora. {mk(t,"Com o próximo passo.")}</h2>')
            + box(72, 440, 936, 0, img))
def c1_6(t):
    nums = "".join(f'<div style="width:190px;height:190px;border-radius:40px;background:{"#92C549" if n=="4" else "#14232C"};border:1px solid {"#92C549" if n=="4" else "#2B3640"};color:{NAVY if n=="4" else "#FFFFFF"};display:flex;align-items:center;justify-content:center" class="d"><span style="font-size:110px">{n}</span></div>' for n in "1234")
    return (box(72, 200, 936, 0, f'<h2 style="font-size:88px;line-height:94px">E na sua empresa, {mk(t,"qual é o final?")}</h2>'
                f'<p style="margin-top:28px;font-size:34px;line-height:46px;color:#9AA7B0">Comenta o número.</p>')
            + box(72, 640, 936, 0, f'<div style="display:flex;justify-content:space-between">{nums}</div>')
            + box(72, 950, 936, 0, f'<p style="font-size:30px;color:#FFFFFF;margin-bottom:22px">Quer chegar no 4? A 4metrics conecta os seus dados e a sua IA às regras do seu negócio.</p>' + cta_btn(t)))
C1 = [("escuro", c1_1, ("px-7644064.jpg", 760, "center 30%"), False, None), ("claro", c1_2, None, True, None), ("nevoa", c1_3, None, False, None),
      ("escuro", c1_4, None, True, (600, -200, 700)), ("claro", c1_5, None, True, (300, 400, 800)), ("escuro", c1_6, None, True, (520, 520, 760))]

# ===================== CARROSSEL 2 · "Segunda, 9h" =====================
def c2_1(t):
    tabs = ["CRM", "Meta Ads", "ERP", "planilha_v3_final.xlsx", "Power BI"]
    tb = "".join(f'<div style="display:flex;align-items:center;gap:10px;height:62px;padding:0 22px;border-radius:14px 14px 0 0;background:{"#FFFFFF" if i==4 else "rgba(255,255,255,.55)"};font-size:24px;font-weight:600;white-space:nowrap">{s}<span style="color:#7F8D88">×</span></div>' for i, s in enumerate(tabs))
    return (box(72, 150, 936, 0, f'<p class="d" style="font-size:44px;line-height:52px">Segunda-feira, 9h.</p>'
                f'<h1 style="margin-top:20px;font-size:112px;line-height:114px">5 abas abertas pra responder {mk(t,"1 pergunta.") if False else "1 pergunta."}</h1>')
            + box(0, 800, 1300, 0, f'<div style="display:flex;gap:8px;padding-left:72px">{tb}</div><div style="height:300px;background:#FFFFFF;padding:44px 72px;display:flex;flex-direction:column;gap:22px"><div style="width:520px;height:22px;border-radius:11px;background:#E1E7E4"></div><div style="width:760px;height:22px;border-radius:11px;background:#EEF2F0"></div><div style="width:640px;height:22px;border-radius:11px;background:#EEF2F0"></div><div style="width:380px;height:22px;border-radius:11px;background:#EEF2F0"></div></div>'))
def c2_2(t):
    row = lambda s, tg: (f'<div style="display:flex;align-items:center;gap:24px;padding:26px 0;border-bottom:1px solid #E1E7E4"><span style="width:44px;height:44px;border-radius:99px;border:3px solid #C9D3CE;flex:none"></span>'
                         f'<p style="font-size:38px;line-height:46px;color:#4F5B63;text-decoration:line-through;text-decoration-color:{RED};text-decoration-thickness:3px">{s}</p><span style="margin-left:auto;font-size:24px;color:#7F8D88">{tg}</span></div>')
    return (box(72, 130, 936, 0, f'<h2 style="font-size:84px;line-height:90px">Isso não é análise. {mk(t,"É montagem.")}</h2>')
            + box(72, 480, 936, 0, row("Exportar de cada ferramenta", "CRM · Ads · ERP") + row("Cruzar em planilha", "Excel") + row("Montar a visão no BI", "Power BI · Data Studio") + row("Esperar a próxima atualização", "toda semana")))
def c2_3(t):
    return (box(72, 110, 936, 0, f'<h2 style="font-size:76px;line-height:84px">E o dashboard? Mostra o que aconteceu. {mk(t,"Não diz o que fazer.")}</h2>')
            + box(-40, 450, 1120, 0, f'<img class="shot" src="{u(TEL+"/dashboards-dinamicos-desktop.png")}" style="width:1120px;transform:rotate(-3deg)">'))
def c2_4(t):
    bars = "".join(f'<div style="width:52px;height:{h}px;border-radius:10px;background:{c}"></div>' for h, c in [(60,"#C9D3CE"),(70,"#C9D3CE"),(54,"#C9D3CE"),(72,"#C9D3CE"),(78,"#C9D3CE"),(160,RED)])
    ans = (f'<div style="background:#FFFFFF;border:1px solid #E1E7E4;border-radius:28px;padding:34px 38px;box-shadow:0 18px 50px rgba(5,19,28,.12)">'
           f'<div style="display:flex;align-items:center;gap:12px;font-size:26px;font-weight:700;margin-bottom:18px">{SYM(30,dots=NAVY,accent=LIME)} 4metrics</div>'
           f'<div style="display:flex;justify-content:space-between;align-items:flex-end"><div><p style="font-size:26px;color:#4F5B63">CPL de junho</p><p class="d" style="font-size:80px;line-height:88px">R$ 17,51</p><p style="font-size:30px;color:{RED};font-weight:600">▲ +49,9% vs maio</p></div>'
           f'<div style="display:flex;gap:12px;align-items:flex-end">{bars}</div></div>'
           f'<div style="margin-top:26px;background:#EAF5DD;border-radius:18px;padding:22px 26px"><p style="font-size:22px;font-weight:700;color:#406500">PRÓXIMO PASSO</p><p style="font-size:30px;line-height:40px;margin-top:6px">Revisar os criativos com menor conversão.</p></div></div>')
    return (box(72, 110, 936, 0, f'<p class="d" style="font-size:44px;color:#406500">Agora é assim:</p><h2 style="margin-top:14px;font-size:84px;line-height:90px">Você pergunta. {mk(t,"Ponto.")}</h2>')
            + box(72, 470, 936, 0, f'<div style="text-align:right;margin-bottom:24px">{bubble("Por que o CPL subiu em junho?", 34, "r")}</div>' + ans))
def c2_5(t):
    chip = lambda n, l: f'<div style="display:flex;align-items:center;gap:18px;background:#FFFFFF;border:1px solid #E1E7E4;border-radius:99px;padding:16px 36px 16px 20px;font-size:38px;font-weight:700;box-shadow:0 10px 30px rgba(5,19,28,.08)">{lg_ai(n,56)}{l}</div>'
    return (box(72, 120, 936, 0, f'<h2 style="font-size:84px;line-height:90px">Até na IA que {mk(t,"você já usa.")}</h2>'
                f'<p style="margin-top:26px;font-size:34px;line-height:46px;color:#4F5B63">Com o MCP, o seu assistente responde com os dados da sua empresa. E com as regras dela.</p>')
            + box(72, 600, 936, 0, f'<div style="display:flex;flex-direction:column;gap:22px;align-items:flex-start">{chip("chatgpt","ChatGPT")}<div style="margin-left:120px">{chip("claude","Claude")}</div><div style="margin-left:240px">{chip("gemini","Gemini")}</div></div>'))
def c2_6(t):
    return (box(72, 300, 936, 0, f'<h1 style="font-size:120px;line-height:120px">Pare de montar.<br>Comece a perguntar.</h1>'
                f'<p style="margin-top:36px;font-size:36px;line-height:48px;color:#1F3A12">A 4metrics conecta as suas fontes, organiza os dados e cria as regras do seu negócio. O resto é pergunta.</p>'
                f'<div style="margin-top:48px">{cta_btn(t)}</div>'))
C2 = [("lima", c2_1, None, True, None), ("claro", c2_2, None, True, None), ("escuro", c2_3, None, True, (500, 300, 900)),
      ("nevoa", c2_4, None, False, None), ("claro", c2_5, None, True, (500, 500, 800)), ("lima", c2_6, None, True, None)]

# ===================== CARROSSEL 3 · "achismo em 14 dias" =====================
def c3_1(t):
    return (f'<div style="position:absolute;left:0;top:520px;width:1080px;height:830px;background:linear-gradient(180deg,rgba(5,19,28,0) 0%,#05131C 30%)"></div>'
            + box(72, 760, 936, 0, f'<h1 style="font-size:100px;line-height:104px;color:#FFFFFF">Como sair do achismo {mk(t,"em 14 dias.")}</h1>'
                  f'<p style="margin-top:26px;font-size:34px;line-height:46px;color:#9AA7B0">Sem contratar time de dados. Sem trocar de ferramenta.</p>'))
def letter(L, bg, tx): return f'<div class="d" style="width:200px;height:200px;border-radius:48px;background:{bg};color:{tx};display:flex;align-items:center;justify-content:center;font-size:130px">{L}</div>'
def c3_2(t):
    return (box(72, 110, 936, 0, f'<div style="display:flex;align-items:center;gap:36px">{letter("F","#EAF5DD","#406500")}<div><p style="font-size:28px;color:#4F5B63;font-weight:600">Semana 1</p><h2 style="font-size:84px;line-height:88px">Fundação</h2></div></div>'
                f'<p style="margin-top:34px;font-size:38px;line-height:50px">A gente junta CRM, ERP, mídia e planilhas {mk(t,"num lugar só.")} E escreve as regras do seu negócio.</p>')
            + box(40, 640, 1000, 0, f'<img src="{u(SITE+"/metodo/construcao-camada-claro-estatico.webp")}" style="width:1000px">'))
def c3_3(t):
    return (box(72, 110, 936, 0, f'<div style="display:flex;align-items:center;gap:36px">{letter("I","#FFFFFF","#406500")}<div><p style="font-size:28px;color:#3D4A3F;font-weight:600">Semana 2</p><h2 style="font-size:84px;line-height:88px">Inteligência</h2></div></div>'
                f'<p style="margin-top:34px;font-size:38px;line-height:50px">Você abre a plataforma e {mk(t,"já vê onde agir.")}</p>')
            + box(72, 520, 1150, 0, f'<img class="shot" src="{u(TEL+"/resumo-executivo-desktop.png")}" style="width:1150px">'))
def c3_4(t):
    return (box(72, 110, 936, 0, f'<div style="display:flex;align-items:center;gap:36px">{letter("A",LIME,NAVY)}<div><p style="font-size:28px;color:#9AA7B0;font-weight:600">Todo dia</p><h2 style="font-size:84px;line-height:88px">Agentes de IA</h2></div></div>'
                f'<p style="margin-top:34px;font-size:38px;line-height:50px">A resposta {mk(t,"chega até você:")} no e-mail, no Slack, no Teams. Antes da reunião.</p>')
            + box(60, 620, 960, 0, f'<div style="background:#FFFFFF;border-radius:28px;padding:20px"><img src="{u(SITE+"/plataforma/decisao-chega-claro-estatico.webp")}" style="width:920px;display:block"></div>'))
def c3_5(t):
    return (box(72, 260, 936, 0, f'<p class="d" style="font-size:300px;line-height:280px;letter-spacing:-0.05em">14</p><h2 style="font-size:84px;line-height:90px">dias até o primeiro insight.</h2>'
                f'<p style="margin-top:30px;font-size:36px;line-height:48px;color:#1F3A12">Quem faz é a 4metrics. Você só decide.</p><div style="margin-top:44px">{cta_btn(t)}</div>'))
C3 = [("escuro", c3_1, ("px-8134173.jpg", 900, "center 35%"), False, None), ("claro", c3_2, None, True, None), ("nevoa", c3_3, None, False, None),
      ("escuro", c3_4, None, True, (560, 400, 700)), ("lima", c3_5, None, True, None)]

# ===================== POST · Segurança =====================
def p1(t):
    return (box(72, 760, 936, 0, f'<h1 style="font-size:86px;line-height:92px">Você colaria a planilha de vendas {mk(t,"num chat aberto?")}</h1>'
                f'<p style="margin-top:26px;font-size:32px;line-height:44px;color:#4F5B63">Com a 4metrics, a IA consulta os seus dados com regras e permissões. Sem você expor nada.</p>'))
P = [("claro", p1, ("px-12903349.jpg", 700, "center 25%"), True, None)]

SETS = {"c1-quatro-finais": C1, "c2-segunda-9h": C2, "c3-achismo-30-dias": C3, "post-seguranca": P}
from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    b = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": 1080, "height": 1350})
    for name, sl in SETS.items():
        html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + "".join(frame(f"s{i+1}", th, fn, ph, ms, gl) for i, (th, fn, ph, ms, gl) in enumerate(sl)) + "</body></html>"
        open(f"{OUT}/{name}.html", "w").write(html)
        pg.goto(f"file://{OUT}/{name}.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1000)
        files = []
        for i in range(len(sl)):
            f = f"{OUT}/{name}-{i+1:02d}.png" if len(sl) > 1 else f"{OUT}/{name}.png"
            pg.locator(f"#s{i+1}").screenshot(path=f); files.append(f)
        ims = [Image.open(f) for f in files]
        sh = Image.new("RGB", (len(ims) * 370 + 10, 470), "#E1E7E4")
        for k, im in enumerate(ims): sh.paste(im.resize((360, 450), Image.LANCZOS), (10 + k * 370, 10))
        sh.save(f"{OUT}/_{name}-visao.png")
        if len(ims) > 1:
            ims[0].convert("RGB").save(f"{OUT}/{name}-linkedin.pdf", save_all=True, append_images=[i.convert("RGB") for i in ims[1:]])
    b.close()
print("ok")

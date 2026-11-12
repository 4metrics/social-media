import sys
sys.path.insert(0, "/home/claude/tools")
from stories import *
from stories_plat import lab, wrap, ilus, p1, p2, p3, p4, p5


def btn(t):
    bg, fg = (NAVY, "#FFFFFF") if t["bg"] == LIME else (LIME, NAVY)
    return f'<span style="align-self:flex-start;display:inline-flex;align-items:center;height:110px;padding:0 52px;border-radius:14px;background:{bg};color:{fg};font-size:42px;font-weight:600">Agendar diagnóstico</span>'


def card(t, inner, pad=34, feat=False):
    b = "border:1px solid rgba(146,197,73,.7);box-shadow:0 0 36px rgba(146,197,73,.22)" if feat else f"border:1px solid {t['bor']}"
    return f'<div style="background:{t["card"]};{b};border-radius:28px;padding:{pad}px">{inner}</div>'


def chip(t, s, on=False, strike=False):
    st = f"background:{LIME};color:{NAVY};border:1px solid {LIME}" if on else f"background:{t['card']};color:{t['mut']};border:1px solid {t['bor']}"
    d = "text-decoration:line-through;text-decoration-thickness:3px;" if strike else ""
    return f'<span style="display:inline-flex;align-items:center;height:88px;padding:0 36px;border-radius:999px;font-size:36px;font-weight:600;{st};{d}">{s}</span>'


def layers(t, items, hi):
    out = ""
    for k, (s, w) in enumerate(items):
        on = k == hi
        st = f"background:{LIME};color:{NAVY};border:1px solid {LIME};box-shadow:0 0 30px rgba(146,197,73,.4)" if on else f"background:{t['card']};border:1px solid {t['bor']}"
        out += f'<div style="width:{w}px;height:120px;border-radius:24px;{st};display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:600">{s}</div>'
    return f'<div style="display:flex;flex-direction:column;align-items:center;gap:16px">{out}</div>'


# ---------- Método
def m1(t):
    tile = lambda L, on: f'<div style="flex:1;height:260px;border-radius:32px;display:flex;align-items:center;justify-content:center;font-family:\'Plus Jakarta Sans\';font-size:150px;font-weight:700;{"background:"+NAVY+";color:#FFFFFF" if on else "background:rgba(255,255,255,.4);color:"+NAVY}">{L}</div>'
    return wrap(f'<h1 style="font-size:124px;line-height:128px">Método F.I.A.</h1>'
                f'<p class="lead" style="color:{t["mut"]}">Três etapas para sair do relatório do mês e chegar à decisão do dia.</p>'
                f'<div style="display:flex;gap:20px">{tile("F",False)}{tile("I",False)}{tile("A",True)}</div>')


def m2(t):
    srcs = "".join(chip(t, s) for s in ["CRM", "Mídia", "ERP", "Planilhas"]) + chip(t, "+50 fontes de dados", on=True)
    base = f'<div style="height:120px;border-radius:24px;background:{LIME};color:{NAVY};display:flex;align-items:center;justify-content:center;font-size:38px;font-weight:600;box-shadow:0 0 30px rgba(146,197,73,.4)">Uma base, as mesmas regras</div>'
    return wrap(f'{lab(t,"F · Fundação")}<h1 style="margin-top:-20px">Conectamos e {hl(t,"organizamos tudo.")}</h1>'
                f'<p class="lead" style="color:{t["mut"]}">CRM, mídia, ERP, planilhas e mais de 50 fontes de dados, com as mesmas regras de negócio.</p>'
                f'<div style="display:flex;flex-direction:column;gap:28px"><div style="display:flex;flex-wrap:wrap;gap:16px">{srcs}</div>'
                f'<div style="text-align:center;font-size:52px;color:{LIME}">↓</div>{base}</div>')


def m3(t):
    def row(n, q, a, on=False):
        st = f"background:{LIME};color:{NAVY};border:1px solid {LIME};box-shadow:0 0 30px rgba(146,197,73,.35)" if on else f"background:{t['card']};border:1px solid {t['bor']}"
        sub = NAVY if on else t["mut"]
        return (f'<div style="border-radius:22px;padding:22px 28px;{st};display:flex;gap:20px;align-items:flex-start">'
                f'<span style="font-family:\'Plus Jakarta Sans\';font-size:30px;font-weight:700;opacity:.7;padding-top:6px">{n}</span>'
                f'<div><div style="font-size:38px;font-weight:700;line-height:46px">{q}</div><div style="font-size:28px;line-height:36px;color:{sub};margin-top:4px">{a}</div></div></div>')
    rows = (row("01", "Dado bruto", "<span style=\"font-family:monospace\">status = 'qlf_2'</span>, cada sistema com um nome.")
            + row("02", "Camada semântica", "'qlf_2' vira <b>Lead qualificado</b>.")
            + row("03", "Regras de negócio", "O que é venda e conversão na sua empresa.")
            + row("→", "Inteligência de verdade", "Um número que todo mundo entende e confia.", True))
    return wrap(f'{lab(t,"I · Inteligência")}<h1 style="margin-top:-20px;font-size:92px;line-height:98px">Dado vira {hl(t,"inteligência de verdade.")}</h1>'
                f'<p class="lead" style="color:{t["mut"]}">Criamos a camada semântica e as regras de negócio.</p>'
                f'<div style="display:flex;flex-direction:column;gap:16px">{rows}{ilus(t)}</div>')


def m4(t):
    q = f'<div style="align-self:flex-end;max-width:760px;background:{LIME};color:{NAVY};border-radius:32px 32px 8px 32px;padding:30px 36px;font-size:38px;line-height:50px;font-weight:600">Onde o funil travou esta semana?</div>'
    a = (f'<div style="align-self:flex-start;max-width:840px;background:#FFFFFF;color:{NAVY};border:1px solid {t["bor"]};border-radius:32px 32px 32px 8px;padding:30px 36px;font-size:36px;line-height:50px">'
         f'Na etapa de proposta: a conversão caiu de 34% para 27% desde terça.</div>')
    return wrap(f'{lab(t,"A · Agentes de IA")}<h1 style="margin-top:-20px">A IA trabalha em cima de {hl(t,"uma base confiável.")}</h1>'
                f'<p class="lead" style="color:{t["mut"]}">E responde perguntas sobre o seu funil.</p>'
                f'<div style="display:flex;flex-direction:column;gap:22px">{q}{a}{ilus(t)}</div>')


def m5(t):
    return wrap(f'{lab(t,"A ordem importa")}<h1 style="margin-top:-20px">Sem fundação, {hl(t,"a IA não fica de pé.")}</h1>'
                f'{layers(t,[("A · Agentes de IA",560),("I · Inteligência",740),("F · Fundação",900)],2)}{reply(t)}')


# ---------- Era da IA
def e1(t):
    return wrap(f'<h1 style="font-size:112px;line-height:118px">A era da IA mudou a forma como as empresas trabalham {hl(t,"com dados.")}</h1>'
                f'<div style="display:flex;flex-direction:column;gap:20px;align-items:flex-start">{chip(t,"Relatório do mês",strike=True)}'
                f'<span style="font-size:52px;color:{LIME};padding-left:40px">↓</span>{chip(t,"Dado diário + IA",on=True)}</div>')


def e2(t):
    rows = "".join(f'<div style="display:flex;border-top:1px solid {t["bor"]}">' + "".join(f'<div style="flex:1;height:86px;border-left:1px solid {t["bor"]};padding:24px 20px;font-size:28px;color:{t["mut"]}">{c}</div>' for c in r) + '</div>'
                   for r in [["Canal", "Leads", "Vendas"], ["Google", "?", "?"], ["Meta", "?", "?"], ["CRM", "?", "?"]])
    sheet = (f'<div style="border:1px solid {t["bor"]};border-radius:24px;overflow:hidden;background:#F4F7F5"><div style="display:flex;justify-content:space-between;padding:26px 24px">'
             f'<span style="font-size:26px;font-weight:600;color:{t["mut"]}">relatorio_outubro_FINAL.xlsx</span><span style="font-size:26px;font-weight:600;color:#D92D20">dia 30</span></div>'
             f'<div style="background:#FFFFFF">{rows}</div></div>')
    return wrap(f'{lab(t,"Antes")}<h1 style="margin-top:-20px;color:{t["mut"]}">Dado era relatório.</h1>'
                f'<p class="lead" style="color:{t["mut"]}">Chegava no fim do mês e explicava o passado.</p>{sheet}')


def e3(t):
    node = lambda s, on=False: f'<div style="height:110px;padding:0 40px;border-radius:24px;display:flex;align-items:center;font-size:38px;font-weight:600;{"background:"+LIME+";color:"+NAVY if on else "background:#FFFFFF;border:1px solid "+t["bor"]}">{s}</div>'
    viz = (f'<div style="display:flex;align-items:center;justify-content:space-between">'
           f'<div style="width:300px;height:300px;border-radius:40px;background:#FFFFFF;border:1px solid rgba(146,197,73,.8);box-shadow:0 0 36px rgba(146,197,73,.3);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px">{SYM(150,dots=NAVY,accent=LIME)}<span style="font-size:24px;font-weight:600;color:#406500">atualizado hoje</span></div>'
           f'<span style="font-size:56px;color:#406500">→</span><div style="display:flex;flex-direction:column;gap:20px">{node("Seu time")}{node("Sua IA",True)}</div></div>')
    return wrap(f'{lab(t,"Agora")}<h1 style="margin-top:-20px">Dado é {hl(t,"ativo.")}</h1>'
                f'<p class="lead" style="color:{t["mut"]}">Integrado, diário, lido por pessoas e por IA.</p>{viz}')


def e4(t):
    return wrap(f'{lab(t,"O que não mudou")}<h1 style="margin-top:-20px">IA com dado desorganizado só {hl(t,"erra mais rápido.")}</h1>'
                f'{layers(t,[("IA e agentes",560),("Painéis e análises",740),("Dados integrados e confiáveis",900)],2)}')


def e5(t):
    return wrap(f'<div>{SYM(200,dots=t["dots"],accent=t["acc"])}</div>'
                f'<h1>Nessa nova era, a 4metrics está {hl(t,"ao lado da sua empresa.")}</h1>{reply(t)}')


# ---------- covers
def ic_tiles(t):  # Plataforma: 2x2 tiles, top-right lime (echo of the symbol)
    c = "#FFFFFF"
    return (f'<svg width="420" height="420" viewBox="0 0 420 420">'
            f'<rect x="40" y="40" width="150" height="150" rx="36" fill="none" stroke="{c}" stroke-width="18"/>'
            f'<rect x="230" y="40" width="150" height="150" rx="36" fill="{LIME}"/>'
            f'<rect x="40" y="230" width="150" height="150" rx="36" fill="none" stroke="{c}" stroke-width="18"/>'
            f'<rect x="230" y="230" width="150" height="150" rx="36" fill="none" stroke="{c}" stroke-width="18"/></svg>')


def ic_steps(t):  # Método: three rising dots joined, last one lime and bigger
    return (f'<svg width="440" height="420" viewBox="0 0 440 420"><polyline points="70,330 210,230 360,110" fill="none" stroke="{NAVY}" stroke-width="16" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<circle cx="70" cy="330" r="46" fill="{NAVY}"/><circle cx="210" cy="230" r="46" fill="{NAVY}"/><circle cx="360" cy="110" r="62" fill="{LIME}"/></svg>')


def ic_spark(t):  # Era da IA: navy sparkle + small lime sparkle
    star = lambda cx, cy, r, f: f'<path d="M{cx},{cy-r} C{cx+r*0.18},{cy-r*0.18} {cx+r*0.18},{cy-r*0.18} {cx+r},{cy} C{cx+r*0.18},{cy+r*0.18} {cx+r*0.18},{cy+r*0.18} {cx},{cy+r} C{cx-r*0.18},{cy+r*0.18} {cx-r*0.18},{cy+r*0.18} {cx-r},{cy} C{cx-r*0.18},{cy-r*0.18} {cx-r*0.18},{cy-r*0.18} {cx},{cy-r} Z" fill="{f}"/>'
    return f'<svg width="420" height="420" viewBox="0 0 420 420">{star(185,235,165,NAVY)}{star(335,95,72,LIME)}</svg>'


if __name__ == "__main__":
    ST = {"metodo": [("lima", m1), ("claro", m2), ("escuro", m3), ("nevoa", m4), ("escuro", m5)],
          "era-da-ia": [("escuro", e1), ("claro", e2), ("nevoa", e3), ("escuro", e4), ("lima", e5)],
          "plataforma": [("escuro", p1), ("claro", p2), ("nevoa", p3), ("escuro", p4), ("lima", p5)]}
    CV = {"metodo": ("claro", ic_steps), "era-da-ia": ("nevoa", ic_spark), "plataforma": ("escuro", ic_tiles)}
    LB = {"metodo": "Método", "era-da-ia": "Era da IA", "plataforma": "Plataforma"}
    import sys as _s
    only=_s.argv[1:] or list(ST)
    run({k:ST[k] for k in only}, CV, LB)

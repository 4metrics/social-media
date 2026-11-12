import sys
sys.path.insert(0, "/home/claude/tools")
from stories import *


def lab(t, s): return f'<span style="font-size:34px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:{t["hl"]}">{s}</span>'
def wrap(x): return f'<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:52px">{x}</div>'
def ilus(t): return ""


def p1(t):
    chip = lambda s: f'<div style="height:96px;width:300px;border-radius:20px;background:{t["card"]};border:1px solid {t["bor"]};display:flex;align-items:center;justify-content:center;font-size:36px;font-weight:600">{s}</div>'
    bars = "".join(f'<rect x="{20+k*52}" y="{170-h}" width="34" height="{h}" rx="7" fill="{LIME if k==6 else "#3A4A52"}"/>' for k, h in enumerate([60, 85, 70, 110, 95, 120, 150]))
    dots3 = "".join(f'<i style="width:16px;height:16px;border-radius:99px;background:{t["bor"]}"></i>' for _ in range(3))
    kpis = "".join(f'<div style="flex:1;height:80px;border-radius:14px;border:1px solid {t["bor"]};padding:12px 14px"><div style="font-size:18px;color:{t["mut"]}">{a}</div><div style="font-size:28px;font-weight:700">{b}</div></div>' for a, b in [("Vendas", "+8%"), ("Leads", "+12%"), ("CAC", "−5%")])
    win = (f'<div style="width:470px;height:420px;border-radius:28px;background:{t["card"]};border:1px solid rgba(146,197,73,.6);box-shadow:0 0 40px rgba(146,197,73,.2);padding:26px;display:flex;flex-direction:column;gap:16px">'
           f'<div style="display:flex;gap:10px">{dots3}</div><div style="display:flex;gap:12px">{kpis}</div>'
           f'<svg width="418" height="190" viewBox="0 0 400 190">{bars}</svg></div>')
    return wrap(f'<h1>Tudo num {hl(t,"lugar só.")}</h1>'
                f'<p class="lead" style="color:{t["mut"]}">Uma plataforma para ver vendas, marketing e CRM juntos.</p>'
                f'<div style="display:flex;align-items:center;justify-content:space-between"><div style="display:flex;flex-direction:column;gap:16px">{chip("Vendas")}{chip("Marketing")}{chip("CRM")}</div>'
                f'<span style="font-size:52px;color:{LIME}">→</span>{win}</div>')


def p2(t):
    vals = [40, 55, 48, 70, 62, 88, 80, 105]
    poly = " ".join(f"{20+i*50},{150-v}" for i, v in enumerate(vals))
    card = (f'<div style="background:{t["card"]};border:1px solid {t["bor"]};border-radius:28px;padding:36px;display:flex;flex-direction:column;gap:22px;box-shadow:0 12px 32px rgba(5,19,28,.06)">'
            f'<div style="display:flex;align-items:center;gap:16px;font-size:34px;font-weight:600"><span style="width:22px;height:22px;border-radius:99px;background:{LIME};box-shadow:0 0 16px {LIME}"></span>Atualizado hoje, 06:00</div>'
            f'<div style="font-size:28px;color:{t["mut"]}">Receita de ontem</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline"><div style="font-family:\'Plus Jakarta Sans\';font-size:112px;line-height:116px;font-weight:700;letter-spacing:-0.03em">R$ 84 mil</div></div>'
            f'<svg width="860" height="170" viewBox="0 0 400 170" preserveAspectRatio="none"><polyline points="{poly}" fill="none" stroke="{LIME}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg></div>')
    return wrap(f'{lab(t,"Dados atualizados todo dia")}'
                f'<h1 style="margin-top:-20px">Você abre de manhã e o número de ontem {hl(t,"já está lá.")}</h1>{card}')


def p3(t):
    kpi = lambda a, b, c: (f'<div style="flex:1;border:1px solid #E1E7E4;border-radius:20px;padding:22px"><div style="font-size:24px;color:#4F5B63">{a}</div>'
                           f'<div style="font-family:\'Plus Jakarta Sans\';font-size:52px;font-weight:700;letter-spacing:-0.02em;white-space:nowrap">{b}</div>'
                           f'<div style="font-size:22px;color:#406500;font-weight:600">{c}</div></div>')
    fun = "".join(f'<div style="display:flex;align-items:center;gap:18px"><span style="width:210px;font-size:28px;color:#4F5B63">{l}</span><div style="height:48px;width:{w*5.6}px;border-radius:10px;background:{LIME if l=="Vendas" else "#C9D6CF"}"></div></div>'
                  for l, w in [("Leads", 100), ("Qualificados", 62), ("Propostas", 34), ("Vendas", 18)])
    dash = (f'<div style="background:#FFFFFF;border:1px solid {t["bor"]};border-radius:28px;padding:34px;display:flex;flex-direction:column;gap:28px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font-family:\'Plus Jakarta Sans\';font-size:34px;font-weight:700">Painel de receita</span></div>'
            f'<div style="display:flex;gap:14px">{kpi("Receita","R$ 1,2 mi","+8%")}{kpi("CAC","R$ 310","−5%")}{kpi("ROAS","4,1","+0,3")}</div>'
            f'<div style="display:flex;flex-direction:column;gap:16px">{fun}</div></div>')
    return wrap(f'{lab(t,"Painéis prontos")}<h1 style="margin-top:-20px">O seu time {hl(t,"não precisa montar nada.")}</h1>{dash}')


def p4(t):
    me = f'<div style="align-self:flex-end;max-width:760px;background:{LIME};color:{NAVY};border-radius:32px 32px 8px 32px;padding:30px 36px;font-size:38px;line-height:50px;font-weight:600">Qual canal trouxe mais receita ontem?</div>'
    ai = (f'<div style="align-self:flex-start;max-width:820px;background:{t["card"]};border:1px solid {t["bor"]};border-radius:32px 32px 32px 8px;padding:30px 36px;font-size:36px;line-height:50px">'
          f'<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;font-size:26px;color:{t["mut"]}">{SYM(36,dots=t["dots"],accent=LIME)} IA da 4metrics</div>'
          f'Google Ads: <b>R$ 48 mil</b>, 38% do total. Meta ficou <b style="color:#F97066">12% abaixo</b> da média da semana.</div>')
    return wrap(f'{lab(t,"Converse com os seus dados")}'
                f'<h1 style="margin-top:-20px">Pergunte para a IA. {hl(t,"Ela responde com os seus números.")}</h1>'
                f'<div style="display:flex;flex-direction:column;gap:24px">{me}{ai}{ilus(t)}</div>')


def p5(t):
    lock = (f'<svg width="200" height="230" viewBox="0 0 200 230"><path d="M50,100 V70 a50,50 0 0 1 100,0 V100" fill="none" stroke="{NAVY}" stroke-width="18" stroke-linecap="round"/>'
            f'<rect x="20" y="100" width="160" height="125" rx="30" fill="{NAVY}"/><circle cx="100" cy="160" r="18" fill="#FFFFFF"/></svg>')
    return wrap(f'<div>{lock}</div>{lab(t,"Segurança")}'
                f'<h1 style="margin-top:-20px">Seu próprio ambiente de dados.</h1>'
                f'<p class="lead" style="color:{t["mut"]}">Em infraestrutura Google Cloud.</p>'
                f'{reply(t)}')


def ic_panel(t):
    bars = "".join(f'<rect x="{80+k*70}" y="{320-h}" width="44" height="{h}" rx="10" fill="{LIME if k==3 else "#FFFFFF"}"/>' for k, h in enumerate([90, 140, 115, 200]))
    return f'<svg width="420" height="420" viewBox="0 0 420 420"><rect x="30" y="50" width="360" height="320" rx="44" fill="none" stroke="#FFFFFF" stroke-width="18"/>{bars}</svg>'


if __name__ == "__main__":
    STORIES["plataforma"] = [("escuro", p1), ("claro", p2), ("nevoa", p3), ("escuro", p4), ("lima", p5)]
    COVERS["plataforma"] = ("escuro", ic_panel)
    run({"plataforma": STORIES["plataforma"]}, COVERS, {"sobre-nos": "Sobre nós", "plataforma": "Plataforma"})

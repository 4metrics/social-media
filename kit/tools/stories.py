import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD

FS = "/home/claude/fonts/fs"
ff = ""
for fam, pkg, pre in [("Inter", "fontsource-inter-5.3.0", "inter"), ("Plus Jakarta Sans", "fontsource-plus-jakarta-sans-5.3.0", "plus-jakarta-sans")]:
    for w in (400, 500, 600, 700):
        ff += f"@font-face{{font-family:'{fam}';src:url('file://{FS}/{pkg}/package/files/{pre}-latin-{w}-normal.woff2') format('woff2');font-weight:{w}}}"

NAVY, LIME, WHT = "#05131C", "#92C549", "#FFFFFF"
# MIV surfaces
TH = {
 "claro":  dict(bg="#FFFFFF", mesh="rgba(5,19,28,0.07)", txt=NAVY, mut="#4F5B63", hl="#406500", card="#FFFFFF", bor="#E1E7E4", pill_bg="#EAF5DD", pill_tx="#406500", dots=NAVY, acc=LIME, idot=LIME, glow=0.26),
 "nevoa":  dict(bg="#EAF5DD", mesh="rgba(5,19,28,0.07)", txt=NAVY, mut="#3D4A3F", hl="#406500", card="#FFFFFF", bor="#CFE3B6", pill_bg="#FFFFFF", pill_tx="#406500", dots=NAVY, acc=LIME, idot=LIME, glow=0.0),
 "escuro": dict(bg=NAVY, mesh="rgba(255,255,255,0.09)", txt=WHT, mut="#9AA7B0", hl=LIME, card="#14232C", bor="#2B3640", pill_bg="#16301F", pill_tx=LIME, dots=WHT, acc=LIME, idot=LIME, glow=0.24),
 "lima":   dict(bg=LIME, mesh="rgba(5,19,28,0.10)", txt=NAVY, mut="#1F3A12", hl=NAVY, card="rgba(255,255,255,0.35)", bor="rgba(5,19,28,0.15)", pill_bg="rgba(255,255,255,0.4)", pill_tx=NAVY, dots=NAVY, acc=WHT, idot=WHT, glow=0.0),
}

CSS = ff + """*{box-sizing:border-box} body{margin:0}
.st{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:'Inter',sans-serif;
 background-size:24px 24px;padding:250px 90px 330px;display:flex;flex-direction:column;gap:44px;margin-bottom:20px}
.g{position:absolute;border-radius:999px;pointer-events:none}
.pill{align-self:flex-start;display:inline-flex;align-items:center;height:56px;padding:0 26px;border-radius:999px;font-size:26px;font-weight:600}
h1{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em;font-size:104px;line-height:110px}
.lead{margin:0;font-size:44px;line-height:60px}
.foot{position:absolute;left:90px;right:90px;bottom:250px;display:flex;justify-content:space-between;align-items:center}
"""

def story(sid, th, label, body, glows=True):
    t = TH[th]
    gl = ""
    if t["glow"]:
        gl = f'<div class="g" style="left:480px;top:-200px;width:900px;height:900px;background:radial-gradient(closest-side,rgba(146,197,73,{t["glow"]}),rgba(146,197,73,0))"></div>'
    logo = f'<span style="display:inline-flex;align-items:center;gap:14px">{SYM(48,dots=t["dots"],accent=t["acc"])}{WORD(38,t["txt"],t["idot"])}</span>'
    return f'''<section class="st" id="{sid}" style="background-color:{t["bg"]};background-image:radial-gradient({t["mesh"]} 1px,transparent 1.2px);color:{t["txt"]}">{gl}
<span class="pill" style="position:relative;background:{t["pill_bg"]};color:{t["pill_tx"]};border:1px solid {t["bor"]}">{label}</span>
{body(t)}
<div class="foot">{logo}</div></section>'''

def reply(t):
    on_lime = t["bg"] == LIME
    bar_bg = "rgba(255,255,255,0.45)" if on_lime else ("rgba(255,255,255,0.08)" if t["bg"] == NAVY else "#FFFFFF")
    bor = "rgba(5,19,28,0.25)" if on_lime else t["bor"]
    acc = NAVY if on_lime else LIME
    return (f'<div style="display:flex;flex-direction:column;gap:22px">'
            f'<div style="font-size:40px;line-height:52px;font-weight:600">Responda este story com <span style="font-weight:800;color:{acc if not on_lime else NAVY};{"text-decoration:underline;text-decoration-thickness:5px;text-underline-offset:8px" if on_lime else ""}">DIAGNÓSTICO</span> e a gente te atende.</div>'
            f'<div style="display:flex;align-items:center;gap:20px;height:112px;padding:0 36px;border-radius:999px;background:{bar_bg};border:2px solid {bor}">'
            f'<span style="flex:1;font-size:36px;color:{t["mut"]}">Enviar mensagem…</span>'
            f'<svg width="52" height="52" viewBox="0 0 24 24"><path d="M3 11.5 21 3l-8.5 18-2-7.5z" fill="none" stroke="{t["txt"]}" stroke-width="2" stroke-linejoin="round"/></svg></div>'
            f'<div style="text-align:center;font-size:56px;color:{acc}">↓</div></div>')


def hl(t, s): return f'<span style="color:{t["hl"]}">{s}</span>'

# ---------- Sobre nós
def s1(t):
    return f'''<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:56px">
<div>{SYM(220,dots=t["dots"],accent=t["acc"])}</div>
<h1 style="font-size:120px;line-height:124px">Prazer, somos a 4metrics.</h1>
<p class="lead" style="color:{t["mut"]}">Revenue Intelligence para vendas, marketing e CRM.</p></div>'''

def s2(t):
    def c(src, v, l):
        return f'<div style="flex:1;background:{t["card"]};border:1px solid {t["bor"]};border-radius:24px;padding:28px 26px"><div style="font-size:26px;color:{t["mut"]}">{src}</div><div style="font-family:\'Plus Jakarta Sans\';font-size:84px;line-height:92px;font-weight:700;letter-spacing:-0.03em">{v}</div><div style="font-size:24px;color:{t["mut"]}">{l}</div></div>'
    row = lambda txt: f'<div style="display:flex;gap:20px;align-items:center;font-size:44px;line-height:56px;font-weight:600"><span style="flex:none;width:18px;height:18px;border-radius:99px;background:#F97066"></span>{txt}</div>'
    return f'''<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:56px">
<h1>O problema que {hl(t,"a gente resolve.")}</h1>
<div style="display:flex;flex-direction:column;gap:26px">{row("Dados espalhados.")}{row("Cada ferramenta com um número.")}{row("Relatório que chega no fim do mês.")}</div>
<div style="display:flex;gap:18px">{c("CRM","142","vendas")}{c("Mídia","168","conversões")}{c("Financeiro","131","pedidos")}</div></div>'''

def s3(t):
    def step(n, txt, on=False):
        st = f"background:{LIME};color:{NAVY};border:1px solid {LIME};box-shadow:0 0 28px rgba(146,197,73,0.4)" if on else f"background:{t['card']};border:1px solid {t['bor']}"
        return f'<div style="display:flex;align-items:center;gap:24px;height:120px;padding:0 36px;border-radius:24px;{st};font-size:44px;font-weight:600"><span style="font-family:\'Plus Jakarta Sans\';font-size:30px;font-weight:700;opacity:.7">{n}</span>{txt}</div>'
    return f'''<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:56px">
<span style="font-size:34px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:{t["hl"]}">O nosso jeito</span>
<h1 style="margin-top:-24px">A gente integra, modela e entrega tudo dentro da plataforma.</h1>
<div style="display:flex;flex-direction:column;gap:16px">{step("01","Integra")}{step("02","Modela")}{step("03","Entrega")}{step("→","Você só acessa.",True)}</div></div>'''

def s4(t):
    chip = lambda s: f'<span style="display:inline-flex;align-items:center;height:88px;padding:0 40px;border-radius:999px;background:{t["card"]};border:1px solid {t["bor"]};font-size:40px;font-weight:600">{s}</span>'
    return f'''<div style="position:relative;flex:1;display:flex;flex-direction:column;justify-content:center;gap:56px">
<span style="font-size:34px;font-weight:700;letter-spacing:0.08em;text-transform:uppercase;color:{t["hl"]}">Para quem</span>
<h1 style="margin-top:-24px">Times comerciais e de marketing que precisam decidir com {hl(t,"o número de hoje.")}</h1>
<div style="display:flex;gap:18px;flex-wrap:wrap">{chip("Comercial")}{chip("Marketing")}{chip("CRM")}</div>
<div style="align-self:flex-start;display:inline-flex;align-items:center;gap:16px;height:88px;padding:0 36px;border-radius:20px;background:{NAVY};color:{WHT};font-size:36px;font-weight:600"><span style="width:20px;height:20px;border-radius:99px;background:{LIME};box-shadow:0 0 14px {LIME}"></span>Atualizado hoje, 06:00</div></div>'''

def cover(th, icon):
    t = TH[th]
    return f'''<section class="st" id="cover" style="background:{t["bg"]};padding:0;display:flex;align-items:center;justify-content:center">
<div style="width:620px;height:620px;border-radius:999px;display:flex;align-items:center;justify-content:center">{icon(t)}</div></section>'''

STORIES = {"sobre-nos": [("lima", s1), ("escuro", s2), ("claro", s3), ("nevoa", s4)]}
COVERS = {"sobre-nos": ("lima", lambda t: SYM(420, dots=t["dots"], accent=t["acc"]))}

def run(STORIES, COVERS, LABELS):
    from playwright.sync_api import sync_playwright
    from PIL import Image
    D = "/home/claude/out/destaques"; os.makedirs(D, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": 1080, "height": 1920})
        for key, items in STORIES.items():
            secs = "".join(story(f"s{i+1}", th, LABELS[key], fn) for i, (th, fn) in enumerate(items))
            cth, ic = COVERS[key]
            html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{secs}{cover(cth, ic)}</body></html>"
            open(f"{D}/{key}.html", "w").write(html)
            pg.goto(f"file://{D}/{key}.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
            files = []
            for i in range(len(items)):
                f = f"{D}/destaque-{key}-{i+1:02d}.png"; pg.locator(f"#s{i+1}").screenshot(path=f); files.append(f)
            pg.locator("#cover").screenshot(path=f"{D}/destaque-{key}-capa.png")
            ims = [Image.open(f) for f in files] + [Image.open(f"{D}/destaque-{key}-capa.png")]
            W_, H_ = 360, 640
            sh = Image.new("RGB", (len(ims) * (W_ + 10) + 10, H_ + 20), "#E1E7E4")
            for k, im in enumerate(ims): sh.paste(im.resize((W_, H_), Image.LANCZOS), (10 + k * (W_ + 10), 10))
            sh.save(f"{D}/destaque-{key}-visao-geral.png")
        b.close()
    print("ok")

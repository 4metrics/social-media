# 4metrics · peças sociais no padrão do Design System (artifact "4metrics")
# Desenho em tamanho lógico (feed 540x675, story 540x960) com os tokens exatos do DS
# e exportação em deviceScaleFactor 2 (1080x1350 e 1080x1920).
import os
FS = "/home/claude/fonts/fs"
LOGOS = "/home/claude/social-media/kit/logos"
PH = "/home/claude/out/stock/full"

ff = ""
for fam, pkg, pre in [("Inter", "fontsource-inter-5.3.0", "inter"), ("Plus Jakarta Sans", "fontsource-plus-jakarta-sans-5.3.0", "plus-jakarta-sans")]:
    for w in (400, 500, 600, 700):
        ff += f"@font-face{{font-family:'{fam}';src:url('file://{FS}/{pkg}/package/files/{pre}-latin-{w}-normal.woff2') format('woff2');font-weight:{w}}}"

# tokens.json do DS (claro / escuro) + fundos de feed do MIV (névoa, lima)
THEMES = {
 "light": dict(surface="#FFFFFF", subtle="#F4F7F5", raised="#FFFFFF", border="#E1E7E4", bstrong="#7F8D88", ink="#05131C", muted="#4F5B63",
               brand="#92C549", onbrand="#05131C", strong="#406500", bsub="#EAF5DD", crit="#C8372D", critsub="#FBE9E7", warn="#A85F05", warnsub="#FCF0DC",
               pos="#3E7D12", possub="#EAF5DD", glow="rgba(146,197,73,0.20)", sglow="0 0 0 1px rgba(146,197,73,0.15), 0 0 24px rgba(146,197,73,0.22)", dots="rgba(5,19,28,0.08)", mark="mark"),
 "dark": dict(surface="#05131C", subtle="#14232C", raised="#14232C", border="#2B3640", bstrong="#66757F", ink="#FFFFFF", muted="#9AA7B0",
              brand="#92C549", onbrand="#05131C", strong="#92C549", bsub="#16301F", crit="#F06A5B", critsub="#3A1E1E", warn="#E8A33D", warnsub="#3A2C14",
              pos="#92C549", possub="#1E3318", glow="rgba(146,197,73,0.24)", sglow="0 0 0 1px rgba(146,197,73,0.12), 0 0 28px rgba(146,197,73,0.16)", dots="rgba(255,255,255,0.08)", mark="strong"),
}
THEMES["nevoa"] = {**THEMES["light"], "surface": "#EAF5DD", "subtle": "#FFFFFF", "bsub": "#FFFFFF"}
THEMES["lima"] = {**THEMES["light"], "surface": "#92C549", "subtle": "rgba(255,255,255,0.45)", "raised": "#FFFFFF", "border": "rgba(5,19,28,0.16)", "muted": "#1F3A12", "strong": "#05131C", "bsub": "#FFFFFF", "dots": "rgba(5,19,28,0.10)", "mark": "none"}
THEMES["photo"] = THEMES["dark"]

def css_vars(t):
    return ";".join(f"--{k}:{v}" for k, v in t.items() if k != "mark")

CSS = ff + """
*{box-sizing:border-box} body{margin:0;background:#888}
.f{position:relative;overflow:hidden;display:flex;flex-direction:column;font-family:'Inter',system-ui,sans-serif;color:var(--ink);background-color:var(--surface);
   background-image:radial-gradient(var(--dots) 1px,transparent 1.2px);background-size:22px 22px;margin-bottom:10px;-webkit-font-smoothing:antialiased;font-variant-numeric:tabular-nums}
.fe{width:540px;height:675px;padding:32px 32px 76px;gap:16px}
.st{width:540px;height:960px;padding:120px 32px 140px;gap:24px}
.st{justify-content:center} .st .mid{flex:none} .st>.badge{position:absolute;top:120px;left:32px}
.glow{position:absolute;width:420px;height:420px;right:-120px;top:-160px;border-radius:999px;background:radial-gradient(closest-side,var(--glow),transparent);pointer-events:none}
.display{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-size:56px;line-height:60px;font-weight:700;letter-spacing:-0.02em}
.h1{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-size:36px;line-height:44px;font-weight:700;letter-spacing:-0.01em}
.h2{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;line-height:32px;font-weight:600}
.h3{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-size:18px;line-height:26px;font-weight:600}
.body{margin:0;font-size:16px;line-height:24px}
.small{margin:0;font-size:14px;line-height:20px}
.label{font-size:13px;line-height:18px;font-weight:500;color:var(--muted)}
.muted{color:var(--muted)}
.mxl{font-family:'Plus Jakarta Sans',sans-serif;font-size:40px;line-height:44px;font-weight:700;letter-spacing:-0.02em}
.metric{font-family:'Plus Jakarta Sans',sans-serif;font-size:24px;line-height:32px;font-weight:700}
.mark{background:var(--brand);color:var(--onbrand);padding:0 6px;border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.strong{color:var(--strong)}
.badge{align-self:flex-start;display:inline-flex;align-items:center;gap:4px;font-size:13px;line-height:18px;font-weight:500;padding:2px 8px;border-radius:999px;background:var(--bsub);color:var(--strong);border:1px solid var(--glow)}
.lima .badge{background:rgba(255,255,255,0.45);color:#05131C;border-color:rgba(5,19,28,0.16)}
.photo .badge{background:#16301F}
.btn{align-self:flex-start;display:inline-flex;align-items:center;gap:8px;font-size:15px;line-height:20px;font-weight:600;padding:10px 18px;border-radius:8px;background:var(--brand);color:var(--onbrand)}
.lima .btn{background:#05131C;color:#FFFFFF}
.card{background:var(--raised);border:1px solid var(--border);border-radius:16px;padding:24px}
.card.insight{background:var(--bsub);border-color:transparent}
.card.feat{border-color:rgba(146,197,73,0.6);box-shadow:var(--sglow)}
.dot{width:8px;height:8px;border-radius:999px;display:inline-block;background:currentColor;flex:none}
.delta{display:inline-flex;align-items:baseline;gap:4px;font-size:13px;line-height:20px;font-weight:600;white-space:nowrap}
.delta.up{color:var(--strong)} .delta.down{color:var(--crit)} .delta .base{font-weight:400;color:var(--muted)}
.tbl{width:100%;border-collapse:collapse;font-size:14px;line-height:20px;background:var(--raised)}
.tbl th{text-align:left;font-size:13px;font-weight:500;color:var(--muted);background:var(--subtle);padding:8px 12px;border-bottom:1px solid var(--border)}
.tbl td{padding:12px;border-bottom:1px solid var(--border);vertical-align:top}
.tbl tr.sel td{background:var(--bsub)}
.mid{flex:1;display:flex;flex-direction:column;justify-content:center;gap:16px;position:relative}
.foot{position:absolute;left:32px;bottom:32px;display:flex;align-items:center}
.st .foot{bottom:64px}
.ph{position:relative;border-radius:16px;overflow:hidden;background-size:cover;background-position:center}
.ico{width:20px;height:20px;flex:none;stroke:currentColor;fill:none;stroke-width:1.5;stroke-linecap:round;stroke-linejoin:round}
"""

# ícones Lucide (traço 1.5)
LUCIDE = {
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "arrow-right": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
 "arrow-down": '<path d="M12 5v14"/><path d="m19 12-7 7-7-7"/>',
 "arrow-left-right": '<path d="M8 3 4 7l4 4"/><path d="M4 7h16"/><path d="m16 21 4-4-4-4"/><path d="M20 17H4"/>',
 "shield-check": '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/><path d="m9 12 2 2 4-4"/>',
 "refresh": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
 "mail": '<rect width="20" height="16" x="2" y="4" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
 "message": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
 "bot": '<path d="M12 8V4H8"/><rect width="16" height="12" x="4" y="8" rx="2"/><path d="M2 14h2"/><path d="M20 14h2"/><path d="M15 13v2"/><path d="M9 13v2"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/>',
}
def ico(n, size=20, color=None):
    c = f"color:{color};" if color else ""
    return f'<svg class="ico" viewBox="0 0 24 24" style="width:{size}px;height:{size}px;{c}">{LUCIDE[n]}</svg>'

def title(text, kw, cls="display", theme="light", style=""):
    m = THEMES[theme]["mark"]
    if kw:
        assert kw in text, (kw, text)
        rep = {"mark": f'<span class="mark">{kw}</span>', "strong": f'<span class="strong">{kw}</span>', "none": kw}[m]
        text = text.replace(kw, rep, 1)
    return f'<h1 class="{cls}" style="{style}">{text}</h1>'

def logo(theme):
    if theme == "lima":
        return f'<img src="file://{LOGOS}/4metrics-logo-sobre-lima.svg" style="height:26px">'
    f = "4metrics-logotipo-negativo.svg" if theme in ("dark", "photo") else "4metrics-logotipo.svg"
    return f'<img src="file://{LOGOS}/{f}" style="height:20px">'

def photo_bg(pid, pos="center"):
    return (f"background-image:radial-gradient(rgba(255,255,255,0.08) 1px,transparent 1.2px),"
            f"linear-gradient(180deg,rgba(5,19,28,0.30) 0%,rgba(5,19,28,0.70) 45%,rgba(5,19,28,0.95) 100%),url(file://{PH}/{pid}.jpg);"
            f"background-size:22px 22px,cover,cover;background-position:0 0,center,{pos}")

def ph(pid, h, pos="center", radius="16px"):
    return f'<div class="ph" style="height:{h}px;border-radius:{radius};background-image:url(file://{PH}/{pid}.jpg);background-position:{pos}"></div>'

FR = []
def frame(name, kind, theme, body, badge=None, glow=True, photo=None, foot=True):
    t = THEMES[theme]
    extra = photo_bg(*photo) if photo else ""
    g = '<div class="glow"></div>' if glow and theme != "lima" else ""
    b = f'<span class="badge">{badge}</span>' if badge else ""
    lg = f'<div class="foot">{logo(theme)}</div>' if foot else ""
    FR.append((name, kind, f'<section class="f {kind} {theme}" id="x{len(FR)}" style="{css_vars(t)};{extra}">{g}{b}{body}{lg}</section>'))

# ---------- componentes
def btn(t="Agendar diagnóstico"): return f'<span class="btn">{t} {ico("arrow-right",18)}</span>'
def badge(t): return f'<span class="badge">{t}</span>'
def delta(v, base, up=True): return f'<span class="delta {"up" if up else "down"}">{"▲" if up else "▼"} {v} <span class="base">{base}</span></span>'
def metric(label, value, d=None, hero=True, feat=False, extra=""):
    return (f'<div class="card {"feat" if feat else ""}" style="display:grid;gap:8px;{extra}"><span class="label">{label}</span>'
            f'<span class="{"mxl" if hero else "metric"}">{value}</span>{d or ""}</div>')
def state(kind, text):
    k = {"crit": ("var(--crit)", "var(--critsub)"), "warn": ("var(--warn)", "var(--warnsub)"), "pos": ("var(--pos)", "var(--possub)")}[kind]
    return f'<span class="badge" style="background:{k[1]};color:{k[0]};border-color:transparent"><span class="dot"></span>{text}</span>'
def items(lst, icon="check"):
    return '<div style="display:flex;flex-direction:column;gap:8px">' + "".join(
        f'<div class="card" style="padding:12px 16px;display:flex;align-items:center;gap:12px"><span class="strong" style="display:flex">{ico(icon)}</span><span class="small" style="font-weight:500">{x}</span></div>' for x in lst) + '</div>'
def steps(lst):
    return '<div style="display:flex;flex-direction:column;gap:8px">' + "".join(
        f'<div class="card" style="padding:12px 16px;display:flex;align-items:center;gap:12px"><span class="badge" style="align-self:center;background:var(--brand);color:var(--onbrand);border-color:transparent">{i+1}</span><span class="small" style="font-weight:500">{x}</span></div>' for i, x in enumerate(lst)) + '</div>'
def chips(lst): return '<div style="display:flex;flex-wrap:wrap;gap:8px">' + "".join(f'<span class="badge" style="align-self:center">{x}</span>' for x in lst) + '</div>'
def progress(cur, labels=("Fundação","Inteligência","Agentes de IA")):
    return '<div style="display:flex;gap:8px">' + "".join(
        f'<div style="flex:1;display:flex;flex-direction:column;gap:6px"><i style="display:block;height:4px;border-radius:999px;background:{"var(--brand)" if k<=cur else "var(--border)"}"></i><span class="label" style="{"color:var(--ink)" if k==cur else ""}">{t}</span></div>' for k, t in enumerate(labels)) + '</div>'

def render(outdir, html_name="all.html"):
    os.makedirs(outdir, exist_ok=True)
    html = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>" + "".join(h for _, _, h in FR) + "</body></html>"
    open(f"{outdir}/{html_name}", "w").write(html)
    from playwright.sync_api import sync_playwright
    problems = []
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": 540, "height": 960}, device_scale_factor=2)
        pg.goto(f"file://{outdir}/{html_name}"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
        res = pg.evaluate("""()=>[...document.querySelectorAll('section')].map(s=>{const r=s.getBoundingClientRect();const f=s.querySelector('.foot');const ft=f?f.getBoundingClientRect().top:r.bottom;
          return [...s.querySelectorAll('*')].filter(e=>!e.closest('.foot')&&!e.classList.contains('glow')&&!e.closest('svg')).filter(e=>{const q=e.getBoundingClientRect();return q.width&&(q.right>r.right-0.5||q.left<r.left+0.5&&!e.classList.contains('ph')&&q.left<r.left-0.5||q.bottom>ft-6)}).length})""")
        for i, (name, kind, _) in enumerate(FR):
            loc = pg.locator(f"#x{i}"); loc.scroll_into_view_if_needed(); pg.wait_for_timeout(120)
            loc.screenshot(path=f"{outdir}/{name}.png")
            if res[i]: problems.append((name, res[i]))
        b.close()
    return problems

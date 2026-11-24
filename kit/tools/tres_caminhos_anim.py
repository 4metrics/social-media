# 4metrics · "Três jeitos de responder" animado (05/02/2027): carrossel simples com vídeo em cada tela
# Desenho no DS (ds4m) + animações CSS; captura quadro a quadro (Web Animations currentTime) → MP4 1080x1350.
import sys, os, subprocess, shutil
sys.path.insert(0, "/home/claude/tools")
import ds4m
from ds4m import *
V = "v4"
OUT = "/home/claude/out/tres-anim"
C = f"2027-02-05-tres-caminhos-{V}"
FPS, DUR = 30, 6.0

ds4m.CSS += """
.a{animation-fill-mode:both;animation-timing-function:cubic-bezier(.2,.7,.2,1)}
@keyframes up{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:none}}
@keyframes pop{0%{opacity:0;transform:scale(.85)}70%{transform:scale(1.04)}100%{opacity:1;transform:none}}
@keyframes kb{from{transform:scale(1)}to{transform:scale(1.10) translate(-2%,-1%)}}
@keyframes type{from{clip-path:inset(0 100% 0 0)}to{clip-path:inset(0 0 0 0)}}
@keyframes blink{0%,49%{opacity:1}50%,100%{opacity:0}}
@keyframes fill{from{width:0}to{width:100%}}
@keyframes on{from{background:var(--raised);color:var(--muted)}to{background:var(--brand);color:#05131C;border-color:var(--brand)}}
@keyframes flow{to{stroke-dashoffset:-16}}
@keyframes pulse{0%,100%{transform:scale(1)}50%{transform:scale(1.04)}}
@keyframes show{from{opacity:0}to{opacity:1}}
@keyframes hide{from{opacity:1}to{opacity:0}}
.stack{position:relative;display:inline-block}
.stack>span{position:absolute;left:0;top:0;opacity:0}
.stack>span:first-child{position:relative}
.node{width:44px;height:44px;border-radius:999px;display:flex;align-items:center;justify-content:center;border:1.5px solid var(--border);background:var(--raised);color:var(--muted);font-weight:700;font-size:15px}
.code{font-family:ui-monospace,Menlo,monospace;font-size:17px;line-height:24px;background:#05131C;color:#D7E3DC;border:1px solid #2B3640;border-radius:8px;padding:12px 16px}
.pill{display:inline-flex;align-items:center;height:32px;padding:0 14px;border-radius:999px;border:1.5px solid var(--brand);background:var(--raised);font-size:14px;font-weight:600}
"""
A = lambda name, dur, delay=0, extra="": f"animation:{name} {dur}s {delay}s both {extra};"

def cycle(values, period=0.6, start=0.0, stop=None):
    """números trocando sem parar (cada span aparece numa fatia do período)"""
    n = len(values); sl = period / n
    spans = []
    for i, v in enumerate(values):
        kf = f"cy{abs(hash((tuple(values), period, i)))%10**6}"
        a, b = i / n * 100, (i + 1) / n * 100
        ds4m.CSS += f"@keyframes {kf}{{0%,{a:.2f}%{{opacity:0}}{a+0.01:.2f}%,{b:.2f}%{{opacity:1}}{b+0.01:.2f}%,100%{{opacity:0}}}}"
        spans.append(f'<span style="animation:{kf} {period}s {start}s linear infinite">{v}</span>')
    inner = "".join(spans)
    hide = f'{A("hide", 0.01, stop)}' if stop is not None else ""
    return f'<span class="stack" style="{hide}">{inner}</span>'

# 01 · capa névoa: foto com zoom lento + pergunta digitada
frame(C+"-01", "fe", "nevoa", f'''<div class="mid" style="gap:0">
<div style="position:relative;height:360px;border-radius:16px;overflow:hidden"><div style="position:absolute;inset:0;background:url(file://{PH}/3184634.jpg) center 40%/cover;{A("kb", DUR, 0, "linear")}"></div></div>
<div style="margin:-48px 20px 0;position:relative;background:#05131C;color:#fff;border-radius:16px;padding:20px 24px;box-shadow:0 8px 24px rgba(5,19,28,.18);{A("up",0.5,0.2)}">
<h1 class="h1" style="color:#fff;margin:0"><span style="display:inline-block;{A("type",1.6,0.6,"steps(26)")}">Quanto vendemos este mês?</span></h1></div>
<p class="h3" style="margin-top:24px;display:flex;align-items:center;gap:8px;{A("up",0.5,2.6)}">Três jeitos de responder {ico("arrow-right",20)}</p></div>''', "IA com contexto")

# 02 · analista: trilha que anda devagar + contador de dias
etapas = ["Pergunta", "Fila", "SQL", "Dashboard"]
track = f'''<div style="position:relative;display:flex;justify-content:space-between;align-items:center">
<div style="position:absolute;left:22px;right:22px;top:21px;height:2px;background:var(--border)"><div style="height:100%;background:var(--brand);{A("fill",4.2,0.6,"linear")}"></div></div>
{"".join(f'<div style="display:grid;justify-items:center;gap:8px;position:relative"><span class="node" style="{A("on",0.3,0.6+i*1.4)}">{i+1}</span><span class="small" style="font-weight:500">{t}</span></div>' for i,t in enumerate(etapas))}</div>'''
def window(t0, t1=None):
    """visível só entre t0 e t1 (segundos), numa animação do tamanho do vídeo"""
    p0 = t0 / DUR * 100; p1 = (t1 / DUR * 100) if t1 else 100.01
    kf = f"w{int(t0*100)}_{int((t1 or 0)*100)}"
    ds4m.CSS += f"@keyframes {kf}{{0%,{max(p0-0.01,0):.2f}%{{opacity:0}}{p0:.2f}%,{min(p1-0.01,100):.2f}%{{opacity:1}}{min(p1,100):.2f}%,100%{{opacity:{0 if t1 else 1}}}}}"
    return f"animation:{kf} {DUR}s 0s linear both;"
dias = '<span class="stack mxl" style="font-size:72px;line-height:76px">' + "".join(
    f'<span style="{window(0.6+i*1.4, 0.6+(i+1)*1.4 if i<3 else None)}">D+{i}</span>' for i in range(4)) + '</span>'
frame(C+"-02", "fe", "light", f'''<span class="label">Caminho 1</span>{title("Analista de BI: certo, mas demora.", "demora", "h1", "light")}
<div class="mid" style="gap:32px">{track}<div class="card" style="display:flex;align-items:center;justify-content:space-between"><span class="body muted">Tempo até a resposta</span>{dias}</div>
<div style="display:flex;gap:8px;{A("up",0.4,5.0)}">{state("pos","Acerto alto")}{state("warn","Demora")}</div></div>''')

# 03 · IA sem contexto: número trocando sem parar
frame(C+"-03", "fe", "dark", f'''<span class="label">Caminho 2</span>{title("IA sem contexto: rápido, mas é chute.", "chute", "h1", "dark")}
<div class="mid" style="gap:16px"><div class="card" style="display:grid;gap:8px;{A("up",0.4,0.3)}"><span class="label">Clientes ativos</span>
<span class="mxl" style="font-size:64px;line-height:68px">{cycle(["1.284","1.112","1.390"],0.75,0.8)}</span></div>
<div class="code" style="{A("up",0.4,1.2)}">"cliente ativo" = <span style="color:#F06A5B;font-weight:700;animation:blink 0.8s 1.2s step-end infinite">???</span></div>
<div style="display:flex;gap:8px;{A("up",0.4,2.4)}">{state("pos","Rápido")}{state("crit","Acerto baixo")}</div></div>''')

# 04 · IA com contexto: linhas fluindo para o símbolo, número trava com selo
Wd, Hd = 476, 190
lines = "".join(f'<path d="M{x},34 C{x},110 238,80 238,140"/>' for x in (70, 238, 406))
hub = f'''<div style="position:relative;width:{Wd}px;height:{Hd}px">
<svg width="{Wd}" height="{Hd}" style="position:absolute;inset:0"><g style="stroke:var(--strong);stroke-width:2;stroke-dasharray:6 6;fill:none;animation:flow 0.6s linear infinite">{lines}</g></svg>
<div style="position:absolute;left:0;right:0;top:0;display:flex;justify-content:space-between">{"".join(f'<span class="pill" style="{A("up",0.4,0.2+i*0.2)}">{t}</span>' for i,t in enumerate(("Glossário","Camada semântica","Regras")))}</div>
<span style="position:absolute;left:{238-32}px;top:118px;width:64px;height:64px;border-radius:16px;background:#05131C;border:1px solid rgba(146,197,73,.6);box-shadow:var(--sglow);display:flex;align-items:center;justify-content:center;{A("pop",0.5,0.8)}"><img src="file://{LOGOS}/4metrics-simbolo-negativo.svg" style="width:42px;height:42px"></span></div>'''
frame(C+"-04", "fe", "nevoa", f'''<span class="label">Caminho 3</span>{title("IA com contexto: certo e na hora.", "na hora", "h1", "nevoa")}
<div class="mid" style="gap:20px">{hub}
<div class="card feat" style="display:grid;gap:8px;{A("up",0.4,1.2)}"><div style="display:flex;justify-content:space-between;align-items:center"><span class="label">Clientes ativos · número oficial</span><span style="{A("pop",0.4,2.6)}">{state("pos","Regra oficial")}</span></div>
<span class="mxl" style="font-size:64px;line-height:68px;position:relative">{cycle(["1.284","1.390","1.112"],0.45,1.2,2.4)}<span style="position:absolute;left:0;top:0;{A("show",0.01,2.4)}">1.112</span></span></div></div>''')

# 05 · camadas empilhando + CTA pulsando
def layer(t, sub, ch, i, feat=False):
    return f'<div class="card {"feat" if feat else ""}" style="padding:14px 18px;display:grid;gap:8px;{A("up",0.5,0.6+i*0.6)}"><div style="display:flex;justify-content:space-between;align-items:center"><span class="h3">{t}</span><span class="label">{sub}</span></div>{chips(ch)}</div>'
frame(C+"-05", "fe", "light", f'''{title("Quem escreve o contexto? A 4metrics.", "A 4metrics.", "h1", "light")}
<div class="mid" style="gap:10px">{layer("Suas fontes","sem trocar nada",["CRM","ERP","Mídia","Planilhas"],0)}
{layer("Camada semântica 4metrics","a gente constrói e mantém",["Glossário","Regras","Versões"],1,True)}
{layer("Sua IA e seus agentes","conexão única",["ChatGPT","Claude","Gemini","Copilot"],2)}</div>
<div style="{A("up",0.4,2.6)}"><span style="display:inline-block;animation:pulse 1.4s 3.2s ease-in-out infinite">{btn()}</span></div>''')

def capture():
    os.makedirs(OUT, exist_ok=True)
    html = f"<html><head><meta charset='utf-8'><style>{ds4m.CSS}</style></head><body>" + "".join(h for _, _, h in FR) + "</body></html>"
    open(f"{OUT}/anim.html", "w").write(html)
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
        pg = b.new_page(viewport={"width": 540, "height": 700}, device_scale_factor=2)
        pg.goto(f"file://{OUT}/anim.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1500)
        pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for i, (name, kind, _) in enumerate(FR):
            fd = f"{OUT}/frames/{name}"; shutil.rmtree(fd, ignore_errors=True); os.makedirs(fd)
            loc = pg.locator(f"#x{i}"); loc.scroll_into_view_if_needed()
            n = int(FPS * DUR)
            for k in range(n):
                pg.evaluate(f"document.getAnimations().forEach(a=>{{a.currentTime={k*1000/FPS}}})")
                loc.screenshot(path=f"{fd}/{k:04d}.png")
            shutil.copy(f"{fd}/{n-1:04d}.png", f"{OUT}/{name}.png")   # quadro final = versão estática (LinkedIn)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-framerate", str(FPS), "-i", f"{fd}/%04d.png",
                            "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-shortest",
                            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-profile:v", "high", "-r", str(FPS),
                            "-c:a", "aac", "-b:a", "64k", "-movflags", "+faststart", f"{OUT}/{name}.mp4"], check=True)
            print(name, "ok", flush=True)
        b.close()

if __name__ == "__main__":
    capture()

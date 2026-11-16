"""Vídeo 'Em 2027, seu time vai perguntar à IA' + MCP. Uso: python3 video_2027.py [preview|render] [9x16|4x5]"""
import sys, os, subprocess, wave
import numpy as np
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from stories import ff

mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
fmt = sys.argv[2] if len(sys.argv) > 2 else "9x16"
W, H = (1080, 1920) if fmt == "9x16" else (1080, 1350)
FPS, DUR = 30, 25.0
NAVY, LIME, GTXT, MUT, BOR, NEV, RED = "#05131C", "#92C549", "#406500", "#4F5B63", "#E1E7E4", "#EAF5DD", "#D92D20"
big = fmt == "9x16"
TS = 92 if big else 78          # título
GAP = 90 if big else 56
D = "/home/claude/out/video-2027"; os.makedirs(D, exist_ok=True)

# cenas: (in, out, html)
def title(t): return f'<h1 class="it" data-d="0">{t}</h1>'
def chip(t, extra=""): return f'<span class="chip" {extra}>{t}</span>'
def card(inner, cls="", d=0.25, style=""): return f'<div class="card it {cls}" data-d="{d}" style="{style}">{inner}</div>'

bubble = f'''<div class="it" data-d=".35" style="width:860px;display:flex;flex-direction:column;gap:22px">
 <div style="align-self:flex-end;max-width:720px;padding:30px 36px;background:{NAVY};color:#fff;border-radius:30px 30px 8px 30px;font-size:38px;line-height:50px">Qual canal trouxe as vendas que fecharam este mês?</div>
 <div class="it" data-d=".9" style="align-self:flex-start;display:flex;gap:12px;padding:30px 34px;background:#fff;border:1px solid {BOR};border-radius:30px 30px 30px 8px">
  <i class="dot" style="background:#C9D6CF"></i><i class="dot" style="background:#C9D6CF;animation-delay:.2s"></i><i class="dot" style="background:{LIME}"></i></div></div>'''

def src(t, d): return f'<div class="card it" data-d="{d}" style="width:300px;height:104px;border-radius:20px;display:flex;align-items:center;justify-content:center;gap:12px;font-size:32px;font-weight:600">{t}<span class="mcp">MCP</span></div>'
mcp = f'''<div style="display:flex;align-items:center;gap:36px">
 <div style="display:flex;flex-direction:column;gap:18px">{src("CRM",.3)}{src("Mídia",.45)}{src("ERP",.6)}</div>
 <div class="it" data-d=".8" style="font-size:52px;color:{GTXT}">→</div>
 <div class="card feat it" data-d=".95" style="width:300px;height:300px;border-radius:32px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:18px">
  <span style="font-family:'Plus Jakarta Sans';font-size:64px;font-weight:700">IA</span><span style="font-size:26px;color:{MUT}">do seu time</span></div></div>'''

def num(src_, n, lbl, d):
    return f'''<div class="card it" data-d="{d}" style="width:860px;height:120px;border-radius:22px;display:flex;align-items:center;justify-content:space-between;padding:0 40px">
 <span style="font-size:32px;font-weight:600">{src_} <span class="mcp">MCP</span></span>
 <span style="font-size:28px;color:{MUT}">{lbl} <b style="font-family:'Plus Jakarta Sans';font-size:52px;color:{NAVY};margin-left:14px">{n}</b></span></div>'''
nums = f'<div style="display:flex;flex-direction:column;gap:20px">{num("CRM","42","vendas",.3)}{num("Meta Ads","67","conversões",.5)}{num("ERP","38","pedidos",.7)}</div>'

erro = f'''<div class="card it" data-d=".3" style="width:860px;padding:44px;border-radius:28px;display:flex;flex-direction:column;gap:22px;border-color:#F4B4AE">
 <div style="display:flex;gap:16px;align-items:center"><i style="width:18px;height:18px;border-radius:99px;background:{RED}"></i><span style="font-size:30px;font-weight:600;color:{RED}">Resposta sem regra</span></div>
 <div style="font-size:36px;line-height:50px">“O canal campeão foi Meta Ads, com 67 vendas.”</div>
 <div class="it" data-d="1.0" style="font-size:28px;color:{MUT};border-top:1px solid {BOR};padding-top:20px">Mas no ERP, só 38 viraram pedido.</div></div>'''

base = f'''<div style="display:flex;flex-direction:column;align-items:center;gap:16px">
 <div class="it" data-d=".3" style="display:flex;gap:14px">{chip("CRM")}{chip("Mídia")}{chip("ERP")}{chip("Planilhas")}{chip("+50")}</div>
 <div class="it" data-d=".5" style="font-size:40px;color:{GTXT}">↓</div>
 <div class="card feat it" data-d=".7" style="width:860px;padding:36px 40px;border-radius:28px;display:flex;align-items:center;gap:30px">
  {SYM(110,dots=NAVY,accent=LIME)}<div style="display:flex;flex-direction:column;gap:8px"><span style="font-family:'Plus Jakarta Sans';font-size:40px;font-weight:700">Uma base. Um MCP.</span>
  <span style="font-size:28px;color:{MUT}">As mesmas regras de negócio para tudo.</span></div></div>
 <div class="it" data-d="1.1" style="font-size:40px;color:{GTXT}">↓</div>
 <div class="card it" data-d="1.3" style="width:860px;padding:30px 40px;border-radius:24px;font-size:32px;line-height:44px"><b>Meta Ads:</b> 38 vendas fechadas. <span style="color:{GTXT};font-weight:600">Bate com o ERP.</span></div></div>'''

cta = f'''<div style="display:flex;flex-direction:column;align-items:center;gap:44px">
 <div class="it" data-d=".2">{SYM(150,dots=NAVY,accent=LIME)}</div>
 <h1 class="it" data-d=".35" style="text-align:center">A IA responde.<br>A base decide <span class="hl">se está certa.</span></h1>
 <div class="it" data-d=".9"><span class="btn">Comente DIAGNÓSTICO</span></div></div>'''

S = [(0.0, 4.2, title('Em 2027, seu time vai perguntar <span class="hl">à IA.</span>') + bubble),
     (4.2, 8.4, title('Com <span class="hl">MCP</span>, a IA já acessa o CRM, a mídia e o ERP.') + mcp),
     (8.4, 12.4, title('Mas cada fonte responde com <span class="hl">a sua regra.</span>') + nums),
     (12.4, 16.2, title('A IA cruza tudo. E <span style="color:#D92D20">erra mais rápido.</span>') + erro),
     (16.2, 20.6, title('A 4metrics organiza <span class="hl">a base primeiro.</span>') + base),
     (20.6, 25.0, cta)]
CUTS = [s[0] for s in S[1:]]

scenes = "".join(f'<div class="sc" id="sc{i}" data-a="{a}" data-b="{b}">{h}</div>' for i, (a, b, h) in enumerate(S))
html = f"""<html><head><meta charset='utf-8'><style>{ff}
*{{box-sizing:border-box}} body{{margin:0}}
#st{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background-color:{NEV};
 background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px);background-size:24px 24px;font-family:'Inter',sans-serif;color:{NAVY}}}
.g{{position:absolute;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.30),rgba(146,197,73,0))}}
.sc{{position:absolute;left:0;right:0;top:{130 if big else 110}px;bottom:{150 if big else 130}px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:{GAP}px;padding:0 90px;zoom:{1.12 if big else 1}}}
h1{{margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em;font-size:{TS}px;line-height:{TS+8}px;text-align:center}}
.hl{{color:{GTXT}}}
.card{{background:#fff;border:1px solid {BOR};box-shadow:0 1px 2px rgba(5,19,28,.04),0 14px 36px rgba(5,19,28,.07)}}
.feat{{border:1px solid rgba(146,197,73,.85);box-shadow:0 0 0 1px rgba(146,197,73,.15),0 0 34px rgba(146,197,73,.3)}}
.chip{{display:inline-flex;align-items:center;height:64px;padding:0 26px;border-radius:999px;background:#fff;border:1px solid {BOR};font-size:28px;font-weight:600}}
.mcp{{display:inline-flex;align-items:center;height:30px;padding:0 10px;border-radius:8px;background:{NEV};color:{GTXT};font-size:18px;font-weight:700;letter-spacing:.04em}}
.btn{{display:inline-flex;align-items:center;height:96px;padding:0 48px;border-radius:12px;background:{LIME};color:#05131D;font-size:38px;font-weight:600}}
.dot{{width:18px;height:18px;border-radius:99px;display:block}}
.it{{will-change:transform,opacity}}
</style></head><body><div id="st">
<div class="g" id="g1" style="left:420px;top:-300px;width:1000px;height:1000px"></div>
<div class="g" style="left:-360px;top:{H-520}px;width:760px;height:760px;opacity:.6"></div>
{scenes}
<div style="position:absolute;left:72px;bottom:{70 if big else 56}px;display:inline-flex;align-items:center;gap:12px">{SYM(44,dots=NAVY,accent=LIME)}{WORD(36,NAVY,LIME)}</div>
<div id="bar" style="position:absolute;right:72px;bottom:{88 if big else 74}px;width:220px;height:6px;border-radius:9px;background:rgba(5,19,28,.12)"><div id="bf" style="height:100%;width:0;border-radius:9px;background:{GTXT}"></div></div>
</div>
<script>
const cl=x=>Math.max(0,Math.min(1,x)), eo=x=>1-Math.pow(1-cl(x),3), seg=(t,a,b)=>cl((t-a)/(b-a));
const SC=[...document.querySelectorAll('.sc')];
function render(t){{
  SC.forEach(s=>{{const a=+s.dataset.a,b=+s.dataset.b; const last=b>={DUR}-0.01;
    const o=last?0:eo(seg(t,b-.35,b)); const vis=t>=a-0.01&&t<b+0.01;
    s.style.display=vis?'flex':'none'; s.style.opacity=1-o; s.style.transform=`translateY(${{-o*40}}px)`;
    s.querySelectorAll('.it').forEach(e=>{{const d=+e.dataset.d; const i=eo(seg(t,a+d,a+d+.5));
      e.style.opacity=i; e.style.transform=`translateY(${{(1-i)*46}}px)`;}});
    s.querySelectorAll('.dot').forEach((e,k)=>{{e.style.transform=`translateY(${{-8*Math.max(0,Math.sin((t*5)-k*0.9))}}px)`;}});
  }});
  document.getElementById('bf').style.width=(100*cl(t/{DUR}))+'%';
  document.getElementById('g1').style.transform=`translate(${{Math.sin(t*.4)*30}}px,${{Math.cos(t*.3)*20}}px)`;
}}
render(0);
</script></body></html>"""
open(f"{D}/v.html", "w").write(html)

def audio(path):
    sr = 44100; n = int(sr * DUR); t = np.arange(n) / sr
    out = np.zeros(n)
    hz = lambda m: 440 * 2 ** ((m - 69) / 12)
    chords = [[57, 64, 69, 72], [53, 60, 65, 69], [48, 55, 60, 64], [55, 62, 67, 71]]  # Am F C G
    cl_ = 4.2
    for k in range(int(DUR / cl_) + 1):
        a = k * cl_; ch = chords[k % 4]
        seg_ = (t >= a - 0.6) & (t < a + cl_ + 1.2)
        tt = t[seg_] - a
        env = np.clip((tt + 0.6) / 1.2, 0, 1) * np.clip((cl_ + 1.2 - tt) / 1.4, 0, 1)
        for m in ch:
            f = hz(m)
            out[seg_] += env * 0.05 * (np.sin(2*np.pi*f*tt) + 0.35*np.sin(2*np.pi*2*f*tt+0.3) + 0.4*np.sin(2*np.pi*f*1.003*tt))
        # baixo
        out[seg_] += env * 0.07 * np.sin(2*np.pi*hz(ch[0]-12)*tt)
    # pulso suave (arpejo) em colcheias
    step = 60 / 96 / 2
    for k in range(int(DUR / step)):
        a = k * step; ch = chords[int(a // cl_) % 4]; m = ch[k % 4] + 12
        i0 = int(a * sr); L = int(0.35 * sr); i1 = min(n, i0 + L)
        tt = np.arange(i1 - i0) / sr
        out[i0:i1] += 0.025 * np.exp(-tt * 9) * np.sin(2*np.pi*hz(m)*tt)
    # whoosh nas trocas de cena
    rng = np.random.default_rng(4)
    for c in CUTS + [DUR - 4.4]:
        i0 = int((c - 0.45) * sr); L = int(0.6 * sr); tt = np.arange(L) / L
        noise = rng.standard_normal(L); noise = np.convolve(noise, np.ones(30) / 30, 'same')
        out[i0:i0+L] += 0.10 * np.sin(np.pi * tt) ** 2 * noise
    fade = np.clip(t / 1.0, 0, 1) * np.clip((DUR - t) / 1.8, 0, 1)
    out *= fade
    out /= np.max(np.abs(out)) / 0.6
    st = np.stack([out, np.roll(out, 220)], 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((st * 32767).astype(np.int16).tobytes())

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": W, "height": H})
    pg.goto(f"file://{D}/v.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
    el = pg.locator("#st")
    if mode == "preview":
        for t in (3.5, 7.8, 11.8, 15.6, 20.0, 24.5):
            pg.evaluate(f"render({t})"); el.screenshot(path=f"{D}/prev-{fmt}-{t}.png")
    else:
        silent = f"{D}/_silent-{fmt}.mp4"
        pr = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", silent], stdin=subprocess.PIPE)
        for f in range(int(DUR * FPS)):
            pg.evaluate(f"render({f / FPS})"); pr.stdin.write(el.screenshot(type="jpeg", quality=92))
        pr.stdin.close(); pr.wait()
        audio(f"{D}/trilha.wav")
        outp = f"{D}/2026-11-16-perguntas-2027-mcp-{fmt}-v1.mp4"
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", silent, "-i", f"{D}/trilha.wav", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-shortest", "-movflags", "+faststart", outp], check=True)
        print(outp)
    b.close()
print("ok")

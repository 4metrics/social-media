import sys, os, subprocess
sys.path.insert(0, "/home/claude/tools")
from page import WORD

FS = "/home/claude/fonts/fs"
ff = ""
for fam, pkg, pre in [("Inter", "fontsource-inter-5.3.0", "inter"), ("Plus Jakarta Sans", "fontsource-plus-jakarta-sans-5.3.0", "plus-jakarta-sans")]:
    for w in (400, 500, 600, 700):
        ff += f"@font-face{{font-family:'{fam}';src:url('file://{FS}/{pkg}/package/files/{pre}-latin-{w}-normal.woff2') format('woff2');font-weight:{w}}}"

NAVY, LIME, WHT, MUT = "#05131C", "#92C549", "#FFFFFF", "#9AA7B0"
W, H, FPS, DUR = 1080, 1920, 30, 13.0

html = f"""<html><head><meta charset='utf-8'><style>{ff}
*{{box-sizing:border-box}} body{{margin:0}}
#st{{position:relative;width:{W}px;height:{H}px;overflow:hidden;background:{NAVY};
 background-image:radial-gradient(rgba(255,255,255,0.09) 1px,transparent 1.2px);background-size:24px 24px;
 font-family:'Inter',sans-serif;color:{WHT}}}
.g{{position:absolute;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,0.30),rgba(146,197,73,0))}}
.t{{position:absolute;left:90px;right:90px;text-align:center;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em}}
.d{{position:absolute;border-radius:999px}}
</style></head><body><div id="st">
<div class="g" id="g1" style="left:240px;top:260px;width:900px;height:900px"></div>
<div class="g" id="g2" style="left:-300px;top:1300px;width:700px;height:700px;opacity:.5"></div>
<div id="sym" style="position:absolute;left:{W/2-210}px;top:520px;width:420px;height:420px;transform-origin:50% 50%">
 <div class="d" id="d1" style="left:79px;top:79px;width:88px;height:88px;background:{WHT}"></div>
 <div class="d" id="d2" style="left:79px;top:253px;width:88px;height:88px;background:{WHT}"></div>
 <div class="d" id="d3" style="left:253px;top:253px;width:88px;height:88px;background:{WHT}"></div>
 <div class="d" id="d4" style="left:236px;top:62px;width:122px;height:122px;background:{LIME};box-shadow:0 0 60px rgba(146,197,73,.8)"></div>
</div>
<div class="t" id="t1" style="top:780px;font-size:110px;line-height:118px">A 4metrics está de <span style="color:{LIME}">cara nova.</span></div>
<div class="t" id="a1" style="top:1080px;font-size:88px;line-height:98px">Quatro pontos.</div>
<div class="t" id="a2" style="top:1080px;font-size:80px;line-height:92px">Três são os dados dispersos que você tem.</div>
<div class="t" id="a3" style="top:1080px;font-size:76px;line-height:88px">O verde é o <span style="color:{LIME};white-space:nowrap">insight e a decisão</span>, quando estão integrados.</div>
<div id="end" style="position:absolute;left:0;right:0;top:800px;display:flex;flex-direction:column;align-items:center;gap:44px">
 <div id="wm" style="height:150px;display:flex;align-items:center">{WORD(150, WHT, LIME)}</div>
 <div id="e2" style="font-size:44px;color:{MUT};letter-spacing:0.02em">Revenue Intelligence</div>
</div>
</div>
<script>
const $=id=>document.getElementById(id);
const cl=(x)=>Math.max(0,Math.min(1,x));
const eo=(x)=>1-Math.pow(1-cl(x),3);
const back=(x)=>{{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}};
const seg=(t,a,b)=>cl((t-a)/(b-a));
function txt(el,t,a,b){{ // in at a, out at b
  const i=eo(seg(t,a,a+.45)), o=eo(seg(t,b-.35,b));
  $(el).style.opacity=i*(1-o);
  $(el).style.transform=`translateY(${{(1-i)*40 - o*30}}px)`;
}}
function render(t){{
  txt('t1',t,0.2,2.4);
  [['d1',2.5],['d2',2.7],['d3',2.9]].forEach(([id,a])=>{{const s=back(seg(t,a,a+.4));
     const dim=1-0.7*eo(seg(t,7.0,7.4)); const hi=1+0.12*Math.sin(Math.PI*seg(t,5.0,5.8));
     $(id).style.transform=`scale(${{s*hi}})`;$(id).style.opacity=cl(seg(t,a,a+.15))*dim;}});
  const g=back(seg(t,3.15,3.65));
  const dimG=1-0.75*eo(seg(t,4.7,5.1))+0.75*eo(seg(t,7.0,7.4));
  const rise=eo(seg(t,7.2,8.0))*-28;
  const pulse=1+0.08*Math.sin(Math.max(0,t-8.0)*4)*(1-seg(t,9.0,9.4))*(t>8.0?1:0);
  $('d4').style.transform=`translateY(${{rise}}px) scale(${{g*pulse*(1+0.15*eo(seg(t,7.0,7.6)))}})`;
  $('d4').style.opacity=cl(seg(t,3.15,3.3))*dimG;
  $('g1').style.opacity=.3+.7*eo(seg(t,0.2,1.2));
  txt('a1',t,3.2,4.7); txt('a2',t,4.7,7.0); txt('a3',t,7.0,9.5);
  $('a1').style.opacity=Math.min(+$('a1').style.opacity, 1); 
  const sOut=eo(seg(t,9.3,9.8)); $('sym').style.opacity=1-sOut;
  $('sym').style.transform=`scale(${{1-0.15*sOut}})`;
  const w=eo(seg(t,9.8,10.7));
  $('wm').style.clipPath=`inset(0 ${{(1-w)*100}}% 0 0)`; $('wm').style.opacity=cl(seg(t,9.8,10.0));
  txt('e2',t,10.5,99);
  $('end').style.display=t>=9.75?'flex':'none';
}}
render(0);
</script></body></html>"""
os.makedirs("/home/claude/out/reel", exist_ok=True)
open("/home/claude/out/reel/reel.html", "w").write(html)

from playwright.sync_api import sync_playwright
mode = sys.argv[1] if len(sys.argv) > 1 else "preview"
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome")
    pg = b.new_page(viewport={"width": W, "height": H})
    pg.goto("file:///home/claude/out/reel/reel.html")
    pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(600)
    el = pg.locator("#st")
    if mode == "preview":
        for t in (1.5, 4.0, 5.5, 8.5, 12.0):
            pg.evaluate(f"render({t})")
            el.screenshot(path=f"/home/claude/out/reel/prev_{t}.png")
    else:
        tmp = "/home/claude/out/reel/_tmp.mp4"
        ff_ = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                                "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", tmp], stdin=subprocess.PIPE)
        for f in range(int(DUR * FPS)):
            pg.evaluate(f"render({f / FPS})")
            ff_.stdin.write(el.screenshot(type="jpeg", quality=92))
        ff_.stdin.close(); rc = ff_.wait()
        if rc == 0:
            os.replace(tmp, "/home/claude/out/reel/reel-silent.mp4")
        print("rc", rc)
    b.close()
print("ok")

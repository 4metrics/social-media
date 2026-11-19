import sys, os
sys.path.insert(0, "/home/claude/tools")
from page import SYM, WORD
from PIL import Image

FS = "/home/claude/fonts/fs"
ff = ""
for fam, pkg, pre in [("Inter", "fontsource-inter-5.3.0", "inter"), ("Plus Jakarta Sans", "fontsource-plus-jakarta-sans-5.3.0", "plus-jakarta-sans")]:
    for w in (400, 500, 600, 700):
        ff += f"@font-face{{font-family:'{fam}';src:url('file://{FS}/{pkg}/package/files/{pre}-latin-{w}-normal.woff2') format('woff2');font-weight:{w}}}"

NAVY, LIME, GTXT, CARD, BORD, NEV = "#05131C", "#92C549", "#406500", "#14232C", "#2B3640", "#EAF5DD"
MUTD, MUTL, RED = "#9AA7B0", "#4F5B63", "#F97066"
A = "/home/claude/assets/plataforma"
D = "/home/claude/out/festas"
os.makedirs(D, exist_ok=True)

CSS = ff + f"""*{{box-sizing:border-box}} body{{margin:0;background:#888}}
.s{{position:relative;width:1080px;height:1350px;overflow:hidden;font-family:'Inter',sans-serif;background-size:22px 22px;margin-bottom:20px;padding:72px;display:flex;flex-direction:column;gap:34px}}
.dk{{background-color:{NAVY};background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.2px);color:#fff}}
.lt{{background-color:#fff;background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px);color:{NAVY}}}
.nv{{background-color:{NEV};background-image:radial-gradient(rgba(5,19,28,.07) 1px,transparent 1.2px);color:{NAVY}}}
h1,h2{{position:relative;margin:0;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;letter-spacing:-0.03em}}
h1{{font-size:88px;line-height:94px}} h2{{font-size:76px;line-height:84px}}
.dk .hl{{color:{LIME}}} .lt .hl,.nv .hl{{color:{GTXT}}}
p.lead{{position:relative;margin:0;font-size:34px;line-height:48px}}
.dk p.lead{{color:{MUTD}}} .lt p.lead{{color:{MUTL}}} .nv p.lead{{color:#3D4A3F}}
.pill{{position:relative;align-self:flex-start;display:inline-flex;align-items:center;height:42px;padding:0 20px;border-radius:999px;font-size:20px;font-weight:600}}
.dk .pill{{background:#16301F;color:{LIME};border:1px solid rgba(146,197,73,.45)}}
.lt .pill{{background:{NEV};color:{GTXT};border:1px solid rgba(146,197,73,.6)}}
.nv .pill{{background:#fff;color:{GTXT};border:1px solid #CFE3B6}}
.g{{position:absolute;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.26),rgba(146,197,73,0));pointer-events:none}}
.card{{position:relative;border-radius:24px}}
.dk .card{{background:{CARD};border:1px solid {BORD}}}
.lt .card,.nv .card{{background:#fff;border:1px solid #E1E7E4;box-shadow:0 12px 32px rgba(5,19,28,.06)}}
.feat{{border:1px solid rgba(146,197,73,.8)!important;box-shadow:0 0 0 1px rgba(146,197,73,.15),0 0 32px rgba(146,197,73,.25)!important}}
.foot{{position:relative;display:flex;justify-content:space-between;align-items:center;margin-top:auto;min-height:48px}}
.mid{{position:relative;flex:1;display:flex;flex-direction:column;justify-content:center}}
.btn{{display:inline-flex;align-items:center;height:84px;padding:0 40px;border-radius:12px;background:{LIME};color:#05131D;font-size:32px;font-weight:600}}
.prog{{display:flex;gap:8px}} .prog i{{width:44px;height:6px;border-radius:9px}}
"""

def glow(x, y, s): return f'<div class="g" style="left:{x}px;top:{y}px;width:{s}px;height:{s}px"></div>'
def logo(dark):
    ink = "#FFFFFF" if dark else NAVY
    return f'<span style="display:inline-flex;align-items:center;gap:12px">{SYM(40,dots=ink,accent=LIME)}{WORD(32,ink,LIME)}</span>'
def prog(i, n, dark):
    off = "#2B3640" if dark else "#D5DDD8"
    return '<span class="prog">' + "".join(f'<i style="background:{LIME if k==i else off}"></i>' for k in range(1, n+1)) + '</span>'


"""Layout 'Post-texto' (acervo 4metrics): card estilo post de rede social, frase curta + ilustração.
Uso como biblioteca: render(slides, out_prefix) com slides = [{"txt": "...", "media": html|None, "fonte": str|None, "cta": bool}]
Destaque: envolva a palavra-chave com hl("...")."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
_src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "posts_deck2.py")).read()
exec(_src[:_src.index("# ===================== CARROSSEL 1")])
from PIL import Image

AVA = ('<svg width="56" height="56" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#05131C"/>'
       '<circle cx="23" cy="23" r="6" fill="#FFFFFF"/><circle cx="23" cy="41" r="6" fill="#FFFFFF"/><circle cx="41" cy="41" r="6" fill="#FFFFFF"/><circle cx="41" cy="23" r="7.5" fill="#92C549"/></svg>')
BG = {"claro": "#F4F7F5", "nevoa": "#EAF5DD", "escuro": "#05131C"}
def hl(s): return f'<span style="background:#92C549;color:#05131C;padding:0 10px;border-radius:8px;-webkit-box-decoration-break:clone;box-decoration-break:clone">{s}</span>'

def slide(i, n, s, fundo="claro"):
    txt = s["txt"]; size = s.get("size") or (84 if len(txt) < 40 else 70)
    media = f'<div style="margin-top:34px;display:flex;justify-content:center">{s["media"]}</div>' if s.get("media") else ""
    fonte = f'<p style="margin-top:20px;font-size:22px;color:#4F5B63">{s["fonte"]}</p>' if s.get("fonte") else ""
    cta = (f'<div style="margin-top:44px;display:inline-flex;align-items:center;height:92px;padding:0 42px;border-radius:99px;background:#05131C;color:#FFFFFF;'
           f'font-size:34px;font-weight:700">{s.get("cta_txt", "Agende um diagnóstico")} <span style="color:#92C549;margin-left:14px">→</span></div>') if s.get("cta") else ""
    dark = fundo == "escuro"
    bar = "".join(f'<span style="flex:1;height:6px;border-radius:9px;background:{("#92C549" if dark else "#05131C") if k <= i else ("#2B3640" if dark else "#D5DBD8")}"></span>' for k in range(n))
    return (f'<section id="p{i}" style="width:1080px;height:1350px;position:relative;background:{BG[fundo]};display:flex;align-items:center;justify-content:center;'
            f'font-family:Inter,sans-serif">'
            f'<div style="width:900px;background:#FFFFFF;border-radius:36px;padding:56px;box-shadow:0 24px 60px rgba(5,19,28,.10)">'
            f'<div style="display:flex;align-items:center;gap:18px">{AVA}<div><p style="font-size:30px;font-weight:700;color:#05131C">4metrics</p>'
            f'<p style="font-size:24px;color:#4F5B63">Revenue Intelligence</p></div></div>'
            f'<p class="d" style="margin-top:38px;font-size:{size}px;line-height:{size+10}px;color:#05131C;font-weight:700">{txt}</p>{media}{fonte}{cta}</div>'
            f'<div style="position:absolute;left:90px;right:90px;bottom:70px;display:flex;gap:8px">{bar}</div></section>')

def render(slides, out_prefix, fundos=None):
    from playwright.sync_api import sync_playwright
    n = len(slides); fundos = fundos or ["claro"] * n
    html = f"<html><head><meta charset='utf-8'><style>{CSS} b{{font-weight:800}}</style></head><body style='margin:0'>" + "".join(
        slide(i, n, s, fundos[i]) for i, s in enumerate(slides)) + "</body></html>"
    open(out_prefix + ".html", "w").write(html)
    with sync_playwright() as pw:
        br = pw.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--allow-file-access-from-files"])
        pg = br.new_page(viewport={"width": 1080, "height": 1350}); pg.goto("file://" + out_prefix + ".html")
        pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(1200)
        fs = []
        for i in range(n):
            f = f"{out_prefix}-{i+1:02d}.png"; pg.locator(f"#p{i}").screenshot(path=f); fs.append(f)
        br.close()
    ims = [Image.open(f).convert("RGB") for f in fs]
    ims[0].save(out_prefix + "-linkedin.pdf", save_all=True, append_images=ims[1:])
    sh = Image.new("RGB", (n * 370 + 10, 470), "#E1E7E4")
    for k, im in enumerate(ims): sh.paste(im.resize((360, 450), Image.LANCZOS), (10 + k * 370, 10))
    sh.save(out_prefix + "-visao.png")
    return fs

import sys; sys.path.insert(0,"/home/claude/tools"); from page import *
BR, BRD, LIME, INK, INKD, ON_D = "#0E7C5A","#34C38F","#C8F04B","#0F1A17","#E8EEEB","#06140F"
P4 = "M36 12 L14 40 H40 M36 12 V52"
def svg(s, inner, label=None):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg width="{s}" height="{s}" viewBox="0 0 64 64" {a}>{inner}</svg>'
def b1(s, dark=False, sq=None):
    bg = BRD if dark else BR; st = ON_D if dark else "#FFFFFF"
    return svg(s, f'<rect width="64" height="64" rx="14" fill="{bg}"></rect><path d="{P4}" stroke="{st}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"></path><circle cx="51" cy="40" r="5" fill="{LIME}"></circle>')
def b2(s, dark=False):
    st = INKD if dark else INK; dot = BRD if dark else BR
    return svg(s, f'<path d="{P4}" stroke="{st}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" fill="none"></path><circle cx="52" cy="40" r="6" fill="{dot}"></circle>')
def b3(s, dark=False):
    bg = BRD if dark else BR; st = ON_D if dark else "#FFFFFF"
    return svg(s, f'<circle cx="32" cy="32" r="32" fill="{bg}"></circle><path d="{P4}" stroke="{st}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"></path><circle cx="50" cy="40" r="4.5" fill="{LIME}"></circle>')
def b4(s, dark=False):
    bg = BRD if dark else BR; st = ON_D if dark else "#FFFFFF"
    return svg(s, f'<rect width="64" height="64" rx="6" fill="{bg}"></rect><path d="M37 10 L13 41 H41 M37 10 V54" stroke="{st}" stroke-width="8" stroke-linecap="butt" stroke-linejoin="miter" fill="none"></path><rect x="45" y="37" width="8" height="8" fill="{LIME}"></rect>')
def b5(s, dark=False):
    bg = BRD if dark else BR; st = ON_D if dark else "#FFFFFF"
    return svg(s, f'<rect width="64" height="64" rx="14" fill="{bg}"></rect><path d="M32 12 L14 40 H40 M38 24 V52" stroke="{st}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"></path><circle cx="51" cy="40" r="5" fill="{LIME}"></circle>')
GLYPH = ["...X.","..XX.",".X.X.","X..X.","XXXXL","...X.","...X."]
def b6(s, dark=False):
    bg = BRD if dark else BR; st = ON_D if dark else "#FFFFFF"
    cells = ""
    for r,row in enumerate(GLYPH):
        for c,ch in enumerate(row):
            if ch in "XL":
                cells += f'<rect x="{15.75+c*6.5:.2f}" y="{9.25+r*6.5:.2f}" width="5.5" height="5.5" rx="1" fill="{LIME if ch=="L" else st}"></rect>'
    return svg(s, f'<rect width="64" height="64" rx="14" fill="{bg}"></rect>{cells}')
def ilt(dot_css):
    return f'<span style="position: relative; display: inline-block">ı<span style="position: absolute; {dot_css}"></span></span>'
def c1(fs, dark=False):
    d = LIME if dark else BR
    return f'<span style="font-size: {fs}px; font-weight: 700; letter-spacing: -0.04em; color: {INKD if dark else INK}; line-height: 1">4metr{ilt(f"left: 50%; top: 0.06em; width: 0.2em; height: 0.2em; margin-left: -0.1em; background: {d}; border-radius: 0.03em")}cs</span>'
def c2(fs, dark=False):
    d = LIME if dark else BR
    return f'<span style="font-size: {fs}px; font-weight: 600; letter-spacing: -0.03em; color: {INKD if dark else INK}; line-height: 1">4metr{ilt(f"left: 50%; top: 0.04em; width: 0.22em; height: 0.22em; margin-left: -0.11em; background: {d}; border-radius: 999px")}cs</span>'
def c3(fs, dark=False):
    d = BRD if dark else BR
    return f'<span style="font-size: {fs}px; font-weight: 700; letter-spacing: -0.04em; color: {INKD if dark else INK}; line-height: 1"><span style="color: {d}">4</span>metr{ilt(f"left: 50%; top: 0.06em; width: 0.2em; height: 0.2em; margin-left: -0.1em; background: {d}; border-radius: 0.03em")}cs</span>'
def c4(fs, dark=False):
    d = LIME if dark else BR
    return f'<span style="font-size: {fs}px; font-weight: 700; letter-spacing: -0.04em; color: {INKD if dark else INK}; line-height: 1">4metr{ilt(f"left: 50%; top: -0.14em; width: 0.13em; height: 0.36em; margin-left: -0.065em; background: {d}; border-radius: 0.03em")}cs</span>'
def c5(fs, dark=False):
    d = LIME if dark else BR
    return f'<span style="font-size: {fs}px; font-weight: 700; letter-spacing: -0.04em; color: {INKD if dark else INK}; line-height: 1">4metr{ilt(f"left: 50%; top: -0.08em; width: 0.22em; height: 0.22em; margin-left: 0.02em; background: {d}; border-radius: 999px")}cs</span>'
def c6(fs, dark=False):
    return (f'<span style="font-family: \'Geist Mono\', monospace; font-size: {fs}px; font-weight: 500; letter-spacing: -0.04em; color: {INKD if dark else INK}; line-height: 1">'
            f'<span style="background: {LIME}; color: {INK}; padding: 0 0.08em; border-radius: 0.08em; margin-right: 0.04em">4</span>metrics</span>')
def tile(code, name, desc, light, dark):
    return f'''<div style="background: #FFFFFF; border: 1px solid #E1E6E4; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column">
<div style="height: 128px; display: flex; align-items: center; justify-content: center; gap: 20px">{light}</div>
<div style="height: 72px; background: #0E1513; display: flex; align-items: center; justify-content: center; gap: 14px">{dark}</div>
<div style="padding: 12px 16px; display: flex; flex-direction: column; gap: 2px">
<p style="margin: 0; font-size: 14px; line-height: 20px; font-weight: 600"><span style="font-family: 'Geist Mono', monospace; color: #0E7C5A">{code}</span> · {name}</p>
<p style="margin: 0; font-size: 13px; line-height: 18px; color: #5A6762">{desc}</p></div></div>'''
def board(path, title, kicker, intro, tiles, cols=3):
    body = f'''<div style="display: flex; justify-content: space-between; align-items: flex-end">
<div><p style="margin: 0; font-size: 13px; font-weight: 500; color: #5A6762">{kicker}</p>
<h1 style="margin: 4px 0 0; font-size: 32px; line-height: 40px; font-weight: 600; letter-spacing: -0.01em">{title}</h1></div>
<p style="margin: 0; max-width: 460px; font-size: 14px; line-height: 20px; color: #5A6762">{intro}</p></div>
<div style="display: grid; grid-template-columns: repeat({cols}, 1fr); gap: 16px; flex: 1">{"".join(tiles)}</div>'''
    page(path, title, body, bg="#F4F6F5")

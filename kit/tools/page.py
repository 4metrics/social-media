import sys
LIME="#92C549"
LIGHT_INKS=("#F5F5F5","#FFFFFF","#E8EEEB")
def _v2(dots, accent):
    return (f'<circle cx="19" cy="19" r="7" fill="{dots}"></circle><circle cx="19" cy="45" r="7" fill="{dots}"></circle>'
            f'<circle cx="45" cy="45" r="7" fill="{dots}"></circle><circle cx="45" cy="19" r="9" fill="{accent}"></circle>')
def SYM(s, bg=None, bar=None, last=None, label=None, dots="#05131C", accent="#92C549", container=None):
    a = f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    if bg is not None:   # legacy call: treat as app icon on that container
        container = bg
        if bg.upper()=="#92C549": dots, accent = (bar or "#0A0A0A"), "#FFFFFF"
        else: dots, accent = "#FFFFFF", (last if last and last.upper()!="#FFFFFF" else "#92C549")
    if container:
        inner=f'<rect width="64" height="64" rx="14" fill="{container}"></rect><g transform="translate(9 9) scale(0.72)">{_v2(dots,accent)}</g>'
    else:
        inner=_v2(dots,accent)
    return f'<svg width="{s}" height="{s}" viewBox="0 0 64 64" {a} style="flex: none">{inner}</svg>'
import logo_lib as _ll
_WG={}
def WORD(fs, ink="#141712", idot=None):
    if idot is None: idot = "#92C549"
    g,w=_ll.inline_word_plain(ink, idot)
    return (f'<svg viewBox="0 -850 {w:.0f} 1000" aria-hidden="true" style="display: inline-block; height: {fs}px; width: {fs*w/1000:.1f}px; vertical-align: -{fs*0.15:.1f}px; flex: none">{g}</svg>')
def LOGO(s, ink="#141712", idot=None, dots=None, accent=None, **kw):
    if kw.get("bg") is not None:
        sym = SYM(s, **kw)
    else:
        light = ink.upper() in LIGHT_INKS
        sym = SYM(s, dots=dots or ("#FFFFFF" if light else ink), accent=accent or "#92C549")
    return (f'<span style="display: inline-flex; align-items: center; gap: {round(s*0.25)}px">' + sym + WORD(round(s*0.62), ink, idot) + '</span>')
def HEAD(n, title, dark=False):
    c = "#A3A3A3" if dark else "#5D6358"
    return (f'<div style="display: flex; justify-content: space-between; align-items: baseline">'
            f'<p style="margin: 0; font-size: 13px; font-weight: 500; color: {c}">MIV 4metrics · {n}</p>'
            f'<p style="margin: 0; font-family: \'Geist Mono\', monospace; font-size: 13px; color: {c}">v1 · nov 2026</p></div>')
def page(path, title, body, bg="#FFFFFF", ink="#141712"):
    html = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&amp;family=Geist+Mono:wght@400;500&amp;display=swap">
<style>
body{{margin:0}}
a{{color:#406500}}a:hover{{color:#2D4A00}}
</style>
</helmet>
<div style="width: 1280px; height: 720px; box-sizing: border-box; padding: 48px; background: {bg}; color: {ink}; font-family: 'Geist', system-ui, sans-serif; display: flex; flex-direction: column; gap: 32px; overflow: hidden">
{body}
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1280,"height":720}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    open(path, "w").write(html)

def WORDP(fs, ink="#141712", idot=None):
    if idot is None: idot = "#92C549"
    g,w=_ll.inline_word_plain(ink, idot)
    return (f'<svg viewBox="0 -850 {w:.0f} 1000" aria-hidden="true" style="display: inline-block; height: {fs}px; width: {fs*w/1000:.1f}px; vertical-align: -{fs*0.15:.1f}px; flex: none">{g}</svg>')

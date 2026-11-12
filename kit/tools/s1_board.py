import sys, os; sys.path.insert(0,"/home/claude/tools")
from symbols import *; from page import WORDP
import miv_site as MS
os.chdir("/home/claude/dz/project")
CARD,BOR,MUT="#14232C","#2B3640","#9AA7B0"
def mk(fn,size,dark=True): return svg(size, fn(WHT if dark else NAVY, LIME))
def app(fn,size):
    if fn is v5: return svg(size, v5(WHT,LIME))
    return svg(size, f'<rect width="64" height="64" rx="14" fill="{NAVY}"></rect><g transform="translate(9 9) scale(0.72)">{fn(WHT,LIME)}</g>')
def lock(fn,dark):
    ink=WHT if dark else NAVY
    return f'<span style="display: inline-flex; align-items: center; gap: 10px">{mk(fn,34,dark)}{WORDP(22,ink,"#92C549" if dark else "#6D9E15")}</span>'
def tile(code,name,desc,fn):
    return f'''<div style="position: relative; background: {CARD}; border: 1px solid {BOR}; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column">
<div style="position: relative; height: 140px; display: flex; align-items: center; justify-content: space-between; padding: 0 24px">
<div style="position: absolute; left: -40px; top: -60px; width: 240px; height: 240px; border-radius: 999px; background: radial-gradient(closest-side, rgba(146,197,73,0.16), rgba(146,197,73,0))"></div>
<span style="position: relative">{mk(fn,86)}</span>
<span style="position: relative; display: flex; gap: 9px; align-items: flex-end">{app(fn,40)}{app(fn,24)}{app(fn,16)}</span></div>
<div style="height: 56px; display: flex; align-items: center; justify-content: center; border-top: 1px solid {BOR}; background: {NAVY}">{lock(fn,True)}</div>
<div style="height: 56px; display: flex; align-items: center; justify-content: center; background: {WHT}">{lock(fn,False)}</div>
<div style="padding: 10px 14px 12px"><p style="margin: 0; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 14px; line-height: 20px; font-weight: 700"><span style="font-family: 'Inter', sans-serif; font-weight: 500; color: {MUT}">{code}</span> {name}</p>
<p style="margin: 2px 0 0; font-size: 12px; line-height: 17px; color: {MUT}">{desc}</p></div></div>'''
body=f'''<div style="position: relative; display: flex; justify-content: space-between; align-items: flex-end">
<div><p style="margin: 0; font-size: 13px; font-weight: 500; color: {MUT}">4metrics · Símbolo S1</p>
<h1 style="margin: 4px 0 0; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 32px; line-height: 40px; font-weight: 700; letter-spacing: -0.01em">Variações de <span style="color: #92C549">Quatro pontos</span></h1></div>
<p style="margin: 0; max-width: 470px; font-size: 14px; line-height: 20px; color: {MUT}">O nome usa o 4 normal da Geist e o pingo do i verde. Ícone de app em 40, 24 e 16 px.</p></div>
<div style="position: relative; display: grid; grid-template-columns: repeat(4, 1fr); gap: 14px">{"".join(tile(*v) for v in VARS)}</div>'''
MS.page("Simbolo-S1-variacoes.dc.html","Variações do S1",body,w=1280,h=880)

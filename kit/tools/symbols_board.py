import sys, os; sys.path.insert(0,"/home/claude/tools")
from symbols import *; from page import WORD
import miv_site as MS
os.chdir("/home/claude/dz/project")
CARD,BOR,MUT="#14232C","#2B3640","#9AA7B0"
def lock(fn,dark):
    ink=WHT if dark else NAVY
    return f'<span style="display: inline-flex; align-items: center; gap: 10px">{mark(fn,34,dark)}{WORD(21,ink,"#92C549" if dark else "#6D9E15")}</span>'
def tile(code,name,desc,fn,ref=False):
    tag = f'<span style="display: inline-flex; align-items: center; height: 22px; padding: 0 9px; border-radius: 999px; border: 1px solid {BOR}; font-size: 11px; color: {MUT}">atual</span>' if ref else ""
    return f'''<div style="position: relative; background: {CARD}; border: 1px solid {BOR}; border-radius: 16px; overflow: hidden; display: flex; flex-direction: column">
<div style="position: relative; height: 150px; display: flex; align-items: center; justify-content: space-between; padding: 0 28px">
<div style="position: absolute; left: -40px; top: -60px; width: 260px; height: 260px; border-radius: 999px; background: radial-gradient(closest-side, rgba(146,197,73,0.16), rgba(146,197,73,0))"></div>
<span style="position: relative">{mark(fn,92)}</span>
<span style="position: relative; display: flex; gap: 10px; align-items: flex-end">{appicon(fn,44)}{appicon(fn,28)}{appicon(fn,16)}</span></div>
<div style="height: 60px; display: flex; align-items: center; justify-content: center; border-top: 1px solid {BOR}; background: {NAVY}">{lock(fn,True)}</div>
<div style="height: 60px; display: flex; align-items: center; justify-content: center; background: {WHT}">{lock(fn,False)}</div>
<div style="padding: 12px 16px"><p style="margin: 0; display: flex; gap: 8px; align-items: center; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 15px; line-height: 22px; font-weight: 700"><span style="font-family: 'Inter', sans-serif; font-weight: 500; color: {MUT}">{code}</span> {name} {tag}</p>
<p style="margin: 2px 0 0; font-size: 12px; line-height: 17px; color: {MUT}">{desc}</p></div></div>'''
tiles="".join(tile(*s) for s in SYMS)+tile("S0","4 com ponto","Para comparar.",s0,True)
body=f'''<div style="position: relative; display: flex; justify-content: space-between; align-items: flex-end">
<div><p style="margin: 0; font-size: 13px; font-weight: 500; color: {MUT}">4metrics · Símbolo</p>
<h1 style="margin: 4px 0 0; font-family: 'Plus Jakarta Sans', sans-serif; font-size: 32px; line-height: 40px; font-weight: 700; letter-spacing: -0.01em">Novas ideias de <span style="color: #92C549">símbolo</span></h1></div>
<p style="margin: 0; max-width: 480px; font-size: 14px; line-height: 20px; color: {MUT}">Cada ideia: o símbolo grande, o ícone de app em 44, 28 e 16 px (favicon) e o logo com o nome no escuro e no claro.</p></div>
<div style="position: relative; display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px">{tiles}</div>'''
MS.page("Simbolos-novos.dc.html","Novas ideias de símbolo",body,w=1280,h=1250)

import sys, os; sys.path.insert(0,"/home/claude/tools")
import miv_final as F
from stories import ff
from page import SYM, WORD
LIME,NAVY,WHT=F.LIME,F.NAVY,F.WHT; GT=LIME; D=F.T["dark"]; H,B=F.H,F.B; glow=F.glow
# loss curve: daily accumulation over 30 days, marker at day 2 and day 30
pts=[(60+i*(820/29), 300-(i/29)*230) for i in range(30)]
poly=" ".join(f"{x:.1f},{y:.1f}" for x,y in pts)
area=f"M60,300 "+" ".join(f"L{x:.1f},{y:.1f}" for x,y in pts)+" L880,300 Z"
chart=f'''<svg width="940" height="360" viewBox="0 0 940 360" aria-hidden="true" style="display: block">
<defs><linearGradient id="lg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F97066" stop-opacity="0.35"></stop><stop offset="1" stop-color="#F97066" stop-opacity="0"></stop></linearGradient></defs>
<line x1="60" y1="300" x2="880" y2="300" stroke="{D["bor"]}" stroke-width="2"></line>
<path d="{area}" fill="url(#lg)"></path>
<polyline points="{poly}" fill="none" stroke="#F97066" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"></polyline>
<line x1="{pts[1][0]:.1f}" y1="300" x2="{pts[1][0]:.1f}" y2="70" stroke="{LIME}" stroke-width="2" stroke-dasharray="6 6"></line>
<circle cx="{pts[1][0]:.1f}" cy="{pts[1][1]:.1f}" r="13" fill="{LIME}" style="filter: drop-shadow(0 0 10px rgba(146,197,73,0.9))"></circle>
<circle cx="880" cy="{pts[-1][1]:.1f}" r="13" fill="#F97066"></circle>
<text x="{pts[1][0]+20:.1f}" y="84" font-family="Inter, sans-serif" font-size="24" font-weight="600" fill="{GT}">Dia 2: dava para corrigir</text>
<text x="880" y="40" text-anchor="end" font-family="Inter, sans-serif" font-size="24" font-weight="600" fill="#F97066">Dia 30: o relatório chega</text>
<text x="60" y="340" font-family="Inter, sans-serif" font-size="22" fill="{D["mut"]}">dia 1</text>
<text x="880" y="340" text-anchor="end" font-family="Inter, sans-serif" font-size="22" fill="{D["mut"]}">dia 30</text>
</svg>'''
step=lambda n,t: f'<div style="display: flex; gap: 16px; align-items: baseline"><span style="flex: none; width: 34px; height: 34px; border-radius: 999px; border: 1px solid rgba(146,197,73,0.5); background: {D["bsub"]}; color: {GT}; font-size: 18px; font-weight: 700; display: inline-flex; align-items: center; justify-content: center">{n}</span><span style="font-size: 28px; line-height: 38px; color: {WHT}">{t}</span></div>'
body=f'''<div style="position: relative; display: flex; justify-content: space-between; align-items: center">
<span style="display: inline-flex; align-items: center; height: 42px; padding: 0 20px; border-radius: 999px; background: {D["bsub"]}; color: {LIME}; border: 1px solid rgba(146,197,73,0.45); font-size: 20px; font-weight: 600">Custo da demora</span>
</div>
<h1 style="position: relative; margin: 8px 0 0; font-family: {H}; font-size: 76px; line-height: 82px; font-weight: 700; letter-spacing: -0.03em">Quanto custa decidir com o relatório do <span style="color: {GT}">mês passado?</span></h1>
<div style="position: relative; display: flex; flex-direction: column; gap: 14px">
{step(1,"Seu funil gira <b>R$ 500 mil</b> por mês.")}
{step(2,"No dia 2, uma etapa perde <b>10%</b> de conversão.")}
{step(3,"Ninguém vê: o número só fecha no fim do mês.")}</div>
<div style="position: relative; background: {D["card"]}; border: 1px solid {D["bor"]}; border-radius: 28px; padding: 28px 30px 20px; display: flex; flex-direction: column; gap: 8px">
<p style="margin: 0; font-size: 24px; color: {D["mut"]}">Quando o relatório chega, já ficaram para trás</p>
<p style="margin: 0; font-family: {H}; font-size: 104px; line-height: 108px; font-weight: 700; letter-spacing: -0.03em; color: #F97066; font-variant-numeric: tabular-nums">R$ 50 mil</p>
{chart}</div>
<div style="flex: 1"></div>
<div style="position: relative; display: flex; justify-content: space-between; align-items: center">
<p style="margin: 0; font-size: 26px; line-height: 34px; color: {WHT}; max-width: 700px">Com dado diário, você vê no dia 2 e <span style="color: {GT}; font-weight: 600; white-space: nowrap">corrige no dia 3.</span></p>
<span style="display: inline-flex; align-items: center; gap: 12px">{SYM(40,dots=WHT,accent=LIME)}{WORD(32,WHT,LIME)}</span></div>'''
html=f"""<html><head><meta charset='utf-8'><style>{ff}*{{box-sizing:border-box}}body{{margin:0}}</style></head><body>
<section id="p" style="position:relative;width:1080px;height:1350px;overflow:hidden;background-color:#05131C;background-image:radial-gradient(rgba(255,255,255,.09) 1px,transparent 1.2px);background-size:22px 22px;color:#FFFFFF;font-family:Inter,sans-serif;padding:72px;display:flex;flex-direction:column;gap:34px">
<div style="position:absolute;left:600px;top:-240px;width:760px;height:760px;border-radius:999px;background:radial-gradient(closest-side,rgba(146,197,73,.26),rgba(146,197,73,0))"></div>
{body}</section></body></html>"""
D2="/home/claude/out/post01-v2"; os.makedirs(D2,exist_ok=True)
open(f"{D2}/p.html","w").write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome"); pg=b.new_page(viewport={"width":1080,"height":1350})
    pg.goto(f"file://{D2}/p.html"); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(700)
    pg.locator("#p").screenshot(path=f"{D2}/2026-11-20-custo-da-demora-v2.png"); b.close()
print("ok")

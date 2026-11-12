import math
SW=124; X=546; T=62; TOP=-(X-T); MID=-(X/2); BOT=-T; R=(X-2*T)/2  # centerline radius 211
K=(710-SW)/40
def f(v): return f"{v:.1f}"
def four(x, dot=True):
    x0=x+45+SW/2
    P=lambda px,py:(x0+(px-14)*K, -(SW/2+(52-py)*K))
    a,b,c,d=P(36,12),P(14,40),P(40,40),P(36,52)
    path=f"M{f(a[0])} {f(a[1])} L{f(b[0])} {f(b[1])} H{f(c[0])} M{f(a[0])} {f(a[1])} V{f(d[1])}"
    dx,dy=P(51,40); dr=5*K
    adv = (dx+dr+75-x) if dot else 595
    return path,(dx,dy,dr) if dot else None, adv
def m(x):
    s=x+40+SW/2; r=(R*0.72)
    top=TOP+0; cy=top+r
    return (f"M{f(s)} {f(BOT)} V{f(TOP)} M{f(s)} {f(cy)} A{f(r)} {f(r)} 0 0 1 {f(s+2*r)} {f(cy)} V{f(BOT)} "
            f"M{f(s+2*r)} {f(cy)} A{f(r)} {f(r)} 0 0 1 {f(s+4*r)} {f(cy)} V{f(BOT)}"), (s+4*r+SW/2+40)-x
def e(x):
    cx=x+40+SW/2+R; a=math.radians(42)
    return (f"M{f(cx-R)} {f(MID)} H{f(cx+R)} A{f(R)} {f(R)} 0 1 0 {f(cx+R*math.cos(a))} {f(MID+R*math.sin(a))}"), (cx+R+SW/2+40)-x
def t(x):
    s=x+40+SW/2+70
    return (f"M{f(s)} {-650} V{f(BOT)} M{f(s-70)} {f(TOP)} H{f(s+150)}"), (s+150+SW/2+20)-x
def r_(x):
    s=x+40+SW/2; rr=R*0.85
    return (f"M{f(s)} {f(BOT)} V{f(TOP)} M{f(s)} {f(TOP+rr)} A{f(rr)} {f(rr)} 0 0 1 {f(s+rr)} {f(TOP)}"), (s+rr+SW/2+20)-x
def i_(x):
    s=x+40+SW/2
    return (f"M{f(s)} {f(BOT)} V{f(TOP)}"), (s+SW/2+40)-x, s
def c(x):
    cx=x+40+SW/2+R; a=math.radians(45)
    return (f"M{f(cx+R*math.cos(a))} {f(MID-R*math.sin(a))} A{f(R)} {f(R)} 0 1 0 {f(cx+R*math.cos(a))} {f(MID+R*math.sin(a))}"), (cx+R*math.cos(a)+SW/2+40)-x
def s_(x):
    r=R/2; cx=x+40+SW/2+r+12; c1=MID-r; c2=MID+r; a=math.radians(35)
    p=(f"M{f(cx+r*math.cos(a)+10)} {f(c1-r*math.sin(a))} A{f(r)} {f(r)} 0 1 0 {f(cx)} {f(MID)} "
       f"A{f(r)} {f(r)} 0 1 1 {f(cx-r*math.cos(a)-10)} {f(c2+r*math.sin(a))}")
    return p, (cx+r+SW/2+40+12)-x
def logotype(ink="#141712", dot4="#6D9E15", idot="#6D9E15", ls=-10):
    x=0; parts=[]; circles=[]
    p,d,adv=four(x); parts.append(p); circles.append((d,dot4)); x+=adv+ls
    for fn in (m,e,t,r_):
        p,adv=fn(x); parts.append(p); x+=adv+ls
    p,adv,sx=i_(x); parts.append(p); circles.append(((sx,TOP-SW/2-60-0.11*1000*0.8,0.09*1000),idot)); x+=adv+ls
    for fn in (c,s_):
        p,adv=fn(x); parts.append(p); x+=adv+ls
    w=x-ls
    g=f'<path d="{" ".join(parts)}" stroke="{ink}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
    g+="".join(f'<circle cx="{f(cx)}" cy="{f(cy)}" r="{f(rr)}" fill="{col}"/>' for (cx,cy,rr),col in circles)
    return g, w

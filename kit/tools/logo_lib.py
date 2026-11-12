from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.recordingPen import RecordingPen, DecomposingRecordingPen
f = TTFont("/home/claude/fonts/package/dist/fonts/geist-sans/Geist-SemiBold.ttf")
gs = f.getGlyphSet(); cmap = f.getBestCmap(); upm = f["head"].unitsPerEm
hh = f["hhea"]; A, D = hh.ascent, -hh.descent
def gname(ch): return cmap[ord(ch)]
# find dot of 'i'
rp = DecomposingRecordingPen(gs); gs[gname("i")].draw(rp)
contours=[]; cur=[]
for op,args in rp.value:
    cur.append((op,args))
    if op in ("closePath","endPath"): contours.append(cur); cur=[]
def cb(c):
    p=RecordingPen(); p.value=c; b=BoundsPen(gs); p.replay(b); return b.bounds
dotb = max((cb(c) for c in contours), key=lambda b:b[1])
_b=BoundsPen(gs); gs[cmap[0x131]].draw(_b); dot_cx_off = (_b.bounds[0]+_b.bounds[2])/2;  dot_cy = (dotb[1]+dotb[3])/2

SW=124; ADV4=595
def four_path(x, s):
    k=(710-SW)/40; x0=45+SW/2
    P=lambda px,py: (x+(x0+(px-14)*k)*s, -(SW/2+(52-py)*k)*s)
    a=P(36,12); b=P(14,40); c=P(40,40); d=P(36,52)
    return f"M{a[0]:.2f} {a[1]:.2f} L{b[0]:.2f} {b[1]:.2f} H{c[0]:.2f} M{a[0]:.2f} {a[1]:.2f} V{d[1]:.2f}", SW*s
def word(text_size, ls=-0.03, plain=False):
    s = text_size/upm; x=0; ds=[]; dot=None; four=None
    hmtx=f["hmtx"]
    for ch in "4metrıcs":
        g = gname(ch)
        if ch=="4" and not plain:
            four = four_path(x, s); x += ADV4*s + ls*text_size; continue
        sp = SVGPathPen(gs)
        tp = TransformPen(sp,(s,0,0,-s,x,0))
        gs[g].draw(tp); ds.append(sp.getCommands())
        if ch=="ı":
            _r=SW*(5/7); _gap=SW*(2.5/7); dot=(x+dot_cx_off*s, -(534+_gap+_r)*s, _r*s)
        x += hmtx[g][0]*s + ls*text_size
    x -= ls*text_size
    return " ".join(ds), x, dot, (four if four else ('',0))
def v2dots(dots, accent):
    return (f'<circle cx="19" cy="19" r="7" fill="{dots}"/><circle cx="19" cy="45" r="7" fill="{dots}"/>'
            f'<circle cx="45" cy="45" r="7" fill="{dots}"/><circle cx="45" cy="19" r="9" fill="{accent}"/>')
def sym(x,y,S,dots,accent,container=None):
    k=S/64; c=f'<rect width="64" height="64" rx="14" fill="{container}"/>' if container else ""
    inner = v2dots(dots,accent) if not container else f'<g transform="translate(9 9) scale(0.72)">{v2dots(dots,accent)}</g>'
    return f'<g transform="translate({x:.2f} {y:.2f}) scale({k:.5f})">{c}{inner}</g>'
def wordsvg(x, base, fs, ink, idot):
    d,w,(cx,cy,r),_f=word(fs, plain=True)
    return f'<g transform="translate({x:.2f} {base:.2f})"><path d="{d}" fill="{ink}"/><circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{idot}"/></g>', w
def wrap(w,h,body): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.2f} {h:.2f}">{body}</svg>\n'
def lockup(S, ink, dots, accent, idot):
    fs=0.62*S; gap=0.25*S
    top=(S-fs)/2; base = top + (fs-(A+D)/upm*fs)/2 + A/upm*fs
    ws,w = wordsvg(S+gap, base, fs, ink, idot)
    return wrap(S+gap+w, S, sym(0,0,S,dots,accent)+ws)
def wordonly(fs, ink, idot):
    # tight box: from top of dot to descender-free baseline
    d,w,(cx,cy,r),_f=word(fs, plain=True)
    asc = max(f["OS/2"].sCapHeight/upm*fs, -(cy-r))
    pad=0
    ws,_ = wordsvg(0, asc, fs, ink, idot)
    return wrap(w, asc+0.02*fs, ws)

def inline_word(fs_unused, ink, idot):
    d,w,(cx,cy,r),(fd,fw)=word(1000)
    g=(f'<path d="{fd}" stroke="{ink}" stroke-width="{fw:.1f}" stroke-linecap="round" stroke-linejoin="round" fill="none"></path>'
       f'<path d="{d}" fill="{ink}"></path><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{idot}"></circle>')
    return g, w

def inline_word_plain(ink, idot):
    d,w,(cx,cy,r),_=word(1000, plain=True)
    g=(f'<path d="{d}" fill="{ink}"></path><circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{idot}"></circle>')
    return g, w

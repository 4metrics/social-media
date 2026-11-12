import math
NAVY,LIME,WHT="#05131C","#92C549","#FFFFFF"
S=lambda d,fg,w=6.5: f'<path d="{d}" stroke="{fg}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" fill="none"></path>'
C=lambda x,y,r,col: f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"></circle>'
def s1(fg,ac): return C(19,19,7,fg)+C(45,19,7,fg)+C(19,45,7,fg)+C(45,45,9,ac)
def s2(fg,ac): return (f'<rect x="9" y="9" width="21" height="21" rx="5" fill="{fg}"></rect><rect x="9" y="34" width="21" height="21" rx="5" fill="{fg}"></rect><rect x="34" y="34" width="21" height="21" rx="5" fill="{fg}"></rect>'
                       f'<path d="M34 30 V9 A21 21 0 0 1 55 30 Z" fill="{ac}"></path>')
def s3(fg,ac): return S("M9 47 L23 34 L33 41 L47 22",fg)+C(51,17,7,ac)
def s4(fg,ac): return f'<circle cx="31" cy="33" r="19" stroke="{fg}" stroke-width="6.5" fill="none"></circle>'+C(44.4,19.6,8.5,ac)
def s5(fg,ac): return S("M20 10 L6 33 H20 M20 10 V54 M20 36 A7 7 0 0 1 34 36 V54",fg,5.5)+S("M34 36 A7 7 0 0 1 48 36 V54",ac,5.5)+C(56,50,4,ac)
def s6(fg,ac):
    sq=lambda x,y,col: f'<rect x="{x-7}" y="{y-7}" width="14" height="14" rx="3" transform="rotate(45 {x} {y})" fill="{col}"></rect>'
    return sq(32,14,ac)+sq(14,32,fg)+sq(50,32,fg)+sq(32,50,fg)
def s7(fg,ac): return S("M12 50 L32 33 L52 50",fg)+S("M12 36 L32 19 L52 36",fg)+C(32,7.5,5.5,ac)
def s8(fg,ac):
    cx,cy,r=30,34,20
    return (f'<path d="M{cx} {cy} L{cx} {cy-r} A{r} {r} 0 1 0 {cx+r} {cy} Z" fill="{fg}"></path>'
            f'<path d="M{cx+5} {cy-5} L{cx+5} {cy-5-r} A{r} {r} 0 0 1 {cx+5+r} {cy-5} Z" fill="{ac}"></path>')
def s0(fg,ac): return S("M36 12 L14 40 H40 M36 12 V52",fg,7)+C(51,40,5,ac)
SYMS=[("S1","Quatro pontos","As 4 métricas; a verde, maior, é a que decide. Conversa com a malha de pontos do site.",s1),
 ("S2","Quadrante","4 partes da operação; uma vira gráfico em verde. Geométrico e firme.",s2),
 ("S3","Curva da receita","Linha de dados que sobe e termina no ponto de decisão.",s3),
 ("S4","Órbita","Um ciclo de dados com o ponto de insight sobre a linha. Simples e redondo.",s4),
 ("S5","Ligadura 4m","O 4 e o m de 4metrics num traço só; a última perna do m em verde.",s5),
 ("S6","Diamante","4 peças em losango; a do topo em verde: a métrica em alta.",s6),
 ("S7","Crescimento","Duas setas para cima e um ponto: avanço passo a passo.",s7),
 ("S8","Fatia","Gráfico de pizza com a fatia de receita destacada.",s8)]
def svg(size, inner, label=None, extra=""):
    a=f'role="img" aria-label="{label}"' if label else 'aria-hidden="true"'
    return f'<svg width="{size}" height="{size}" viewBox="0 0 64 64" {a} style="display: block; flex: none{extra}">{inner}</svg>'
def mark(fn,size,dark=True): return svg(size, fn(WHT if dark else NAVY, LIME))
def appicon(fn,size,glow=False):
    return svg(size, f'<rect width="64" height="64" rx="14" fill="{NAVY}"></rect><g transform="translate(9 9) scale(0.72)">{fn(WHT,LIME)}</g>')

def v1(fg,ac): return C(19,19,7,fg)+C(45,19,7,fg)+C(19,45,7,fg)+C(45,45,9,ac)
def v2(fg,ac): return C(19,19,7,fg)+C(45,19,9,ac)+C(19,45,7,fg)+C(45,45,7,fg)
def v3(fg,ac): return C(18,46,5,fg)+C(18,22,6.5,fg)+C(43,46,8,fg)+C(43,21,10.5,ac)
def v4(fg,ac): return C(19,19,8,fg)+C(45,19,8,fg)+C(19,45,8,fg)+C(45,45,8,ac)
def v5(fg,ac): return '<rect width="64" height="64" rx="14" fill="#92C549"></rect>'+C(22,22,6,"#05131C")+C(42,22,6,"#05131C")+C(22,42,6,"#05131C")+C(42,42,7.5,"#FFFFFF")
def v6(fg,ac): return (f'<path d="M19 19 L45 45 M45 19 L45 45 M19 45 L45 45" stroke="{fg}" stroke-opacity="0.45" stroke-width="2.5" stroke-linecap="round"></path>'
                       +C(19,19,6.5,fg)+C(45,19,6.5,fg)+C(19,45,6.5,fg)+C(45,45,9.5,ac))
def v7(fg,ac): return (f'<rect x="11" y="11" width="16" height="16" rx="5" fill="{fg}"></rect><rect x="37" y="11" width="16" height="16" rx="5" fill="{fg}"></rect><rect x="11" y="37" width="16" height="16" rx="5" fill="{fg}"></rect>'+C(45,45,9,ac))
def v8(fg,ac):
    pts=[(36,10),(28,22),(36,22),(20,34),(36,34),(12,46),(20,46),(28,46),(36,46),(36,58)]
    out="".join(C(x,y-2,3.6,fg) for x,y in pts)
    return out+C(50,44,5.5,ac)
VARS=[("V1","Original","3 pontos brancos e o verde maior embaixo à direita.",v1),
 ("V2","Verde no alto","O ponto verde sobe para o canto de cima: leitura de alta.",v2),
 ("V3","Crescendo","Os pontos crescem em ordem até o verde: dado que ganha valor.",v3),
 ("V4","Iguais","4 pontos do mesmo tamanho; só a cor destaca. Mais calmo.",v4),
 ("V5","Ícone lima","Moldura verde com pontos azul-noite e o destaque branco.",v5),
 ("V6","Conectados","Linhas finas ligam os 3 pontos ao verde: dados que convergem.",v6),
 ("V7","Pixels","3 quadrados arredondados e 1 ponto verde: dado bruto e insight.",v7),
 ("V8","4 em pontos","Um 4 desenhado com a malha de pontos, com o ponto verde.",v8)]

# 4metrics · "Três jeitos de responder" (05/02/2027) · v2 mais visual e técnica (diagramas, código, hub)
import sys
sys.path.insert(0, "/home/claude/tools")
from ds4m import *
V = "v3"
OUT = "/home/claude/out/tres-caminhos"
C = f"2027-02-05-tres-caminhos-{V}"

LUCIDE.update({
 "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 "cpu": '<rect width="16" height="16" x="4" y="4" rx="2"/><rect width="6" height="6" x="9" y="9" rx="1"/><path d="M15 2v2"/><path d="M15 20v2"/><path d="M2 15h2"/><path d="M2 9h2"/><path d="M20 15h2"/><path d="M20 9h2"/><path d="M9 2v2"/><path d="M9 20v2"/>',
 "chart": '<path d="M3 3v16a2 2 0 0 0 2 2h16"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
 "file-x": '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="m14.5 12.5-5 5"/><path d="m9.5 12.5 5 5"/>',
 "layers": '<path d="m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z"/><path d="m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65"/><path d="m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65"/>',
 "database": '<ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M3 5V19A9 3 0 0 0 21 19V5"/><path d="M3 12A9 3 0 0 0 21 12"/>',
 "x": '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
})

EXTRA = """
.code{font-family:ui-monospace,'SF Mono',Menlo,monospace;font-size:12.5px;line-height:19px;background:#05131C;color:#D7E3DC;border:1px solid #2B3640;border-radius:8px;padding:10px 12px;white-space:pre;margin:0}
.code .k{color:#92C549;font-weight:600} .code .s{color:#E8A33D} .code .e{color:#F06A5B;font-weight:700} .code .c{color:#66757F}
.node{width:44px;height:44px;border-radius:999px;display:flex;align-items:center;justify-content:center;flex:none;background:var(--raised);border:1.5px solid var(--brand);color:var(--strong);position:relative;z-index:1}
.node.hot{background:var(--brand);color:#05131C;border-color:var(--brand)} .node.bad{border-color:var(--crit);color:var(--crit)}
.pipe{position:relative;display:flex;flex-direction:column;gap:14px}
.pipe:before{content:"";position:absolute;left:21px;top:22px;bottom:22px;border-left:2px dashed var(--bstrong);opacity:.6}
.prow{display:flex;align-items:center;gap:14px}
.ann{font-size:12.5px;line-height:17px;color:var(--muted)}
.pill{position:absolute;height:30px;display:flex;align-items:center;justify-content:center;gap:6px;border-radius:999px;border:1.5px solid var(--brand);background:var(--raised);font-size:13px;font-weight:600}
.box{position:absolute;white-space:nowrap;display:flex;align-items:center;gap:8px;padding:0 12px;border-radius:8px;border:1px solid var(--border);background:var(--raised);font-size:13px;font-weight:600}
"""
import ds4m
ds4m.CSS += EXTRA

def node(icon, cls=""): return f'<span class="node {cls}">{ico(icon,22)}</span>'
def prow(icon, label, right, cls=""):
    return f'<div class="prow">{node(icon, cls)}<div style="display:grid;gap:4px;flex:1;min-width:0"><span class="h3" style="font-size:15px;line-height:20px">{label}</span>{right}</div></div>'
row = lambda *s: '<div style="display:flex;gap:8px;flex-wrap:wrap">' + "".join(s) + '</div>'

# 01 · capa névoa: foto + os três caminhos em miniatura
paths = [("user", "Analista de BI", ""), ("cpu", "IA sem contexto", "bad"), ("layers", "IA com contexto", "hot")]
frame(C+"-01", "fe", "nevoa", f'''{title("Três jeitos de responder: quanto vendemos este mês?", "quanto vendemos", "h1", "nevoa")}
<div class="mid" style="gap:12px">{ph("3184634", 230, "center 40%")}
<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px">{"".join(f'<div class="card" style="padding:12px;display:grid;justify-items:start;gap:8px"><span class="node {c}" style="width:36px;height:36px">{ico(i,18)}</span><span class="small" style="font-weight:600">{t}</span></div>' for i,t,c in paths)}</div></div>''', "IA com contexto")

# 02 · caminho 1: pipeline vertical com SQL à mão
sql1 = '<pre class="code"><span class="k">SELECT</span> SUM(valor)\n  <span class="k">FROM</span> pedidos\n <span class="k">WHERE</span> status = <span class="s">\'faturado\'</span>\n   <span class="k">AND</span> mes = <span class="s">\'2027-01\'</span></pre>'
frame(C+"-02", "fe", "light", f'''<span class="label">Caminho 1 · Analista de BI</span>{title("O número certo, dias depois.", "dias depois", "h1", "light")}
<div class="mid"><div class="pipe">
{prow("message", "Pergunta", '<span class="ann">“Quanto vendemos este mês?” entra na fila</span>')}
{prow("user", "Analista", '<span class="ann">O conhecimento fica na cabeça de uma pessoa</span>')}
{prow("database", "SQL à mão", sql1)}
{prow("chart", "Dashboard", '<span class="ann">Trata, monta e envia. Chega em dias.</span>')}
</div>{row(state("pos","Acerto alto"), state("warn","Cada resposta passa por todas as etapas"))}</div>''')

# 03 · caminho 2: IA chuta o filtro
sql2 = '<pre class="code"><span class="c">-- gerado pela IA</span>\n<span class="k">SELECT</span> COUNT(*) <span class="k">FROM</span> clientes\n <span class="k">WHERE</span> <span class="e">ativo = ???</span></pre>'
guess = row(*[f'<span class="badge" style="background:var(--critsub);color:var(--crit);border-color:transparent;font-weight:600">{n}</span>' for n in ("1.284?", "1.112?", "1.390?")])
frame(C+"-03", "fe", "dark", f'''<span class="label">Caminho 2 · IA sem contexto</span>{title("Rápido. Mas é chute.", "chute", "h1", "dark")}
<div class="mid"><div class="pipe">
{prow("message", "Pergunta", '<span class="ann">“Quantos clientes ativos temos?” vai direto para a IA</span>')}
{prow("cpu", "IA genérica", sql2, "hot")}
{prow("file-x", "Resposta", guess + '<span class="ann">Não sabe o que “cliente ativo” significa na sua empresa</span>', "bad")}
</div>{row(state("pos","Rápido"), state("crit","Acerto baixo"))}</div>''')

# 04 · caminho 3: hub com contexto escrito e governado
W, H = 476, 262
ai_x, ai_y = 188, 150
lines = "".join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}"/>' for a, b, c, d in (
    (50, 30, ai_x-14, ai_y-26), (188, 30, ai_x, ai_y-30), (378, 30, ai_x+14, ai_y-26),
    (96, ai_y, ai_x-30, ai_y), (ai_x+30, ai_y-8, 312, 96), (ai_x+30, ai_y, 312, 150), (ai_x+30, ai_y+8, 312, 204)))
dots = "".join(f'<circle cx="{x}" cy="{y}" r="4"/>' for x, y in ((116, 87), (188, 76), (282, 87), (132, ai_y), (266, 123), (266, 150), (266, 177)))
hub = f'''<div style="position:relative;width:{W}px;height:{H}px">
<svg width="{W}" height="{H}" style="position:absolute;inset:0"><g style="stroke:var(--strong);stroke-width:1.5;stroke-dasharray:4 4;fill:none">{lines}</g><g style="fill:var(--brand)">{dots}</g></svg>
<span class="pill" style="left:0;top:0;width:100px">Glossário</span><span class="pill" style="left:108px;top:0;width:160px">Camada semântica</span><span class="pill" style="left:280px;top:0;width:196px">Regras versionadas</span>
<span class="box" style="left:0;top:{ai_y-18}px;height:36px;width:96px">{ico("message",16)} Pergunta</span>
<span class="node" style="position:absolute;left:{ai_x-30}px;top:{ai_y-30}px;width:60px;height:60px;border-radius:16px;background:#05131C;border-color:rgba(146,197,73,0.6);box-shadow:var(--sglow)"><img src="file://{LOGOS}/4metrics-simbolo-negativo.svg" style="width:40px;height:40px"></span>
{"".join(f'<span class="box" style="left:312px;top:{y-18}px;height:36px;width:164px"><span class="strong" style="display:flex">{ico("check",16)}</span>{t}</span>' for y,t in ((96,"WhatsApp"),(150,"Slack e Teams"),(204,"Agentes via MCP")))}
<span class="ann" style="position:absolute;left:0;top:{H-20}px">Você controla o que a IA lê e responde.</span></div>'''
yml = '<pre class="code"><span class="k">metric:</span> cliente_ativo\n<span class="k">regra:</span>  compra faturada nos últimos 90 dias\n<span class="k">fonte:</span>  erp.pedidos\n<span class="k">versao:</span> v2 <span class="c"># aprovada pelo comercial</span></pre>'
frame(C+"-04", "fe", "nevoa", f'''<span class="label">Caminho 3 · IA com contexto</span>{title("Certo e na hora.", "na hora", "h1", "nevoa")}
<div class="mid" style="gap:12px">{hub}{yml}</div>''')

# 05 · comparativo lado a lado
ok = f'<span class="strong" style="display:inline-flex">{ico("check",18)}</span>'
no = f'<span style="display:inline-flex;color:var(--crit)">{ico("x",18)}</span>'
rows = [("Acerto", ok, no, ok), ("Tempo", "dias", "segundos", "segundos"), ("Contexto", "na cabeça de uma pessoa", "nenhum", "escrito e governado"),
        ("Escala", no, ok, ok), ("Serve para agentes", no, no, ok)]
cell = lambda v, sel=False: f'<td style="text-align:center;{"background:var(--bsub);font-weight:600" if sel else ""}">{v}</td>'
frame(C+"-05", "fe", "light", f'''{title("Lado a lado.", "Lado a lado.", "h1", "light")}<div class="mid">
<table class="tbl" style="border:1px solid var(--border);border-radius:16px;overflow:hidden;border-collapse:separate;border-spacing:0;font-size:13px;table-layout:fixed">
<tr><th style="width:92px"></th><th style="text-align:center">Analista de BI</th><th style="text-align:center">IA sem contexto</th><th style="text-align:center;background:var(--brand);color:#05131C">IA com contexto</th></tr>
{"".join(f'<tr><td class="muted" style="font-weight:500">{a}</td>{cell(b)}{cell(c)}{cell(d, True)}</tr>' for a,b,c,d in rows)}</table>
<p class="small muted">A diferença não está no modelo de IA. Está no contexto que ele recebe.</p></div>''')

# 06 · quem escreve o contexto + CTA
def layer(t, sub, chips_, feat=False):
    return f'<div class="card {"feat" if feat else ""}" style="padding:12px 16px;display:grid;gap:8px"><div style="display:flex;justify-content:space-between;align-items:center"><span class="h3" style="font-size:15px;line-height:20px">{t}</span><span class="label">{sub}</span></div>{chips(chips_)}</div>'
arrow = f'<span class="muted" style="display:flex;justify-content:center">{ico("arrow-down",16)}</span>'
frame(C+"-06", "fe", "light", f'''{title("Quem escreve o contexto? A 4metrics.", "A 4metrics.", "h1", "light")}
<div class="mid" style="gap:4px">{layer("Suas fontes", "sem trocar nada", ["CRM","ERP","Mídia","Planilhas","+50"])}{arrow}
{layer("Camada semântica 4metrics", "a gente constrói e mantém", ["Glossário","Regras","Versões","Acesso auditável"], True)}{arrow}
{layer("Sua IA e seus agentes", "conexão única", ["ChatGPT","Claude","Gemini","Copilot"])}</div>
<div style="display:flex;flex-direction:column;gap:10px"><span class="body" style="font-weight:600">Em qual dos três caminhos sua empresa está hoje?</span>{btn()}</div>''')

def feedstory(name, cover, theme):
    frame(name, "st", theme, f'<div class="mid" style="align-items:center"><img src="file://{OUT}/{cover}.png" style="width:440px;border-radius:16px;border:1px solid var(--border)"><span class="h3" style="display:flex;align-items:center;gap:8px">Confira no perfil {ico("arrow-right",20)}</span></div>', "Post novo no feed", foot=False)

if __name__ == "__main__":
    render(OUT)
    feedstory(f"2027-02-05-story-tres-caminhos-{V}", C+"-01", "dark")
    print(len(FR), render(OUT))

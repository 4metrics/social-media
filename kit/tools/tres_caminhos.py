# 4metrics · "Três jeitos de responder" (05/02/2027) · comparativo, um caminho por tela
import sys
sys.path.insert(0, "/home/claude/tools")
from ds4m import *
V = "v1"
OUT = "/home/claude/out/tres-caminhos"
C = f"2027-02-05-tres-caminhos-{V}"

def flow(nodes):
    arrow = f'<span class="muted" style="display:flex;justify-content:center">{ico("arrow-down",18)}</span>'
    return '<div style="display:flex;flex-direction:column;gap:4px">' + arrow.join(
        f'<div class="card" style="padding:12px 18px;display:flex;justify-content:space-between;align-items:center;gap:12px"><span class="h3">{a}</span><span class="label" style="text-align:right">{b}</span></div>' for a, b in nodes) + '</div>'
code = lambda t: f'<span style="align-self:flex-start;font-family:ui-monospace,Menlo,monospace;font-size:14px;line-height:20px;padding:6px 12px;border-radius:8px;background:var(--subtle);border:1px solid var(--border)">{t}</span>'
row = lambda *s: '<div style="display:flex;gap:8px;flex-wrap:wrap">' + "".join(s) + '</div>'

frame(C+"-01", "fe", "nevoa", f'''{title("Três jeitos de responder: quanto vendemos este mês?", "quanto vendemos", "h1", "nevoa")}
<div class="mid">{ph("3184634", 330, "center 40%")}</div>''', "IA com contexto")

frame(C+"-02", "fe", "light", f'''<span class="label">Caminho 1 · Analista de BI</span>{title("O número certo, dias depois.", "dias depois", "h1", "light")}
<div class="mid">{flow([("Pergunta", "do comercial"), ("Fila de pedidos", "espera a vez"), ("SQL e planilha", "feito à mão"), ("Dashboard", "chega dias depois")])}
{row(state("pos","Acerto alto"), state("warn","Demora"))}</div>''')

frame(C+"-03", "fe", "dark", f'''<span class="label">Caminho 2 · IA sem contexto</span>{title("Rápido. Mas é chute.", "chute", "h1", "dark")}
<div class="mid"><div style="align-self:flex-end;background:#FFFFFF;color:#05131C;border-radius:16px;padding:12px 16px" class="body">Quantos clientes ativos temos?</div>
<div class="card" style="display:grid;gap:8px"><span class="label">Resposta da IA</span><span class="metric">1.284 clientes ativos</span>{code('"cliente ativo" = ???')}<span class="small muted">A IA não sabe o que esse termo significa na sua empresa.</span></div>
{row(state("pos","Rápido"), state("crit","Acerto baixo"))}</div>''')

frame(C+"-04", "fe", "nevoa", f'''<span class="label">Caminho 3 · IA com contexto</span>{title("Certo e na hora.", "na hora", "h1", "nevoa")}
<div class="mid"><div class="card feat" style="display:grid;gap:0;padding:20px 24px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px"><span class="h3">Cliente ativo</span>{state("pos","Regra oficial")}</div>
{"".join(f'<div style="display:flex;justify-content:space-between;gap:16px;padding:8px 0;border-top:1px solid var(--border)"><span class="small muted">{k}</span><span class="small" style="font-weight:500;text-align:right">{v}</span></div>' for k,v in (("Regra","comprou nos últimos 90 dias"),("Fonte","ERP"),("Versão","v2, aprovada pelo comercial"),("Usada por","painel, alertas e a sua IA")))}</div>
{row(state("pos","Acerto alto"), state("pos","Na hora"))}</div>''')

frame(C+"-05", "fe", "light", f'''<div class="mid">{title("Quem escreve o contexto? A 4metrics.", "A 4metrics.", "h1", "light")}
<p class="body">Glossário, regras e camada semântica, construídos e mantidos por nós. Você só acessa. Primeiro insight em até 14 dias.</p>
<div class="card insight"><p class="h3">Em qual dos três caminhos a sua empresa está hoje?</p></div>{btn()}<p class="small muted">Ou comente DIAGNÓSTICO.</p></div>''')

def feedstory(name, cover, theme):
    frame(name, "st", theme, f'<div class="mid" style="align-items:center"><img src="file://{OUT}/{cover}.png" style="width:440px;border-radius:16px;border:1px solid var(--border)"><span class="h3" style="display:flex;align-items:center;gap:8px">Confira no perfil {ico("arrow-right",20)}</span></div>', "Post novo no feed", foot=False)

if __name__ == "__main__":
    render(OUT)
    feedstory(f"2027-02-05-story-tres-caminhos-{V}", C+"-01", "dark")
    print(len(FR), render(OUT))

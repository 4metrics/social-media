# 4metrics · Série "Como fazer" (referência: formato prático da Nekt, adaptado à 4metrics)
# Estrutura de cada episódio: por que importa → o que precisa → passo a passo → onde trava → como a 4metrics faz → CTA
import sys
sys.path.insert(0, "/home/claude/tools")
from ds4m import *
V = "v1"
OUT = "/home/claude/out/serie-como"
B = "Como fazer"

def flow(nodes):
    arrow = f'<span class="muted" style="display:flex;justify-content:center">{ico("arrow-down",20)}</span>'
    return '<div style="display:flex;flex-direction:column;gap:6px">' + arrow.join(
        f'<div class="card {"feat" if f else ""}" style="padding:14px 18px;display:flex;justify-content:space-between;align-items:center;gap:12px"><div style="display:grid;gap:2px"><span class="h3">{a}</span><span class="small muted">{b}</span></div><span class="label" style="text-align:right">{c}</span></div>'
        for a, b, c, f in nodes) + '</div>'

def rules(title_, rows):
    return (f'<div class="card feat" style="display:grid;gap:0;padding:20px 24px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px"><span class="h3">{title_}</span>{state("pos","Regra oficial")}</div>'
            + "".join(f'<div style="display:flex;justify-content:space-between;gap:16px;padding:8px 0;border-top:1px solid var(--border)"><span class="small muted">{k}</span><span class="small" style="font-weight:500;text-align:right">{v}</span></div>' for k, v in rows) + '</div>')

def cta(text, kw, body, theme="light", extra=""):
    return f'<div class="mid">{title(text, kw, "h1", theme)}{extra}<p class="body">{body}</p>{btn()}<p class="small muted">Ou comente DIAGNÓSTICO.</p></div>'

trava = lambda lst: items(lst, "arrow-right")

# ============ EP1 · CAC · 22/01 (sexta) · capa névoa com foto em card
C = f"2027-01-22-como-cac-{V}"
frame(C+"-01", "fe", "nevoa", f'''{title("Como calcular o CAC certo", "CAC certo", "display", "nevoa")}
<p class="body muted">Com dados de CRM, mídia e ERP.</p><div class="mid">{ph("3183153", 300, "center 40%")}</div>''', B)
frame(C+"-02", "fe", "light", f'''{title("Cada sistema tem um pedaço da conta.", "pedaço", "h1", "light")}<div class="mid">{flow([
 ("Mídia", "Meta Ads, Google Ads", "Investimento", False),
 ("CRM", "RD Station, HubSpot, Kommo", "Leads e oportunidades", False),
 ("ERP", "Bling, Omie", "Venda faturada", True)])}</div>''')
frame(C+"-03", "fe", "nevoa", f'''<span class="label">Passo 1</span>{title("Escreva a regra antes da fórmula.", "regra", "h1", "nevoa")}<div class="mid">{rules("CAC", [
 ("Fórmula", "(mídia + custo comercial) ÷ clientes novos"), ("Cliente novo", "primeira venda faturada no ERP"), ("Período", "mês da venda"), ("Versão", "v1, aprovada pelo comercial")])}
<p class="small muted">Quem decide o que conta é o seu time. Uma vez só.</p></div>''')
frame(C+"-04", "fe", "light", f'''<span class="label">Passo 2</span>{title("Ligue as fontes pela mesma chave.", "mesma chave", "h1", "light")}<div class="mid">{steps([
 "Investimento por campanha, da mídia", "Oportunidade ganha, do CRM", "Pedido faturado, do ERP", "Chave comum: CNPJ ou e-mail do cliente"])}</div>''')
frame(C+"-05", "fe", "dark", f'''{title("Onde costuma travar.", "travar", "h1", "dark")}<div class="mid">{trava([
 "Cliente com cadastro diferente no CRM e no ERP", "Custo comercial fora de qualquer sistema", "Planilha refeita todo mês, por uma pessoa só"])}</div>''')
frame(C+"-06", "fe", "light", cta("Na 4metrics, o CAC sai pronto todo dia.", "todo dia",
 "Conectamos as fontes, aplicamos a regra oficial e avisamos quando o número muda. Primeiro insight em até 14 dias."))

# ============ EP2 · campanha → venda · 26/01 (terça) · foto em tela cheia
C = f"2027-01-26-como-campanha-venda-{V}"
frame(C+"-01", "fe", "photo", f'''<div class="mid" style="justify-content:flex-end">{title("Como saber qual campanha vira venda", "vira venda", "display", "photo")}
<p class="body muted">E não só lead.</p></div>''', B, photo=("7688460", "center"))
frame(C+"-02", "fe", "dark", f'''{title("A mídia mostra o lead. A venda está no ERP.", "ERP", "h1", "dark")}<div class="mid">{flow([
 ("Campanha", "Meta Ads, Google Ads", "Clique e lead", False),
 ("Oportunidade", "CRM", "Proposta e fechamento", False),
 ("Pedido", "ERP", "Receita faturada", True)])}</div>''')
tb = [("Campanha A", "420", "9", False), ("Campanha B", "180", "21", True), ("Campanha C", "260", "12", False)]
frame(C+"-03", "fe", "light", f'''{title("Mais lead nem sempre é mais venda.", "mais venda", "h1", "light")}<div class="mid">
<table class="tbl" style="border:1px solid var(--border);border-radius:16px;overflow:hidden;border-collapse:separate;border-spacing:0">
<tr><th>Campanha</th><th style="text-align:right">Leads</th><th style="text-align:right">Vendas faturadas</th></tr>
{"".join(f'<tr class="{"sel" if s else ""}"><td style="font-weight:500">{a}</td><td style="text-align:right">{b}</td><td style="text-align:right;font-weight:600">{c}</td></tr>' for a,b,c,s in tb)}</table>
<p class="small muted">Só dá para ver isso com mídia, CRM e ERP na mesma base.</p></div>''')
frame(C+"-04", "fe", "nevoa", f'''{title("O passo a passo.", "passo a passo", "h1", "nevoa")}<div class="mid">{steps([
 "Leve a origem da mídia (UTM) para o CRM", "Ligue a oportunidade ganha ao pedido no ERP", "Some a receita faturada por campanha", "Compare com o investimento de cada uma"])}</div>''')
frame(C+"-05", "fe", "light", f'''{title("Onde costuma travar.", "travar", "h1", "light")}<div class="mid">{trava([
 "Origem perdida no formulário ou no WhatsApp", "Venda fechada fora do CRM", "Pedido no ERP sem ligação com a oportunidade"])}</div>''')
frame(C+"-06", "fe", "dark", cta("Na 4metrics, receita por campanha todo dia.", "receita por campanha",
 "Mídia, CRM e ERP na mesma base, com a regra oficial. E um alerta quando a campanha gasta e não vende.", "dark"))

# ============ EP3 · CRM + ERP · 29/01 (sexta) · capa clara com foto em card
C = f"2027-01-29-como-crm-erp-{V}"
frame(C+"-01", "fe", "light", f'''<div style="margin:-32px -32px 0">{ph("3183150", 260, "center", "0")}</div>
{badge(B)}{title("Como integrar o CRM com o ERP sem time de dados", "sem time de dados", "h1", "light")}''', None)
frame(C+"-02", "fe", "nevoa", f'''{title("Por que integrar.", "integrar", "h1", "nevoa")}<div class="mid">{items([
 "Ver quanto cada vendedor fatura, não só quanto fecha", "Acompanhar o cliente do lead até o pedido", "Medir CAC, ticket e recompra do mesmo cliente"])}</div>''')
frame(C+"-03", "fe", "light", f'''{progress(0)}{title("Mapeie as fontes e a chave do cliente.", "chave", "h1", "light")}<div class="mid">
<div class="card" style="display:grid;gap:12px"><span class="label">CRM</span>{chips(["HubSpot","RD Station","Kommo","Salesforce"])}<span class="label">ERP</span>{chips(["Bling","Omie"])}</div>
<p class="small muted">A chave que liga os dois: CNPJ ou e-mail do cliente.</p></div>''')
frame(C+"-04", "fe", "nevoa", f'''{progress(1)}{title("Crie as métricas oficiais.", "oficiais", "h1", "nevoa")}<div class="mid">{rules("Receita faturada", [
 ("Fonte", "ERP"), ("Ligada a", "vendedor e origem, do CRM"), ("Atualização", "todo dia")])}<p class="small muted">E o mesmo para ticket médio, conversão e recompra.</p></div>''')
frame(C+"-05", "fe", "dark", f'''{progress(2)}{title("Leve a resposta para a rotina.", "rotina", "h1", "dark")}<div class="mid">{chips(["WhatsApp","E-mail","Slack","Teams","MCP"])}
<p class="body muted">Um alerta quando o número sai do esperado, com o próximo passo.</p></div>''')
frame(C+"-06", "fe", "light", cta("Sem montar time de dados. Sem trocar suas ferramentas.", "Sem trocar",
 "A 4metrics faz as três etapas com você. Primeiro insight em até 14 dias."))

# ============ EP4 · dados prontos para IA · 02/02 (terça) · capa escura com foto em círculo
C = f"2027-02-02-como-dados-ia-{V}"
frame(C+"-01", "fe", "dark", f'''<div style="width:220px">{ph("6802042", 220, "center", "999px")}</div>
<div class="mid" style="justify-content:flex-end">{title("Como deixar seus dados prontos para a IA", "prontos", "display", "dark")}</div>''', B)
frame(C+"-02", "fe", "nevoa", f'''<div class="mid" style="align-items:flex-start"><span class="display" style="font-size:120px;line-height:120px;letter-spacing:-0.04em">60%</span>
{title("dos projetos de IA sem dados prontos serão abandonados.", "abandonados", "h1", "nevoa")}</div><p class="label" style="position:absolute;right:32px;bottom:32px">Fonte: Gartner</p>''')
ctx = [("Contexto do negócio", "Metas, regras e o que conta como cliente ativo"), ("Contexto dos dados", "De onde vem cada número e quando atualizou"), ("Camada semântica", "A mesma definição para pessoas e agentes")]
frame(C+"-03", "fe", "light", f'''{title("A IA precisa de contexto.", "contexto", "h1", "light")}<div class="mid" style="gap:8px">{"".join(f'<div class="card {"feat" if i==2 else ""}" style="padding:16px 20px;display:grid;gap:4px"><span class="h3">{a}</span><span class="small muted">{b}</span></div>' for i,(a,b) in enumerate(ctx))}</div>''')
frame(C+"-04", "fe", "nevoa", f'''{title("O passo a passo.", "passo a passo", "h1", "nevoa")}<div class="mid">{steps([
 "Junte as fontes numa base só", "Defina cada métrica uma vez, com versão", "Dê acesso à IA por uma conexão única (MCP)", "Deixe os agentes executarem com a sua aprovação"])}</div>''')
frame(C+"-05", "fe", "dark", f'''{title("Onde costuma travar.", "travar", "h1", "dark")}<div class="mid">{trava([
 "IA ligada em cada ferramenta, cada uma com um número", "Métrica sem dono e sem regra escrita", "Acesso sem controle e sem registro"])}</div>''')
frame(C+"-06", "fe", "light", cta("Na 4metrics, sua IA lê os números oficiais.", "números oficiais",
 "Base pronta, regras versionadas e uma conexão única para a IA que a sua empresa usar.", "light", chips(["ChatGPT","Claude","Gemini","Copilot"])))

def feedstory(name, cover, theme):
    frame(name, "st", theme, f'<div class="mid" style="align-items:center"><img src="file://{OUT}/{cover}.png" style="width:440px;border-radius:16px;border:1px solid var(--border)"><span class="h3" style="display:flex;align-items:center;gap:8px">Confira no perfil {ico("arrow-right",20)}</span></div>', "Post novo no feed", foot=False)
FEEDS = [("2027-01-22-story-como-cac", f"2027-01-22-como-cac-{V}-01", "dark"), ("2027-01-26-story-como-campanha-venda", f"2027-01-26-como-campanha-venda-{V}-01", "nevoa"),
         ("2027-01-29-story-como-crm-erp", f"2027-01-29-como-crm-erp-{V}-01", "dark"), ("2027-02-02-story-como-dados-ia", f"2027-02-02-como-dados-ia-{V}-01", "nevoa")]

if __name__ == "__main__":
    render(OUT)
    for n, c, t in FEEDS: feedstory(f"{n}-{V}", c, t)
    print(len(FR), "frames", render(OUT))

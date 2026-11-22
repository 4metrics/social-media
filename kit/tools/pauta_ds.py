import sys
sys.path.insert(0, "/home/claude/tools")
from ds4m import *
V = "v3"
OUT = "/home/claude/out/pauta-ds"

# ============ T10 · 67% · 04/12 · estático névoa
bars = "".join(f'<div style="display:flex;align-items:center;gap:12px"><span class="label" style="width:36px">{y}</span><div style="flex:1;height:12px;border-radius:999px;background:var(--subtle);border:1px solid var(--border);overflow:hidden"><div style="width:{v}%;height:100%;background:{c}"></div></div><span class="metric" style="width:56px;text-align:right">{v}%</span></div>' for y, v, c in (("2023", 55, "var(--bstrong)"), ("2024", 67, "var(--brand)")))
frame(f"2026-12-04-confianca-67-{V}", "fe", "nevoa", f'''
<div style="display:flex;gap:16px;align-items:center"><span class="display" style="font-size:96px;line-height:96px;letter-spacing:-0.04em">67%</span><div style="flex:1">{ph("5716001",120)}</div></div>
{title("das organizações não confiam totalmente nos dados que usam para decidir.", "não confiam", "h1", "nevoa")}
<div class="mid"><div class="card" style="display:grid;gap:12px">{bars}<span class="small muted">A desconfiança cresceu em um ano.</span></div></div>
<p class="label" style="position:absolute;right:32px;bottom:32px;text-align:right;font-size:11px;line-height:15px">Fonte: Precisely e Drexel University,<br>2025 Outlook: Data Integrity Trends and Insights</p>''', "Dados de mercado")
S = f"2026-12-04-st-confianca-67-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("2 em cada 3 empresas não confiam no próprio número.", "não confiam", "display", "photo")}</div>', "Dados de mercado", photo=("3184292",))
frame(S+"-02", "st", "light", f'{title("A desconfiança está crescendo.", "crescendo", "h1", "light")}<div class="mid"><div class="card" style="display:grid;gap:16px">{bars}</div><p class="small muted">Organizações que não confiam totalmente nos dados que usam para decidir. Fonte: Precisely e Drexel University, 2025 Outlook.</p></div>')
nums = '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px">' + "".join(f'<div class="card" style="padding:16px;display:grid;gap:4px"><span class="label">{a}</span><span class="metric" style="font-size:22px">{b}</span></div>' for a, b in (("Planilha", "R$ 1,08 mi"), ("Power BI", "R$ 1,24 mi"), ("Relatório", "R$ 980 mil"))) + '</div>'
frame(S+"-03", "st", "dark", f'{title("O sintoma: cada área chega com o seu número.", "sintoma", "h1", "dark")}<div class="mid"><p class="body muted">Quanto vendemos este mês?</p>{nums}</div>')
oficial = metric("Receita do mês · número oficial", "R$ 1,12 mi", delta("+8%", "vs. outubro"), feat=True)
frame(S+"-04", "st", "lima", f'<div class="mid">{title("Com a 4metrics, um número oficial.", None, "display", "lima")}{oficial}<p class="body">Uma regra por métrica, verificada e igual para todo mundo.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T6 · fila · 07/12 · stories (feed = Reel)
S = f"2026-12-07-st-fila-relatorios-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("Seu time de dados virou fila de relatórios?", "fila", "display", "photo")}</div>', "Custo da demora", photo=("7688336",))
tk = [("#124", "Receita por canal", "há 6 dias"), ("#125", "CAC de outubro", "há 4 dias"), ("#126", "Leads parados no funil", "há 3 dias"), ("#127", "Meta x realizado por loja", "há 1 dia")]
frame(S+"-02", "st", "light", f'''{title("Um pedido para cada número.", "pedido", "h1", "light")}<div class="mid"><table class="tbl" style="border:1px solid var(--border);border-radius:16px;overflow:hidden;border-collapse:separate;border-spacing:0">
<tr><th>Pedido</th><th>Relatório</th><th style="text-align:right">Na fila</th></tr>{"".join(f'<tr><td class="muted">{a}</td><td style="font-weight:500">{b}</td><td style="text-align:right;color:var(--warn);font-weight:600;white-space:nowrap">{c}</td></tr>' for a,b,c in tk)}</table>
<p class="body muted">E a semana passa montando relatório.</p></div>''')
frame(S+"-03", "st", "nevoa", f'''{title("Com a 4metrics, a resposta chega na hora.", "na hora", "h1", "nevoa")}<div class="mid">
<div style="align-self:flex-end;background:#05131C;color:#fff;border-radius:16px;padding:12px 16px" class="body">Qual foi o CAC de outubro?</div>
{metric("CAC de outubro · número oficial", "R$ 48", '<span class="small muted">O mesmo número do painel, com a regra oficial.</span>', feat=True)}</div>''')
frame(S+"-04", "st", "dark", f'<div class="mid">{title("E o time de dados volta a melhorar o dado.", "melhorar", "display", "dark")}<p class="body muted">Comercial e marketing saem da fila.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T1 · métricas oficiais · 14/12 · carrossel névoa 5
C = f"2026-12-14-metricas-oficiais-{V}"
frame(C+"-01", "fe", "nevoa", f'''{title("Acabou a briga pelo número certo.", "certo", "display", "nevoa")}
<div class="mid" style="gap:0">{ph("3184339",250)}<div style="margin:-56px 24px 0;position:relative">{metric("Receita do mês · número oficial","R$ 1,12 mi",delta("+8%","vs. outubro"),feat=True,extra="background:#fff")}</div></div>''', "Métricas oficiais")
frame(C+"-02", "fe", "dark", f'<p class="body muted">Quanto vendemos este mês?</p>{title("Três ferramentas. Três números.", "Três números.", "h1", "dark")}<div class="mid">{nums}<p class="body muted">E a reunião discute qual está certo.</p></div>')
mcard = lambda: f'''<div class="card feat" style="display:grid;gap:0;padding:20px 24px"><div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px"><span class="h3">Ticket médio</span>{state("pos","Verificada")}</div>
{"".join(f'<div style="display:flex;justify-content:space-between;padding:8px 0;border-top:1px solid var(--border)"><span class="small muted">{k}</span><span class="small" style="font-weight:500">{v}</span></div>' for k,v in (("Fórmula","receita faturada ÷ pedidos"),("Fonte","ERP"),("Versão","v3, aprovada pelo comercial"),("Usada em","painel, alerta, resumo e sua IA")))}</div>'''
frame(C+"-03", "fe", "light", f'{title("Uma regra por métrica.", "regra", "h1", "light")}<p class="body muted">Conversão, ticket médio, meta e receita: definidas uma vez com o seu time.</p><div class="mid">{mcard()}</div>')
frame(C+"-04", "fe", "nevoa", f'{title("Verificado antes de publicar.", "Verificado", "h1", "nevoa")}<p class="body muted">Se a regra muda, o número volta para revisão antes de chegar à diretoria.</p><div class="mid">{steps(["A regra muda","O número vai para revisão","A nova versão é aprovada","A diretoria recebe o número certo"])}</div>')
frame(C+"-05", "fe", "light", f'<div class="mid">{title("Igual em todo lugar.", "todo lugar", "h1", "light")}{chips(["Painel","Alerta","Resumo diário","Agentes de IA"])}<p class="body">Uma regra, um número oficial e a mesma resposta para o seu time e para os seus agentes de IA.</p>{btn()}<p class="small muted">Ou comente DIAGNÓSTICO.</p></div>')
S = f"2026-12-14-st-metricas-oficiais-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("Qual número está certo?", "certo?", "display", "photo")}</div>', "Métricas oficiais", photo=("3183197",))
frame(S+"-02", "st", "dark", f'{title("Planilha, Power BI e relatório. Três respostas.", "Três respostas.", "h1", "dark")}<div class="mid">{nums}</div>')
frame(S+"-03", "st", "light", f'{title("Na 4metrics, cada métrica tem uma regra oficial.", "regra oficial", "h1", "light")}<div class="mid">{mcard()}</div>')
frame(S+"-04", "st", "lima", f'<div class="mid">{title("A reunião discute o que fazer.", None, "display", "lima")}<p class="body">Não qual número está certo.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T7 · segurança · 21/12 · estático névoa
seals = ["Conformidade com a LGPD", "Criptografia", "Acesso auditável", "Verificação em duas etapas", "DPA disponível"]
frame(f"2026-12-21-seguranca-{V}", "fe", "nevoa", f'''<div style="display:flex;gap:16px;align-items:center">{title("Seus dados protegidos do início ao fim.", "protegidos", "h1", "nevoa", "flex:1")}<div style="width:140px;flex:none">{ph("1181467",140,"30% center","999px")}</div></div>
<div class="mid">{items(seals,"shield-check")}</div><p class="small muted">E os seus agentes de IA executam com a sua aprovação.</p>''', "Segurança")
S = f"2026-12-21-st-seguranca-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("IA com os dados da empresa. E a segurança?", "segurança?", "display", "photo")}</div>', "Segurança", photo=("3861969",))
frame(S+"-02", "st", "light", f'{title("Com IA genérica, o controle sai da sua mão.", "controle", "h1", "light")}<div class="mid">{items(["Dados da empresa e de clientes fora do seu controle","Sem rastreabilidade de onde o número veio","A responsabilidade continua sendo sua"],"arrow-right")}</div>')
frame(S+"-03", "st", "nevoa", f'{title("Na 4metrics, a segurança vem junto.", "segurança", "h1", "nevoa")}<div class="mid">{items(seals,"shield-check")}</div>')
frame(S+"-04", "st", "dark", f'<div class="mid">{title("O mesmo controle de acesso, também na sua IA.", "também", "display", "dark")}<p class="body muted">Seus agentes executam com a sua aprovação. E fica registrado.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T2 · regra muda · 06/01 · stories (feed = Reel)
S = f"2027-01-06-st-regra-muda-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("E quando a regra muda?", "muda?", "display", "photo")}<p class="body muted">O CPL passa a contar só lead qualificado.</p></div>', "Métricas oficiais", photo=("669615",))
frame(S+"-02", "st", "light", f'''{title("Sem regra oficial, tudo é refeito.", "refeito", "h1", "light")}<div class="mid"><div style="display:flex;flex-direction:column;gap:8px">{"".join(f'<div class="card" style="padding:12px 16px;display:flex;justify-content:space-between;align-items:center"><span class="body" style="font-weight:500">{x}</span>{state("warn","Refazer")}</div>' for x in ("Planilha","Power BI","Relatório"))}</div><p class="body muted">Por semanas, cada um mostra uma regra.</p></div>''')
ver = f'''<div class="card feat" style="display:grid;gap:12px"><div style="display:flex;justify-content:space-between;align-items:center"><span class="h2">CPL</span>{state("pos","Versão 2 · hoje")}</div>
<span class="small muted" style="text-decoration:line-through">Versão 1: custo ÷ todos os leads</span><span class="body" style="font-weight:500">Versão 2: custo ÷ leads qualificados</span></div>'''
frame(S+"-03", "st", "dark", f'{title("Na 4metrics, a regra muda uma vez, com nova versão.", "uma vez", "h1", "dark")}<div class="mid">{ver}</div>')
frame(S+"-04", "st", "lima", f'<div class="mid">{title("No mesmo dia, em todo lugar.", None, "display", "lima")}{chips(["Painel","Alerta","Sua IA"])}<p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T3 · camada semântica · 08/01 · estático névoa
frame(f"2027-01-08-camada-semantica-{V}", "fe", "nevoa", f'''{title("A IA consulta a métrica pronta. Nunca a tabela crua.", "pronta", "h1", "nevoa")}
<div class="mid" style="gap:0">{ph("7213549",170)}<div style="margin:-48px 20px 0;position:relative">{mcard().replace('class="card feat"','class="card feat" style="background:#fff"',1)}</div></div>''', "Camada semântica")
S = f"2027-01-08-st-camada-semantica-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("Por que a IA erra o número?", "erra", "display", "photo")}</div>', "Camada semântica", photo=("6801648",))
frame(S+"-02", "st", "light", f'{title("Ela não conhece as regras do seu negócio.", "regras", "h1", "light")}<p class="body muted">Para acertar, a IA precisa de três coisas:</p><div class="mid">{steps(["Contexto do negócio: metas, regras e o que cada área chama de venda","Contexto dos dados: de onde vem cada número","Camada semântica: as métricas oficiais"])}</div>')
frame(S+"-03", "st", "nevoa", f'{title("A métrica pronta, com nome, fórmula e versão.", "pronta", "h1", "nevoa")}<div class="mid">{mcard()}</div>')
frame(S+"-04", "st", "dark", f'<div class="mid">{title("O mesmo contexto em todo lugar.", "contexto", "display", "dark")}<p class="body muted">No painel, no alerta, no chat e na sua IA via MCP.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T5 · time de dados · 11/01 · carrossel claro 5
C = f"2027-01-11-sem-time-de-dados-{V}"
frame(C+"-01", "fe", "light", f'{title("Você não precisa de um time de dados. Você precisa da resposta.", "resposta", "h1", "light")}<div class="mid">{ph("3182812",330,"center 30%")}</div>', "Revenue Intelligence")
frame(C+"-02", "fe", "nevoa", f'{title("Montar um time de dados é caro e demorado.", "caro", "h1", "nevoa")}<div class="mid">{items(["Contratar e reter especialistas","Conectar e manter as fontes","Criar e ajustar as regras do negócio","Atender a fila de pedidos"],"arrow-right")}</div>')
tb = [("Quem faz", "Você contrata um projeto", "O seu time monta", "A 4metrics faz, sempre"), ("O que recebe", "Dashboard no fim", "Ferramentas para montar", "Resposta com o próximo passo"), ("1ª resposta", "Semanas a meses", "Depende do seu time", "Até 14 dias"), ("Negócio mudou", "Novo orçamento", "O seu time refaz", "A 4metrics ajusta"), ("Pronto para IA", "Fora do escopo", "Se o seu time montar", "Sim, via MCP")]
tbl = '<table class="tbl" style="font-size:12px;line-height:16px;border:1px solid var(--border);border-radius:16px;overflow:hidden;border-collapse:separate;border-spacing:0"><tr><th></th><th>Consultoria de BI</th><th>Plataforma de dados</th><th style="color:var(--strong)">4metrics</th></tr>' + "".join(f'<tr><td style="font-weight:600;padding:10px 8px">{r[0]}</td><td class="muted" style="padding:10px 8px">{r[1]}</td><td class="muted" style="padding:10px 8px">{r[2]}</td><td style="font-weight:600;padding:10px 8px;background:var(--bsub)">{r[3]}</td></tr>' for r in tb) + '</table>'
frame(C+"-03", "fe", "light", f'{title("Consultoria, plataforma ou 4metrics?", "4metrics?", "h1", "light")}<div class="mid">{tbl}</div>')
frame(C+"-04", "fe", "dark", f'{title("A fundação é com a gente.", "com a gente", "h1", "dark")}<div class="mid">{steps(["Mapeamento: entendemos o negócio antes do dado","Acesso: você libera, a gente conecta","Extração: os dados chegam sozinhos, todo dia","Modelagem: um número só, com uma regra só","Manutenção: a fundação não para no primeiro dia"])}</div>')
frame(C+"-05", "fe", "nevoa", f'<div class="mid">{metric("Primeiro insight","Até 14 dias",feat=True)}{title("Sem montar time de dados. Sem trocar suas ferramentas.", "Sem trocar", "h1", "nevoa")}{btn()}<p class="small muted">Ou comente DIAGNÓSTICO.</p></div>')
S = f"2027-01-11-st-sem-time-de-dados-{V}"
frame(S+"-01", "st", "nevoa", f'{title("Precisa contratar um time de dados?", "time de dados?", "display", "nevoa")}<div class="mid">{ph("5439381",420)}</div>', "Revenue Intelligence")
frame(S+"-02", "st", "light", f'<div class="mid">{title("Não.", "Não.", "display", "light")}<p class="body">O time da 4metrics conecta as fontes, cria as métricas e ajusta as regras quando o seu negócio muda.</p></div>')
frame(S+"-03", "st", "dark", f'{title("A fundação é com a gente.", "com a gente", "h1", "dark")}<div class="mid">{steps(["Mapeamento","Acesso","Extração","Modelagem","Manutenção"])}</div>')
frame(S+"-04", "st", "lima", f'<div class="mid">{title("Primeiro insight em até 14 dias.", None, "display", "lima")}<p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T4 · agentes · 13/01 · stories (feed = Reel)
S = f"2027-01-13-st-agentes-aprovacao-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("E se a IA executasse o próximo passo?", "próximo passo?", "display", "photo")}</div>', "Agentes de IA", photo=("7567443",))
frame(S+"-02", "st", "light", f'{title("Do gargalo à execução.", "execução", "h1", "light")}<div class="mid">{steps(["A 4metrics encontra o gargalo","O próximo passo vai para o seu agente","Você aprova","Ele executa no CRM e fica registrado"])}</div>')
appr = f'''<div class="card feat" style="display:grid;gap:16px">{state("warn","Atenção")}<span class="h2">Priorizar os contatos parados há mais de 30 dias.</span>
<div style="display:flex;gap:8px"><span class="btn">Aprovar</span><span class="btn" style="background:var(--surface);color:var(--ink);border:1px solid var(--bstrong)">Ajustar</span></div></div>'''
frame(S+"-03", "st", "nevoa", f'{title("Nada acontece sem você.", "sem você", "h1", "nevoa")}<div class="mid">{appr}</div>')
frame(S+"-04", "st", "dark", f'<div class="mid">{title("Você decide quem executa: o seu time ou os seus agentes.", "Você decide", "display", "dark")}<p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T8 · parceiros · 15/01 · estático lima
pt = '<div style="display:flex;flex-direction:column;gap:8px">' + "".join(f'<div class="card" style="padding:16px 20px;display:flex;align-items:center;gap:12px"><span style="display:flex;color:#406500">{ico("check")}</span><span class="h2">{x}</span></div>' for x in ("Google Cloud", "Gemini Enterprise", "Claude Partner Network")) + '</div>'
frame(f"2027-01-15-parceiros-{V}", "fe", "lima", f'''<div style="display:flex;gap:16px;align-items:center">{title("Parceiros oficiais de quem faz a IA.", None, "h1", "lima", "flex:1")}<div style="width:130px;flex:none">{ph("3184465",130,"center","999px")}</div></div>
<div class="mid">{pt}</div><p class="small" style="color:#1F3A12">Seus números oficiais chegam a qualquer IA por uma conexão única.</p>''', "Parceiros")
S = f"2027-01-15-st-parceiros-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("Com quem a 4metrics trabalha?", "trabalha?", "display", "photo")}</div>', "Parceiros", photo=("5673488",))
frame(S+"-02", "st", "lima", f'{title("Parceiros oficiais.", None, "h1", "lima")}<div class="mid">{pt}</div>')
frame(S+"-03", "st", "dark", f'{title("Uma conexão única para qualquer IA.", "qualquer IA", "h1", "dark")}<div class="mid">{chips(["ChatGPT","Claude","Gemini","Copilot"])}<p class="body muted">Quando a sua empresa trocar ou adicionar uma IA, ela já lê os mesmos números.</p></div>')
frame(S+"-04", "st", "light", f'<div class="mid">{title("Sua empresa pronta para cada nova IA.", "pronta", "display", "light")}<p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T9 · BI e company brain · 18/01 · carrossel claro 4
C = f"2027-01-18-bi-company-brain-{V}"
frame(C+"-01", "fe", "light", f'''<div class="mid" style="flex-direction:row;align-items:center;gap:20px"><div style="flex:1;display:flex;flex-direction:column;gap:16px"><p class="body muted">As dúvidas que ouvimos antes de todo diagnóstico.</p>{title("Já tenho BI. Faz sentido?", "sentido?", "h1", "light")}{chips(["BI","Company brain","MCP do CRM"])}</div>
<div style="width:200px;flex:none">{ph("8867431",400,"60% center")}</div></div>''', "Dúvidas frequentes")
hub = lambda a, b: f'''<div style="display:flex;align-items:center;gap:12px"><div class="card" style="flex:1;text-align:center;padding:20px 12px"><span class="h3">{a}</span></div><span class="strong" style="display:flex">{ico("arrow-left-right",24)}</span>
<div class="card feat" style="flex:1;display:flex;flex-direction:column;align-items:center;gap:8px;padding:16px 12px"><img src="file://{LOGOS}/4metrics-simbolo.svg" style="height:32px"><span class="h3">{b}</span></div></div>'''
frame(C+"-02", "fe", "nevoa", f'{title("A 4metrics substitui o meu BI?", "BI?", "h1", "nevoa")}<p class="body">Pode substituir, mas não precisa. Funciona junto com o BI que você já usa e tira o comercial da fila de pedidos.</p><div class="mid">{hub("Seu BI","4metrics")}</div>')
frame(C+"-03", "fe", "light", f'{title("Já usamos um company brain.", "company brain.", "h1", "light")}<p class="body">Ele conhece documentos e conversas. A 4metrics entrega para ele os números oficiais e o próximo passo, via MCP.</p><div class="mid">{hub("Company brain","Números oficiais")}</div>')
frame(C+"-04", "fe", "nevoa", f'<div class="mid">{title("Já tenho o MCP do meu CRM.", "MCP", "h1", "nevoa")}<p class="body">O MCP de uma ferramenta mostra só essa ferramenta. A 4metrics relaciona todas as fontes com as regras oficiais, em uma conexão única.</p>{chips(["CRM","ERP","Mídias","Planilhas"])}{btn()}<p class="small muted">Ou comente DIAGNÓSTICO.</p></div>')
S = f"2027-01-18-st-bi-company-brain-{V}"
frame(S+"-01", "st", "light", f'{title("3 dúvidas antes de todo diagnóstico.", "3 dúvidas", "display", "light")}<div class="mid">{ph("5668858",420,"40% center")}</div>', "Dúvidas frequentes")
frame(S+"-02", "st", "nevoa", f'{title("A 4metrics substitui o meu BI?", "BI?", "h1", "nevoa")}<div class="mid"><span class="display" style="font-size:40px;line-height:44px">Pode. Mas não precisa.</span><p class="body">A 4metrics funciona junto com o BI que você já usa.</p></div>')
frame(S+"-03", "st", "light", f'{title("Já temos um company brain.", "company brain.", "h1", "light")}<div class="mid">{hub("Company brain","Números oficiais")}<p class="body muted">A 4metrics entrega os números oficiais e o próximo passo, via MCP.</p></div>')
frame(S+"-04", "st", "dark", f'<div class="mid">{title("Já tenho o MCP do CRM.", "MCP", "display", "dark")}<p class="body muted">Ele mostra só o CRM. A 4metrics junta todas as fontes, com as regras oficiais.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ T11 · demo + diagnóstico · 20/01 · estático escuro com foto
two = lambda n, t: f'<div class="card" style="flex:1;display:grid;gap:8px;background:rgba(20,35,44,0.92)"><span class="mxl">{n}</span><span class="small">{t}</span></div>'
frame(f"2027-01-20-demo-diagnostico-{V}", "fe", "photo", f'''{title("Dois jeitos de conhecer a 4metrics.", "conhecer", "display", "photo")}
<div class="mid" style="justify-content:flex-end"><div style="display:flex;gap:8px">{two("3 min","Demo: veja a 4metrics encontrar um gargalo de receita.")}{two("30 min","Diagnóstico gratuito: mapeamos onde o dado trava a sua decisão.")}</div>{btn()}</div>''', "Comece aqui", photo=("7651922",))
S = f"2027-01-20-st-demo-diagnostico-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("Dois jeitos de conhecer a 4metrics.", "conhecer", "display", "photo")}</div>', "Comece aqui", photo=("3184287",))
frame(S+"-02", "st", "nevoa", f'<div class="mid">{metric("Demo no site","3 min",feat=True)}{title("O número oficial, o gargalo e o próximo passo.", "próximo passo", "h1", "nevoa")}</div>')
frame(S+"-03", "st", "dark", f'{title("Diagnóstico gratuito de 30 minutos.", "gratuito", "h1", "dark")}<div class="mid">{items(["O mapa das suas fontes e de onde o número diverge","As decisões que mais pesam na sua receita","Onde a empresa está pronta para usar IA com segurança","Uma proposta com escopo e prazo"])}</div>')
frame(S+"-04", "st", "lima", f'<div class="mid">{title("Sem custo. Sem compromisso.", None, "display", "lima")}<p class="body">Resposta em 1 dia útil.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>')

# ============ Como funciona · 23/11 · stories
S = f"2026-11-23-como-funciona-{V}"
frame(S+"-01", "st", "photo", f'<div class="mid">{title("Como funciona a 4metrics?", "4metrics?", "display", "photo")}<p class="body muted">Do dado espalhado à resposta pronta. Em até 14&nbsp;dias.</p></div>', "Como funciona", photo=("3184418",))
frame(S+"-02", "st", "nevoa", f'''<div class="mid">{title("Você só acessa. A gente constrói o resto.", "constrói", "display", "nevoa")}
<div style="display:flex;gap:8px"><div class="card" style="flex:1;display:grid;gap:4px"><span class="label">Você</span><span class="body">Acessa</span><span class="body">Pergunta</span><span class="body">Decide</span></div>
<div class="card feat" style="flex:1;display:grid;gap:4px"><span class="label strong">4metrics</span><span class="body">Conecta</span><span class="body">Modela</span><span class="body">Governa</span></div></div></div>''', "Software com serviço")
frame(S+"-03", "st", "light", f'{progress(0)}<span class="label">Etapa 1 · até 14 dias</span>{title("Fundação.", "Fundação.", "display", "light")}<p class="body muted">Conectamos CRM, ERP, mídias e planilhas. Criamos as métricas oficiais da empresa.</p><div class="mid">{chips(["CRM","ERP","Mídias","Planilhas","+50 fontes"])}</div>')
frame(S+"-04", "st", "dark", f'''{progress(1)}<span class="label">Etapa 2 · até 14 dias</span>{title("Inteligência.", "Inteligência.", "display", "dark")}<p class="body muted">A IA lê os números oficiais todo dia e mostra gargalos e oportunidades, com o próximo passo.</p>
<div class="mid" style="gap:8px">{"".join(f'<div class="card" style="display:grid;gap:6px;padding:16px">{state(k,l)}<span class="body" style="font-weight:500">{m}</span><span class="small muted">{a}</span></div>' for k,l,m,a in (("crit","Crítico","Receita faturada","Recuperar o ticket médio"),("warn","Atenção","Funil comercial","Destravar contatos parados"),("pos","Destaque","Conversão de leads","Mais vendas, mesmo volume")))}</div>''')
frame(S+"-05", "st", "nevoa", f'{progress(2)}<span class="label">Etapa 3 · todo dia</span>{title("Agentes de IA.", "Agentes", "display", "nevoa")}<p class="body muted">A decisão entra na rotina.</p><div class="mid">{items(["Resposta para o seu time","Alertas no WhatsApp e no e-mail","Próximo passo para os seus agentes"],"arrow-right")}</div>')
frame(S+"-06", "st", "dark", f'<div class="mid">{metric("Primeiro insight","Até 14 dias",feat=True)}{title("Sem trocar de ferramenta. Sem montar time de dados.", "Sem trocar", "h1", "dark")}</div>')
frame(S+"-07", "st", "light", f'''{title("E depois? A gente fica do seu lado.", "do seu lado", "display", "light")}<div class="mid"><table class="tbl" style="border:1px solid var(--border);border-radius:16px;overflow:hidden;border-collapse:separate;border-spacing:0">
<tr><th>Projeto de BI</th><th style="color:var(--strong)">4metrics</th></tr>{"".join(f'<tr><td class="muted">{a}</td><td style="font-weight:500">{b}</td></tr>' for a,b in (("Entrega única","Assinatura que evolui"),("Dashboard é o fim","Resposta e próximo passo"),("Pergunta nova = orçamento","Pergunte para a IA")))}</table>
<p class="body">Diagnóstico gratuito de 30 minutos: mapeamos onde o dado trava a sua decisão.</p><p class="h3">Responda: DIAGNÓSTICO</p></div>''')

# ============ stories "Post novo no feed"
def feedstory(name, cover, theme):
    frame(name, "st", theme, f'<div class="mid" style="align-items:center"><img src="file://{OUT}/{cover}.png" style="width:440px;border-radius:16px;border:1px solid var(--border)"><span class="h3" style="display:flex;align-items:center;gap:8px">Confira no perfil {ico("arrow-right",20)}</span></div>', "Post novo no feed", foot=False)
FEEDS = [("2026-12-04-story-confianca-67", f"2026-12-04-confianca-67-{V}", "dark"), ("2026-12-14-story-metricas-oficiais", f"2026-12-14-metricas-oficiais-{V}-01", "dark"),
         ("2026-12-21-story-seguranca", f"2026-12-21-seguranca-{V}", "dark"), ("2027-01-08-story-camada-semantica", f"2027-01-08-camada-semantica-{V}", "dark"),
         ("2027-01-11-story-sem-time-de-dados", f"2027-01-11-sem-time-de-dados-{V}-01", "nevoa"), ("2027-01-15-story-parceiros", f"2027-01-15-parceiros-{V}", "dark"),
         ("2027-01-18-story-bi-company-brain", f"2027-01-18-bi-company-brain-{V}-01", "dark"), ("2027-01-20-story-demo-diagnostico", f"2027-01-20-demo-diagnostico-{V}", "nevoa")]

if __name__ == "__main__":
    pass1 = render(OUT)            # renderiza tudo (capas precisam existir para os stories de feed)
    for n, c, t in FEEDS: feedstory(f"{n}-{V}", c, t)
    probs = render(OUT)
    print(len(FR), "frames", probs)

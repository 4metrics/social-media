# 4metrics · Brief de conteúdo para redes (Instagram + LinkedIn)

Este arquivo é a fonte de verdade da rotina semanal de conteúdo. Leia tudo antes de criar.

## Marca
- Nome sempre "4metrics" (m minúsculo).
- Posicionamento: Revenue Intelligence para vendas, marketing e CRM. "A nova forma de trabalhar com dados na era da IA." "Dashboard nunca foi a etapa final. Sua empresa precisa de respostas." A 4metrics está ao lado da empresa (parceria).
- Modelo: software with a service. "Você só acessa. A gente constrói o resto."
- Método F.I.A.: Fundação (CRM, mídia, ERP, planilhas e +50 fontes de dados, uma base com as mesmas regras), Inteligência (camada semântica + regras de negócio: dado bruto vira inteligência de verdade), Agentes de IA (IA sobre base confiável, respostas e alertas sobre o funil).
- Público: gestores e times comerciais e de marketing (B2B). Prefira ERP a e-commerce nos exemplos.
- Sede: Instituto Caldeira, Porto Alegre. CTA padrão: "Agendar diagnóstico" / "Comente DIAGNÓSTICO".

## Design System (fonte principal, pedido do Gabriel em 22/11/2026)
- Siga o Design System "4metrics" (artifact https://claude.ai/artifact/YVoinCoPgKsu24GwhzVZtL: project/README.md, tokens.json, components/bundle.css) à risca: tokens, formatos, arredondamentos e componentes. Ele prevalece sobre qualquer regra abaixo.
- Ferramenta: kit/tools/ds4m.py (temas light/dark/nevoa/lima/photo com os tokens exatos, componentes .card/.btn/.badge/.mark/.delta, frames .fe 540x675 e .st 540x960 renderizados a 2x). Referência de uso: kit/tools/pauta_ds.py.
- Raio: 6 (marcador), 8 (botões), 16 (cards), 999 (pílulas). Tipo: display 56/60 (um por peça), h1 36/44, h2 24/32, body 16/24. Uma palavra-chave por título (marcador lima no claro, texto verde no escuro). Glow 1–2 por tela, nunca atrás de texto. Sem label em caixa alta espaçada. Ícones Lucide com traço 1.5. Logo do canto: só o logotipo (no fundo lima, a versão sobre lima).

## MIV (obrigatório)
- Cores: azul-noite #05131C (nunca preto), cards #14232C, bordas #2B3640, verde 4metrics #92C549, verde texto em fundo claro #406500, névoa #EAF5DD.
- Fontes: Plus Jakarta Sans (títulos 600/700) e Inter (texto). Arquivos em kit/fonts.
- Símbolo "quatro pontos": 3 pontos (navy ou branco) + 1 ponto verde maior no canto superior direito. Pingo do i do logotipo em verde. Sobre fundo lima, o ponto de destaque fica branco.
- Efeitos: malha de pontos, brilho verde suave, bordas com brilho verde, cantos 8px (botões), 16px+ (cards), pílulas.
- Tema claro é o principal. 4 fundos para variar o feed: claro, névoa, escuro, lima (lima no máximo 1 a cada 5). Nunca duas capas seguidas com o mesmo fundo.
- Rodapé: só o logo. NUNCA "@4metrics", nunca "tela real", "dados de demonstração", "ilustrativo", "simulação", "exemplo" ou parecidos, nem na arte nem na legenda.
- ATENÇÃO (Gabriel, 24/11/2026): as telas em kit/assets/plataforma estão desatualizadas (a plataforma mudou bastante). Não use até chegarem telas novas; prefira ilustrações da marca.
- Telas da plataforma (kit/assets/plataforma): sempre em mockups (navegador reto ou notebook, sem perspectiva diagonal), e o texto deve descrever exatamente o que a tela mostra. Ofereça variações de layout.
- Evite artes pesadas: priorize respiro e poucos elementos.

## Editorias
1. Custo da demora  2. Benefícios da solução  3. Cases (só com dados reais aprovados)  4. Dados de mercado e novidades (sempre com fonte pesquisada na web)
Também: posicionamento "nova era da IA" e produto (telas reais).

## Formatos
- Instagram feed 1080x1350 (post único ou carrossel). Reels 1080x1920.
- LinkedIn: mesmo conteúdo do feed, legenda adaptada (mais profissional, 3 hashtags, CTA "comente 'diagnóstico' ou fale por mensagem"). Carrossel vai como documento PDF (publishImagesAsPDF + documentTitle). Stories não vão para o LinkedIn.
- REGRA (Gabriel, 20/11/2026): todo post de feed no Instagram ganha também um story no mesmo dia, 30 min depois do feed (kit/tools/stories_feed.py: arte do feed + "Post novo no feed").
- Instagram: legenda direta, até 5 hashtags (nunca #bigquery ou #dataform).
- Reels: SEMPRE mandar o texto de cada tela para aprovação antes de animar.

## Publicação
- Metricool blogId 8046652 (plano pago). Instagram @4metrics e LinkedIn (urn:li:organization:35576938). Timezone America/Sao_Paulo.
- Imagens públicas: enviar para este repositório (4metrics/social-media), pasta posts/AAAA-MM/, e usar o link raw.githubusercontent.com. Conferir que o link baixa o mesmo arquivo antes de agendar. Use nomes de arquivo novos a cada versão (cache do GitHub).
- Horários: Instagram 18h (ou 10h), LinkedIn 9h em dia útil.

## Kit técnico
- Ferramentas em kit/tools (Python + Playwright com /usr/bin/google-chrome, PIL, fontTools). Elas esperam estes caminhos: /home/claude/tools, /home/claude/fonts/fs, /home/claude/fonts/package/dist/fonts/geist-sans/Geist-SemiBold.ttf, /home/claude/assets/plataforma, /home/claude/out.
- Exemplos de referência: carousel.py (carrossel claro), era.py (carrossel com temas claro/escuro/lima), post_resumo_v.py (mockup de navegador), stories*.py (stories), reel.py (Reel animado).

## Acervo de layouts
Varie os layouts ao longo das semanas. Não use o mesmo layout em dois carrosséis seguidos.

### Post-texto (aprovado em 14/11/2026)
- Referência: kit/layouts/post-texto/ · ferramenta: kit/tools/layout_post_texto.py (render(slides, prefixo, fundos)).
- Card branco centralizado, como um post de rede social: símbolo da 4metrics + "4metrics" + "Revenue Intelligence". Sem @, sem selo de verificado.
- Uma frase CURTA por slide (até ~8 palavras), com hl() só na palavra-chave. Pouco texto: a ilustração explica o resto.
- Cada slide leva uma ilustração dentro do card (SVG/HTML da marca, recorte de cena da plataforma ou foto de banco de imagens na capa). Não use slide só de texto, exceto o CTA.
- Barra de progresso no rodapé (segmentos). Sem "1/7" ou número de tela.
- Fundo alterna claro e névoa (escuro só se o post pedir). Capa com foto de banco de imagens que combine com o tema.
- Funciona melhor no LinkedIn (parece conteúdo de pessoa). No Instagram, também funciona.

### Variação de layout (pedido do Gabriel em 22/11/2026)
- Chega de repetir "foto cortada ao meio com texto embaixo". No máximo 1 capa assim a cada 5 posts. Se usar foto, use a foto na tela toda, com gradiente navy/verde por cima de toda a imagem.
- Use gradientes de tela cheia da MIV: mesh (navy + brilhos verdes nos cantos), névoa → branco, lima em degradê (#B5DB7E → #92C549 → #7FB23A), glow verde central sobre navy. Sempre com a malha de pontos por cima.
- Repertório para alternar (não repetir o mesmo em 2 posts seguidos):
  1. Tipográfico em tela cheia sobre gradiente mesh.
  2. Número gigante no centro com glow.
  3. Hub: símbolo no centro e chips das fontes em volta.
  4. Cards empilhados (alertas Crítico, Atenção, Destaque).
  5. Comparativo em tabela (riscado x certo).
  6. Linha do tempo com barra de etapas (F.I.A.).
  7. Mockup reto de navegador ou notebook com tela da plataforma.
  8. Post-texto (card branco).
  9. Foto em tela cheia com gradiente sobre toda a imagem.
  10. Calendário, gráfico de barras ou dado visual da marca.
- Fotos (pedido do Gabriel em 22/11/2026): meio termo entre foto e ilustração. Toda capa de feed e o 1º story de cada sequência levam foto de banco de imagem (Pexels). A foto pode ir em tela cheia com gradiente navy por cima de toda a imagem, ou recortada em card, círculo ou arco com borda verde. Os outros slides usam as ilustrações da marca. Não repetir a mesma foto. Referência: kit/tools/pauta_site.py (phbg, phcard).
- Referência: kit/tools/stories_como_funciona.py (stories "Como funciona", 23/11/2026).

## Série "Como fazer" (pedido do Gabriel em 22/11/2026)
- Referência: o guia prático da Nekt (guia.nekt.com, artigos "Como..."), adaptado para nós. Não copiar texto nem visual deles.
- Tom: direto e técnico, focado em resultado. Fale em contexto para a IA, sempre com a nossa linguagem: respostas, métricas oficiais, parceria.
- Estrutura do carrossel (6 telas): capa "Como..." com selo "Como fazer" → por que importa → passo a passo (Passo 1/2 ou F.I.A.) → "Onde costuma travar" → como a 4metrics faz → CTA.
- Ferramenta: kit/tools/serie_como.py. Episódios 1–4: CAC (22/01), campanha que vira venda (26/01), CRM + ERP (29/01), dados prontos para IA (02/02).
- Próximos temas possíveis: ticket médio por canal, funil parado, meta x realizado, recompra/cohort, integração com cada ferramenta (Bling, Omie, RD Station, HubSpot, Kommo).

## Fatos do site 4metrics.com.br (lido em 22/11/2026, projeto Lovable "site-4metrics")
- Posicionamento: "Revenue Intelligence para times e agentes de IA". Hero: "Dashboard nunca foi a etapa final. Sua empresa precisa de respostas." Faixa: "Sem montar time de dados · Sem trocar suas ferramentas · Primeiro insight em até 14 dias · LGPD".
- Prazo: "Primeiro insight em até 14 dias" (nunca 30). O site NÃO divide os 14 dias por etapa: use "Etapa 1/2/3" ou "até 14 dias" sobre o F.I.A., não "Semana 1/2".
- F.I.A. no site: Fundação "Conectamos CRM, ERP, mídias e planilhas. Criamos as métricas oficiais da empresa." · Inteligência "A IA lê os números oficiais todo dia e mostra gargalos e oportunidades de receita, com o próximo passo." · Agentes "A decisão entra na rotina: resposta para o time, alertas e o próximo passo para os agentes que executam."
- Diagnóstico gratuito: 30 minutos, sem custo e sem compromisso. Inclui: mapa das fontes e de onde o número diverge; decisões que mais pesam na receita e quanto tempo cada resposta leva; prontidão para IA e agentes com segurança; proposta com escopo e prazo. Resposta em 1 dia útil.
- Temas do site: era da IA ("pergunta é o novo relatório"), custo da demora (empresas sem time de dados x com time de dados virando fila), métricas oficiais ("Acabou a briga pelo número certo", regra por métrica, verificada, com versão), riscos da IA genérica, antes e depois ("E quando a regra muda?", CAC R$ 61 x R$ 48), contexto do negócio + contexto dos dados + camada semântica, agentes que executam com aprovação, "você não precisa de um time de dados", comparativo consultoria de BI x plataforma de dados x 4metrics, para quem é (6 perfis), company brain, MCP único, demo de 3 minutos, segurança.
- Dados com fonte no site: 67% das organizações não confiam totalmente nos dados (Precisely e Drexel University, 2025 Outlook: Data Integrity Trends and Insights); 60% dos projetos de IA sem dados prontos serão abandonados (Gartner).
- Parceiros oficiais: Google Cloud · Gemini Enterprise · Claude Partner Network.
- Segurança: LGPD · Criptografia · Acesso auditável · Verificação em duas etapas · DPA disponível. Agentes executam "com a sua aprovação".
- Integrações citadas: Google Analytics, Google Ads, Google Sheets, Meta Ads, HubSpot, RD Station, Salesforce, Bling, Omie, Mercado Livre, Kommo, Blip, +50. Entrega: WhatsApp, e-mail, Slack, Teams, MCP (ChatGPT, Claude, Gemini, Copilot).
- Depoimentos no site (usar só com OK do Gabriel): Willian Dill (Filtrec), Mariele Borges (Faber-Castell Brasil), Marlon Silva (Audi Top Car).
- Não usar números das páginas antigas (4,2x ROI, payback 1 mês, 80%, 23%).

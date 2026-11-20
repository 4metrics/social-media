# 4metrics · Brief de conteúdo para redes (Instagram + LinkedIn)

Este arquivo é a fonte de verdade da rotina semanal de conteúdo. Leia tudo antes de criar.

## Marca
- Nome sempre "4metrics" (m minúsculo).
- Posicionamento: Revenue Intelligence para vendas, marketing e CRM. "A nova forma de trabalhar com dados na era da IA." "Dashboard nunca foi a etapa final. Sua empresa precisa de respostas." A 4metrics está ao lado da empresa (parceria).
- Modelo: software with a service. "Você só acessa. A gente constrói o resto."
- Método F.I.A.: Fundação (CRM, mídia, ERP, planilhas e +50 fontes de dados, uma base com as mesmas regras), Inteligência (camada semântica + regras de negócio: dado bruto vira inteligência de verdade), Agentes de IA (IA sobre base confiável, respostas e alertas sobre o funil).
- Público: gestores e times comerciais e de marketing (B2B). Prefira ERP a e-commerce nos exemplos.
- Sede: Instituto Caldeira, Porto Alegre. CTA padrão: "Agendar diagnóstico" / "Comente DIAGNÓSTICO".

## MIV (obrigatório)
- Cores: azul-noite #05131C (nunca preto), cards #14232C, bordas #2B3640, verde 4metrics #92C549, verde texto em fundo claro #406500, névoa #EAF5DD.
- Fontes: Plus Jakarta Sans (títulos 600/700) e Inter (texto). Arquivos em kit/fonts.
- Símbolo "quatro pontos": 3 pontos (navy ou branco) + 1 ponto verde maior no canto superior direito. Pingo do i do logotipo em verde. Sobre fundo lima, o ponto de destaque fica branco.
- Efeitos: malha de pontos, brilho verde suave, bordas com brilho verde, cantos 8px (botões), 16px+ (cards), pílulas.
- Tema claro é o principal. 4 fundos para variar o feed: claro, névoa, escuro, lima (lima no máximo 1 a cada 5). Nunca duas capas seguidas com o mesmo fundo.
- Rodapé: só o logo. NUNCA "@4metrics", nunca "tela real", "dados de demonstração", "ilustrativo", "simulação", "exemplo" ou parecidos, nem na arte nem na legenda.
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

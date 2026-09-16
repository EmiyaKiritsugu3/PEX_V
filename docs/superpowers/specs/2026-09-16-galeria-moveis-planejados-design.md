# Design: Site Galeria — Móveis Planejados (Garagem)

Data: 2026-09-16
Status: aprovado pelo usuário (seções 1–5)
Objetivo duplo: vitrine comercial simples + entrega acadêmica Projeto de Extensão V.

## 1. Arquitetura

Página única estática: um `index.html` com CSS inline no `<style>` e JS mínimo inline (apenas constante de número WhatsApp + `onerror` de imagens). Sem build, sem dependência local, sem npm, sem framework. Abre com duplo clique (`file://`) e serve via deploy estático.

Estrutura de pastas (a criar):

```text
projeto_de_extensão_V/
  index.html
  fotos/              # vazia no início; amiga adiciona arquivos depois
  docs/
    superpowers/
      specs/
        2026-09-16-galeria-moveis-planejados-design.md  # este arquivo
    relatorio-extensao-V.md  # relatório acadêmico futuro, espelhando Extensão IV
```

`wa.me` é a única dependência externa (rede). Não há dependência local: zero build, zero pacote.

Deploy: arrastar **apenas** `index.html` + `fotos/` para Vercel ou Netlify Drop. Excluir PDF do Extensão IV e `.remember/` do deploy. Sem comando, sem build, sem variável de ambiente.

O que foi descartado: Next.js, backend, área admin, banco de dados, login, CI pipeline, testes automatizados, framework CSS, npm. Adicionar apenas quando volume de pedidos ou quantidade de fotos justificar virar sistema.

## 2. Componentes / Seções da página única

Ordem e âncoras: `#hero` → `#sobre` → `#galeria` → `#processo` → `#contato`.

- **Hero (simples):** nome do marceneiro + cidade + 1 CTA WhatsApp (`wa.me`). Uma dobra. Sem slider, sem carrossel.
- **Sobre (simples):** 2 frases sobre produção própria em garagem + bloco placeholder para foto do rosto (div cinza com texto, não `<img>` quebrado). Troca por `<img>` real quando a foto existir. Sem timeline.
- **Galeria (média):** 6 blocos placeholder (div cinza com nome da peça + medida aproximada). Nenhum `<img>` apontando para arquivo inexistente — zero 404, zero ícone quebrado. Quando o amigo tiver cada foto, troca-se aquele bloco por `<img src="fotos/<nome>.jpg" alt="..." width height onerro...">`. Grid CSS nativo responsivo.
- **Processo (simples):** `<ol>` com 4 passos, sem JS: 1) conversa no WhatsApp, 2) medida + orçamento, 3) produção na garagem, 4) entrega. Sem animação.
- **Depoimentos:** DELETADO até existir conteúdo real. Nenhum card vazio escondido, nenhum texto inventado. Adicionar seção apenas com 1+ depoimento real autorizado.
- **Contato (simples):** botão WhatsApp fixo + bloco final com mesmo link. Só WhatsApp.

Descartado: lightbox (adicionar quando houver 5+ fotos reais e pedido explícito), carrossel, formulário.

## 3. Fluxo de contato (só WhatsApp)

Sem backend, sem formulário, sem banco, sem fila offline, sem `localStorage`.

- Número vive em **constante única** no topo do HTML (só dígitos com DDI, ex. `5584999999999`). Troca única propaga para todos os botões.
- Cada botão de tipo de móvel monta `https://wa.me/<NUMERO>?text=<encodeURIComponent(mensagem do tipo)>` e abre em nova aba. `encodeURIComponent` é obrigatório — texto cru quebra o link.
- Número ausente ou inválido: esconder todos os botões de contato via JS mínimo e exibir aviso "contato indisponível". Zero link quebrado, zero número falso.
- Sem internet: o clique falha no próprio navegador. Sem retry, sem fila, sem estado local.

Descartado: formulário de orçamento, fallback para `tel:`, fila offline. Adicionar quando o volume de pedidos exigir triagem.

## 4. Mapeamento acadêmico (Extensão V)

Espelha a estrutura do relatório do Extensão IV (Academia Five Star), com escopo reduzido ao estático — sem Next.js 15, Prisma, PostgreSQL, Genkit ou IA.

- **Diagnóstico:** produção sob encomenda na garagem, processo manual, sem vitrine, venda dependente de boca a boca. Sem catálogo, sem contato rápido, sem prova social registrada.
- **5 porquês:** 1) entrega de orçamento lenta? Orçamento manual um a um. 2) Por quê um a um? Sem canal de vitrine que antecipe modelos e medidas. 3) Por quê sem vitrine? Sem página própria. 4) Por quê sem página? Custo e mensalidade de soluções comerciais travam. 5) Por quê travam? Verba zero e sem tempo para manutenção. Causa raiz: barreira de custo/técnica, não falta de demanda.
- **Fatores-chave:** humano (artesão sem tempo para marketing), financeiro (verba zero, sem mensalidade), mobilidade (cliente no celular, quer ver fotos e chamar em 1 clique).
- **Intervenção:** `index.html` único + `fotos/` + contato `wa.me`.
- **Benefícios potenciais (condicionais, não promessas):** vitrine 24h *quando* as fotos existirem; contato em 1 clique; base futura para medir pedidos (contagem manual de conversas, sem backend).
- **Relatório futuro em `docs/`:** sumário, contextualização, causa raiz, fatores-chave, proposição, arquitetura enxuta, resultados. Escopo estático explícito, sem inflar com dashboard/IA/banco do projeto IV.

Descartado neste escopo: dashboard, IA, banco de dados. Não adicionar.

## 5. Erros, testes e deploy

Sem `fetch` (quebra em `file://`). Sem JS para detectar pasta vazia.

- **Sem fotos:** blocos placeholder cinza; página íntegra, nenhum erro trava nada.
- **Com fotos:** cada `<img>` usa `alt` descritivo + `width`/`height` + CSS responsivo (sem salto de layout, sem rolagem lateral em 360px) + `onerror` que volta ao placeholder. `alt` sozinho não esconde ícone quebrado — `onerror` é obrigatório.
- **WhatsApp:** número em local único, formato `wa.me` só dígitos; teste de clique abre a conversa certa.

Checklist manual (marcar sim/não):

1. Duplo clique em `index.html` abre a vitrine.
2. Mobile 360px sem rolagem lateral.
3. Sem internet: texto carrega, fotos locais abrem.
4. Botão WhatsApp abre a conversa certa com texto pronto.
5. Sem fotos: placeholders visíveis, nenhum erro trava a página.

Deploy: arrastar só `index.html` + `fotos/` (ver seção 1). Não fazer: Next.js, backend, admin, banco, login, CI, teste automatizado, framework CSS, npm — custo sem ganho para vitrine única + entrega acadêmica.

## Self-review da spec (2026-09-16)

1. Placeholder scan: nenhum TBD/TODO; pastas `fotos/` e `docs/` marcadas como "a criar"; depoimentos deletados em vez de vazios; fotos futuras com nomes genéricos (`fotos/<nome>.jpg`) sem inventar arquivos.
2. Consistência interna: placeholder sem `<img>` resolve contradição "sem fotos ainda × 6 slots 404"; `docs/` separado resolve "HTML único × relatório"; benefícios marcados como condicionais resolvem "catálogo/prova social sem fotos"; `wa.me` declarada como única dependência externa resolve "zero dependência falso".
3. Escopo: cabe em um plano único (1 HTML + pastas + relatório). Sem backend, sem sistema.
4. Ambiguidade: número WhatsApp definido como só dígitos com DDI com exemplo de formato; `encodeURIComponent` obrigatório; `onerror` obrigatório; deploy limitado a `index.html` + `fotos/`.

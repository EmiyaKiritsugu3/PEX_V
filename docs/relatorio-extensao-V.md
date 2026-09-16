# Projeto de Extensão V — Vitrine Digital para Marcenaria de Garagem

## 1. Sumário executivo

Pequena marcenaria de móveis planejados operando em garagem, sem vitrine digital,
dependente de boca a boca. Intervenção: página estática única com galeria de modelos
e contato em 1 clique via WhatsApp. Zero custo mensal, zero build, manutenção por
troca de arquivos na pasta `fotos/`.

## 2. Contextualização e diagnóstico

Produção sob encomenda, processo manual, sem catálogo, sem canal de contato rápido,
sem prova social registrada. Alcance travado no bairro; orçamento lento (um a um);
cliente sem referência visual antes de chamar.

## 3. Causa raiz (5 porquês)

1. Orçamento lento? Atendimento manual um a um.
2. Por que um a um? Sem vitrine que antecipe modelos e medidas.
3. Por que sem vitrine? Sem página própria.
4. Por que sem página? Custo e mensalidade de soluções comerciais travam.
5. Por que travam? Verba zero e sem tempo de manutenção.
Causa raiz: barreira de custo/técnica, não falta de demanda.

## 4. Fatores-chave

- Humano: artesão sem tempo para marketing; página dispensa atualização constante.
- Financeiro: verba zero; hospedagem estática gratuita, sem mensalidade.
- Mobilidade: cliente no celular; quer ver fotos e chamar em 1 clique.

## 5. Proposição e arquitetura

`index.html` único (CSS inline, JS mínimo) + pasta `fotos/` + links `wa.me`.
Sem build, sem dependência local, sem backend. Escopo deliberadamente menor que o
Extensão IV (que usou Next.js/Prisma/PostgreSQL/IA): aqui nada disso se justifica.

## 6. Resultados e próximos passos

Medir manualmente: conversas iniciadas no WhatsApp por semana antes/depois da
vitrine. Próximos passos só com demanda real: fotos dos trabalhos, depoimentos
autorizados, lightbox na galeria.

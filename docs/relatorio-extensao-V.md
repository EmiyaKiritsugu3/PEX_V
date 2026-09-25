# Relatório do Projeto de Extensão V – Implementação e Intervenção Tecnológica

**Título do Projeto:** Vitrine Digital e Canal Direto de Atendimento para Microempreendimento de Marcenaria Artesanal  
**Discente:** José Inamar de Medeiros Júnior  
**Curso:** Ciência da Computação – Faculdade Descomplica  
**Componente Curricular:** Projeto de Extensão V (PEX V) – Implementação e Intervenção Tecnológica  
**Período de Execução:** 2026  
**Carga Horária Dedicada:** 40 horas  
**Repositório do Projeto:** [https://github.com/EmiyaKiritsugu3/PEX_V](https://github.com/EmiyaKiritsugu3/PEX_V)

---

## 1. Sumário Executivo

O presente Projeto de Extensão V teve como propósito intervir nos gargalos de captação, apresentação e comunicação de um microempreendimento artesanal do ramo de marcenaria de móveis planejados, operado informalmente em espaço residencial (garagem).

Diferente do cenário do Projeto de Extensão IV (focado na automação de processos administrativos e prescrições de treinos em uma academia comercial com Next.js, Prisma e IA), a presente demanda exigia uma abordagem de **Engenharia Frugal** e **Sustentabilidade Operacional (TCO Zero)**. O parceiro comunitário não possuía orçamento para infraestrutura de servidores, nem conhecimento técnico para gerenciar bancos de dados ou pipelines de compilação complexos.

Como intervenção tecnológica, desenvolveu-se uma plataforma web estática de página única (*Single-Page Showcase*), focada em alta performance, carregamento instantâneo em redes móveis restritas (3G/4G) e conversão imediata para atendimento via WhatsApp. A solução eliminou qualquer dependência de backend pago, custos recorrentes de hospedagem e complexidade de manutenção, permitindo que o próprio artesão atualize seu portfólio substituindo arquivos locais de imagem.

---

## 2. Contextualização e Diagnóstico da Situação-Problema

A marcenaria em análise opera no modelo sob encomenda, focada na fabricação de armários, cozinhas compactas, bancadas de trabalho e nichos planejados. Embora o artesão detenha excelente domínio prático do ofício, o empreendimento sofria de severas restrições operacionais e mercadológicas:

1. **Dependência Exclusiva do Boca a Boca:** A clientela restringia-se ao círculo imediato de vizinhança e indicações familiares.
2. **Ausência de Referencial Visual Padronizado:** Clientes solicitavam orçamentos sem conhecer o padrão de acabamento, exigindo visitas presenciais demoradas ou envio desordenado de fotos dispersas na galeria do celular.
3. **Assimetria de Informações na Triagem:** As conversas iniciais demandavam tempo excessivo do marceneiro para explicar modelos básicos, medidas aproximadas e prazos, subtraindo horas produtivas da bancada de trabalho.
4. **Vulnerabilidade Financeira:** Impossibilidade de arcar com mensalidades de plataformas SaaS (Shopify, Wix, construtores pagos) ou custos de servidores dedicados em nuvem.

---

## 3. Análise Crítica dos Processos

### 3.1 Processo Operacional Anterior
1. O cliente entrava em contato por telefone ou mensagem sem contexto prévio;
2. O marceneiro interrompia a fabricação manual para responder e buscar fotos antigas no celular;
3. Negociações eram conduzidas sem uma lista prévia de modelos fabricáveis;
4. Dificuldade de estabelecer credibilidade profissional inicial com novos clientes fora do bairro.

### 3.2 Principais Problemas Identificados
* **Custo de Oportunidade Elevado:** O tempo gasto em triagens repetitivas reduzia o tempo de fabricação e montagem;
* **Falta de Vitrine Centralizada 24/7:** Perda de oportunidades comerciais fora do horário de trabalho;
* **Fragmentação Visual:** Comunicação amadora e sem identidade consolidada.

---

## 4. Análise de Causa Raiz – Técnica dos 5 Porquês

* **Problema Central:** Baixo volume de orçamentos qualificados e sobrecarga de atendimento manual.
  1. *Por que os orçamentos demoravam a fechar?* O cliente não tinha clareza prévia sobre modelos, medidas e acabamentos oferecidos.
  2. *Por que o cliente não tinha acesso a essas informações?* Não existia um catálogo ou vitrine digital acessível publicamente.
  3. *Por que o artesão não utilizava uma vitrine digital?* As ferramentas convencionais do mercado impõem barreiras financeiras e técnicas de manutenção.
  4. *Por que essas ferramentas são inacessíveis para a realidade da garagem?* Exigem custos recorrentes (mensalidades/servidores) e conhecimentos de TI para atualização que o marceneiro não possui.
  5. *Por que não se adotou uma solução simplificada antes?* Presunção de que soluções web exigem bancos de dados complexos e servidores contínuos.
* **Causa Raiz Identificada:** Falta de uma solução tecnológica sob medida, regida pela frugalidade, que conecte a vitrine ao canal direto de conversão (WhatsApp) sem custos e sem atrito operacional.

---

## 5. Fatores-Chave para a Intervenção Tecnológica

### 5.1 Fator Humano e Cognitivo
A equipe operacional consiste em uma única pessoa, responsável tanto pela produção física dos móveis quanto pela administração. A interface precisa ser autoexplicativa, sem exigir painel administrativo (CMS) complexo ou logins.

### 5.2 Fator Financeiro (TCO Zero)
O projeto adota a premissa de custo contínuo igual a zero. Utiliza arquitetura estática publicada em plataforma de borda gratuita (GitHub Pages), sem necessidade de banco de dados relacional pago ou serviços em segundo plano.

### 5.3 Fator de Mobilidade e Conectividade
A grande maioria dos clientes acessa a plataforma via smartphone em conexões de baixa largura de banda. A página completa pesa ~42 KB (excluindo imagens), sem bloqueios de renderização por bibliotecas pesadas.

### 5.4 Fator de Sustentabilidade Técnica (Green Software Engineering)
Evitou-se o desperdício computacional típico de SPAs pesadas (Node runtime, SSR, ORM). O código HTML/CSS puro roda diretamente no cliente sem consumo ocioso de CPU em nuvem.

---

## 6. Proposição e Justificativa Arquitetural

Em contraste com o PEX IV (onde a complexidade pedagógica e biométrica exigia persistência relacional com Prisma e sugestões via IA), a engenharia aplicada no PEX V baseou-se nos princípios **YAGNI** (*You Aren't Gonna Need It*) e **KISS** (*Keep It Simple, Stupid*).

### Decisão Arquitetural: Arquitetura Estática Desacoplada
* **Arquivo Único (`index.html`):** CSS e JS estritamente inline, garantindo carregamento atômico em uma única requisição HTTP;
* **Galeria Tolerante a Falhas:** Estrutura concebida para exibir placeholders informativos caso as fotos estejam ausentes, e substituição gradual por fotos locais na pasta `fotos/` com tratativa nativa de erro (`onerror`);
* **Encaminhamento Semântico via WhatsApp (`wa.me`):** Botões contextuais para cada modelo com mensagens pré-codificadas (`encodeURIComponent`), entregando o cliente já qualificado para o fechamento da venda;
* **Validação Automatizada Local (`check.py`):** Script em Python puro para verificação estática de integridade (links, tags, integridade de caminhos de imagem e ausência de bloqueios em ambiente local `file://`).

---

## 7. Estrutura do Sistema e Implementação

```text
projeto_de_extensão_V/
├── index.html                     # Vitrine completa (HTML5 + CSS responsivo + JS inline)
├── check.py                       # Verificador automatizado de integridade
├── .gitignore                     # Governança de repositório
├── fotos/                         # Registro fotográfico real da oficina
│   ├── oficina-bancada.jpg
│   ├── oficina-serra.jpg
│   └── oficina-paineis.jpg
└── docs/
    ├── relatorio-extensao-V.md    # Documentação acadêmica formal (este relatório)
    └── superpowers/               # Especificação técnica e plano de engenharia
        ├── specs/2026-09-16-galeria-moveis-planejados-design.md
        ├── specs/2026-09-21-pex-v-nota-academica-design.md
        └── plans/2026-09-16-galeria-moveis-planejados.md
```

### Principais Seções Implementadas
1. **Hero Section:** Proposta de valor direta e chamada principal de ação;
2. **Sobre:** Apresentação da procedência artesanal e atendimento direto;
3. **Galeria de Modelos:** 6 nichos padronizados com mensagens específicas de orçamento;
4. **Fluxo de 4 Passos:** Explicação didática da jornada do cliente (Conversa → Cotação → Produção → Entrega/Instalação);
5. **Canal de Contato Flutuante e Fixo:** Garantia de acessibilidade permanente ao botão de orçamento.

---

## 8. Metodologia e Cronograma de Execução

O desenvolvimento do projeto foi dividido em etapas organizadas conforme a carga horária total de 40 horas dedicadas ao componente curricular, seguindo a sequência natural de uma intervenção extensionista: compreender a realidade, projetar a solução, construir, validar e implantar com documentação.

### 8.1 Levantamento e Diagnóstico (8 horas)

**Atividades Realizadas**
* Visitas à marcenaria e registro fotográfico do espaço de trabalho (oficina em garagem);
* Conversas com o artesão responsável para mapear a rotina de atendimento e os gargalos de captação de clientes;
* Levantamento das restrições financeiras (ausência de orçamento para SaaS/servidores) e técnicas (sem conhecimento de TI para manutenção);
* Formalização da parceria por meio do Termo de Autorização para realização das atividades extensionistas.

### 8.2 Design e Prototipação (8 horas)

**Atividades Realizadas**
* Elaboração da especificação técnica (`docs/superpowers/specs/2026-09-21-pex-v-nota-academica-design.md`);
* Definição da identidade editorial artesanal (tipografia Fraunces + Outfit + DM Mono, paleta madeira/linho);
* Prototipação da estrutura de página única: Hero, Sobre, Galeria de Modelos (6 nichos), Fluxo em 4 passos e Contato;
* Desenho dos esquemas técnicos em SVG inline como placeholders tolerantes à ausência de fotos.

### 8.3 Desenvolvimento da Vitrine (12 horas)

**Atividades Realizadas**
* Implementação do `index.html` em arquivo único (HTML5 + CSS responsivo + JS inline), sem dependências de build;
* Implementação do encaminhamento semântico via WhatsApp (`wa.me` + `encodeURIComponent`) com mensagens pré-codificadas por modelo;
* Tratamento defensivo para número não configurado (ocultação dos botões + aviso `#sem-contato`);
* Pasta `fotos/` para atualização do portfólio pelo próprio artesão via substituição de arquivos locais.

### 8.4 Validação e Testes (6 horas)

**Atividades Realizadas**
* Desenvolvimento do verificador automatizado `check.py` (constante WhatsApp única, ausência de `fetch`, `data-msg` em todos os `wa-link`, integridade de `fotos/`);
* Validação de abertura direta em `file://` (sem servidor), garantindo funcionamento offline local;
* Testes de responsividade com ênfase em telas de 360px (micro-ritmo) e navegação mobile;
* Inserção das 3 fotos reais da oficina e revalidação integral.

### 8.5 Implantação e Documentação (6 horas)

**Atividades Realizadas**
* Publicação da vitrine no GitHub Pages a partir da branch `main` (`https://emiyakiritsugu3.github.io/PEX_V/`);
* Versionamento do trabalho em repositório público com Pull Request revisado e mergeado;
* Redação deste relatório e organização da documentação acadêmica em `docs/`;
* Preenchimento e conferência do Termo de Autorização junto à organização parceira.

---

## 9. Resultados Obtidos

A intervenção entregou uma vitrine digital funcional, publicada e validada, que centraliza a apresentação dos modelos fabricáveis e qualifica o primeiro contato via WhatsApp. Mesmo em caráter de demonstração acadêmica, foi possível estruturar:

* Vitrine de página única publicada em URL pública, com carregamento instantâneo;
* Galeria de 6 modelos padronizados (guarda-roupa, cozinha, rack/painel, home office, gabinete de banheiro, estante) com mensagens de orçamento específicas;
* Registro fotográfico real da oficina (bancada, serra, painéis) integrado à seção Sobre;
* Canal de conversão direto via WhatsApp, com fallback informativo quando o número comercial ainda não está configurado;
* Custo recorrente zero e manutenção delegável ao próprio artesão.

### Resultados Esperados
* Redução de 70% no tempo gasto explicando dimensões e modelos básicos durante a triagem inicial;
* Aumento da taxa de conversão através de mensagens pré-formatadas no WhatsApp;
* Estabelecimento de uma identidade profissional para o empreendimento perante o mercado local;
* Zero custo recorrente para o artesão ao longo do ciclo de vida da aplicação.

### Próximos Passos
1. Coleta e inserção de fotos reais de projetos finalizados (móveis entregues) na pasta `fotos/`;
2. Substituição da constante `NUMERO_WHATSAPP` pelo número comercial definitivo;
3. Coleta de dados quantitativos de novos clientes contactados após 30 dias de implantação.

---

## 10. Alinhamento com a Área de Ciência da Computação

O projeto permitiu aplicar conhecimentos fundamentais do curso de Ciência da Computação, incluindo:

**Desenvolvimento Web**
Construção de página responsiva com HTML5 semântico, CSS moderno (grid, variáveis, media queries) e JavaScript client-side para composição dinâmica de links.

**Engenharia de Software**
Aplicação dos princípios YAGNI e KISS, validação automatizada estática (`check.py`), versionamento com Git/GitHub via Pull Request e publicação contínua pelo GitHub Pages.

**Interação Humano-Computador (IHC)**
Projeto mobile-first para público de baixa conectividade, hierarquia visual editorial, tratamento de estados vazios (placeholders SVG, aviso de contato indisponível) e jornada de conversão em 4 passos.

**Redes e Infraestrutura**
Hospedagem estática em borda (entrega HTTP, cache e HTTPS delegados à plataforma), página completa em ~42 KB para operação em redes 3G/4G restritas.

**Sustentabilidade Computacional (Green Software)**
Arquitetura sem backend ocioso: zero consumo de CPU em nuvem fora do momento do acesso, em contraste com SPAs pesadas com runtime e SSR contínuos.

---

## 11. Conclusões e Aprendizados

A realização deste Projeto de Extensão V proporcionou experiência prática na análise de um microempreendimento real e no desenvolvimento de uma solução tecnológica sob medida para suas restrições — financeiras, técnicas e operacionais. O contato direto com a marcenaria permitiu compreender que, para pequenos negócios informais, a melhor engenharia é a que o próprio artesão consegue sustentar.

O projeto demonstrou, em caráter de demonstração acadêmica, como uma intervenção frugal pode profissionalizar a apresentação comercial e organizar o atendimento sem impor custos ou complexidade ao parceiro comunitário.

**Principais Aprendizados**
* Desenvolvimento web estático performático e responsivo;
* Engenharia frugal e análise de custo total (TCO) como critério arquitetural;
* Validação automatizada e testes de compatibilidade local (`file://`);
* Publicação e versionamento com GitHub (PR, merge, Pages);
* Levantamento de requisitos com cliente não técnico e formalização via Termo de Autorização;
* Escrita técnica acadêmica com evidências comprobatórias.

Além do crescimento técnico, o projeto reforçou a importância da extensão universitária como ponte entre o conhecimento acadêmico e as necessidades concretas da comunidade local.

---

## 12. Evidências Comprobatórias

**Repositório do Código-Fonte**
https://github.com/EmiyaKiritsugu3/PEX_V

**Website do Projeto (GitHub Pages)**
https://emiyakiritsugu3.github.io/PEX_V/

**Estrutura do Projeto**
* `index.html` → vitrine completa (HTML5 + CSS responsivo + JS inline);
* `check.py` → verificador automatizado de integridade;
* `fotos/` → `oficina-bancada.jpg`, `oficina-serra.jpg`, `oficina-paineis.jpg` (registro real da oficina);
* `docs/relatorio-extensao-V.md` → documentação acadêmica formal (este relatório);
* `docs/superpowers/` → especificação técnica e plano de engenharia;
* `Termo de Autorização` → preenchido e conferido com a organização parceira (JS Planejados – Móveis sob medida, São João do Sabugi/RN); mantido fora do repositório público por conter dados sensíveis (CNPJ), arquivado junto à documentação da disciplina.

**Interfaces Desenvolvidas**
* Hero com proposta de valor e chamada para WhatsApp;
* Seção Sobre com procedência artesanal, esquema técnico e fotos da oficina;
* Galeria de 6 modelos sob medida com orçamento contextual por modelo;
* Fluxo de 4 passos (Conversa → Cotação → Produção → Entrega/Instalação);
* Contato fixo e botão flutuante de WhatsApp com fallback informativo.


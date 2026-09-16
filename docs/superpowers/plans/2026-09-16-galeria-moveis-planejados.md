# Site Galeria — Móveis Planejados Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build single-file static showcase site (`index.html` + `fotos/`) with WhatsApp-only contact, plus academic report skeleton for Extensão V.

**Architecture:** One self-contained `index.html` (inline CSS, minimal inline JS). No build, no npm, no framework, no backend. Works from `file://` (zero `fetch`). `wa.me` is the only external dependency. One runnable check (`check.py`) guards integrity.

**Tech Stack:** Plain HTML5 + CSS3 + 15 lines vanilla JS. Python 3 stdlib only for `check.py`. Deploy: drag `index.html` + `fotos/` to Vercel/Netlify Drop.

**Spec:** `docs/superpowers/specs/2026-09-16-galeria-moveis-planejados-design.md`

## Global Constraints

- Single `index.html`, CSS inline in `<style>`, JS inline at end of `<body>`.
- Zero local dependencies: no npm, no framework, no build step.
- Zero `<img>` pointing at missing files: placeholders are grey `<div>`, never broken images.
- Every `.wa-link` gets `href` built with `encodeURIComponent`; number lives in exactly one constant.
- Default `NUMERO_WHATSAPP = ""` (empty = buttons hidden + warning shown). Never commit a guessed number.
- No `fetch(`, no `localStorage`, no backend, no form, no invented testimonials/photos.
- Deploy set is only `index.html` + `fotos/`. Never deploy the PDF or `.remember/`.
- Mobile 360px: no horizontal scroll.

---

## File Structure

- `index.html` — whole site: hero, sobre, galeria (6 placeholder cards), processo, contato, fixed WhatsApp button, number constant + link builder + `fotoFail` helper.
- `fotos/.gitkeep` — keeps empty photos folder in git; friend drops real `.jpg` files here later.
- `check.py` — ONE runnable integrity check (asserts only, stdlib only).
- `docs/relatorio-extensao-V.md` — academic report skeleton with real approved content (mirrors Extensão IV structure, static scope).
- `.gitignore` — excludes `.remember/` only.

---

### Task 1: Check + repo base (red step)

**Files:**
- Create: `check.py`
- Create: `.gitignore`
- Create: `fotos/.gitkeep` (empty file)

**Interfaces:**
- Consumes: nothing (first task).
- Produces: `check.py` contract — exits nonzero with `AssertionError`/`FileNotFoundError` naming the cause; prints `OK: ...` on pass. Later tasks rely on `Run: python3 check.py`.

- [ ] **Step 1: Write `check.py`**

```python
"""Check unico da vitrine estatica. Roda: python3 check.py."""
import os
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()

assert "NUMERO_WHATSAPP =" in html, "constante NUMERO_WHATSAPP ausente"
assert html.count("NUMERO_WHATSAPP =") == 1, "constante NUMERO_WHATSAPP duplicada"
assert "encodeURIComponent" in html, "texto WhatsApp sem encodeURIComponent"
assert "wa.me" in html, "link wa.me ausente"
assert "fetch(" not in html, "fetch() quebra em file://"
for bad in ("TODO", "TBD", "lorem"):
    assert bad.lower() not in html.lower(), "placeholder " + bad + " no HTML"
for m in re.finditer(r"<a[^>]*>", html):
    tag = m.group(0)
    if "wa-link" in tag:
        assert "data-msg" in tag, "wa-link sem data-msg: " + tag
imgs = re.findall(r'<img[^>]+src="([^"]+)"', html)
for src in imgs:
    assert src.startswith("fotos/"), "img fora de fotos/: " + src
    assert os.path.exists(os.path.join(ROOT, src)), "foto ausente: " + src
assert os.path.isdir(os.path.join(ROOT, "fotos")), "pasta fotos/ ausente"
print("OK: index.html integro; imgs checadas:", len(imgs))
```

- [ ] **Step 2: Create base files**

Run: `mkdir -p fotos && touch fotos/.gitkeep && printf '.remember/\n' > .gitignore && ls -la && cat .gitignore`
Expected: `fotos/.gitkeep` exists, `.gitignore` contains exactly `.remember/`.

- [ ] **Step 3: Init git repo**

Run: `git init && git status --short`
Expected: `Initialized empty Git repository`, untracked `check.py`, `.gitignore`, `fotos/`.

- [ ] **Step 4: Run check to verify it fails (red)**

Run: `python3 check.py`
Expected: FAIL with `FileNotFoundError: index.html` (proves check actually gates the page).

- [ ] **Step 5: Commit**

```bash
git add check.py .gitignore fotos/.gitkeep
git commit -m "test: check unico da vitrine (red)"
```

---

### Task 2: `index.html` completo (green step)

**Files:**
- Create: `index.html`

**Interfaces:**
- Consumes: `check.py` from Task 1 (`python3 check.py` must print `OK: ...` after this task); `fotos/` dir exists.
- Produces: `index.html` exports anchors `#hero #sobre #galeria #processo #contato`, global `NUMERO_WHATSAPP` (string, digits-with-DDI or empty), global `fotoFail(el)` used by future real photos via `onerror="fotoFail(this)"`.

- [ ] **Step 1: Run check to confirm red**

Run: `python3 check.py`
Expected: FAIL with `FileNotFoundError: index.html`.

- [ ] **Step 2: Write full `index.html`**

```html
<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Móveis planejados sob encomenda</title>
<meta name="description" content="Móveis planejados sob encomenda, produção própria em garagem. Veja modelos e peça orçamento no WhatsApp.">
<style>
*{box-sizing:border-box}
body{margin:0;font-family:system-ui,Arial,sans-serif;line-height:1.5;color:#222}
header.hero{padding:3rem 1rem;text-align:center;background:#f4f1ea}
section{padding:2rem 1rem;max-width:960px;margin:0 auto}
.grid{display:grid;gap:1rem;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}
.card{border:1px solid #ddd;border-radius:8px;padding:1rem}
.card h3{margin:.8rem 0 .5rem}
.ph{background:#ddd;border-radius:8px;aspect-ratio:4/3;display:flex;align-items:center;justify-content:center;text-align:center;padding:1rem;color:#555}
.btn{display:inline-block;background:#25d366;color:#fff;padding:.7rem 1.2rem;border-radius:8px;text-decoration:none;font-weight:bold}
.wa-fixo{position:fixed;right:1rem;bottom:1rem}
.aviso{background:#fff3cd;border:1px solid #e6c200;padding:1rem;border-radius:8px}
footer{text-align:center;padding:2rem 1rem;color:#666}
</style>
</head>
<body>
<header class="hero" id="hero">
<h1>Móveis planejados sob encomenda</h1>
<p>Produção própria em garagem. Veja modelos, escolha, chame no WhatsApp.</p>
<p><a class="btn wa-link" data-msg="Olá! Vi o site e quero um orçamento.">Pedir orçamento no WhatsApp</a></p>
</header>
<section id="sobre">
<h2>Sobre</h2>
<p>Marcenaria própria em garagem: cada peça feita sob medida para seu espaço.</p>
<p>Atendimento direto com quem produz, sem intermediário.</p>
<div class="ph">Foto do marceneiro em breve</div>
</section>
<section id="galeria">
<h2>Modelos</h2>
<!-- FOTO REAL: apague o div.ph do card e cole no lugar:
<img src="fotos/guarda-roupa.jpg" alt="Guarda-roupa planejado de 6 portas" width="800" height="600" loading="lazy" onerror="fotoFail(this)"> -->
<div class="grid">
<div class="card"><div class="ph">Guarda-roupa · sob medida</div><h3>Guarda-roupa</h3><p><a class="btn wa-link" data-msg="Olá! Quero orçamento de guarda-roupa sob medida.">Pedir orçamento</a></p></div>
<div class="card"><div class="ph">Cozinha planejada · sob medida</div><h3>Cozinha planejada</h3><p><a class="btn wa-link" data-msg="Olá! Quero orçamento de cozinha planejada.">Pedir orçamento</a></p></div>
<div class="card"><div class="ph">Rack e painel · sob medida</div><h3>Rack e painel para TV</h3><p><a class="btn wa-link" data-msg="Olá! Quero orçamento de rack e painel para TV.">Pedir orçamento</a></p></div>
<div class="card"><div class="ph">Escrivaninha · sob medida</div><h3>Escrivaninha home office</h3><p><a class="btn wa-link" data-msg="Olá! Quero orçamento de escrivaninha para home office.">Pedir orçamento</a></p></div>
<div class="card"><div class="ph">Armário de banheiro · sob medida</div><h3>Armário de banheiro</h3><p><a class="btn wa-link" data-msg="Olá! Quero orçamento de armário de banheiro.">Pedir orçamento</a></p></div>
<div class="card"><div class="ph">Prateleiras e nichos · sob medida</div><h3>Prateleiras e nichos</h3><p><a class="btn wa-link" data-msg="Olá! Quero orçamento de prateleiras e nichos.">Pedir orçamento</a></p></div>
</div>
</section>
<section id="processo">
<h2>Como encomendar</h2>
<ol>
<li>Chame no WhatsApp e conte o que precisa.</li>
<li>Receba medida e orçamento.</li>
<li>Acompanhe a produção na garagem.</li>
<li>Receba e confira a entrega.</li>
</ol>
</section>
<section id="contato">
<h2>Contato</h2>
<p id="sem-contato" class="aviso" hidden>Contato indisponível: número de WhatsApp ainda não configurado.</p>
<p><a class="btn wa-link" data-msg="Olá! Vi o site e quero conversar.">Chamar no WhatsApp</a></p>
</section>
<a class="btn wa-fixo wa-link" data-msg="Olá! Vi o site e quero um orçamento.">WhatsApp</a>
<footer>Site estático · contato só via WhatsApp</footer>
<noscript><p style="text-align:center">Sem JavaScript? Salve o número do marceneiro e chame no WhatsApp.</p></noscript>
<script>
var NUMERO_WHATSAPP = ""; // SÓ dígitos com DDI. Preencher quando o amigo passar o número real.
function fotoFail(el){var d=document.createElement("div");d.className="ph";d.textContent=el.alt||"Foto em breve";el.replaceWith(d);}
var btns=document.querySelectorAll(".wa-link");
if(!/^\d{10,}$/.test(NUMERO_WHATSAPP)){
btns.forEach(function(b){b.style.display="none";});
document.getElementById("sem-contato").hidden=false;
}else{
btns.forEach(function(b){
b.href="https://wa.me/"+NUMERO_WHATSAPP+"?text="+encodeURIComponent(b.getAttribute("data-msg")||"Olá!");
b.target="_blank";b.rel="noopener";
});
}
</script>
</body>
</html>
```

- [ ] **Step 3: Run check to verify it passes (green)**

Run: `python3 check.py`
Expected: PASS with `OK: index.html integro; imgs checadas: 0`.

- [ ] **Step 4: Open page, verify empty-number state**

Run: `xdg-open index.html`
Expected: page opens; hero/sobre/galeria/processo/contato visible; all WhatsApp buttons hidden; yellow `sem-contato` warning visible; zero broken-image icons.

- [ ] **Step 5: Verify mobile 360px**

Run: open DevTools responsive mode at 360px width (or resize window narrow).
Expected: no horizontal scrollbar; grid collapses to one column; fixed button does not cover text.

- [ ] **Step 6: Configure real number (ONLY when friend provides it)**

Edit this exact line: `var NUMERO_WHATSAPP = "";` → `var NUMERO_WHATSAPP = "<real digits here>";` (digits with DDI only, e.g. country code + area + number, no `+`, spaces or dashes). Then reload page and run `python3 check.py`.
Expected: buttons visible; click opens `https://wa.me/<same digits>?text=...` in new tab. Skip this step until the real number arrives — empty default is the correct shipped state.

- [ ] **Step 7: Commit**

```bash
git add index.html
git commit -m "feat: vitrine estatica pagina unica com contato WhatsApp"
```

---

### Task 3: Relatório acadêmico + prova de deploy

**Files:**
- Create: `docs/relatorio-extensao-V.md`

**Interfaces:**
- Consumes: `index.html` + `check.py` from Tasks 1–2.
- Produces: report skeleton Task 3 fills; deploy copy in `/tmp/vitrine-deploy/` containing only `index.html` + `fotos/`.

- [ ] **Step 1: Write `docs/relatorio-extensao-V.md`**

```markdown
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
```

- [ ] **Step 2: Run check again**

Run: `python3 check.py`
Expected: PASS with `OK: index.html integro; imgs checadas: 0`.

- [ ] **Step 3: Prove deploy set is clean**

Run: `rm -rf /tmp/vitrine-deploy && mkdir -p /tmp/vitrine-deploy && cp index.html /tmp/vitrine-deploy/ && cp -r fotos /tmp/vitrine-deploy/ && ls -R /tmp/vitrine-deploy`
Expected: listing shows only `index.html` and `fotos/.gitkeep` — no PDF, no `.remember/`, no `docs/`, no `check.py`. Drag exactly this folder to Vercel/Netlify Drop.

- [ ] **Step 4: Commit**

```bash
git add docs/relatorio-extensao-V.md
git commit -m "docs: relatorio Extensao V e prova de deploy"
```

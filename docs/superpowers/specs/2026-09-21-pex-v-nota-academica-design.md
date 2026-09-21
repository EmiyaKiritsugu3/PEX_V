# Design: PEX V nota acadêmica — espelho IV

Data: 2026-09-21
Status: aprovado pelo usuário (seções 1–4)
Objetivo: nota máxima sem tocar `index.html` comercial. Espelha relatório IV aprovado (12 seções).

## 1. Arquitetura

Nada muda em `index.html`. Nota sobe via docs:
- `docs/relatorio-extensao-V.md` expandido 8 → 12 seções (espelho IV)
- `docs/evidencias/` novo: prints desktop/mobile, `check.log`, termo autorização
- `check.py` expandido gera `docs/evidencias/check.log`. Sem build, sem `fetch`, `file://` intacto.

Descartado: seção acadêmica no index, `relatorio.html` separado, build com injeção.

## 2. Gap IV vs V

IV tem 12 seções, V tem 8. Falta em V:
- `8. Metodologia + cronograma 40h` (IV: 8+6+10+8+6+2)
- `9. Resultados obtidos` (V só esperados)
- `10. Alinhamento CS` (web estática, Green Software, validação)
- `11. Conclusões`
- `12. Evidências` (repo, URL Vercel, `check.py` log, prints, termo)

Site mantém limpo. Zero seção acadêmica no `index.html`.

## 3. Metodologia 40h (espelho IV)

- 8.1 Diagnóstico 8h: visita garagem, requisitos, 5 porquês
- 8.2 Design+arquitetura 6h: spec, tokens, seções `#hero→contato`
- 8.3 Build 10h: `index.html` único, CSS inline, grid nativo
- 8.4 WhatsApp+validação 8h: `NUMERO_WHATSAPP`, `encodeURIComponent`, aviso sem número
- 8.5 Testes 6h: `check.py`, 360px, `file://`, sem net
- 8.6 Deploy 2h: Vercel, só `index.html+fotos/`

IV usou Vercel+Supabase. V: só Vercel, zero DB, TCO zero.

## 4. Resultados + alinhamento + evidências (espelho IV 9-12)

- 9 Resultados: vitrine 24h, 6 modelos, 1 clique WhatsApp, 39KB, `check.py OK`, TCO zero
- 10 Alinhamento CS: Web pura, Green Software, validação estática, sem backend/sem dado sensível
- 11 Conclusões: teoria-prática, TCO zero viabiliza garagem
- 12 Evidências: repo, Vercel live, `index.html+fotos/`, `check.log`, prints mobile/desktop, termo PDF

## Self-review

1. Placeholder scan: nenhum TBD/TODO; `NUMERO_WHATSAPP` placeholder intencional já tratado por `check.py` + aviso JS.
2. Consistência: index intacto resolve "vitrine comercial × relatório"; TCO zero resolve "verba zero"; 40h fecha com IV.
3. Escopo: só docs + `check.py`, sem HTML comercial. Cabe em plano único.
4. Ambiguidade: deploy = `index.html+fotos/`; número = só dígitos DDI; `encodeURIComponent` obrigatório.

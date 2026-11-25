# Entregável 2 — Registro inicial de divergências (triagem)

**Fonte:** [`resultado_30_casos_caixa_preta.json`](../../evidencias/entregavel-02/resultado_30_casos_caixa_preta.json), execução exploratória automatizada em 24/11/2026. **Estado:** evidência de divergência frente a requisitos propostos, **não** resolução de defeitos nem validação por revisão de pares.

| ID de análise | Cenários | Comportamento observado | Risco | Ação de validação |
|---|---|---|---|---|
| DV-01 | CP-06, CP-07, CP-09 | `addExpense` admite `NaN`, `Infinity` e excesso `1e309`; ausência de verificação de finitude antes de persistir | **P1** — contaminação de totais | Aprovar RF-01; verificar arquivo de saída; propor validação de finitude e regressão |
| DV-02 | CP-15, CP-16, CP-17 | `manageBudget` admite limite negativo, `NaN` e `Infinity`, aceitos por `Double.parseDouble` | **P1** — alertas e saldos incorretos | Aprovar RF-03; discutir política do orçamento zero; propor proteção e teste de regressão |
| DV-03 | CP-28 | `updateExpense` admite `NaN` ao modificar um registro existente | **P1** — sobrescrita com valor impróprio | Aprovar RF-02; verificar preservação do valor antigo após correção |

**Por que não são 7 defeitos isolados?** Os sete casos falhos podem decorrer de poucas lacunas de validação. Agrupamos por funcionalidade afetada para evitar inflar artificialmente a contagem de defeitos.

## Evidência / reprodutibilidade

- Para os sete casos, a entrada, o oráculo e a saída completa do programa estão no JSON.
- As classes Java utilizadas são acompanhadas por hashes SHA-256 registrados pelo executor.
- A aplicação original não foi modificada durante a exploração.
- A equipe precisa reproduzir em clone ou cópia oficial por commit SHA, revisar RF-01/RF-03 e emitir decisão registrada em ata.

## Próximos estados possíveis

- **Confirmado:** regra de domínio aprovada, desvio reproduzido sobre versão oficial, evidencia linkada.
- **Reclassificado:** regra de domínio não exige o comportamento proposto; corrigir o plano e justificar.
- **Resolvido:** código alterado por commit com teste de regressão passando, revisão documentada.

Não atribuir estado “resolvido” enquanto não existir commit corretivo e evidência de reexecução.

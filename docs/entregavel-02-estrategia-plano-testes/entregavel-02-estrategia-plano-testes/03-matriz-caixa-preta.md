# Entregável 2 — Casos de caixa-preta (equivalência e valores-limite)

**Elaboração:** casos especificados com apoio de IA para o planejamento do A3. **Não são os testes manuais independentes que servirão de comparação com a IA**. Os integrantes devem revisar os oráculos e produzir o braço manual separadamente.

## 1. Classes de equivalência por requisito

| Requisito | Classes equivalentes válidas | Classes equivalentes inválidas | Limites escolhidos |
|---|---|---|---|
| RF-01 — despesa | Número decimal finito > 0 | Negativo, zero, texto, `NaN`, `Infinity`, overflow | -0,01 / 0 / +0,01 |
| RF-02 — edição | Índice existente e novo valor > 0 e finito | Índice ausente, valor 0/negativo ou não finito | índice -1 / 0; montante 0 / 0,01 |
| RF-03 — orçamento | Número finito ≥ 0 (incluindo zero) | Negativo, texto, `NaN`, `Infinity` | -0,01 / 0 / +0,01 |
| RF-04 — alerta | Despesa menor/igual ao teto | Despesa acima do teto | 9,99 / 10,00 / 10,01 para teto 10,00 |
| RF-05 — resumo | Pertence ao mês ou categoria; várias despesas | Não pertence ao mês/categoria | 1 despesa / 2 despesas; categoria com caixa diversa |
| RF-06 — data | Data real ISO, inclusive bissexta | Data impossível ou mês inexistente | 2024-02-29 / 2025-02-29; 2026-13 |
| RF-07 — CSV | Texto simples e texto com vírgulas/aspas | Arquivo malformado (pendente) | Descrição com vírgula |
| RF-08 — índice/menu | Índice existente, opção válida | Índice negativo/fora do tamanho, opção inexistente | -1 / 0; 99 no menu |

> Limites de R$ 0,01 são escolhas do grupo para testes de campo financeiro; o legado aceita `double`, e a exigência de exatamente duas casas decimais não está implementada nem foi presumida. RF-01/RF-03 dependem de aprovação humana.

## 2. Matriz detalhada — 30 casos

| ID | Requisito | Técnica | Descrição e entrada principal | Resultado esperado | Exploratório |
|---|---|---|---|---|---|
| CP-01 | RF-01 | EP / BVA | **Despesa R$ 0,01 válida** — 1 → 2026-07-21 → Almoco → 0.01 → Alimentacao → 0 | contém `Expense added.`; não contém `Amount must be greater than zero`; arquivo `expenses.txt` contém `0.01` | PASSOU |
| CP-02 | RF-01 | BVA | **Despesa zero rejeitada** — 1 → 2026-07-21 → Almoco → 0 → Alimentacao → 0 | contém `Amount must be greater than zero. Expense not added.`; não contém `Expense added.`; arquivo `expenses.txt` existe | PASSOU |
| CP-03 | RF-01 | BVA | **Despesa negativa -0,01 rejeitada** — 1 → 2026-07-21 → Almoco → -0.01 → Alimentacao → 0 | contém `Amount must be greater than zero. Expense not added.`; não contém `Expense added.` | PASSOU |
| CP-04 | RF-01 | EP | **Despesa positiva usual aceita** — 1 → 2026-07-21 → Almoco → 15.50 → Alimentacao → 0 | contém `Expense added.`; arquivo `expenses.txt` contém `15.5` | PASSOU |
| CP-05 | RF-01 | EP | **Texto alfabético rejeitado** — 1 → 2026-07-21 → Almoco → abc → Alimentacao → 0 | contém `Invalid amount. Expense not added.`; não contém `Expense added.` | PASSOU |
| CP-06 | RF-01 | EP | **NaN deve ser rejeitado** — 1 → 2026-07-21 → Almoco → NaN → Alimentacao → 0 | contém `Invalid amount. Expense not added.`; não contém `Expense added.` | FALHOU |
| CP-07 | RF-01 | EP | **Infinity deve ser rejeitado** — 1 → 2026-07-21 → Almoco → Infinity → Alimentacao → 0 | contém `Invalid amount. Expense not added.`; não contém `Expense added.` | FALHOU |
| CP-08 | RF-01 | EP | **-Infinity deve ser rejeitado** — 1 → 2026-07-21 → Almoco → -Infinity → Alimentacao → 0 | não contém `Expense added.` | PASSOU |
| CP-09 | RF-01 | EP / BVA | **Overflow numérico rejeitado** — 1 → 2026-07-21 → Almoco → 1e309 → Alimentacao → 0 | contém `Invalid amount. Expense not added.`; não contém `Expense added.` | FALHOU |
| CP-10 | RF-06 | EP | **Data bissexta válida 2024-02-29** — 1 → 2024-02-29 → Almoco → 1.00 → Alimentacao → 0 | contém `Expense added.`; arquivo `expenses.txt` contém `2024-02-29` | PASSOU |
| CP-11 | RF-06 | EP / BVA | **Data impossível 2025-02-29** — 1 → 2025-02-29 →  → 0 | contém `Invalid date format. Please use YYYY-MM-DD.`; não contém `Expense added.` | PASSOU |
| CP-12 | RF-06 | EP | **Mês inválido 2026-13** — 6 → 2026-13 →  → 0 | contém `Invalid month format. Please use YYYY-MM.` | PASSOU |
| CP-13 | RF-03 / RF-04 | BVA | **Orçamento zero permitido** — 8 → 2026-07 → 0 → 0 | contém `Budget for 2026-07 set to 0.0`; arquivo `budgets.txt` contém `2026-07,0.0` | PASSOU |
| CP-14 | RF-03 / RF-04 | BVA | **Orçamento mínimo positivo** — 8 → 2026-07 → 0.01 → 0 | contém `Budget for 2026-07 set to 0.01`; arquivo `budgets.txt` contém `2026-07,0.01` | PASSOU |
| CP-15 | RF-03 / RF-04 | BVA | **Orçamento negativo rejeitado** — 8 → 2026-07 → -0.01 → 0 | contém `Invalid amount.`; não contém `Budget for 2026-07 set to` | FALHOU |
| CP-16 | RF-03 / RF-04 | EP | **Orçamento NaN rejeitado** — 8 → 2026-07 → NaN → 0 | contém `Invalid amount.`; não contém `Budget for 2026-07 set to` | FALHOU |
| CP-17 | RF-03 / RF-04 | EP | **Orçamento Infinity rejeitado** — 8 → 2026-07 → Infinity → 0 | contém `Invalid amount.`; não contém `Budget for 2026-07 set to` | FALHOU |
| CP-18 | RF-03 / RF-04 | EP | **Orçamento com texto rejeitado** — 8 → 2026-07 → abc → 0 | contém `Invalid amount.`; não contém `Budget for 2026-07 set to` | PASSOU |
| CP-19 | RF-03 / RF-04 | BVA | **Gasto abaixo do orçamento não alerta** — 8 → 2026-07 → 10 → 1 → 2026-07-21 → Almoco → 9.99 → Alimentacao → 0 | contém `Expense added.`; não contém `Warning: expenses for 2026-07` | PASSOU |
| CP-20 | RF-03 / RF-04 | BVA | **Gasto igual ao orçamento não alerta** — 8 → 2026-07 → 10 → 1 → 2026-07-21 → Almoco → 10.00 → Alimentacao → 0 | contém `Expense added.`; não contém `Warning: expenses for 2026-07` | PASSOU |
| CP-21 | RF-03 / RF-04 | BVA | **Gasto acima do orçamento alerta** — 8 → 2026-07 → 10 → 1 → 2026-07-21 → Almoco → 10.01 → Alimentacao → 0 | contém `Warning: expenses for 2026-07` | PASSOU |
| CP-22 | RF-05 | EP | **Resumo soma valores corretamente** — 1 → 2026-07-21 → Almoco → 10.25 → Alimentacao → 1 → 2026-07-21 → Almoco → 2.75 → Alimentacao →… | contém `Total expenses: 13.00` | PASSOU |
| CP-23 | RF-05 | EP | **Resumo do mês exclui mês distinto** — 1 → 2026-07-21 → Almoco → 10 → Alimentacao → 1 → 2026-08-21 → Almoco → 5 → Alimentacao → 6 → 2… | contém `Total for 2026-07: 10.00` | PASSOU |
| CP-24 | RF-05 | EP | **Filtro de categoria ignora maiúsculas** — 1 → 2026-07-21 → Almoco → 7 → Food → 7 → food → 0 | contém `Total for category 'food': 7.00` | PASSOU |
| CP-25 | RF-08 | BVA | **Índice -1 rejeitado** — 3 → -1 → 0 | contém `Invalid index.` | PASSOU |
| CP-26 | RF-08 | BVA | **Índice 0 exclui registro** — 1 → 2026-07-21 → Almoco → 7 → Alimentacao → 3 → 0 → 5 → 0 | contém `Expense deleted.`, `Total expenses: 0.00` | PASSOU |
| CP-27 | RF-02 | BVA | **Alteração de valor zero rejeitada** — 1 → 2026-07-21 → Almoco → 7 → Alimentacao → 2 → 0 → 2026-07-21 → Atualizada → 0 → 5 → 0 | contém `Amount must be greater than zero. Expense not updated.`, `Total expenses: 7.00` | PASSOU |
| CP-28 | RF-02 | EP | **Alteração de valor NaN rejeitada** — 1 → 2026-07-21 → Almoco → 7 → Alimentacao → 2 → 0 → 2026-07-21 → Atualizada → NaN → 5 → 0 | contém `Invalid amount. Expense not updated.`, `Total expenses: 7.00` | FALHOU |
| CP-29 | RF-07 | EP | **Exportar descrição com vírgula mantém aspas** — 1 → 2026-07-21 → cafe, bolo → 12.5 → Alimentacao → 9 → 0 | contém `Expenses exported to expenses_export.csv`; arquivo `expenses_export.csv` contém `"cafe, bolo"` | PASSOU |
| CP-30 | RF-08 | EP | **Opção de menu fora do intervalo rejeitada** — 99 → 0 | contém `Invalid choice. Please try again.` | PASSOU |

**Registro completo dos inputs, oráculos e saída real:** [`casos_caixa_preta.csv`](../../tests/planejamento/entregavel-02/casos_caixa_preta.csv), [`resultado_30_casos_caixa_preta.json`](../../evidencias/entregavel-02/resultado_30_casos_caixa_preta.json).

## 3. Interpretação dos resultados

Na execução exploratória foram avaliados **30 casos**: **23 passaram**, **7 não satisfizeram seus oráculos**. Divergências: `CP-06`, `CP-07`, `CP-09`, `CP-15`, `CP-16`, `CP-17`, `CP-28`.

As sete falhas não significam sete defeitos independentes: vários casos refletem a mesma lacuna de validação de valores especiais. Requer-se revisão da regra de negócio antes de declarar não conformidades definitivas.

## 4. Critérios de desenho e limitação do experimento

- Os oráculos foram definidos antes de executar os cenários para não reproduzir as decisões do legado como se fossem requisitos corretos.
- A execução foi feita com novas pastas temporárias por cenário; dados não vazam entre testes.
- A elaboração com IA destes casos impede chamá-los de testes escritos manualmente pelos integrantes; o braço humano da comparação precisa ser independente.
- Os resultados devem ser reproduzidos no clone do repositório sob SHA fixo antes da apresentação.
- Metas JaCoCo P1: 90% decisões, 85% linhas. **Não medidas** nesta etapa.

## 5. Novos casos para evolução

- Consulta de orçamento ainda inexistente (ramo ausente).
- Consulta com categoria inexistente.
- Edição movimentando despesa entre meses diferentes.
- Carregamento de arquivos contendo linhas de CSV malformadas e conteúdo inválido.
- Valores positivos com mais de duas casas decimais após o grupo definir política monetária.

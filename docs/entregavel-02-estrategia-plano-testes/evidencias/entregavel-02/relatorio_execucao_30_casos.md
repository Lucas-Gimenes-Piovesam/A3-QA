# Evidência — execução dos casos de caixa-preta (Entregável 2)

**Data UTC:** 2026-11-24T23:54:48.580994+00:00  
**Ambiente:** openjdk version "21.0.12.1" 2026-08-18  
**Compilação:** 0.877 s  
**Resultados:** 23/30 casos com todos os oráculos satisfeitos; 7 divergências.

> Não confundir falha no oráculo com defeito confirmado sem validação da regra de negócio. Os casos são especificações inicialmente elaboradas com assistência de IA; não são a amostra manual independente da comparação do A3.

| Caso | Método | Cenário | Resultado |
|---|---|---|---|
| CP-01 | EP / BVA | Despesa R$ 0,01 válida | **PASSOU** |
| CP-02 | BVA | Despesa zero rejeitada | **PASSOU** |
| CP-03 | BVA | Despesa negativa -0,01 rejeitada | **PASSOU** |
| CP-04 | EP | Despesa positiva usual aceita | **PASSOU** |
| CP-05 | EP | Texto alfabético rejeitado | **PASSOU** |
| CP-06 | EP | NaN deve ser rejeitado | **FALHOU** |
| CP-07 | EP | Infinity deve ser rejeitado | **FALHOU** |
| CP-08 | EP | -Infinity deve ser rejeitado | **PASSOU** |
| CP-09 | EP / BVA | Overflow numérico rejeitado | **FALHOU** |
| CP-10 | EP | Data bissexta válida 2024-02-29 | **PASSOU** |
| CP-11 | EP / BVA | Data impossível 2025-02-29 | **PASSOU** |
| CP-12 | EP | Mês inválido 2026-13 | **PASSOU** |
| CP-13 | BVA | Orçamento zero permitido | **PASSOU** |
| CP-14 | BVA | Orçamento mínimo positivo | **PASSOU** |
| CP-15 | BVA | Orçamento negativo rejeitado | **FALHOU** |
| CP-16 | EP | Orçamento NaN rejeitado | **FALHOU** |
| CP-17 | EP | Orçamento Infinity rejeitado | **FALHOU** |
| CP-18 | EP | Orçamento com texto rejeitado | **PASSOU** |
| CP-19 | BVA | Gasto abaixo do orçamento não alerta | **PASSOU** |
| CP-20 | BVA | Gasto igual ao orçamento não alerta | **PASSOU** |
| CP-21 | BVA | Gasto acima do orçamento alerta | **PASSOU** |
| CP-22 | EP | Resumo soma valores corretamente | **PASSOU** |
| CP-23 | EP | Resumo do mês exclui mês distinto | **PASSOU** |
| CP-24 | EP | Filtro de categoria ignora maiúsculas | **PASSOU** |
| CP-25 | BVA | Índice -1 rejeitado | **PASSOU** |
| CP-26 | BVA | Índice 0 exclui registro | **PASSOU** |
| CP-27 | BVA | Alteração de valor zero rejeitada | **PASSOU** |
| CP-28 | EP | Alteração de valor NaN rejeitada | **FALHOU** |
| CP-29 | EP | Exportar descrição com vírgula mantém aspas | **PASSOU** |
| CP-30 | EP | Opção de menu fora do intervalo rejeitada | **PASSOU** |

## Divergências

### CP-06 — NaN deve ser rejeitado
- Critério não satisfeito: Contém 'Invalid amount. Expense not added.'
- Critério não satisfeito: Não contém 'Expense added.'
- Comportamento observado (trecho): `Enter your choice: Expenses saved. Exiting...`

### CP-07 — Infinity deve ser rejeitado
- Critério não satisfeito: Contém 'Invalid amount. Expense not added.'
- Critério não satisfeito: Não contém 'Expense added.'
- Comportamento observado (trecho): `Enter your choice: Expenses saved. Exiting...`

### CP-09 — Overflow numérico rejeitado
- Critério não satisfeito: Contém 'Invalid amount. Expense not added.'
- Critério não satisfeito: Não contém 'Expense added.'
- Comportamento observado (trecho): `Enter your choice: Expenses saved. Exiting...`

### CP-15 — Orçamento negativo rejeitado
- Critério não satisfeito: Contém 'Invalid amount.'
- Critério não satisfeito: Não contém 'Budget for 2026-07 set to'
- Comportamento observado (trecho): `Enter your choice: Expenses saved. Exiting...`

### CP-16 — Orçamento NaN rejeitado
- Critério não satisfeito: Contém 'Invalid amount.'
- Critério não satisfeito: Não contém 'Budget for 2026-07 set to'
- Comportamento observado (trecho): `Enter your choice: Expenses saved. Exiting...`

### CP-17 — Orçamento Infinity rejeitado
- Critério não satisfeito: Contém 'Invalid amount.'
- Critério não satisfeito: Não contém 'Budget for 2026-07 set to'
- Comportamento observado (trecho): `Enter your choice: Expenses saved. Exiting...`

### CP-28 — Alteração de valor NaN rejeitada
- Critério não satisfeito: Contém 'Invalid amount. Expense not updated.'
- Critério não satisfeito: Contém 'Total expenses: 7.00'
- Comportamento observado (trecho): `Enter your choice: Expenses saved. Exiting...`

## Limitações

- Executado sem alterações no programa e com dados isolados por cenário.
- Regras de domínio propostas para valores financeiros finitos e orçamento não negativo exigem aprovação humana.
- O relatório não contém cobertura JaCoCo e não fornece comparação com testes desenvolvidos manualmente.
- Validar no repositório original fixado por commit SHA antes de utilizar como evidência final.

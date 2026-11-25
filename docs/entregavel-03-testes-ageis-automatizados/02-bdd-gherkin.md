# BDD em Gherkin — entendimento do negócio

O cenário de negócio está definido em português em [`valores-financeiros.feature`](../../tests/bdd/valores-financeiros.feature), com linguagem `Dado / Quando / Então / E`, para facilitar a leitura por pessoas que não programam.

## Matriz de rastreabilidade

| Comportamento BDD | Método de verificação automatizada |
|---|---|
| Despesa positiva válida | `ExpenseAmountTest.acceptsOrdinaryAmount`, `CliFinancialIntegrationTest.acceptsOrdinaryExpense` |
| Despesas zero/negativas/não finitas rejeitadas | `ExpenseAmountTest.rejectsInvalidExpenseAmounts`; CLI integrada para `NaN`/`Infinity` |
| Orçamento zero aceito | `FinancialRulesTest.budgetCanBeZeroButNotNegative`, `CliFinancialIntegrationTest.acceptsZeroBudget` |
| Orçamento negativo e `NaN` rejeitados | `FinancialRulesTest`, `CliFinancialIntegrationTest.rejectsNegativeBudget`, `rejectsNanBudget` |
| Atualização com `NaN` preserva despesa anterior | `CliFinancialIntegrationTest.updateRejectsNanAndPreservesSavedAmount` |
| Orçamento antigo `NaN` ignorado | `CliFinancialIntegrationTest.skipsInvalidPersistedBudget` |
| Registro antigo contendo `NaN` ignorado | `CliFinancialIntegrationTest.skipsInvalidPersistedExpense` |

**Limitação importante:** este arquivo `.feature` foi preparado como especificação BDD **legível**, mas não está ligado a *step definitions* do Cucumber. Os testes JUnit verificam os comportamentos equivalentes, portanto `mvn test` executa a suíte automatizada JUnit, e **não** interpreta diretamente o Gherkin.

Para automatizar os cenários Gherkin integralmente, poderemos futuramente acrescentar Cucumber-JVM e step definitions, registrando essa nova funcionalidade em um commit distinto.

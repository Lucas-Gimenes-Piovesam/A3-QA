# CR-09-01 — Corrigir validação de valores financeiros

**Tipo:** manutenção **corretiva** · **Prioridade:** P1 (resultado financeiro) · **Status:** **implementada anteriormente ao E9**, não é tarefa nova.  
**Solicitante:** análise de qualidade do A3 (não confundir com Issue do usuário).  
**Escopo:** `Expense.java`, `FinancialRules.java`, `ExpenseTracker.java`, `ExpenseStorage.java` e `BudgetStorage.java`.

## Motivação

O piloto documentado em [`docs/linha-base-e-piloto.md`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/docs/linha-base-e-piloto.md) observou que a aplicação inicial aceitava `NaN`/`Infinity` em caminhos financeiros. Esses valores podiam contaminar totais e orçamentos. O grupo propôs a regra de aceitar somente quantias **finitas e positivas para despesas** e **finitas e não negativas para orçamento**, validando também dados importados.

## Situação atual verificada

- [`FinancialRules.validExpenseAmount`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/FinancialRules.java#L8-L10) verifica `Double.isFinite(amount) && amount > 0`.
- [`FinancialRules.validBudgetAmount`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/FinancialRules.java#L13-L15) aceita orçamento zero e rejeita quantias não finitas e negativas.
- [`Expense` construtor](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/Expense.java#L9-L15) lança exceção para despesa inválida.
- Rotas da CLI e carregamento de arquivo consultam as regras; há testes correspondentes em [`tests/junit/Expense_Tracker/`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/tests/junit/Expense_Tracker).

## Impacto da intervenção

- **Funcional:** alto — validação das operações essenciais e tratamento de entradas.
- **Dados:** alto — evita criação e reimportação de quantias não finitas; arquivos históricos inválidos podem ser ignorados.
- **Arquitetura:** baixo — validador puro extraído, sem alterar plataforma ou dados em massa.
- **Testes:** alto — casos de classes inválidas, limites e persistência.
- **Usuário:** médio — novas rejeições, com mensagens de erro no console.

## Aceite retrospectivo e riscos residuais

Evidência: [workflow verde](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45527258647) e `ExpenseAmountTest`, `FinancialRulesTest` e `CliFinancialIntegrationTest`. **A CI atesta execução dos testes, não a inexistência de todo defeito.** Confirmar com o grupo a política sobre zero, valores fracionários e limpeza de registros legados antes de expandir o produto. Os valores `double` e arredondamento monetário exigem análise separada se a precisão contábil entrar nos requisitos.

# CR-09-04 — Separar interface do terminal, domínio e persistência

**Tipo:** manutenção **perfectiva** · **Prioridade:** P2 · **Status:** **proposta, não implementada** · **Esforço relativo:** 8 SP.

## Contexto

[`ExpenseTracker.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseTracker.java) acumula menu, leitura de dados, decisões de cadastro/edição, cálculo de resumo e chamadas de armazenamento. Isso dificulta isolar lógica para testes sem emular terminal, apesar de os testes JUnit atuais já cobrirem muitos caminhos. O projeto contém `FinancialRules`, evidenciando que a extração de regras puras é viável.

## Solicitação

Introduzir gradualmente uma camada de serviços, por exemplo `ExpenseService`, `BudgetService` e um contrato simples de armazenamento, mantendo a `main()` como adaptador de CLI. Os nomes são **propostas de design**: não são arquivos existentes na versão inspecionada. Evitar introduzir frameworks complexos, serviço web ou banco sem requisito validado.

## Impactos

- **Funcional:** baixo (comportamento observável deve permanecer igual).
- **Dados:** médio (mudança de dependências exige preservar serialização e ordem).
- **Arquitetura:** **alto** (interfaces/responsabilidades).
- **Testes:** **alto** (testes unitários puros, além dos end-to-end existentes).
- **Usuário:** baixo (CLI e arquivos permanecem compatíveis).

## Critérios de aceite

- **AC1:** operações de adicionar, atualizar, apagar, resumir por mês/categoria e orçamento permanecem com resultados equivalentes em fixtures definidas.
- **AC2:** não mudar formato de CSV ou nomes de arquivos nesta CR.
- **AC3:** novas regras podem ser testadas sem invocar `ProcessBuilder`.
- **AC4:** o job `ci-quality-gate` passa e não ocorre regressão de contrato CLI.
- **AC5:** manter PRs pequenos, fazendo extração por operação para facilitar revisão e rollback.

**Riscos:** refatoração grande pode atrasar experimentos da A3; sugerimos começar pelo serviço de somatório e adiar escopo caso prejudique o E10.

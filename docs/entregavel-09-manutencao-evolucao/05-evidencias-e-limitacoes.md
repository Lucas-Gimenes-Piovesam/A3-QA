# 5. Evidências auditáveis, limitações e rastreabilidade

## 5.1 Código e fonte primária

- [Commit da inspeção — `5bbc42c`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd)
- [Classe principal e lógica do menu](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseTracker.java)
- [Validador financeiro já implementado](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/FinancialRules.java)
- [Classe Expense e validação no construtor](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/Expense.java)
- [Armazenamento de despesas — leitura e escrita](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseStorage.java)
- [Armazenamento de orçamentos](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/BudgetStorage.java)
- [CSV](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/CsvUtil.java)

## 5.2 Evidência de correção prévia de CR-09-01

- [Commit com regras financeiras e refatoração](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/1935c0d187d892174a6bd0eab65ec3f8ae6f0c26) — modificação anterior ao E9.
- [Correção do erro de compilação dos testes](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/3d37fd58b69cf0f8e719ead78ba7d15680fe3684).
- [PR #1 — ampliou cobertura financeira e integrou testes](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1).
- [Workflow verde após o E8](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45527258647): build, JUnit, análise estática e cobertura; o sucesso se refere à suíte executada, não a inexistência de defeitos.

**Cautela histórica:** a documentação do E3 registra que o commit rotulado GREEN de uma sequência foi vazio e a alteração correspondente ocorreu em outro commit. Este E9 **não corrige retroativamente a evidência TDD**, mas registra a correção já presente no produto.

## 5.3 Natureza das constatações

| Enunciado | Classificação epistemológica | Comprovação |
|---|---|---|
| Regras financeiras finitas estão no código atual | Fato verificado por inspeção | `Expense.java`, `FinancialRules.java`, `ExpenseTracker.java` |
| CI está funcionando no snapshot | Execução observada | Workflow verde |
| Escrita em arquivo direto não usa troca atômica explícita | Fato verificado por inspeção | `saveExpenses`, `saveBudgets` |
| Falha durante gravação provoca perda de dados | **Risco previsto, não incidente observado** | Requer experimento de injeção de erro |
| Datas inválidas em arquivo entram no modelo | **Risco fundamentado no fluxo do código**, teste pendente | Requer fixture e execução isolada |
| Separar camadas reduz horas reais de manutenção | **Hipótese de benefício**, ainda não medida | Requer medição pós-intervenção |
| Refatorar é a escolha adequada | Recomendação fundamentada, sujeita à validação do grupo | ADR e critérios ponderados |

## 5.4 Limitações e o que não declaramos

- Não houve criação de Issues formais no GitHub para as CRs. **CR-09-xx são identificadores documentais internos**; podem virar Issues posteriormente.
- Nenhuma alteração adicional em `src/` é realizada pela publicação deste E9.
- Não há prova de defeitos introduzidos por CR-09-02/03/04 ou de execução de suas soluções.
- Notas da matriz de alternativas são juízos iniciais, não valores medidos em produção.
- A reunião de aprovação e as horas realizadas não foram informadas; não inventamos nome de aprovador, data de reunião ou prazo cumprido.
- A baseline histórica foi reconstruída a partir de fonte pública; verificar provenance conforme E1 antes do relatório final.

**Evidência estruturada:** consultar `evidencias/entregavel-09/inspecao-repositorio.json` e os dois arquivos CSV. São cópias estáticas com commit de referência, não conexão em tempo real.

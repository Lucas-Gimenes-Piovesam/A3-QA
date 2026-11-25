# 1. Inspeção técnica e metodologia de classificação

## 1.1 Fonte e escopo

A inspeção documental foi feita no estado da branch `main` em [`5bbc42c`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd) do A3-QA, em 25/11/2026. O software é um gerenciador de despesas **Java CLI**, com dados em arquivos locais (`expenses.txt` e `budgets.txt`), sem banco de dados ou API web. Foram lidos os arquivos `ExpenseTracker.java`, `Expense.java`, `ExpenseStorage.java`, `BudgetStorage.java`, `FinancialRules.java` e `CsvUtil.java` diretamente no repositório.

### Fatos identificados no código (não são hipóteses)

1. A interface recebe e interpreta entradas, gerencia operações, formata resumos e chama persistência na mesma classe: [`ExpenseTracker.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseTracker.java).
2. `Expense` e `FinancialRules` rejeitam despesas não finitas ou não positivas. `manageBudget` verifica valores finitos e não negativos. **A correção monetária já foi aplicada antes deste Entregável 9**: [`FinancialRules.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/FinancialRules.java) e [`Expense.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/Expense.java).
3. As rotinas `saveExpenses` e `saveBudgets` gravam diretamente no arquivo de destino por `new FileWriter(FILENAME)`; não há no código uma etapa explícita de arquivo temporário, sincronização e substituição atômica: [`ExpenseStorage.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseStorage.java#L15-L24), [`BudgetStorage.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/BudgetStorage.java#L49-L59).
4. O menu aceita datas via `LocalDate.parse`, mas `ExpenseStorage.loadExpenses()` repassa a data do arquivo para `new Expense(...)` sem validar sua sintaxe; `monthKey` extrai os primeiros caracteres da string: [`ExpenseStorage.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseStorage.java#L25-L49), [`ExpenseTracker.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseTracker.java#L308-L315).
5. As quantias usam `double`. Isso **não equivale à comprovação de erro de arredondamento em caso de uso específico**; migração para `BigDecimal` é uma alternativa a avaliar com casos de aceitação.

### Hipóteses de risco — ainda não reproduzidas

- Gravação interrompida ou falha de disco **pode** deixar dados incompletos quando se escreve diretamente no arquivo de destino. É risco de projeto/arquitetura, **não incidente observado** no A3.
- Dados de data inválida inseridos manualmente em `expenses.txt` **podem** ser aceitos na leitura, apesar da validação da CLI. A afirmação é uma **inspeção de caminho de código**; ainda cabe reproduzir o cenário com fixture isolada e formalizar política de rejeição.
- Acoplamento entre entrada/saída e cálculos **pode** aumentar custo de manutenção; não medimos seu custo em horas.

## 1.2 Categorias de manutenção adotadas

- **Corretiva:** remover comportamento que contradiz regra aceita ou corrigir defeito confirmado; se o defeito é apenas suspeito, indicar explicitamente "corretiva potencial / a validar".
- **Preventiva:** reduzir risco futuro (ex.: tolerância a falhas de gravação) mesmo sem incidente reproduzido.
- **Perfectiva:** melhorar organização, legibilidade, testabilidade ou outras propriedades internas sem mudar a finalidade funcional.
- **Adaptativa:** ajustar o software a alteração efetiva de ambiente, plataforma ou requisito externo; nenhuma CR principal foi artificialmente rotulada de adaptativa.

**Status:** `implementada`, `proposta`, `descartada`, `em execução`, `validada`. Somente o primeiro é atribuído a CR-09-01 nesta fotografia, com referência ao código e aos testes; "validada pelo grupo" depende de ata.

## 1.3 Priorização e análise de impacto

Impacto estimado por dimensão: **Funcional (F), Dados (D), Arquitetura (A), Testes (T), Operação/usuário (U)** em **baixo / médio / alto**. Não é medição estatística. Classificação P1 = risco de perda/resultado financeiro incorreto; P2 = consistência, evolutividade e experiência; P3 = cosmética. A escala só guia debate do grupo.

Estimativa técnica em **Story Points relativos (1, 2, 3, 5, 8)**, sem conversão para horas, e **não retroativamente somada** ao baseline de 70 SP do Entregável 7. Causas e riscos ainda serão revisados pelo grupo antes de abrir Issues de implementação.

## 1.4 Critérios mínimos de aprovação de uma CR

1. Regra de negócio acordada e caso de teste negativo antes da mudança.
2. Identificação de classes/artefatos afetados e análise de compatibilidade dos arquivos históricos.
3. Plano de rollback e proteção de dados locais.
4. PR com diff pequeno, revisão por outra pessoa, suíte JUnit, JaCoCo e Checkstyle aprovados.
5. Atualização do dicionário de métricas, documentação e rastreabilidade entre CR, teste, commit e resultado.

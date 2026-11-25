# Suíte automatizada JUnit 5 — execução do Entregável 3

## Estrutura

- `tests/junit/Expense_Tracker/ExpenseAmountTest.java`: TDD do construtor de despesa (7 verificações concretas a partir de 2 testes normais e 5 parâmetros inválidos).
- `tests/junit/Expense_Tracker/FinancialRulesTest.java`: 4 testes dos validadores financeiros.
- `tests/junit/Expense_Tracker/CliFinancialIntegrationTest.java`: 9 testes CLI em processos Java isolados e diretórios temporários; não escrevem dados reais na pasta do projeto.
- `tests/junit/Expense_Tracker/CsvRoundTripJUnitTest.java`: 2 testes de regressão do CSV.
- `src/Expense_Tracker/CsvUtilTest.java`: verificador legado via `main`, independente do JUnit, conservado.

**Total planejado: 22 execuções JUnit** (7 no TDD + 4 regras + 9 CLI + 2 CSV). Contagem depende do runner Maven/JUnit efetivamente instalado. A confirmação e a contagem reais deverão ser registradas pelos relatórios Surefire.

## Preparação do ambiente

1. Instalar JDK 17+ e Maven 3.9+; conferir com `java -version` e `mvn -version`.
2. Na raiz do repositório, rodar `mvn -Dtest=ExpenseAmountTest test` para visualizar cada fase TDD.
3. Após o último commit, rodar `mvn clean test` (testes unitários + CLI).
4. Guardar os arquivos `target/surefire-reports/*.xml` e `*.txt` ou artefatos do GitHub Actions.
5. Executar a verificação legado: `cd src && javac Expense_Tracker/*.java && java Expense_Tracker.CsvUtilTest`.

O `pom.xml` usa explicitamente `src/` como diretório de produção e `tests/junit/` como diretório de testes, preservando a estrutura do código legado. A configuração é compatível com o `pom.xml` preparado para o Entregável 4.

## Reprodutibilidade sem Maven

Mesmo se Maven não estiver instalado, é possível executar o verificador autônomo 
`evidencias/entregavel-03/ExpenseContractProof.java`, que **não é JUnit**:

```sh
mkdir -p /tmp/a3qa-build
javac -d /tmp/a3qa-build src/Expense_Tracker/*.java evidencias/entregavel-03/ExpenseContractProof.java
java -cp /tmp/a3qa-build ExpenseContractProof
```

Para ver a etapa Red, usar a versão do código no commit Red antes de executar. As saídas de cada fase já estão registradas em `log-red.txt`, `log-green.txt` e `log-refactor.txt`.

## Validação local realizada

O ambiente que preparou este entregável tinha OpenJDK 21, mas **não tinha Maven instalado**. A compilação Java do código e o verificador autônomo foram executados para as três etapas. A CLI final também foi exercitada com entradas fictícias em diretórios temporários. **Não declarar que a suíte JUnit ou o GitHub Actions passaram até obter os relatórios de execução correspondentes.**

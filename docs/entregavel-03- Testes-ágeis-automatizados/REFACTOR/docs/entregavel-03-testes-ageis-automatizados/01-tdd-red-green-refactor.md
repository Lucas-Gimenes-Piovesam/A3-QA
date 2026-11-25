# Entregável 3 — Demonstração do TDD: Red → Green → Refactor

## 1. Regra e motivação

Módulo P1: `src/Expense_Tracker/Expense.java` armazena valores de despesas. Antes da mudança, o construtor apenas atribuía o valor recebido, sem impedir negativos, zero, `NaN` ou infinitos. A validação do cadastro/edição pelo menu verifica `amount <= 0`, que não bloqueia `NaN` e infinito positivo. Esses valores podem invalidar os totais financeiros.

**Regra de aceitação planejada para o A3:** uma despesa deve ser um valor finito e estritamente positivo. Para o orçamento mensal, valores finitos iguais ou maiores que zero são aceitos; negativos e não finitos são rejeitados. O grupo deve validar esta última regra em ata, pois é uma decisão de domínio introduzida na manutenção.

## 2. Etapa RED — teste antes da mudança

**Commit esperado:** `test(tdd-red): especificar validacao dos valores de despesas`

Arquivos: `pom.xml`, `config/checkstyle/checkstyle.xml`, `tests/junit/Expense_Tracker/ExpenseAmountTest.java` e evidência da execução local.

1. Registrar a versão-base que ainda possui o `Expense.java` original.
2. Rodar `mvn -Dtest=ExpenseAmountTest test`.
3. Guardar o resultado: **espera-se reprovação em cinco casos de valores inválidos**. Não corrigir nem editar o teste nesta fase.
4. Fazer o primeiro commit.

**Execução efetiva local sem Maven:** compilei as seis classes originais com `javac` e rodei o verificador autônomo `ExpenseContractProof` com as mesmas sete situações. Resultado: `PASS=2 FAIL=5` e código de saída 1. Ver [`log-red.txt`](../../evidencias/entregavel-03/log-red.txt). **Isso não é uma execução do JUnit**; a execução JUnit deverá ser registrada no GitHub com Maven.

## 3. Etapa GREEN — menor alteração que faz os testes passarem

**Commit esperado:** `fix(tdd-green): rejeitar despesas com valores invalidos`

Arquivo modificado: `src/Expense_Tracker/Expense.java` (validação diretamente no construtor). Rodar novamente o comando JUnit e registrar o resultado antes do segundo commit.

**Execução efetiva local:** o mesmo verificador com `javac`/`java` terminou com `PASS=7 FAIL=0` e código de saída zero. Ver [`log-green.txt`](../../evidencias/entregavel-03/log-green.txt).

**Observação:** a etapa Green isola a mudança na classe `Expense`. **Não consideramos a integração com o menu concluída nesse ponto** — outras rotas de entrada ainda precisam tratar valores incorretos sem encerrar o programa inesperadamente.

## 4. Etapa REFACTOR — centralização da regra e integração segura

**Commit esperado:** `refactor(tdd): centralizar regras monetarias e validar a CLI`

Mudanças do terceiro commit:

- `src/Expense_Tracker/FinancialRules.java`: centraliza as funções puras `validExpenseAmount` e `validBudgetAmount`;
- `Expense.java`: delega ao validador, sem alterar a interface pública;
- `ExpenseTracker.java`: utiliza a mesma regra em cadastro/edição e orçamento, rejeitando a entrada antes da persistência;
- `ExpenseStorage.java`/`BudgetStorage.java`: ignoram registros persistidos inválidos;
- Testes JUnit complementares, cenário BDD, documentação e evidências.

**Execução efetiva local:** o verificador concluiu com `PASS=7 FAIL=0`. Ver [`log-refactor.txt`](../../evidencias/entregavel-03/log-refactor.txt).

## 5. Verificar histórico de commits

Depois dos três uploads, confirmar na guia **Commits** que a sequência é RED (falha), GREEN (passa), REFACTOR (passa). Incluir as **URLs reais** dos commits neste documento:

| Etapa | Commit SHA/URL | Saída Maven / Actions | Estado |
|---|---|---|---|
| RED | [preencher após upload] | [anexar execução reprovada] | Pendente de registro no GitHub |
| GREEN | [preencher após upload] | [anexar execução aprovada] | Pendente de registro no GitHub |
| REFACTOR | [preencher após upload] | [anexar execução aprovada] | Pendente de registro no GitHub |

**Atenção:** como o projeto não tem branch protegida neste momento, não é necessário abrir PR para demonstrar o TDD, mas não é correto alegar que um gate de CI bloqueou algum merge antes de configurá-lo no Entregável 4.

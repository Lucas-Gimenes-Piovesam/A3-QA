# Entregável 2 — Análise de caixa-branca e critérios de cobertura

**Base:** leitura estática do código-fonte Java do grupo (`A3-QA`, commit `0188d5ee4c8ca05114c933455d450c4148da5fd5`), observando como referência o projeto original (`b35ff1a420499703d0c9ec10851a32468ba31f2a`). **Não é relatório de JaCoCo.**

## 1. Critérios escolhidos

- **Cobertura de decisões/ramos nos métodos P1:** meta **≥ 90%**, pois regras críticas tomam decisões de validação e alerta. Numerador = resultados de ramos executados; denominador = resultados de ramos instrumentáveis nos métodos críticos selecionados. O relatório deverá identificar classe, método e versão, e ser obtido pelo **JaCoCo**, não por estimativa visual.
- **Cobertura de linhas nos métodos P1:** meta **≥ 85%**, incluindo caminhos usuais e erros; também aferida por JaCoCo.
- **Cobertura funcional mínima:** todas as classes críticas de entrada financeira da matriz especificadas e executadas; valores inválidos não podem ser aceitos silenciosamente.
- **Atenção:** caminhos mapeados abaixo indicam **alvos e candidatos de teste**, não porcentagens reais; o código do produto ainda não foi instrumentado.

**Como se mede após instrumentar:**

`Cobertura de decisões (%) = ramos executados / ramos identificados pela ferramenta × 100`.  
`Cobertura de linhas (%) = linhas executadas / linhas instrumentáveis × 100`.

A meta P1 foca risco financeiro e evita mascarar métodos críticos com cobertura alta em partes pouco relevantes. A meta não foi declarada alcançada.

## 2. Análise estática das decisões

| Local / método | Decisão relevante (caminhos verdadeiros/falsos) | Risco | Casos que exercitam comportamento associado |
|---|---|---|---|
| `addExpense` | Data ausente / fornecida | P2 | CP-10 / CP-11 |
| `addExpense` | `Double.parseDouble` lança / não lança exceção | P1 | CP-05 / CP-04 |
| `addExpense` | `amount <= 0` verdadeiro / falso | **P1** | CP-02/CP-03 / CP-01/CP-04 |
| `addExpense` | Valor especial finito / não finito | **P1** | CP-06, CP-07, CP-09 evidenciam **ausência de validação específica** no fluxo atual |
| `updateExpense` | Índice válido / inválido; valor positivo / não positivo | **P1** | CP-27, CP-28 e CP-25 (índice em exclusão) |
| `manageBudget` | Input vazio / preenchido | P1 | **Falta** caso explícito de visualização sem alteração de limite; adicionar na expansão |
| `manageBudget` | Formato aceito / exceção de parse | P1 | CP-14 / CP-18 |
| `manageBudget` | Orçamento presente / ausente | P1 | CP-13, CP-14; **falta** caso dedicado sem orçamento cadastrado |
| `manageBudget` | `spent > budget`: verdadeiro / falso | **P1** | CP-21 / CP-19, CP-20 |
| `warnIfOverBudget` | Mês nulo ou orçamento ausente / orçamento existente | **P1** | CP-01 (ausente) / CP-19–21 (existente) |
| `monthTotal` | Data pertence / não pertence ao mês | **P1** | CP-23 |
| `filterByCategory` | Categoria corresponde / não corresponde | P1 | CP-24; **falta** caso dedicado que não encontre nenhuma categoria |
| `ExpenseStorage.loadExpenses` | Linha vazia / não vazia; CSV malformado / íntegro; valor não numérico / numérico | P2 | **Pendência:** testes de integração de carregamento com arquivos preparados |
| `CsvUtil.escape` | Campo nulo / não nulo; exige aspas / não exige | P2 | CP-29; `CsvUtilTest` nativo cobre exemplos, **cobertura ainda não medida** |
| `CsvUtil.parseLine` | Dentro / fora de aspas; aspas duplicadas / simples | P2 | CP-29 e cenários nativos de CSV (apenas evidência de execução de exemplos) |

**Não extrapolar:** a presença de um ID na tabela não confirma que cada ramo correspondente foi efetivamente medido ou que o teste satisfaz a política de qualidade. A associação é um *plano de alvos*, a conferir em JaCoCo.

## 3. Fluxo de controle principal — cadastro de despesa

```text
[Selecionar opção 1]
       |
[readValidDate]
       |-- data vazia --> [Cancelar cadastro]
       |-- data válida --> [Ler descrição e montante]
                              |
                       [parseDouble]
                         |-- exceção --> [Rejeitar valor inválido]
                         |-- sucesso --> [amount <= 0 ?]
                                          |-- sim --> [Rejeitar]
                                          |-- não --> [Ler categoria, salvar, alertar]
```

**Fragilidade observável:** `Double.parseDouble("NaN")`, `Double.parseDouble("Infinity")` e `Double.parseDouble("1e309")` produzem valores que **não são bloqueados** pelo teste atual `amount <= 0`. O mesmo problema aparece na edição; o orçamento não verifica nem a regra `amount <= 0`. Os casos CP-06, CP-07, CP-09, CP-15, CP-16, CP-17 e CP-28 não satisfizeram os oráculos propostos na execução local. O código ainda precisa de uma mudança aprovada para validar finitude e limites.

**Decisão de teste:** priorizar as condições de erro e os ramos que alteram total, persistência ou alertas, pois um valor impróprio pode contaminar o resumo financeiro. Adicionar regressões após a correção; documentar o comportamento atual antes de alterá-lo.

## 4. Exemplo de decisões e rastreabilidade sem percentual inventado

| Condição / saída | Esperada | Observação do piloto | Evidência |
|---|---|---|---|
| `amount <= 0` para `0` ou negativo | Rejeição | Passou (CP-02, CP-03) | JSON do Entregável 2 |
| `amount > 0` finito | Cadastro permitido | Passou (CP-01, CP-04) | JSON do Entregável 2 |
| `NaN` no cadastro | Rejeição, **regra proposta** | Falhou (CP-06) | JSON do Entregável 2 |
| `Infinity` no cadastro | Rejeição, **regra proposta** | Falhou (CP-07) | JSON do Entregável 2 |
| `gasto > teto` | Alerta | Passou (CP-21) | JSON do Entregável 2 |
| `gasto == teto` | Sem alerta | Passou (CP-20) | JSON do Entregável 2 |

## 5. Preparação da medição com JaCoCo

O código original é Java simples, sem arquivo `pom.xml`; a preparação de Maven/JUnit/JaCoCo é etapa posterior, e **não deve alterar os resultados da linha de base já registrada**. Depois de configurar a suíte:

1. Fixar versão da aplicação em commit e nome das classes/métodos P1 da tabela.
2. Compilar, executar JUnit e gerar `jacoco.xml` e `index.html` do JaCoCo.
3. Identificar os ramos perdidos nos métodos P1 e escrever testes com resultados esperados válidos.
4. Vincular IDs de teste aos commits e relatórios; conferir que exclusões da ferramenta não mascaram P1.
5. Anexar ao GitHub as evidências e registrar percentuais **efetivamente medidos**.

**Métrica atual:** cobertura de linhas e decisões = **NÃO MEDIDA**. Não se deve marcar 0%, 85%, 90% ou 100% sem o relatório real.

## 6. Riscos de teste e próximos pontos a tratar

- **Prioridade P1:** validação de despesas finitas/positivas, validação de orçamentos finitos/não negativos, soma e alertas.
- **Riscos P2:** arquivos corrompidos, linhas inválidas, aspas e limites de índice.
- **Faltas conscientes de cobertura funcional na matriz atual:** entrada vazia de orçamento, orçamento não cadastrado consultado, categoria inexistente, arquivo malformado e alterações de mês por edição. Esses casos devem ser acrescentados antes da revisão final.
- **Rastreabilidade:** fonte em `src/Expense_Tracker/`, matriz no Entregável 2, resultados em `evidencias/entregavel-02/`, futura cobertura em artefato JaCoCo/CI.

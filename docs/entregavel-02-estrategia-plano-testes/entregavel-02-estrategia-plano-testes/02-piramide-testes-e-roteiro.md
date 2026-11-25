# Entregável 2 — Pirâmide de testes e roteiro de execução

## 1. Pirâmide proposta para o Expense Tracker

```text
                    /---------------------------\
                   / E2E CLI  (~10–15%)         \
                  / Entrada→menu→arquivo/saída   \
                 /-------------------------------\
                / Integração  (~20–25%)           \
               / Save/Load, orçamento, CSV         \
              /-------------------------------------\
             / Unitários  (~60–70%)                \
            / Regras de valor, soma, mês, limites    \
           /-----------------------------------------\
```

**Justificativa:** a lógica financeira requer vários testes rápidos que isolem decisões; persistência precisa de testes de integração com arquivos; a interface de terminal exige poucos percursos completos por ser mais lenta e frágil. A aplicação existente concentra regras privadas em `ExpenseTracker.java`; testes unitários poderão exigir refatoração controlada **posterior à linha de base**, preservando o comportamento e registrando o commit. **As porcentagens são metas orientativas da distribuição futura, não a estrutura atualmente medida.**

| Camada | Escopo | Exemplos | Ferramentas e situação |
|---|---|---|---|
| Unitário | Validar funções/regras sem arquivos reais | `amount` finito e positivo; soma mensal; total maior que limite | JUnit 5: **planejado** (Entregável 3) |
| Integração | Conectar regras e persistência | `ExpenseStorage.saveExpenses`→`loadExpenses`, `BudgetStorage`, CSV com aspas | JUnit e pasta temporária: **planejados**; verificação nativa `CsvUtilTest` já existe |
| Ponta a ponta | Simular usuário no menu, observar saída e dados gravados | adicionar, editar, resumo, orçamento, excluir, exportar | **30 cenários exploratórios executados** com Python (IA-assistidos) |

## 2. Preparação — roteiro reproduzível

**Pré-requisitos:** Java JDK 8+ (com `javac` e `java`); Python 3; sistema de arquivos com acesso a diretórios temporários. No diretório raiz `A3-QA`:

```bash
python3 tests/planejamento/entregavel-02/executar_caixa_preta.py \
  --src src/Expense_Tracker \
  --out evidencias/entregavel-02
```

O roteiro:

1. Compila os arquivos `.java` em um diretório temporário (não cria `.class` dentro de `src`).
2. Para cada caso, cria outra pasta temporária vazia, executa `java -cp ... Expense_Tracker.ExpenseTracker` e envia entradas ao terminal.
3. Compara as mensagens esperadas e/ou conteúdo de `expenses.txt`, `budgets.txt` e `expenses_export.csv`; registra o código de retorno.
4. Salva `resultado_30_casos_caixa_preta.json` com entradas, oráculos, saídas e SHA-256 das fontes, além de `relatorio_execucao_30_casos.md`.
5. Mantém o **código Java inalterado** e não guarda dados pessoais.

**Verificação nativa CSV (opcional, independente):**

```bash
cd src
javac Expense_Tracker/*.java
java Expense_Tracker.CsvUtilTest
```

> A execução do roteiro foi feita nesta preparação sobre os arquivos Java da cópia de trabalho enviada ao GitHub. A equipe deve repetir no próprio clone e anexar um novo log identificado pelo commit da execução.

## 3. Procedimento manual de execução de um caso

1. Identificar caso `CP-xx` e sua classe de equivalência ou fronteira na matriz.
2. Iniciar com `expenses.txt` e `budgets.txt` inexistentes em pasta isolada; documentar qualquer pré-condição especial.
3. Executar menus e entradas na sequência informada na especificação.
4. Comparar saída e arquivos com o oráculo **antes** de avaliar o resultado (evita ajustar a expectativa ao comportamento encontrado).
5. Registrar `PASSOU`, `FALHOU`, `BLOQUEADO` ou `NÃO EXECUTADO`, com data, commit e saída.
6. Se falhar: registrar ID de divergência, regra contestada, classificação de risco e encaminhamento; não modificar o sistema antes de preservar a evidência.

## 4. Critérios de divergência / relatório

- **PASSOU:** todas as condições de aceitação observáveis atendidas.
- **FALHOU:** pelo menos um oráculo não atendido (pode indicar falha ou requisito ainda não confirmado).
- **BLOQUEADO:** compilação/ambiente impedem execução.
- **NÃO EXECUTADO:** ainda não se tentou o cenário.

As regras RF-01 e RF-03 são oráculos propostos; a equipe deve registrar a concordância em ata. O teste não comprova desempenho de IA contra humanos.

## 5. Como reproduzir a evidência de cobertura no futuro

Depois de integrar JUnit e JaCoCo, executar a suíte Java e registrar `target/site/jacoco/index.html` e `jacoco.xml` ou artefato de CI; indicar commit, alvo de medição e percentual **de decisões e linhas nos métodos P1**. Nunca derivar cobertura de mera contagem de casos aprovados.

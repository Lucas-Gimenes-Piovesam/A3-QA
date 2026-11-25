# 3. Intervenção, versões e como reproduzir

## O que foi modificado e por quê

A equipe incorporou validações financeiras (rejeição de valores não finitos, valores de despesa não positivos e orçamento negativo), reforçou as rotas de entrada no terminal e as leituras da persistência. A suíte JUnit e o workflow GitHub Actions oferecem regressão automatizada.

| Mudança | Local | Evidência |
|---|---|---|
| Regras financeiras centrais | `src/Expense_Tracker/FinancialRules.java` | [Fonte](../../src/Expense_Tracker/FinancialRules.java) |
| Validação no construtor | `src/Expense_Tracker/Expense.java` | [Fonte](../../src/Expense_Tracker/Expense.java) |
| Validação das operações CLI | `src/Expense_Tracker/ExpenseTracker.java` | [Fonte](../../src/Expense_Tracker/ExpenseTracker.java) |
| Rejeição de registros persistidos inválidos | `ExpenseStorage.java`, `BudgetStorage.java` | [Pasta de fontes](../../src/Expense_Tracker/) |
| Testes de regressão | `tests/junit/Expense_Tracker/` | [Pasta JUnit](../../tests/junit/Expense_Tracker/) |
| Pipeline e Quality Gate | `.github/workflows/ci-quality-gate.yml` | [Workflow](../../.github/workflows/ci-quality-gate.yml) |

**Cautela temporal:** as melhorias foram introduzidas em diferentes commits. A comparação isolada baseline × versão final não atribui o efeito especificamente a uma única mudança, e a demonstração TDD histórica tem um commit GREEN vazio (ver Entregável 3).

## Versões tecnicamente controladas

- **Antes:** `v0.1.0-baseline` / `6b55f9d3f38012f1bcf1e05b272740bdb0ce8571`.
- **Depois, coleta local do pacote E10:** `f4abe2daf159a5a8fab36a5ecb856f64ff843716` (`main` após o Entregável 9).
- Todas as **seis** fontes da baseline e as **sete** da versão corrigida foram verificadas pelos respectivos *Git blob SHA-1* contra o GitHub do grupo na criação deste pacote. O JSON armazena os hashes e o script recalcula novos hashes a cada execução.
- Build de ambas as versões: `javac`, com diretórios compilados independentes; cada caso executado em uma pasta temporária isolada.

## Como reproduzir a comparação diretamente no repositório Git

Clonar o repositório localmente e abrir sua pasta. Verificar JDK e Python disponíveis; no terminal do projeto:

```bash
git fetch --tags
python3 scripts/experimento_10.py --repo . \
  --baseline-ref v0.1.0-baseline --after-ref main \
  --out evidencias/entregavel-10
```

O script usa `git show` sobre cada referência — sem modificar os arquivos da árvore de trabalho —, compila cada versão isolada e executa os **mesmos 10 cenários** em cada uma. Grava `resultado_comparativo.json` e `resultado_casos.csv` e imprime a contagem de sucessos. Em Windows com Python Launcher, usar `py -3 scripts/experimento_10.py` no lugar de `python3`.

**Reprodutibilidade com versão exata da fotografia:** no lugar de `--after-ref main`, use `--after-ref f4abe2daf159a5a8fab36a5ecb856f64ff843716`. A `main` muda com novos commits; o SHA não muda.

## Registros complementares de integração

O [GitHub Actions run 45528152960](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45528152960) passou com suíte JUnit, JaCoCo e Checkstyle. Esses resultados são **outras evidências**, não o mesmo protocolo dos dez cenários anteriores. Ao publicar o E10, a CI deve rodar novamente e seu link final deve ser acrescido ao relatório.

## Leitura dos arquivos de saída

- `resultado_comparativo.json`: compilação, hash de fonte, retorno, duração da **execução dos testes**, saídas relevantes, comparação.
- `resultado_casos.csv`: tabelinha antes/depois por cenário.
- `revisao_oraculos.csv`: ficha para validação humana, **não preenchida** neste pacote.
- `registro_comparacao_manual_ia.csv`: instrumento de medição de esforço e análise de teste humano × IA, **não preenchido**.

**Verificação:** código-fonte deve ter equivalência com as referências escolhidas; resultados de testes e comparativos devem ser publicados com commit e link de CI. Não chamar apenas screenshot de evidência suficiente.

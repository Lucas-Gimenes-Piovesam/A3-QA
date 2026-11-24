# A3 — Expense Tracker | Gestão e Qualidade de Software

Projeto acadêmico da disciplina **Gestão e Qualidade de Software (2026/2)**.

- **Caminho:** Sistema existente ou legado
- **Carta de inovação:** IA a serviço da qualidade
- **Sistema-base:** [Expense Tracker, por chaudhary-lakshay](https://github.com/chaudhary-lakshay/Expense-Tracker) (licença MIT)
- **Objetivo do A3:** investigar a eficácia de testes gerados com IA em comparação com testes manuais, considerando validação, defeitos detectados, cobertura de código e tempo.

## Origem e limitações

Os arquivos Java presentes em `src/Expense_Tracker` são uma **cópia de trabalho reconstruída a partir do repositório público**, utilizada na análise exploratória. Este pacote **não é um fork nem um clone oficial**; o commit exato da origem ainda precisa ser fixado e verificado antes da submissão final.

A documentação e os testes exploratórios iniciais estão disponíveis em `docs/` e `evidencias/`. Os números são medições do piloto local, **não** a comparação final entre IA e trabalho humano.

## Executar o programa

Requer JDK 8 ou posterior.

```bash
cd src
javac Expense_Tracker/*.java
java Expense_Tracker.ExpenseTracker
```

Executar verificação CSV nativa:

```bash
java Expense_Tracker.CsvUtilTest
```

## Organização

```text
src/Expense_Tracker/    código Java sob análise
tests/manuais/        reservado aos testes manuais do grupo
tests/ia/             reservado aos testes gerados por IA
docs/                 proposta acadêmica e relatórios
evidencias/           logs, JSON e scripts do estudo inicial
```

## Próximas entregas

1. Fixar commit do repositório original, confirmar igualdade dos arquivos e executar linha de base oficial.
2. Definir módulo e requisitos de teste; criar suíte manual independente.
3. Criar suíte JUnit gerada por IA e registrar prompts/alterações.
4. Adicionar Maven, JaCoCo e pipeline GitHub Actions para cobertura e quality gates.
5. Comparar os resultados e documentar limitações.

## Licença

O código-base mantém a [licença MIT](LICENSE) do autor original. As atividades acadêmicas adicionais do grupo devem respeitar a atribuição original.

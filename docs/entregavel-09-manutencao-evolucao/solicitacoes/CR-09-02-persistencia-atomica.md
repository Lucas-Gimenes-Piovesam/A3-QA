# CR-09-02 — Proteger a persistência contra gravações incompletas

**Tipo:** manutenção **preventiva** · **Prioridade:** P1 (integridade dos dados) · **Status:** **proposta, não implementada** · **Esforço relativo proposto:** 5 SP.

## Pedido e evidência

Hoje `ExpenseStorage.saveExpenses()` e `BudgetStorage.saveBudgets()` chamam `new FileWriter(FILENAME)` diretamente no destino. Abrir o arquivo para substituição pode truncar o conteúdo anterior antes de a gravação terminar; não há mecanismo explícito de troca atômica e o erro de `PrintWriter` pode precisar ser consultado por `checkError()`. Evidência: [`ExpenseStorage.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseStorage.java#L15-L24) e [`BudgetStorage.java`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/BudgetStorage.java#L49-L59).

**Risco a testar, não incidente já registrado:** falta de espaço, permissão ou interrupção na gravação pode resultar em arquivo parcial/antigo perdido.

## Resultado desejado

Gravar uma versão completa em arquivo temporário **no mesmo diretório/sistema de arquivos**; verificar erro de escrita, fechar o recurso, preservar cópia anterior e então trocar o destino com estratégia atômica onde suportada, definindo comportamento explícito quando `ATOMIC_MOVE` não estiver disponível. Devolver falha observável em vez de somente `System.out.println`, evitando prometer salvamento sem resultado confirmado. A solução exata depende das plataformas visadas.

## Impactos

- **Funcional:** médio — mensagem/retorno de erro de salvar e recuperação.
- **Dados:** **alto** — integridade e durabilidade; necessidade de teste de compatibilidade com arquivos existentes.
- **Arquitetura:** médio — concentrar persistência e estratégia de substituição.
- **Testes:** **alto** — injeção de falha, `@TempDir`, escrita interrompida e preservação do conteúdo anterior.
- **Usuário:** médio — avisos explícitos de falha de gravação.

## Aceitação e rollback

**AC1:** salvar N registros e recarregá-los intactos. **AC2:** falha simulada antes da troca não altera arquivo prévio. **AC3:** condição sem suporte a troca atômica segue política documentada (não degrada silenciosamente). **AC4:** testes de CSV com campos escapados continuam passando. **AC5:** desligamento normal da CLI relata corretamente sucesso/falha.

Rollback: reverter implementação por commit, restaurar backup/fixture de teste sem descartar dados; nunca simular falhas sobre arquivos pessoais.

# CR-09-03 — Validar datas dos registros carregados de arquivo

**Tipo:** manutenção **corretiva potencial** · **Prioridade:** P2 · **Status:** **proposta, requer reprodução e decisão de requisito** · **Esforço:** 3 SP.

## Evidência de risco

O menu usa [`LocalDate.parse`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseTracker.java#L323-L337), porém [`ExpenseStorage.loadExpenses()`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseStorage.java#L25-L49) constrói `Expense` com a data textual recebida do arquivo, sem validação equivalente. Já o método [`monthKey`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd/src/Expense_Tracker/ExpenseTracker.java#L308-L315) usa o prefixo de sete caracteres. Portanto, uma entrada como `2026-02-30,Teste,10.0,Food` é um **cenário de inspeção prioritário**, mas não afirmamos que foi reproduzido neste Entregável 9.

## Política proposta para o grupo validar

Data de despesa deverá ser ISO `YYYY-MM-DD` e corresponder a um dia real. Ao carregar registros fora do contrato, a aplicação deve informar erro e preservar uma cópia auditável das linhas rejeitadas; a política de quarentena, aviso e edição deve ser definida antes de implementar exclusões. **Não sobrescrever silenciosamente o arquivo de entrada no encerramento**, pois isso poderia perder registros rejeitados.

## Impactos

- **Funcional:** médio — somas por mês e confiabilidade da informação.
- **Dados:** médio/alto — arquivos históricos eventualmente inválidos exigem tratamento conservador.
- **Arquitetura:** baixo — extrair validador único e reutilizá-lo em CLI/armazenamento.
- **Testes:** alto — datas inexistentes, válidas, anos bissextos, fronteiras e carregamento.
- **Usuário:** médio — novos avisos sobre registros antigos.

## Critérios de aceite propostos

- **AC1:** data válida (inclusive 29/02 em ano bissexto) aceita.
- **AC2:** `2026-02-30`, formato incorreto e vazio não geram entradas tratadas como datas válidas.
- **AC3:** soma mensal não agrega registros de data inválida.
- **AC4:** preservar conteúdo bruto rejeitado ou exigir confirmação explícita de remoção; relatório mostra número de itens não importados.
- **AC5:** testes de CLI e de persistência anteriores continuam verdes.

**Rollback:** restaurar política antiga apenas com cuidado com dados aceitos/rejeitados; usar fixtures isoladas e registrar decisões na ata.

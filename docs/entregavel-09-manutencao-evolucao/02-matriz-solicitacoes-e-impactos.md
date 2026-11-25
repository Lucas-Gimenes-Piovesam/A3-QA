# 2. Matriz das solicitações de mudança e análise de impacto

**Base:** [`5bbc42c`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd). **Interpretação:** valores de impacto e SP são julgamentos iniciais de planejamento; não significam custo realizado.

| ID | Solicitação | Tipo de manutenção | Estado | Prioridade | F | D | A | T | U | Esforço |
|---|---|---|---|---|---|---|---|---|---|---:|
| CR-09-01 | Validar valores de despesas/orçamentos | Corretiva | Implementada antes do E9 | P1 | Alto | Alto | Baixo | Alto | Médio | —* |
| CR-09-02 | Persistência segura e detecção de erro de I/O | Preventiva | Proposta | P1 | Médio | Alto | Médio | Alto | Médio | 5 SP |
| CR-09-03 | Validar datas carregadas de arquivo | Corretiva potencial | Proposta | P2 | Médio | Médio | Baixo | Alto | Médio | 3 SP |
| CR-09-04 | Extrair lógica do menu e separar dependências | Perfectiva | Proposta | P2 | Baixo | Médio | Alto | Alto | Baixo | 8 SP |

*CR-09-01 já foi implementada, sem apontamento de esforço humano. Não se atribui horas/Story Points realizados retrospectivamente.

## Riscos específicos e mecanismos de mitigação

| ID | Risco de mudança | Mitigação / evidência exigida |
|---|---|---|
| CR-09-01 | Retornar aceitação de `NaN`/`Infinity` ou alterar política de orçamento zero | Preservar testes `ExpenseAmountTest`, `FinancialRulesTest` e `CliFinancialIntegrationTest`; CI verde |
| CR-09-02 | Corrupção/eliminação do arquivo existente por falha entre escrita e troca | Usar pasta temporária, testes com injeção de erro, backup controlado, mover com semântica atômica quando suportada; erro não pode ser silencioso |
| CR-09-03 | Descartar silenciosamente entradas antigas ou perder dados ao sair do programa | Definir política para linhas inválidas; nunca sobrescrever dados originais antes de registrar/colocar em quarentena entradas rejeitadas; testes com fixtures |
| CR-09-04 | Regressão em menu, ordem dos registros, formatos CSV, mensagens e relatórios | Introduzir camadas aos poucos, manter contrato CLI e testes de integração; medir cobertura e reexecutar scripts |

## Dependências e ordem sugerida

- **CR-09-01 é uma correção já executada** e serve de base de regressão.
- **CR-09-02** deve preceder mudanças que transformem arquivos persistidos, porque protege integridade antes de novas migrações.
- **CR-09-03** requer aprovação prévia da política para registros legados inválidos (rejeição, aviso ou quarentena).
- **CR-09-04** deve ocorrer em partes pequenas, de modo a não bloquear o experimento do Entregável 10.

### Impacto em documentação e métricas

Todas as CRs propostas exigem ligação com `docs/entregavel-02-estrategia-plano-testes/`, `tests/junit/`, `docs/entregavel-06-metricas-indicadores/` e o Quality Gate do E4. Novos testes de regressão devem aumentar detecção, **não somente inflar cobertura**. O progresso das ações pode alimentar `docs/entregavel-08-maturidade-melhoria-continua/04-roadmap-e-okrs-qualidade.md`.

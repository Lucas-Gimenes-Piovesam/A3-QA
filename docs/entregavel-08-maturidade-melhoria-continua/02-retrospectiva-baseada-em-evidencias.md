# 2. Retrospectiva documental — hipóteses para validação pelo grupo

> **ATENÇÃO:** este arquivo é uma retrospectiva **do histórico público do projeto**, redigida para subsidiar reunião real. **Não é uma ata de reunião** e não relata declarações de participantes nem consenso do grupo. A ata a preencher está em `03-roteiro-ata-retrospectiva.md`.

**Período inspecionado:** 24–25/11/2026 (UTC). **Foco:** progresso dos Entregáveis 1–7 e estabilização do processo de QA.

## O que funcionou (observado)

1. **CI foi de falha para sucesso:** cinco execuções iniciais reprovadas; depois houve **seis workflows consecutivos aprovados**. A [CI aprovada em PR](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713) executou 33 testes JUnit e gate financeiro; a [execução pós-merge do E7](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45526565474) passou.
2. **Revisão independente demonstrada:** os [PRs #1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1), [#2](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/2) e [#3](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/3) tiveram aprovações de um colaborador e foram incorporados à `main`.
3. **Configuração preservada:** branch `main` protegida, release [v0.1.0-baseline](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline) ligada ao commit inicial e histórico de merges.
4. **Prioridade nos riscos financeiros:** os nove métodos financeiros P1 foram medidos separadamente, sem apresentar cobertura local como global. [Run comprovante](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713).

## O que não funcionou tão bem (observado)

1. **Reorganizações repetidas de upload:** `docs/entregavel-02.../tests` e `docs/entregavel-02.../evidencias` não correspondem aos caminhos originalmente previstos para as pastas raiz. Isso pode quebrar links de reprodução. [Árvore atual E2](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/main/docs/entregavel-02-estrategia-plano-testes).
2. **Demonstração TDD incompleta:** o [commit GREEN `9fed22f`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/9fed22f954aa3c4cdcf42d7f868817a99218f6a5) não contém alterações, embora a suíte final funcione. Nomes dos commits não substituem diferença real e log JUnit para cada etapa.
3. **Lacunas documentais:** há um **modelo** de ata, não uma reunião validada; o arquivo de [horas reais](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/main/evidencias/entregavel-07/registro_horas_reais.csv) não demonstra esforço realizado. Não atribuir horas pelo intervalo entre commits.
4. **Métricas sem série estável:** o painel do E6 representa uma coleta com seis execuções de CI e o PR #1 ainda aberto. Em 25/11, após novos merges, a situação evoluiu para 11 runs (6 sucessos e 5 falhas) e 3 PRs integrados. O painel precisa ser atualizado antes da apresentação.
5. **Linha de base não idêntica byte a byte ao upstream:** a cópia de estudo foi reconstruída e ainda exige confirmação de proveniência e reprodução. [Documento da linha de base](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/main/docs/linha-base-e-piloto.md).

## Hipóteses de causa — a validar com o grupo (não são conclusões)

| Hipótese | Efeito possível | Pergunta de retrospectiva |
|---|---|---|
| Upload pelo navegador sem checklist de caminhos | Pastas aninhadas e retrabalho | Qual verificação pré-commit teria evitado as cópias? |
| Testes e código preparados em pacotes separados, mas enviados fora da ordem | Evidência RED–GREEN inconsistente | Como validar `git diff` e falha/sucesso em cada commit? |
| Priorizar publicação rápida antes de registrar a atividade | Horas/atas incompletas | Qual registro mínimo é sustentável a cada entrega? |
| Painéis derivados de uma coleta única | Métricas desatualizadas | Quem atualiza indicadores após cada merge? |

## Perguntas para a reunião (Start · Stop · Continue)

- **START:** quais duas práticas devem começar na próxima entrega? Sugestão: ata curta e checklist de PR.
- **STOP:** quais ações repetidas geraram retrabalho? Sugestão: upload sem conferir caminhos.
- **CONTINUE:** quais práticas já demonstraram valor? Sugestão: PR revisado e CI obrigatória.
- **Decisão de foco:** quais três ações têm maior impacto e são viáveis até 03/12?

## Saída esperada de uma retrospectiva de verdade

Um documento com data, participantes, observações confirmadas/rejeitadas, **ao menos três ações priorizadas** com donos e prazos e agenda de verificação. Registrar a ata em Git e anexar evidência (link de commit/PR). Até isso acontecer, o status é **reunião não comprovada**.

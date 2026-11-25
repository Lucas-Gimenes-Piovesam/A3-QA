# 2. Comparação — estimado versus realizado

## 2.1 Comparação quantitativa de escopo (não de horas)

| Entrega | Planejado (SP) | Escopo evidenciado (SP) | Pendente (SP) | Status resumido |
|---|---:|---:|---:|---|
| 1. SQA | 5 | 3 | 2 | Ata preenchida pendente |
| 2. Estratégia de testes | 8 | 6 | 2 | Reexecução e organização das evidências |
| 3. TDD, BDD e testes | 13 | 10 | 3 | Prova do ciclo TDD em commits pendente |
| 4. Pipeline e gate | 8 | 7 | 1 | Bloqueio por check reprovado sob regra já ativa a documentar |
| 5. Gestão de configuração | 5 | 5 | 0 | PR #1 mesclado, tag e release publicadas |
| 6. Métricas e indicadores | 5 | 5 | 0 | PR #2 mesclado, painel publicado |
| 7. Estimativa e planejamento | 3 | 0 | 3 | Pacote ainda não publicado no snapshot |
| 8. Maturidade e melhoria | 5 | 0 | 5 | Por realizar |
| 9. Manutenção e evolução | 5 | 0 | 5 | Por realizar |
| 10. Experimento IA | 13 | 0 | 13 | Comparação controlada ainda pendente |
| **Total** | **70** | **36** | **34** | **51,4% de escopo ponderado com evidência** |

**Fórmulas de cálculo:** `SP pendentes = SP estimados − SP evidenciados`; `Progresso de escopo = 36 / 70 × 100 = 51,4%`. Os pesos são estimativas gerenciais registradas após parte da execução e **não** dados observados do trabalho humano. Não interpretar `36 SP` como `36 horas`, nem `34 SP` como `34 horas restantes`.

A classificação preliminar foi feita com base na existência de artefatos e comportamentos do CI. A equipe deve revisar o mérito técnico de cada subtarefa antes de considerar os pontos formalmente aceitos. O detalhamento e as evidências estão no [CSV do backlog](../../evidencias/entregavel-07/backlog_subtarefas.csv).

## 2.2 Realizado efetivamente mensurado no GitHub

**Snapshot: 25/11/2026 UTC, HEAD `eb7aa5880513db359f335f86a6141b9f25be68e9`.**

| Indicador real | Resultado | Fonte | O que mede / não mede |
|---|---:|---|---|
| PRs integrados | **2** | [PR #1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1), [PR #2](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/2) | Entrega de alterações, não horas de trabalho |
| PR #1: criado até merge | **25 min 13 s** | `00:53:05Z → 01:18:18Z` | Tempo decorrido do fluxo de integração; inclui espera |
| PR #2: criado até merge | **2 min 44 s** | `01:20:14Z → 01:22:58Z` | Tempo decorrido do fluxo de integração; inclui espera |
| Commits da história de `main` | **31** | [Commits](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commits/main) | Eventos de versionamento, não atividades/hora |
| Execuções de CI | **9** | [GitHub Actions](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions) | Execuções técnicas na janela de instalação e uso inicial |
| CI com resultado `success` | **4/9** | Dados do snapshot | Aprovação da CI, não confiabilidade em produção |
| Última CI na `main` | **success** | [Run 45525331673](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45525331673) | Pipeline operacional, não esforço gasto |
| Horas de projeto por integrante | **Não medidas** | [Modelo para preenchimento](../../evidencias/entregavel-07/registro_horas_reais.csv) | Sem dados não existe comparação responsável de horas |

**Cuidado metodológico:** o relógio entre commits, PRs e aprovações conta inclusive pausas, espera de revisão, paralelismo e atividades externas. Não pode ser somado como tempo de trabalho individual. CI mede duração da máquina, não tempo humano.

## 2.3 Comparação de horas — lacuna explicitada

| Variável | Valor disponível | O que falta |
|---|---|---|
| Horas previstas por tarefa antes do trabalho | **Não registradas** | Registros de planejamento anteriores à execução, caso existam |
| Horas reais de execução | **Não registradas** | Relatos do grupo com início, término, pausas e atividade |
| Diferença `horas reais − horas previstas` | **Não calculável** | As duas bases acima |
| Desvio percentual em horas | **Não calculável** | Estimativa e apontamento válidos, com mesma unidade |

Se o grupo optar por acrescentar uma **estimativa de horas a partir de agora**, ela deve ter data, premissas, responsáveis e marcar explicitamente quais atividades já ocorreram. Não reclassificar estimativas tardias como se fossem anteriores ao desenvolvimento.

## 2.4 Interpretação e decisão

1. **Risco dominante:** o experimento de inovação E10 tem 13 SP e ainda não possui comparação controlada manual × IA; priorizar seu desenho e o registro de tempos de pessoas.
2. **Pendências antigas são reais:** publicar documentação não equivale a fechar todos os critérios; focar a ata do E1, a reexecução do E2 e a demonstração correta do TDD do E3.
3. **Fluxo técnico estabilizado:** PRs #1 e #2 foram integrados e a última CI da `main` está verde; manter proteção e cobertura, não converter isso em horas fictícias.
4. **Planejamento revisável:** o grupo deve ajustar SP quando houver mudança significativa de escopo e registrar o motivo, preservando a versão anterior para comparação legítima.

**Não declarar:** economia de 20% por IA, produtividade de X SP/hora, velocidade do grupo, índice de acurácia estimado/realizado em horas, conclusão de 51,4% do tempo total. Esses resultados não são sustentados pelos dados disponíveis.

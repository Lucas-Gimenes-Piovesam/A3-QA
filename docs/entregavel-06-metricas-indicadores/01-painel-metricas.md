# Entregável 6 — Painel de métricas e indicadores

**Projeto:** A3-QA / Expense Tracker  
**Referência de coleta:** 25/11/2026 (UTC), [repositório](https://github.com/Lucas-Gimenes-Piovesam/A3-QA)  
**Dados:** [`coleta-github-2026-11-25.json`](../../evidencias/entregavel-06/coleta-github-2026-11-25.json) · [`metricas-calculadas.csv`](../../evidencias/entregavel-06/metricas-calculadas.csv)  
**Estado:** fotografia histórica, **não** atualização em tempo real. Regerar após uma nova coleta.

## Quadro de leitura rápida

| Indicador | Valor verificado | Meta | Interpretação |
|---|---:|---:|---|
| Testes JUnit aprovados | **33/33** (100,0%) | 100% | Conforme para a suíte existente |
| Cobertura de linhas dos **9 métodos P1** | **145/145** (100,0%) | >= 85% | Conforme, não representa projeto inteiro |
| Cobertura de ramos dos **9 métodos P1** | **64/64** (100,0%) | >= 90% | Conforme, não prova ausência de defeitos |
| Análise estática | Checkstyle **success** | Sem violações bloqueadoras | Conforme apenas às regras configuradas |
| Casos de integração CLI | **9/9** aprovados | 100% dos definidos | Testes exercitam entrada e persistência |
| Execuções de CI aprovadas | **1/6** (16,7%) | >= 90% nas próximas 10 execuções | Atenção: configurou-se CI durante a janela |
| Tempo médio por workflow | **25.7 s** | <= 120 s | Adequado à execução curta observada |
| Tempo PR criado → aprovado | **20 min 1 s** | <= 24 h | 1 PR observado; amostra muito pequena |
| PR #1 | **Aprovado, ainda aberto** | PR aprovado e integrado com gate | Lead/cycle time de merge ainda não medidos |

**Escopo da cobertura:** os contadores do JaCoCo utilizados pelo gate são agregados **somente nos 9 métodos P1 definidos em `scripts/check_coverage.py`**. A medição de cobertura **global** do projeto não está declarada neste painel.

## Painel completo — todo indicador ligado a uma decisão

| ID | Indicador | Valor observado | Meta | Decisão apoiada |
|---|---|---|---|---|
| P01 | Testes JUnit aprovados | 100,0% | 100% | Aceitar mudanças somente com a suíte verde |
| P02 | Cobertura de linhas P1 | 100,0% | >= 85% | Exigir novos testes para lacunas em regras financeiras |
| P03 | Cobertura de ramos P1 | 100,0% | >= 90% | Cobrir decisões alternativas antes do merge |
| P04 | Checkstyle (regras configuradas) | Aprovado | Aprovado | Inspecionar e corrigir violações de estilo bloqueadoras |
| P05 | Cenários JUnit de CLI aprovados | 9/9 | 100% dos cenários definidos | Ampliar cenários de entrada e persistência caso haja regressão |
| R01 | Taxa de workflows aprovados | 16,7% | >= 90% em janela de 10 | Reduzir falhas recorrentes, sem baixar o gate |
| R02 | Duração média de workflows | 25,7 s | <= 120 s | Investigar lentidão caso a duração cresça |
| R03 | Tempo de abertura do PR até aprovação | 20 min 1 s | <= 24 h | Pedir revisão antecipada se o tempo ultrapassar a meta |
| R04 | Tempo de abertura do PR ao merge | Não medido | <= 24 h | Remover gargalos de revisão e integração |
| R05 | Tempo do primeiro commit da branch ao merge | Não medido | <= 48 h | Reduzir escopo e duração das branches |
| R06 | Revisão aprovada / PR integrado | Aprovado, ainda aberto | PR revisado + merge com gate verde | Concluir integração somente após requisitos cumpridos |
| D01 | Deployment frequency | Não aplicável / não medido | Só definir se houver deploy real | Não usar publicação de pre-release como deploy |
| D02 | Lead time for changes | Não aplicável / não medido | Só definir se houver produção | Medição requer commit e deployment de produção |
| D03 | Change failure rate | Não aplicável / não medido | Só definir se houver produção | Não confundir falha de pipeline com falha de deploy |
| D04 | Failed deployment recovery time | Não aplicável / não medido | Só definir se houver produção | Não confundir correção de CI com recuperação de serviço |

A classificação ISO/IEC 25010:2023 e a definição operacional de cada indicador estão no [dicionário](02-dicionario-metricas-e-metas.md).

## Evidências — histórico de CI

| Run | Evento | Resultado | Duração aproximada |
|---|---|---|---|
| [45519713000](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45519713000) | push | failure | 16 s |
| [45519906091](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45519906091) | push | failure | 23 s |
| [45520193389](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45520193389) | push | failure | 27 s |
| [45521164157](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45521164157) | push | failure | 34 s |
| [45521550391](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45521550391) | pull_request | failure | 24 s |
| [45522943713](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713) | pull_request | success | 30 s |

**Atenção:** a taxa de aprovação de 16,7% é uma métrica do **processo de configuração inicial**; não mede confiabilidade em produção. A última execução aprovada [#45522943713](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713) registrou 33 testes, Maven, JaCoCo e Checkstyle bem-sucedidos.

## Lead time, cycle time e DORA

- **Tempo até primeira revisão aprovada:** 20 min 1 s, contado entre a criação do PR #1 e a aprovação. É indicador de revisão, não *lead time for changes* do DORA.
- **Lead time interno do PR (abertura → merge):** Não medido. O PR estava aberto na coleta; não transformar tempo decorrido em lead time concluído.
- **Cycle time interno da branch (primeiro commit → merge):** Não medido; não medido, pois não houve merge no momento da coleta.
- **DORA:** não há deploy de produção demonstrado. Frequência de deploy, lead time de mudanças até produção, taxa de falha por mudança e tempo de recuperação não devem receber valores inventados. Uma pre-release (`v0.1.0-baseline`) não equivale a deployment.

## Próxima decisão orientada pelos dados

1. Confirmar integração do PR #1 após aprovação, atualização da branch e gate verde, registrando o SHA de merge.
2. Atualizar a coleta com `merged_at` real para calcular os indicadores internos de lead/cycle time.
3. Acompanhar as próximas 10 execuções de CI (meta >= 90% de sucesso); falhas do período inicial não devem ser apagadas do histórico.
4. Preservar os relatórios JaCoCo/Surefire da execução verde, incluindo a URL do run.
5. Medir outras características ISO 25010 apenas quando houver protocolo e evidência de teste apropriados.

**A nota metodológica e as limitações estão em:** [03-análise e decisões](03-analise-e-decisoes.md).

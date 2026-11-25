# Entregável 7 — Estimativa e planejamento de esforço

**Disciplina:** Gestão e Qualidade de Software — A3 (2026/2)  
**Caminho:** Sistema existente ou legado  
**Projeto:** A3-QA / Expense Tracker  
**Método escolhido dentre as opções do professor:** Story Points  
**Referência dos dados públicos:** repositório [A3-QA](https://github.com/Lucas-Gimenes-Piovesam/A3-QA), snapshot de 25/11/2026 UTC, após merge do PR #2.  
**Status:** pacote preparado; estimativas e critérios de verificação são **proposta de trabalho a validar pelo grupo**.

## 1. Atendimento ao enunciado

> Estimativa de esforço do próprio projeto (pontos de função, story points ou COCOMO básico) e comparação entre estimado e realizado.

O trabalho utiliza Story Points e compara **esforço relativo estimado** com **volume ponderado de trabalho verificavelmente entregue**. A comparação de **horas estimadas versus horas efetivas não é feita** porque o grupo ainda não forneceu registros individuais de tempo. Essa diferença conceitual é fundamental: Story Points *não são horas* e o número de commits ou o intervalo temporal entre commits *não equivale* a esforço humano.

## 2. Documentos do pacote

| Arquivo | Conteúdo |
|---|---|
| [01-metodo-story-points.md](01-metodo-story-points.md) | Escolha justificada do método, escala, critérios e detalhamento do backlog |
| [02-comparacao-estimado-realizado.md](02-comparacao-estimado-realizado.md) | Quadro de comparação, interpretação, métricas Git reais e lacunas |
| [03-planejamento-e-replanejamento.md](03-planejamento-e-replanejamento.md) | Dependências e ações para concluir as próximas etapas |
| [04-validade-evidencias-e-apresentacao.md](04-validade-evidencias-e-apresentacao.md) | Rastreabilidade, riscos metodológicos e roteiro da apresentação |
| [painel-escopo.html](painel-escopo.html) | Painel gráfico estático para demonstração visual, sem fingir horas registradas |

### Evidências e automação

- [`backlog_subtarefas.csv`](../../evidencias/entregavel-07/backlog_subtarefas.csv): 38 subtarefas com Story Points, status e link individual quando há evidência.
- [`comparativo_sp.csv`](../../evidencias/entregavel-07/comparativo_sp.csv): resultado por Entregável.
- [`resumo_planejamento.json`](../../evidencias/entregavel-07/resumo_planejamento.json): agregado calculado a partir do CSV.
- [`snapshot_github.json`](../../evidencias/entregavel-07/snapshot_github.json): PRs, commits, workflows, datas e URLs inspecionados.
- [`registro_horas_reais.csv`](../../evidencias/entregavel-07/registro_horas_reais.csv): planilha CSV **em branco**, para o grupo registrar tempo de trabalho efetivo (não tem valores inventados).
- [`atualizar_planejamento_07.py`](../../scripts/atualizar_planejamento_07.py): script que verifica consistência do backlog e recalcula o comparativo.

## 3. Resultado resumido

| Indicador | Valor | Significado |
|---|---:|---|
| Escopo estimado do A3 | **70 SP** | Estimativa retrospectiva para E1–E6 e prospectiva para E7–E10 |
| Escopo com evidência técnica verificada | **36 SP** | Soma dos subitens marcados `verificado` |
| Escopo com evidência pendente | **34 SP** | Subitens pendentes de publicação, validação ou execução |
| Fração ponderada com evidência | **51,4%** | `36 / 70 × 100`, **não** porcentagem de esforço gasto |
| PRs integrados observados | **2** | PR #1 e PR #2; evidências de avanço do projeto |
| Workflows registrados na coleta | **9** | Quatro resultados `success` e cinco `failure` |
| Horas efetivas de trabalho | **Não medidas** | Necessário preenchimento do registro pelo grupo |

**Leitura correta:** esta é uma **fotografia do escopo documentado e verificável**. O valor 36 SP é um crédito operacional preliminar, não um apontamento de horas gastas ou uma medição de produtividade. O grupo deve revisar e aprovar a pontuação atribuída.

## 4. Como atualizar sem inventar números

Na raiz do repositório, execute:

```bash
python3 scripts/atualizar_planejamento_07.py
```

Atualize os campos `status` e `url_evidencia` em `backlog_subtarefas.csv` somente depois de conferir a evidência. Execute o script novamente, revise os arquivos produzidos e registre as mudanças em um novo commit. Horas devem ser preenchidas por integrantes do grupo, com datas de início/fim e pausas realmente verificadas.

**Evidência principal do código e CI:** [workflow aprovado após os merges](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45525331673).  
**Rastreabilidade de integração:** [PR #1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1) e [PR #2](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/2).

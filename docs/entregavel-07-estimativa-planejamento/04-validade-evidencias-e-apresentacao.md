# 4. Evidências, validade da estimativa e roteiro de apresentação

## Fontes que podem ser auditadas

| Referência | O que comprova |
|---|---|
| [README na main](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/main/README.md) | Existência e apresentação do repositório do grupo |
| [PR #1 mesclado](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1) | Gestão de configuração, branch, aprovação e integração |
| [PR #2 mesclado](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/2) | Documentação do Entregável 6 integrada |
| [Workflow 45525331673](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45525331673) | Último gate verde da main no snapshot |
| [Release baseline](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline) | Versionamento da linha inicial |
| [Documentação TDD](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/blob/main/docs/entregavel-03-testes-ageis-automatizados/01-tdd-red-green-refactor.md) | Documentação do experimento e limitações do histórico de commits |
| [Backlog detalhado](../../evidencias/entregavel-07/backlog_subtarefas.csv) | Metodologia, pontuação de cada subtarefa e avaliação preliminar |

O snapshot em JSON contém os identificadores usados e as datas UTC relevantes para reconsulta. As fontes do GitHub foram consultadas em 25/11/2026. Os resultados podem mudar depois de novos merges; não tratar o snapshot como dado dinâmico.

## Limitações e ameaças à validade

1. **Viés retrospectivo:** não existe uma estimativa preservada antes do desenvolvimento de E1–E6. Os pesos atuais são úteis como reconstrução de escopo, mas não como validação da capacidade preditiva do grupo.
2. **Crédito por evidência:** a pontuação realizada representa **subitens com documentação verificável**, não uma medição de horas, qualidade integral ou desempenho individual. Um item pode passar pela automação e ainda exigir julgamento humano.
3. **Diferença entre documentado e aceito:** os itens chamados `verificado` podem exigir validação formal de integrantes e docente; os estados não pretendem substituir uma ata.
4. **Tempo de máquina ≠ esforço humano:** duração do workflow, PR ou commits não é uma estimativa legítima do tempo despendido pelas pessoas.
5. **Amostra pequena:** duas integrações de PR e nove execuções de CI são suficientes para demonstrar fluxo, mas insuficientes para estimar velocidade sustentável do grupo.
6. **Cobertura ≠ eficiência:** 100% de cobertura de linhas e ramos dos métodos P1 monitorados não equivale a 100% de requisitos ou à economia de esforço prevista na carta de inovação.
7. **Mudanças de escopo:** se o backlog for modificado sem guardar histórico, a comparação entre planejado e realizado perde rastreabilidade. Versionar cada alteração.

## Como apresentar em aula (roteiro de 90 segundos)

> Escolhemos Story Points por ser um projeto de intervenção em código legado, envolvendo testes, documentação, integração e auditoria. Usamos uma escala relativa de 1, 2, 3, 5, 8 e 13 pontos. Detalhamos 70 pontos de escopo, dos quais 36 já possuem evidências técnicas verificáveis na fotografia do repositório de 25 de novembro. Isso significa 51,4% do escopo ponderado demonstrado, e não 51,4% do tempo gasto. O GitHub comprova os PRs #1 e #2 integrados e o pipeline funcionando. Não tínhamos registros individuais de horas nem uma estimativa anterior para as primeiras tarefas, então deixamos esses campos como não medidos em vez de produzir um falso desvio de esforço. Para as próximas entregas, manteremos o planejamento versionado e registraremos as horas efetivas.

## Melhoria de qualidade proposta

A partir de E7, o grupo deve combinar a pontuação antes do início de cada atividade, apontar o tempo de trabalho, usar PRs curtos e atualizar o quadro quando as evidências forem aceitas. Isso transforma o planejamento retrospectivo atual em uma base progressivamente **prospectiva e verificável** para E8–E10.

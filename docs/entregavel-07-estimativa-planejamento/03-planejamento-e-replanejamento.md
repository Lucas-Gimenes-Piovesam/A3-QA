# 3. Planejamento das próximas atividades e replanejamento

## Ordem recomendada e dependências

| Ordem | Frente | SP pendentes no snapshot | Dependência / critério de conclusão | Responsável |
|---:|---|---:|---|---|
| 1 | **E7** — publicar e validar esta estimativa | 3 | Realizar commit/PR, aprovar pesos de Story Points e iniciar registro de horas | A definir pelo grupo |
| 2 | **E1** — registro real de revisão SQA | 2 | Realizar peer review, preencher ata com observações e decisão | A definir |
| 3 | **E2** — execução e organização da estratégia | 2 | Corrigir caminhos, executar script e anexar relatório referente ao código certo | A definir |
| 4 | **E3** — TDD com commits efetivos | 3 | Branch isolada, teste falhando de fato antes da correção, GREEN com diff, REFACTOR mantendo verde | A definir |
| 5 | **E4** — evidência de gate bloqueando merge | 1 | PR de demonstração com status obrigatório efetivamente falhando; não forçar bypass | A definir |
| 6 | **E8** — maturidade e melhoria contínua | 5 | Diagnóstico CMMI/MPS.BR, retrospectiva real, OKRs e roadmap | A definir |
| 7 | **E9** — manutenção e evolução | 5 | Três solicitações de mudança, impacto e decisão refatorar/modernizar/substituir | A definir |
| 8 | **E10** — experimento controlado IA × manual | 13 | Mesmos requisitos, grupos/conjuntos independentes, medição de tempos e defeitos, conclusão com limitações | A definir |
| **Total** | | **34** | | |

**Observação:** a ordem não é um cronograma de horas ou datas; pode haver execução paralela. Ela informa prioridades e dependências de qualidade. O experimento E10 exige planejamento **desde já**, mesmo que sua análise final apareça por último; não deixar coleta de tempos para depois.

## Como registrar esforço humano de modo responsável

O CSV `evidencias/entregavel-07/registro_horas_reais.csv` tem colunas `data_utc`, `integrante`, `entrega`, `atividade`, `inicio_local`, `fim_local`, `pausas_minutos`, `tempo_efetivo_minutos`, `referencia_evidencia` e `observacoes`. Ele foi deixado **sem linhas de dados** porque nenhum registro de horas foi informado. Cada integrante deve inserir suas atividades realizadas, descontar pausas e verificar se não houve dupla contagem em atividades simultâneas.

Depois, se existirem estimativas de horas registradas **antes** da execução da tarefa, será possível calcular:

`desvio_horas = horas_reais − horas_estimadas`

`desvio_percentual = 100 × (horas_reais − horas_estimadas) / horas_estimadas`

com `horas_estimadas > 0`. Não usar Story Points na fórmula de horas.

## Critérios de aceite do Entregável 7

- [x] Método Story Points escolhido e justificado.
- [x] Backlog com estimativas relativas para as dez entregas.
- [x] Comparação numérica de pontos previstos x escopo comprovado, por entrega.
- [x] Dados reais de Git/CI separados das estimativas relativas.
- [x] Registro de limitações e de ausência de apontamentos de horas.
- [ ] Aprovação da escala, pesos e estados pelo grupo.
- [ ] Publicação deste pacote em PR revisado e merge com CI verde.
- [ ] Se o professor exigir desvio em horas: registros reais de estimativa temporal anterior e trabalho efetivo, ambos verificáveis.

## Ritual de atualização

Ao fechar cada subtarefa, anexar URL e marcar `verificado` no CSV, atualizar arquivos gerados com `python3 scripts/atualizar_planejamento_07.py`, criar commit específico e solicitar revisão. Se um requisito mudar, manter o histórico da versão anterior do backlog e justificar o replanejamento na descrição do PR.

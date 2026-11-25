# 1. Método de estimativa — Story Points

## Escolha do método

O enunciado permite **pontos de função, Story Points ou COCOMO básico**. Optamos pelos **Story Points** porque o trabalho é uma intervenção de qualidade em um pequeno sistema legado, com atividades heterogêneas: investigação, documentação, criação de testes, CI, revisão e análise experimental. Estimar cada etapa pelo tamanho funcional de uma implementação nova (pontos de função) ou LOC previstas (COCOMO) seria pouco representativo da carga de auditoria, integração e experimentação.

Story Points são uma avaliação **relativa** de complexidade, esforço comparativo, incerteza e risco. Não devem ser convertidos automaticamente em minutos/hora nem usados para comparar o desempenho individual dos integrantes.

## Escala acordável e critérios

Escala de Fibonacci simplificada `1, 2, 3, 5, 8, 13`. Cada entrega foi subdividida em atividades menores de **1 a 5 pontos**, facilitando documentar a conclusão parcial. A pontuação de cada entrega é a soma de suas atividades.

| Pontos por subtarefa | Critério proposto | Exemplo do A3 |
|---:|---|---|
| 1 | Simples, escopo delimitado, risco baixo | Publicar checklist, documentação de branch |
| 2 | Exige especificar e revisar um artefato relevante | Plano IEEE 829, análise de impacto |
| 3 | Integra múltiplas regras ou apresenta risco de configuração | Testes financeiros, workflow CI, validação de experimento |
| 5 | Implementação com maior complexidade/integração | Suíte JUnit executável e rastreável |

**Estimativa e ordem temporal:** a pontuação dos Entregáveis **1–6** foi proposta em **25/11/2026, depois de seu desenvolvimento**. É uma estimativa **retrospectiva**, sujeita ao viés do conhecimento prévio; **não** constitui prova de previsão inicial acertada. Para **E7–E10**, serve como plano prospectivo a validar antes da execução. Uma estimativa anterior, imutável e datada não consta da documentação revisada.

## Backlog de referência

| Entregável | Escopo resumido | Pontos estimados | Situação no snapshot |
|---|---|---:|---|
| E1 | Plano de qualidade e SQA | 5 | Documento e auditoria; ata real pendente |
| E2 | Estratégia e plano de testes | 8 | Plano e matrizes; caminhos e execução a revalidar |
| E3 | Testes ágeis e automatizados | 13 | Suíte JUnit e BDD; ciclo TDD em commits tem lacuna |
| E4 | CI e Quality Gate | 8 | Workflow verde e status requerido; prova específica de bloqueio por CI pendente |
| E5 | Gestão de configuração | 5 | PR #1 integrado, tag/release e README |
| E6 | Métricas de produto e processo | 5 | PR #2 integrado e painel documentado |
| E7 | Estimativa e planejamento | 3 | Pacote preparado localmente; será contado após publicação e aferição |
| E8 | Maturidade e melhoria contínua | 5 | A desenvolver |
| E9 | Manutenção e evolução | 5 | A desenvolver |
| E10 | Experimento de inovação | 13 | Piloto existe; experimento pareado ainda não executado |
| **Total** | | **70** | |

### Por que 13 SP em E3 e E10?

- **E3:** exige criar testes automáticos, produzir Gherkin, exercitar caminho RED→GREEN→REFACTOR, gerar um histórico correto e integrar código legado a Maven/JUnit. O histórico atual apresenta uma lacuna: o commit rotulado GREEN da segunda sequência está vazio; por isso, a exigência do professor ainda não foi plenamente demonstrada.
- **E10:** concentra o risco científico do projeto: controlar o mesmo escopo, definir oráculos, produzir conjuntos humano e IA independentes, medir tempos válidos, coberturas e defeitos e distinguir erros da ferramenta de falhas reais do software. É mais trabalhoso do que simplesmente contar testes.

### Critério operacional de evidência

Cada subtarefa tem `status = verificado` ou `pendente`. **Verificado** exige link concreto para documentação, PR, commit ou execução que demonstra o subitem. **Pendente** não equivale a 0 horas trabalhadas: apenas faltam comprovação ou aceitação. O script soma os pontos das subtarefas verificadas para avaliar **escopo evidenciado**, não esforço consumido.

A aprovação formal dos pesos, o trabalho individual e os valores em horas devem ser registrados pelo grupo. Não atribuí horas ou nomes de integrantes que não foram informados.

**Fonte detalhada:** [`backlog_subtarefas.csv`](../../evidencias/entregavel-07/backlog_subtarefas.csv).

# 4. Resultados medidos e análise da hipótese

## 4.1 Resultado principal — dez testes iguais em duas revisões

A comparação foi reexecutada localmente com `scripts/experimento_10.py` em 25/11/2026. Foram utilizadas cópias com conteúdo idêntico, verificado por *Git blob SHA-1*, à tag `v0.1.0-baseline` e à revisão `f4abe2daf159a5a8fab36a5ecb856f64ff843716` do repositório do grupo. Foi mantido o protocolo de dez cenários do piloto de IA já existente. Isso compara **resultados do software**, não tempo de geração dos testes.

| Indicador | Antes | Depois | Diferença |
|---|---:|---:|---:|
| Casos executados | 10 | 10 | 0 |
| Casos com oráculo atendido | **6** | **10** | **+4 casos** |
| Taxa de conformidade do conjunto | **60%** | **100%** | **+40 pontos percentuais** |
| Casos divergentes | 4 | 0 | **−4** |
| Regressões nos casos previamente conformes | — | **0** | — |

| ID | Regra / caso | Baseline | Versão corrigida | Efeito |
|---|---|---|---|---|
| IA-01 | Despesa positiva | Conforme | Conforme | Mantido |
| IA-02 | Despesa zero rejeitada | Conforme | Conforme | Mantido |
| IA-03 | Despesa negativa rejeitada | Conforme | Conforme | Mantido |
| IA-04 | Despesa não numérica rejeitada | Conforme | Conforme | Mantido |
| **IA-05** | Despesa `NaN` deve ser rejeitada | **Divergência** | Conforme | **Corrigido** |
| **IA-06** | Despesa `Infinity` deve ser rejeitada | **Divergência** | Conforme | **Corrigido** |
| **IA-07** | Orçamento `NaN` deve ser rejeitado | **Divergência** | Conforme | **Corrigido** |
| **IA-08** | Orçamento negativo deve ser rejeitado | **Divergência** | Conforme | **Corrigido** |
| IA-09 | Alerta acima do orçamento | Conforme | Conforme | Mantido |
| IA-10 | Soma mensal correta | Conforme | Conforme | Mantido |

Os quatro casos corretivos fornecem evidência de que o conjunto sugerido por IA **identificou situações não cobertas pelos testes CSV originais**. Porém, a cobertura funcional do piloto não foi testada contra um catálogo completo de defeitos conhecidos. A hipótese de produtividade de IA **não é aferida** com esta tabela.

## 4.2 Como ler o resultado sem exagero

- **Sucesso de execução do caso**: os oráculos de entrada e saída do script foram atendidos; **não** representa precisão intrínseca de todas as sugestões da IA.
- **Divergência do programa**: uma versão não satisfez o oráculo proposto; **não** é automaticamente um erro ou alucinação do gerador de testes.
- **IA-08 depende de requisito aceito**: orçamento não negativo é uma **decisão de domínio do grupo**; o software original não tinha especificação formal impondo essa regra.
- **Tempos** contidos no JSON foram medidos com cronômetro do Python para a compilação e execução do caso. São **tempos de máquina**, não o tempo necessário para pessoa ou IA elaborar e revisar os testes; não compará-los com a hipótese de 20%.
- **Causalidade limitada**: o sistema evoluiu em múltiplos commits. Os testes revelaram desvios antes e demonstram conformidade depois, mas não isolam o impacto exclusivo de uma ferramenta de IA em comparação com desenvolvimento tradicional.

## 4.3 Dados sobre acertos, erros e alucinações da IA

| Aspecto da carta | Medido e sustentado | Ainda não medido |
|---|---|---|
| Casos fornecidos pelo assistente | **10 casos** documentados e executáveis | — |
| Casos que evidenciaram divergência na baseline | **4 casos** (IA-05…IA-08), sob regras propostas | Aprovação independente das regras/oráculos |
| Casos preservados conformes após correção | **6 casos** | — |
| Erros do gerador de testes | **Sem classificação humana independente** | Quantidade/taxa de erro da IA |
| Alucinações da IA | **Sem classificação humana independente** | Quantidade/taxa e exemplos confirmados |
| Tempo para escrever + revisar + executar suíte IA | **Não medido** | Minutos efetivos |
| Tempo equivalente de teste manual independente | **Não medido** | Minutos efetivos |
| Economia de ≥20% pela IA | **Inconclusiva** | Experimento pareado com mensuração humana |

**Por que não classificar falhas da baseline como "erros da IA"?** Os quatro oráculos *não* estavam satisfeitos pelo software. A falha que o teste revela pode ser útil para a qualidade; se o oráculo for validado, é uma divergência de implementação. Se o oráculo não for aceito, a falha pode apontar para uma premissa inválida do próprio teste. São questões distintas e devem ser revisadas por pessoa independente.

## 4.4 Evidência externa do mesmo programa após intervenção

Na suíte JUnit integrada ao GitHub Actions, a CI registrou **33/33 testes aprovados** e 100% de linhas/decisões **apenas nos nove métodos P1 selecionados** no run [`45522943713`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713), com resultados posteriores de CI verde em PRs de documentação. A comparação do subexperimento aqui permanece a dos **dez casos IA-01 a IA-10**. Não converter 33 testes JUnit em "33 testes gerados pela IA" nem comparar quantidade com 4 verificações CSV de escopo diferente como efeito percentual.

## 4.5 Decisão provisória

**Confirmado, no escopo de dez casos:** a versão corrigida apresenta conformidade superior à baseline, sem regressões observadas nesse conjunto. **Não confirmado:** que IA supere testes manuais em velocidade, precisão, detecção de falhas ou custo. A validação dos oráculos e a coleta de esforços humanos são as próximas ações necessárias.

**Dados reproduzíveis:** [`resultado_comparativo.json`](../../evidencias/entregavel-10/resultado_comparativo.json) e [`resultado_casos.csv`](../../evidencias/entregavel-10/resultado_casos.csv).

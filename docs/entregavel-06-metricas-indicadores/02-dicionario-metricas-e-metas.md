# Dicionário de métricas, metas e decisões

## 1. Critérios de seleção (ISO/IEC 25010:2023)

O Plano de Qualidade e SQA do grupo prioriza **adequação funcional**, **confiabilidade** e **manutenibilidade**; trata **capacidade de interação** como média prioridade. As métricas abaixo são **proxies operacionais** relacionadas a essas características, e não a medição completa ou certificação conforme a norma.

| ID | Característica / dimensão | Cálculo e regra de contagem | Meta própria e justificativa | Decisão apoiada |
|---|---|---|---|---|
| P01 | Adequação funcional / regressão | (Testes JUnit sem falha, erro ou skip) / total executado × 100; relatório Surefire | **100%**: não incorporar comportamento contrário aos oráculos implementados | Falha → corrigir implementação, teste ou requisito e repetir CI |
| P02 | Adequação funcional / testabilidade | JaCoCo: `LINE.covered / (covered + missed)` somado apenas nos **9 métodos P1** | **≥85%**: concentrar atenção em rotas de maior risco, sem custo de exigir todas as classes | Abaixo do limite → ampliar cobertura relevante antes do merge |
| P03 | Adequação funcional / testabilidade | JaCoCo: `BRANCH.covered / (covered + missed)` só nesses métodos | **≥90%**: priorizar condições que mudam validações e resultados financeiros | Abaixo → testar ramos negativos, nulos e limítrofes |
| P04 | Manutenibilidade | Status do Checkstyle configurado no `mvn verify`; não confundir com auditoria integral de código | **Sem violações bloqueadoras** nas regras adotadas | Falha → revisar código e limpar violações reais |
| P05 | Capacidade de interação / adequação funcional | Testes de integração `CliFinancialIntegrationTest` aprovados no Surefire (9 na coleta) | **100% dos cenários definidos**: erros de entrada no console não devem passar despercebidos | Falhas → melhorar mensagens, estados e persistência |
| R01 | Processo CI | Workflows GitHub Actions `conclusion=success` / total com resultado final × 100 | **≥90% nas próximas 10 execuções**: estabilidade após a implantação inicial | Abaixo → mapear causas de falhas e retrabalho, nunca baixar o gate para maquiar taxa |
| R02 | Processo CI | Média de `updated_at − created_at` das execuções completas; unidade segundos | **≤120 s**: o projeto Java CLI é pequeno e deve fornecer feedback rápido | Crescimento → diagnosticar dependências, cache e duração dos testes |
| R03 | Processo / revisão por pares | `submitted_at` da primeira revisão `APPROVED` − `created_at` do PR | **≤24h**: permite trabalhar em ciclos curtos entre integrantes | Atraso → designar revisor antecipadamente |
| R04 | Processo / lead time interno do PR | `merged_at − created_at` do PR **após merge real** | **≤24h** por PR documental ou mudança pequena; alvo inicial de equipe | Atraso → investigar espera de CI, revisão ou atualização da branch |
| R05 | Processo / cycle time interno | `merged_at − data do primeiro commit da branch` após merge real | **≤48h** para mudanças pequenas; reduz acúmulo na branch | Atraso → cortar escopo, dividir PRs e revisar com mais frequência |
| R06 | Processo / gestão de configuração | Verificar PR real, revisão, CI e merge com regra protegida | PR revisto e integrado somente depois de checks obrigatórios | Sem merge → corrigir bloqueio; sem revisão → solicitar colaboração |

**Metas propostas para R01, R02, R03, R04 e R05:** metas do grupo para monitoramento e decisão, não resultados já atingidos em uma série histórica estável. A amostra atual contém apenas seis workflows e um PR.

## 2. DORA — definição correta e limitação neste produto

O DORA associa desempenho de entrega e estabilidade a mudanças **implantadas em produção**. O Expense Tracker do A3 é uma aplicação Java de terminal, sem ambiente de produção ou deploy validado neste trabalho. Publicar um `.jar`, rodar um build ou publicar uma *pre-release* **não comprova implantação**.

| Métrica DORA | Definição operacional | Por que não é mensurável hoje | O que seria necessário para medir |
|---|---|---|---|
| Deployment frequency | Frequência de deployments concluídos em ambiente de uso real | Nenhum deployment real foi demonstrado | Definir ambiente real e registrar eventos/versões implantadas |
| Lead time for changes | Tempo da alteração de código até sua entrada efetiva em produção | Não há evento de produção para delimitar o fim | Relacionar commit à data de deployment em produção |
| Change failure rate | Proporção de deployments que geram falha exigindo correção/intervenção | Não há base de deployments nem incidentes pós-deploy | Registrar incidentes por deployment e classificá-los |
| Failed deployment recovery time (ou MTTR de restauração, na formulação clássica) | Tempo para recuperar o serviço após falha causada por deployment | Não foi observado ambiente operacional nem incidente | Logs de início de incidente e restauração verificada |

**Não converter:** (5 falhas de CI / 6 runs) **não é** change failure rate do DORA; duração de workflow **não é** lead time for changes; tempo para deixar CI verde **não é** recovery time de produção.

Para o A3, os indicadores substitutos **internos** R03–R05 são úteis e reportados à parte, sem rotulá-los como dados DORA de produção.

## 3. Origem, periodicidade e responsabilidades

| Evidência | Consulta / artefato | Quando coletar | Responsável proposto |
|---|---|---|---|
| JUnit | `mvn verify`, `target/surefire-reports/`, GitHub Actions | A cada PR e release | Integrante que alterou o código |
| JaCoCo | `target/site/jacoco/jacoco.xml`, `scripts/check_coverage.py` | A cada PR | Responsável pela CI |
| Checkstyle | `target/checkstyle-result.xml`, status do workflow | A cada PR | Revisor de código |
| R01 e R02 | GitHub Actions: lista dos runs e data/hora | Toda semana ou a cada 10 runs | Responsável pelo painel |
| R03, R04, R05 | GitHub PR, revisões, commits, data de merge | Após conclusão de cada PR | Responsável por gestão de configuração |
| DORA | Sistema de implantação e incidentes (caso exista futuramente) | Só depois de implantar de fato | Responsável pela operação |

## 4. Exceções, interpretação e lacunas

1. **Valores ausentes não são zero.** Quando a fórmula depende de `merged_at` ou deploy inexistente, retornar "Não medido".
2. **Cobertura de código não é cobertura de requisitos.** Complementar JaCoCo com matriz de casos dos Entregáveis 2 e 3.
3. **Taxa de aprovação da CI na fase inicial é enviesada para baixo.** Foi um período de implantação/correções, não a cadência operacional madura.
4. **Resultados 100% dependem do escopo.** Nove métodos P1, 33 testes JUnit; não afirmar 100% de segurança, desempenho ou confiabilidade global.
5. **Evidência reproduzível sempre.** Fonte primária: run do GitHub, PR, revisão, tag, commit; cópia em JSON e CSV para auditoria do projeto.

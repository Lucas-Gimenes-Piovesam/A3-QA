# Análise crítica, decisões de qualidade e limites do experimento

## 1. Questão de qualidade

O Expense Tracker gerencia valores financeiros. Um erro na entrada de uma despesa ou no orçamento pode produzir somas inválidas, alertas incorretos ou persistência de dados inapropriados. Por isso, o Painel do Entregável 6 enfatiza correção financeira (P1), verificações de integração e evolução do processo de CI, em conformidade com o Plano de Qualidade do Entregável 1.

A escolha do professor pede **métricas de produto e processo, com meta e decisão**. Este documento interpreta, não apenas enumera, os indicadores.

## 2. Resultado atual, interpretado com cautela

| Evidência verificada | Interpretação defensável | Não podemos concluir |
|---|---|---|
| 33 testes JUnit aprovados no workflow #45522943713 | A suíte configurada cumpriu os oráculos que exercita nessa versão do código | Que todo requisito ou condição de produção foi testado |
| 145/145 linhas e 64/64 ramos nos nove métodos P1 | O JaCoCo registrou execução de todos os contadores definidos pelo gate nesses métodos | Cobertura de 100% de todo o projeto; ausência de bugs |
| Checkstyle passou no `mvn verify` | Não houve violações bloqueadoras nas regras de análise estática configuradas | Ausência de todas as vulnerabilidades e problemas arquiteturais |
| 1 aprovação em 6 workflows | O pipeline estabilizou após falhas de configuração; a última execução foi verde | Confiabilidade de apenas 16,7% do produto em produção |
| PR #1 aprovado pelo colaborador `EduardoJuvenasso` | Uma revisão por pares ocorreu de fato | Que ele já foi integrado ao `main` (estava aberto no snapshot) |
| Uma release `v0.1.0-baseline` | Existe versão rastreável do estado inicial | Que houve implantação contínua em produção |

## 3. Decisões orientadas pelos indicadores

**D1 — Gate verde como condição de integração.** Manter os limites de ≥85% linhas e ≥90% ramos P1 e 100% de JUnit; o PR com pipeline falhando deve continuar bloqueado. **Responsável proposto:** revisor do PR.

**D2 — Acompanhar tendência do processo, não só a última execução.** Coletar as próximas dez execuções: meta ≥90% de sucesso; se houver falha, classificá-la em compilação, teste, cobertura, análise estática ou infraestrutura. **Responsável proposto:** responsável pela CI.

**D3 — Finalizar PR somente após aprovação e sincronização.** Uma aprovação existe; no snapshot, o PR ainda estava aberto. Após o merge, registrar SHA, `merged_at`, lead time e cycle time. **Responsável proposto:** mantenedor do repositório.

**D4 — Ampliar cobertura sem confundir cobertura com qualidade.** Revisar os testes que alcançam os caminhos e associá-los a requisitos e resultados esperados, inclusive persistência. Os 100% atuais são do escopo P1, não justificam relaxar a análise funcional. **Responsável proposto:** responsável pelos testes.

**D5 — Não inventar DORA para um produto sem deploy.** Se for criada distribuição operacional do software, especificar o que conta como instalação/deployment, registrar versões e incidentes, e somente depois publicar métricas de produção. **Responsável proposto:** grupo.

## 4. Linha de base e validade da comparação

Em `docs/linha-base-e-piloto.md`, o grupo documentou o piloto da cópia reconstruída do software: quatro verificações CSV nativas e dez cenários exploratórios com IA (seis aprovações e quatro divergências sob regras propostas). Esses cenários tinham **escopo e oráculos diferentes** da suíte JUnit de 33 testes. A cobertura JaCoCo **não foi medida na linha de base**.

Portanto, o painel atual não apresenta comparação direta de 4→33 testes como ganho porcentual de qualidade, nem melhora de cobertura de 0→100%. A primeira medida de cobertura rigorosa disponível é a do workflow atual. A comparação *manual × IA* prevista pela carta de inovação ainda depende de conjuntos pareados e tempos de trabalho coletados separadamente.

## 5. Advertência sobre o histórico do TDD

No Entregável 3 houve commits chamados RED, GREEN e REFACTOR, mas em uma das sequências publicadas o commit GREEN não registrou diferenças; parte da correção constou de outro commit. A suíte final é executável e a CI passou, mas **o nome dos commits não prova, por si só, o ciclo TDD**. Recomenda-se demonstrar o ciclo com histórico técnico verificável antes da entrega final.

## 6. Referências auditáveis

- [Workflow aprovado, 33 testes e 100% dos contadores P1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713)
- [PR #1, aprovações e status de integração](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1)
- [Release `v0.1.0-baseline`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline)
- [Plano de Qualidade do grupo](../entregavel-01-plano-qualidade/01-plano-qualidade-sqa.md)
- [Linha de base e piloto](../linha-base-e-piloto.md)
- [Gerador e dados de coleta](../../scripts/gerar_metricas_06.py)

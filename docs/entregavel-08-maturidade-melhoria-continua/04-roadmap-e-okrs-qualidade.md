# 4. Roadmap de melhoria contínua com OKRs de qualidade

**Horizonte proposto:** 25/11 a 03/12/2026. **Status:** planejamento elaborado para discussão do grupo; não é compromisso formal já aprovado. Prazos relativos à apresentação do A3 no início de dezembro.

## Por que usar OKRs aqui?

Os **Objetivos (O)** mostram mudanças desejadas no processo. Os **Resultados-Chave (KR)** especificam métricas e critérios de aceite. As métricas de cobertura e sucesso de CI são indicadores auxiliares; **não substituem a qualidade do oráculo nem revisão de requisitos**.

## O1 — Tornar as mudanças críticas reproduzíveis e rastreáveis

| KR | Meta | Linha de base 25/11 | Aceite verificável |
|---|---|---|---|
| **KR1.1** | 100% dos **2 próximos PRs** com CI verde antes do merge | Novo ciclo ainda não iniciado | URLs dos PRs e checks obrigatórios |
| **KR1.2** | Realizar **1 ciclo TDD completo**, com RED→GREEN→REFACTOR demonstrado | Commit GREEN histórico vazio; nenhum ciclo novo comprovado | Três commits com diffs e relatórios de falha/sucesso |
| **KR1.3** | 100% dos requisitos P1 definidos vinculados a teste + resultado + commit | Não medido; matriz parcial | CSV de rastreabilidade revisado |

**Impacto:** reduz risco de defeitos financeiros retornarem e torna a demonstração TDD realmente verificável.

## O2 — Transformar planejamento em rotina documentada

| KR | Meta | Linha de base 25/11 | Aceite verificável |
|---|---|---|---|
| **KR2.1** | 1 retrospectiva do grupo com ata validada | Reunião não comprovada | Ata preenchida com data real, participantes e decisões |
| **KR2.2** | Horas reais registradas em 100% das **novas** tarefas | Ainda não medidas | Registro preenchido e revisado |
| **KR2.3** | Fechar ≥3 dos 5 débitos técnicos selecionados como prioritários | 0/5 neste recorte inicial | PR/commit mostrando resolução e prova |

**Impacto:** melhora transparência da comparação estimado × realizado, responsabilização e identificação de retrabalho.

## O3 — Estabilizar a integração e o acompanhamento

| KR | Meta | Linha de base 25/11 | Aceite verificável |
|---|---|---|---|
| **KR3.1** | ≥9 sucessos nas **próximas 10 execuções** de CI | Histórico: 6 sucessos / 11 runs, sendo os 6 mais recentes verdes | IDs de 10 runs futuros, medidos de forma fechada |
| **KR3.2** | 0 merges usando bypass de regras nos próximos PRs | Não medido | Auditoria dos PRs futuros e controles de branch |
| **KR3.3** | Painel de métricas atualizado após 100% dos novos merges de entregável | Painel E6 anterior a três merges | Snapshot e commit de atualização após cada merge |

**Impacto:** feedback rápido, decisões baseadas em dados atuais e preservação da política de qualidade.

## Roadmap por ondas

| Onda | Período sugerido | Prioridades | Evidência de fim de onda |
|---|---|---|---|
| **0 — Alinhamento** | 25–26/11 | Validar diagnóstico e OKRs, designar donos, começar registro de horas | Ata de validação / quadro de responsáveis |
| **1 — Correções críticas** | 26–30/11 | Reproduzir TDD correto; corrigir referências E2; testar upstream exato | PRs, logs Maven/JaCoCo e matriz |
| **2 — Medição e experimento** | 29/11–02/12 | Atualizar E6, coletar 10 runs futuros, executar comparação manual × IA com protocolo | CSVs e comparativos reais, sem métricas inventadas |
| **3 — Fechamento acadêmico** | 02–03/12 | Retrospectiva, evidências, revisão cruzada do relatório, screenshots e apresentação | Ata aprovada, PR final verde e evidências consolidadas |

## Regras de acompanhamento

- Cada KR deve ter **responsável real escolhido pelo grupo**, linha de base, prazo, fonte e status: *não iniciado*, *em andamento*, *concluído*, *não atingido*.
- A cada PR, registrar efeito na métrica, impedimentos e decisão sobre retrabalho.
- Se o objetivo de 10 novos runs não for alcançado até a apresentação, reportar **amostra insuficiente**, não extrapolar percentual.
- Nenhuma meta deve ser apresentada como resultado consumado antes da coleta.
- O backlog executável fica em [`plano-de-acoes.csv`](../../evidencias/entregavel-08/plano-de-acoes.csv); a relação dos KRs, em [`roadmap-okrs.csv`](../../evidencias/entregavel-08/roadmap-okrs.csv).

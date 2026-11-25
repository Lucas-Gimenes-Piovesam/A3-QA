# 1. Mini-diagnóstico do processo — referência CMMI

## 1.1 Base conceitual e delimitação

O CMMI oferece um caminho de melhoria de processos. Na classificação oficial atual de **maturity levels**, o nível **0 — Incomplete** caracteriza trabalho incompleto/ad hoc; o **1 — Initial**, desempenho imprevisível e reativo; o **2 — Managed**, processos planejados, executados, medidos e controlados **no projeto**; o **3 — Defined**, padrões organizacionais; o **4 — Quantitatively Managed**, previsibilidade quantitativa; e o **5 — Optimizing**, melhoria contínua institucionalizada. **Não confundir níveis de maturidade organizacional com níveis de capacidade de áreas individuais.**

Fontes primárias: [CMMI Institute — Levels of Capability and Performance](https://prod.cmmiinstitute.com/learning/appraisals/levels) e [ISACA — CMMI Model Quick Reference Guide (25/08/2026)](https://www.isaca.org/resources/reference-guide/cmmi-model-quick-reference-guide).

**Método acadêmico adotado:** *gap assessment* interno e pontual de **9 dimensões selecionadas**, com base exclusivamente em arquivos, PRs, commits e logs públicos do projeto. **Não** foram avaliadas todas as práticas previstas pelo CMMI, não houve entrevistas estruturadas ou auditoria por avaliador credenciado. Portanto, o grupo **não recebeu certificação nem atingiu um nível formal do CMMI**.

## 1.2 Escala própria de evidência (não é escala CMMI)

- **0 = Não evidenciado:** não existe comprovação verificável dentro do recorte.
- **1 = Parcial:** existe plano, artefato ou execução isolada, mas o processo é incompleto/não sustentado.
- **2 = Evidenciado no projeto:** atividade comprovada na amostra, com artefatos rastreáveis.

Essa escala serve apenas para **priorizar melhorias do A3**; não representa nível de capacidade, pontuação oficial do CMMI ou avaliação de conformidade.

## 1.3 Matriz do mini-diagnóstico (fotografia de 25/11/2026)

| ID | Dimensão | Valor (0–2) | Fato observado | Lacuna / decisão |
|---|---|---:|---|---|
| D01 | Gestão de configuração | **2** | `main` protegida, tag de baseline e PRs #1–#3 integrados | Manter proteção, branches curtas e revisões |
| D02 | Integração e verificação | **2** | CI com Maven, JUnit, JaCoCo, Checkstyle e quality gate verde | Monitorar manutenção da cobertura e regressões |
| D03 | Revisão por pares | **2** | Colaborador aprovou os PRs #1, #2 e #3 | Tornar checklist e decisões explícitos |
| D04 | Planejamento / estimativa | **1** | Entregável 7 utiliza Story Points, sem registro efetivo de horas | Preencher horas de tarefas novas; não calcular horas por timestamps |
| D05 | Rastreabilidade de requisitos | **1** | Plano de testes existe, mas não há relação completa requisito→teste→defeito→commit | Consolidar matriz ponta a ponta |
| D06 | Medição e análise | **1** | Painel E6 coletado e publicado; snapshot anterior aos merges | Atualizar snapshot após integrações e observar tendência |
| D07 | Auditoria e qualidade | **1** | Plano SQA e auditoria inicial; ata de revisão permanece modelo | Realizar uma revisão de fato e registrar ata |
| D08 | TDD e prevenção | **1** | Suíte JUnit/BDD e código funcionando; commit GREEN vazio em sequência principal | Repetir TDD com histórico auditável |
| D09 | Retrospectiva e melhoria | **0** | Não foi localizada ata real de retrospectiva no recorte | Realizar reunião e registrar ações/seguimento |
| **Total (rubrica interna)** | | **11/18** | **61,1% dos pontos da rubrica interna** | **Não é percentual de maturidade CMMI** |

**Notas de evidência:**

- [Branches protegidas e repositório](https://github.com/Lucas-Gimenes-Piovesam/A3-QA), [release baseline](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline).
- [PR #1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1), [PR #2](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/2), [PR #3](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/3): integração, revisão independente e status checks.
- [Workflow verde após PR #3](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45526565474); [workflow com 33/33 testes, 145/145 linhas e 64/64 ramos P1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713).
- [Plano de qualidade](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/main/docs/entregavel-01-plano-qualidade), [Plano de testes](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/main/docs/entregavel-02-estrategia-plano-testes), [métricas](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/main/docs/entregavel-06-metricas-indicadores), [planejamento](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/main/docs/entregavel-07-estimativa-planejamento).
- [Commit GREEN vazio](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/9fed22f954aa3c4cdcf42d7f868817a99218f6a5).

## 1.4 Interpretação frente aos níveis de maturidade CMMI

A história mostra a passagem de práticas **reativas e manuais** (uploads e reorganização de diretórios, CI inicialmente vermelho) para práticas **gerenciadas em alguns fluxos** (PR revisado, pipeline obrigatório, branches, métricas). **Isso é compatível com características de transição do nível Inicial para práticas típicas de Managed no âmbito deste projeto**, mas **não** habilita atribuir o nível de maturidade 2 oficialmente, pois ainda faltam institucionalização, planejamento e acompanhamento consistentes e demonstração completa do modelo.

**Lacunas que impedem qualquer conclusão de nível 2 formal:** insuficiência da amostra, registro retrospectivo inexistente, controles de requisitos e horas incompletos, evidência TDD ambígua, ausência de auditoria de processos por avaliador oficial e ausência de verificação sistemática de todas as áreas do modelo.

**Conclusão defensável à banca:** “O processo acadêmico apresenta práticas de gestão e verificação comprovadas, mas ainda requer padronização e medição continuada; não atribuímos nível formal CMMI.”

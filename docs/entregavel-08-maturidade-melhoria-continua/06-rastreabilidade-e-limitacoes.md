# 6. Evidências, limites e recomendações à banca

## 6.1 Evidências verificáveis

| Fato usado | Fonte primária | Nota |
|---|---|---|
| Três PRs integrados e revisados | [#1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1), [#2](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/2), [#3](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/3) | Revisões reais; não representar como ata formal |
| Branch `main` protegida | [https://github.com/Lucas-Gimenes-Piovesam/A3-QA](https://github.com/Lucas-Gimenes-Piovesam/A3-QA) | Conferida na API pública por flag `protected=true`; uma tela da regra pode complementar |
| Histórico de 11 execuções (5 falhas iniciais, 6 sucessos) | [Actions](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions) | Fotografia do histórico até o run 45526565474 |
| Última CI verde após merge E7 | [Run 45526565474](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45526565474) | Não equivale a ausência de defeitos |
| 33 testes aprovados, cobertura P1 e static check | [Run 45522943713](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713) | Somente os métodos financeiros monitorados pelo gate |
| Modelo de ata ainda não preenchido | [Atas E1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/main/docs/entregavel-01-plano-qualidade/atas) | Não alegar retrospectiva já realizada |
| Story Points documentados, horas reais não confirmadas | [Entregável 7](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/tree/main/docs/entregavel-07-estimativa-planejamento) | SP ≠ horas |
| TDD com falha de rastreabilidade GREEN | [Commit vazio](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/9fed22f954aa3c4cdcf42d7f868817a99218f6a5) | Evidência da lacuna, sem ocultar o problema |
| Release de linha de base | [Tag](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline) | Commit histórico; não equivale a deploy de produção |

## 6.2 Limitações metodológicas

1. O diagnóstico pontua **nove dimensões escolhidas internamente**, não todos os itens do modelo CMMI.
2. **11/18 é pontuação interna de evidências, não maturidade CMMI ou conformidade percentual.**
3. Os arquivos no GitHub demonstram práticas da **equipe no projeto**, não maturidade de uma organização inteira.
4. Não foi realizada, nesta preparação, entrevista com o grupo nem retrospectiva síncrona. A reunião deve existir antes de se declarar retrospectiva validada.
5. A estimativa de Story Points do E7 foi retrospectiva; horas reais históricas ainda não comprovadas.
6. Os resultados de 100% de cobertura de P1 são definidos pelo gate, não refletem a cobertura de todo o programa.
7. A taxa histórica de CI inclui a **implantação da ferramenta**, e não deve ser apresentada como confiabilidade estável.
8. A atualização do repositório poderá mudar o snapshot. Atualizar evidências antes da submissão final.

## 6.3 Frase recomendada para apresentação

> Fizemos um diagnóstico interno inspirado no CMMI com nove dimensões do nosso processo. Encontramos práticas gerenciadas e rastreáveis, como revisões de Pull Requests e quality gate obrigatório, mas ainda faltam atas, registro de esforço e evidência rigorosa de TDD. Por isso, não reivindicamos nível formal CMMI. Propusemos três objetivos de melhoria e resultados-chave mensuráveis, que serão acompanhados com evidências no GitHub.

## 6.4 Referências

- [CMMI Institute: Maturity e Capability Levels](https://prod.cmmiinstitute.com/learning/appraisals/levels).
- [ISACA: CMMI Model Quick Reference Guide, 25/08/2026](https://www.isaca.org/resources/reference-guide/cmmi-model-quick-reference-guide).
- Documento da A3 do professor Jessé, p. 6: “Mini-diagnóstico ... frente aos níveis do CMMI ou do MPS.BR, retrospectiva documentada e roadmap de melhoria com OKRs de qualidade”.

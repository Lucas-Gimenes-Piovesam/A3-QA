# 2. Linha de base anterior à intervenção

## Fonte e corte

- Estado inicial do grupo: [`v0.1.0-baseline`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline) = commit [`6b55f9d3`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571).
- Registros anteriores: [`docs/linha-base-e-piloto.md`](../linha-base-e-piloto.md), [`resultado_piloto_ia.json`](../../evidencias/resultado_piloto_ia.json).
- Inspeção de proveniência: o estado do grupo foi reconstruído a partir de código público e não deve ser chamado de clone byte a byte do upstream. A **tag do grupo**, porém, preserva um estado auditável exato.

## Evidências observadas antes

| Métrica | Resultado | Observação |
|---|---:|---|
| Arquivos Java de produção/teste nativo | 6 | Versão baseline do grupo |
| Verificações nativas de CSV | 4/4 | Escopo de utilitário CSV |
| Casos-piloto sugeridos por IA | 10 | O conjunto IA-01 a IA-10 foi versionado antes da intervenção final |
| Oráculos do piloto atendidos | **6/10** | Quatro divergências observadas |
| IA-05 | Falhou | Despesa `NaN` aceita |
| IA-06 | Falhou | Despesa `Infinity` aceita |
| IA-07 | Falhou | Orçamento `NaN` aceito |
| IA-08 | Falhou | Orçamento negativo aceito; regra de domínio proposta |
| JaCoCo da baseline | **Não medido** | Não usar 0% como resultado |
| Tempo para criar/revisar testes humanos | **Não medido** | Não fazer inferência de produtividade |

**Os quatro casos divergentes** não equivalem automaticamente a quatro defeitos distintos e definitivos; o grupo precisa aprovar as premissas de domínio (em especial orçamento zero/negativo). O teste de orçamento negativo reflete **regra nova proposta**, não requisito histórico comprovado.

## Alinhamento do código usado nesta reprodução

O subexperimento reexecutou fontes locais com **Git blob SHA-1 coincidentes com todos os seis arquivos Java consultados na tag baseline**. O arquivo `resultado_comparativo.json` registra seus SHA-1 de blob e SHA-256 de conteúdo. Isso verifica identidade da **cópia de trabalho com a tag do grupo**, não com o commit original do autor externo.

## Limite de comparabilidade

O piloto inicial mediu 1,12 s de **execução de 10 cenários**, não esforço para escrever ou revisar testes. O experimento de agora mediu novamente execução, mas tempos de máquinas/rodadas diferentes não são uma comparação de produtividade humana ou ganho por IA.

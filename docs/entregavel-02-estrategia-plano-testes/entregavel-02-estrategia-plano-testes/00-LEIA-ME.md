# Entregável 2 — Estratégia e Plano de Testes

**Status:** documentação elaborada e 30 casos de caixa-preta executados em piloto local; **23 passaram e 7 divergiram dos oráculos propostos**. Não há ainda cobertura JaCoCo nem comparação independente humano × IA.

## Navegação para avaliação da banca

1. [`01-plano-testes-ieee829.md`](01-plano-testes-ieee829.md) — plano enxuto inspirado na IEEE 829, escopo, riscos, critérios, requisitos, aprovação e ambiente.
2. [`02-piramide-testes-e-roteiro.md`](02-piramide-testes-e-roteiro.md) — pirâmide do produto, comandos e procedimento de execução.
3. [`03-matriz-caixa-preta.md`](03-matriz-caixa-preta.md) — partições de equivalência, valores-limite, trinta casos, resultados.
4. [`04-caixa-branca-e-cobertura.md`](04-caixa-branca-e-cobertura.md) — ramos relevantes, fluxos, critérios de linha/decisão e limitações.
5. [`05-registro-divergencias.md`](05-registro-divergencias.md) — triagem inicial e rastreabilidade de divergências.

## Evidências verificáveis

- [Script reproduzível](../../tests/planejamento/entregavel-02/executar_caixa_preta.py)
- [Casos de teste CSV](../../tests/planejamento/entregavel-02/casos_caixa_preta.csv)
- [Relatório de execução](../../evidencias/entregavel-02/relatorio_execucao_30_casos.md)
- [Resultado completo JSON: entradas, critérios, saídas, hashes](../../evidencias/entregavel-02/resultado_30_casos_caixa_preta.json)

## Relação com o Entregável 1

As metas e prioridades P1 seguem o [`Plano de Qualidade e SQA`](../entregavel-01-plano-qualidade/01-plano-qualidade-sqa.md). Os parâmetros RF-01 e RF-03 (finitude e limites de valores) devem ser aprovados em ata.

**Nota acadêmica:** a especificação e o executor inicial foram elaborados com suporte de IA. **Não apresentar** este conjunto como o braço de testes manual independente que será usado para avaliar a inovação.

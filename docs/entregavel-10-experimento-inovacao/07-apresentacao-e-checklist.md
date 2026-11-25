# 7. Roteiro da apresentação e checklist do E10

## Sequência recomendada para a defesa (2–3 minutos da apresentação total)

1. **Problema (20 s):** Expense Tracker controla despesas; valores inválidos podem contaminar cálculos e orçamentos.
2. **Hipótese (20 s):** IA reduziria esforço em ≥20% sem perder detecção; medir **não é** pressupor o resultado.
3. **Linha de base (25 s):** tag histórica, dez casos IA, **6/10 aprovados**, quatro divergências sob regras propostas.
4. **Intervenção (25 s):** regras financeiras centralizadas, testes de regressão e CI. Referenciar diff e workflow.
5. **Resultados (35 s):** mesmos dez casos, agora **10/10 aprovados**, quatro divergências desapareceram, zero regressão observada nesse conjunto.
6. **Limitações (30 s):** não confundir falha da aplicação com alucinação da IA; falta comparação humana com cronômetro; hipótese de produtividade permanece inconclusiva.
7. **Próximo passo (20 s):** coletar teste manual independente, revisar oráculos, contar erros/alucinações e validar decisão.

## Evidências para mostrar ao professor

- [Release da baseline](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline).
- [Piloto original IA](../../evidencias/resultado_piloto_ia.json).
- [Comparação antes/depois executada](../../evidencias/entregavel-10/resultado_comparativo.json).
- [Tabela de dez resultados](../../evidencias/entregavel-10/resultado_casos.csv).
- [Script reproduzível](../../scripts/experimento_10.py).
- [Workflow de referência verde](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45528152960).

## Checklist da publicação

- [x] Escolha da carta, hipótese e critério de decisão documentados.
- [x] Baseline do **grupo** identificada por tag/commit.
- [x] Dez casos mantidos idênticos entre as versões.
- [x] Comparação realmente executada, artefatos JSON/CSV gerados.
- [x] Resultado negativo/inconclusivo da hipótese principal explicitado.
- [x] Limitações, ameaças à validade e plano de replicação descritos.
- [ ] Arquivos publicados no GitHub em `docs`, `evidencias`, `scripts` **na raiz**.
- [ ] PR do Entregável 10 aberto, revisado por outra pessoa e integrado com CI verde.
- [ ] Revisor do grupo validar especialmente os requisitos IA-07 e IA-08 e assinar a ata.
- [ ] Medir **tempo humano manual e com IA** sob condições comparáveis (se o grupo quiser concluir a hipótese de produtividade).
- [ ] Preencher classificação independente de oráculos corretos, erros e possíveis alucinações.

**Orientação:** um bom relatório deve tratar os três últimos itens como pendentes se não forem executados. Nunca preencher retroativamente tempos com estimativas inventadas.

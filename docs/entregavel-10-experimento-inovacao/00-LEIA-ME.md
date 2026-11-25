# Entregável 10 — Experimento de inovação: IA a serviço da qualidade

**Disciplina:** Gestão e Qualidade de Software — A3 (2026/2)  
**Produto:** Expense Tracker — aplicação Java de terminal  
**Caminho:** sistema existente ou legado  
**Carta de Inovação:** **IA a serviço da qualidade**  
**Repositório:** https://github.com/Lucas-Gimenes-Piovesam/A3-QA  
**Versões comparadas:** tag [`v0.1.0-baseline`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline), commit `6b55f9d3f38012f1bcf1e05b272740bdb0ce8571`; código corrigido da `main`, commit `f4abe2daf159a5a8fab36a5ecb856f64ff843716`.

## A pergunta de pesquisa

**Os testes sugeridos por IA são úteis para revelar desvios nas regras financeiras do Expense Tracker? E conseguem reduzir em pelo menos 20% o esforço de criação/revisão sem perder capacidade de detectar falhas quando comparados com testes feitos manualmente?**

A primeira parte foi investigada com **reexecução real** de dez casos de teste já documentados no piloto original. Para a segunda parte, o pacote entrega um **protocolo controlado e instrumentos de coleta**, mas **não há dados de esforço humano independente**; portanto, a hipótese de economia de 20% **não foi confirmada nem rejeitada**.

## Resultados verificados — comparação dos mesmos dez casos

| Evidência | Antes — baseline | Depois — versão corrigida |
|---|---:|---:|
| Casos IA-01 a IA-10 executados | 10 | 10 |
| Casos aprovados sob os oráculos propostos | **6** | **10** |
| Casos divergentes | 4 | 0 |
| Regressões nos dez casos | — | **0** |
| Regras de `NaN` / `Infinity` / orçamento | Desvios observados | Conformes aos oráculos testados |

Os quatro casos corrigidos foram **IA-05, IA-06, IA-07 e IA-08**. As dez entradas e verificações permaneceram **iguais** nas duas versões. O resultado não significa que os testes de IA tenham 100% de precisão ou que a aplicação esteja livre de defeitos.

**Origem verificável:** [`resultado_comparativo.json`](../../evidencias/entregavel-10/resultado_comparativo.json) · [`resultado_casos.csv`](../../evidencias/entregavel-10/resultado_casos.csv) · [`experimento_10.py`](../../scripts/experimento_10.py). As fontes locais foram cotejadas com os **Git blob SHAs** da tag e do HEAD inspecionados; o JSON registra os hashes de cada arquivo.

## Documentos do pacote

1. [`01-hipotese-e-protocolo.md`](01-hipotese-e-protocolo.md) — perguntas, métricas, controle de variáveis e critérios.
2. [`02-linha-de-base.md`](02-linha-de-base.md) — situação anterior, limitações e proveniência.
3. [`03-intervencao-e-reprodutibilidade.md`](03-intervencao-e-reprodutibilidade.md) — mudanças, versões, script e passo a passo.
4. [`04-resultados-e-analise.md`](04-resultados-e-analise.md) — medidas e interpretação responsável.
5. [`05-protocolo-manual-vs-ia.md`](05-protocolo-manual-vs-ia.md) — procedimento para medir a hipótese restante.
6. [`06-validade-limitacoes-e-proximos-passos.md`](06-validade-limitacoes-e-proximos-passos.md) — riscos metodológicos, conclusões e extensão futura.
7. [`07-apresentacao-e-checklist.md`](07-apresentacao-e-checklist.md) — roteiro de apresentação e critérios de aceite.
8. [`painel-experimento.html`](painel-experimento.html) — visualização estática dos resultados.

## O que não é permitido afirmar

- Que a IA foi **20% mais rápida**: não há medição de criação/revisão de testes independentes.
- Que os quatro casos que falharam na baseline foram **erros da IA**: são divergências observadas do programa em relação aos **requisitos propostos**.
- Que a taxa de `10/10` representa **precisão de 100% das sugestões da IA**: os oráculos ainda precisam de revisão independente.
- Que 100% de cobertura JaCoCo em nove métodos P1 significa **100% de cobertura de requisitos ou ausência de bugs**.
- Que uma linha de base de código reconstruído é uma cópia byte a byte do repositório público original. A tag versiona o **estado inicial do grupo**.

**Status do E10:** documento e comparação técnica reproduzível **prontos**; teste manual independente, tempo humano e avaliação de alucinações **pendentes**. O grupo deverá validar os oráculos e assinar a comparação final.

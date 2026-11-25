# Entregável 6 — Métricas e indicadores

**Disciplina:** Gestão e Qualidade de Software — A3 (2026/2)  
**Produto:** Expense Tracker (Java CLI)  
**Caminho:** Sistema existente ou legado  
**Carta de inovação:** IA a serviço da qualidade  
**Repositório:** https://github.com/Lucas-Gimenes-Piovesam/A3-QA  
**Data do recorte:** 25/11/2026 (UTC).

## Requisito do professor

> "Painel com métricas de produto (ISO 25010) e de processo (lead time, cycle time, DORA), cada uma ligada a uma meta e a uma decisão que ela apoia." — A3 JESSE(1).pdf, p. 5.

## Entrega e como navegar

| Artefato | Para que serve |
|---|---|
| [01-painel-metricas.md](01-painel-metricas.md) | **Painel principal** visível diretamente no GitHub; números, metas, decisões, links das evidências |
| [painel-visual.html](painel-visual.html) | Painel visual em HTML; baixar/abrir num navegador (o GitHub não executa páginas HTML diretamente pelo visualizador de código) |
| [02-dicionario-metricas-e-metas.md](02-dicionario-metricas-e-metas.md) | Fórmulas, fontes, periodicidade, regras de interpretação e justificativas das metas |
| [03-analise-e-decisoes.md](03-analise-e-decisoes.md) | Análise crítica da medição; decisões e limitações |
| [04-atualizacao-e-apresentacao.md](04-atualizacao-e-apresentacao.md) | Roteiro de atualização, demonstração e próximos dados a coletar |
| [`../../evidencias/entregavel-06/coleta-github-2026-11-25.json`](../../evidencias/entregavel-06/coleta-github-2026-11-25.json) | Observações transcritas de GitHub API e logs, com links para auditoria |
| [`../../evidencias/entregavel-06/metricas-calculadas.csv`](../../evidencias/entregavel-06/metricas-calculadas.csv) | Tabela de indicadores e decisões, importável em Excel |
| [`../../evidencias/entregavel-06/execucoes-ci.csv`](../../evidencias/entregavel-06/execucoes-ci.csv) | Histórico das seis execuções, datas, duração e status |
| [`../../scripts/gerar_metricas_06.py`](../../scripts/gerar_metricas_06.py) | Gera painel Markdown, HTML e CSV **offline** a partir da coleta JSON versionada |

## Resumo executivo da fotografia

Na execução [45522943713](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713), a CI aprovou **33 testes JUnit**, compilação, JaCoCo e Checkstyle; o gate registrou **100% de linhas (145/145)** e **100% de ramos (64/64)** especificamente nos **nove métodos financeiros P1**. O histórico de **seis execuções** registrou uma aprovação (**16,7%**), pois os cinco primeiros workflows falharam durante a implantação incremental do pipeline.

O PR #1 foi [aprovado por outro colaborador](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1), **mas ainda estava aberto no instante da coleta**; portanto, tempo de merge e ciclo de desenvolvimento concluído aparecem como **não medidos**. Uma release de linha de base existe, mas **não é um deploy de produção**. Por isso, métricas DORA operacionais estão registradas como **não aplicáveis/não medidas**, e não como zero.

## Escopo e integridade

- As metas são **propostas acadêmicas**, não parâmetros obrigatórios da ISO/IEC 25010 nem benchmarks universais do setor.
- Cobertura alta informa quais trechos foram executados e não é garantia de qualidade funcional integral.
- Valores não medidos permanecem como **não medidos**; nenhuma estatística DORA é inventada.
- Os dados de coleta são **reproduzíveis pelas URLs**, mas não se atualizam automaticamente. O script só recalcula dados que já foram coletados.
- As referências da linha de base de 24/11/2026 vêm de uma cópia de trabalho reconstruída; **não é correto apresentá-las como clone comprovado byte a byte**.

## Regerar após atualizar a coleta

Na raiz do repositório:

```bash
python3 scripts/gerar_metricas_06.py
```

Não são necessárias dependências além do Python 3.10+; o gerador não faz chamadas à rede. Depois de observar um merge verdadeiro, atualize o campo `merged_at` no JSON **com o timestamp do GitHub**, registre nova evidência e gere o painel novamente. Não preencher a data por estimativa.

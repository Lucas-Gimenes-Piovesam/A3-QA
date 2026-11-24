# Auditoria inicial de SQA — Inspeção do repositório (24/11/2026)

**Projeto:** A3-QA / Expense Tracker  
**Tipo:** auditoria leve de existência e rastreabilidade de artefatos — revisão estática.  
**Referência auditada:** [`6b55f9d3f38012f1bcf1e05b272740bdb0ce8571`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571)  
**Repositório original usado na comparação:** [`b35ff1a420499703d0c9ec10851a32468ba31f2a`](https://github.com/chaudhary-lakshay/Expense-Tracker/commit/b35ff1a420499703d0c9ec10851a32468ba31f2a)  
**Execução:** inspeção do código e da árvore GitHub; **não** representa reunião do grupo, execução local dos testes nem aprovação pelo professor.

## 1. Critérios e constatações

| ID | Critério auditado | Estado | Evidência observada | Próxima ação |
|---|---|---|---|---|
| AUD-01 | Repositório identificado, com versão e README | **Conforme** | [Commit inicial](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571), [`README.md`](../../README.md) | Manter README atualizado |
| AUD-02 | Licença e crédito do software original | **Conforme** | [`LICENSE`](../../LICENSE), referência ao repositório original no README | Preservar licença e autoria |
| AUD-03 | Código com origem e cópia idêntica ao upstream | **Parcial** | 6 arquivos Java com linhas não vazias coincidentes com o original, mas hashes e formato de texto não coincidentes; falta [`module-info.java`](https://github.com/chaudhary-lakshay/Expense-Tracker/blob/b35ff1a420499703d0c9ec10851a32468ba31f2a/src/module-info.java) na cópia do grupo | Registrar comparação exata por arquivo e justificar eventual normalização antes de modificar funcionalidades |
| AUD-04 | Documentação de proposta e piloto | **Conforme com ressalva** | [`docs/proposta-inicial.md`](../proposta-inicial.md), [`docs/linha-base-e-piloto.md`](../linha-base-e-piloto.md) | Indicar explicitamente dados preliminares e não equivaler piloto a experimento final |
| AUD-05 | Testes automatizados padronizados JUnit | **Não conforme** | [`CsvUtilTest.java`](../../src/Expense_Tracker/CsvUtilTest.java) é verificação executável, não suíte JUnit; pastas [`tests/ia`](../../tests/ia/) e [`tests/manuais`](../../tests/manuais/) têm apenas instruções | Definir casos e configurar JUnit, preservando verificação original |
| AUD-06 | Build padronizado e cobertura mensurável | **Não conforme** | Ausência de `pom.xml` / configuração Gradle / JaCoCo no commit auditado | Adicionar Maven e JaCoCo; medir cobertura inicial no código de referência |
| AUD-07 | Pipeline de CI com execução verificável | **Não conforme** | Nenhum arquivo em `.github/workflows/` no commit auditado | Implementar workflow e guardar o link da execução |
| AUD-08 | Atas reais de revisão e responsáveis | **Não conforme** | Nenhuma ata existente no commit auditado | Realizar revisão independente, registrar ata e nomes reais |
| AUD-09 | Critérios de risco e metas justificadas | **Não conforme no commit auditado** | Não havia plano SQA formal no commit de inspeção | Publicar o plano SQA e obter aprovação do grupo |
| AUD-10 | Base de evidências do piloto | **Parcial** | [`evidencias/`](../../evidencias/) contém scripts, JSON e saída do teste nativo | Reproduzir os scripts sobre cópia verificada e registrar logs de execução associados a commit |

**Classificação da auditoria:** há organização inicial e material exploratório, porém **não estão concluídos** os controles formais de SQA nem o ambiente de testes e CI exigidos para a entrega final. Esta constatação é documental: nenhuma execução foi simulada ou declarada.

## 2. Riscos técnicos notados na leitura do código

| Código | Observação estática | Tipo | Tratamento previsto |
|---|---|---|---|
| R-01 | O cadastro/edição usa `Double.parseDouble` e bloqueia apenas `amount <= 0`, o que **pode** permitir valores não finitos como `NaN` e `Infinity`. | Risco funcional P1, a confirmar por teste no commit oficial | Definir regra de entrada aceita, executar casos reproduzíveis e registrar defeito se confirmado |
| R-02 | A definição do orçamento aceita valor convertido por `Double.parseDouble`, sem validação explícita de sinal ou finitude antes de gravar. | Risco funcional P1, a confirmar por teste no commit oficial | Registrar testes de fronteira e documentar regra de negócio aceita pelo grupo |
| R-03 | A persistência converte valores numéricos do arquivo; regras de domínio e tratamento de linha corrompida precisam de testes. | Risco de confiabilidade P2 | Planejar cenários de leitura/gravação e integridade |

**Atenção:** os riscos estáticos são pontos de teste, não prova de defeito em produção. A análise exploratória anterior está em [`docs/linha-base-e-piloto.md`](../linha-base-e-piloto.md), mas usa cópia local reconstruída; não substitui reprodução no código oficial identificado.

## 3. Plano de correção por prioridade

1. **Antes de alterar regras financeiras:** fixar referência do upstream, registrar diferenças e reproduzir linha de base sobre código versionado.
2. **Alta prioridade:** criar testes em JUnit para regras P1 e configurar relatório de cobertura JaCoCo.
3. **Alta prioridade:** configurar workflow de GitHub Actions para build/testes/cobertura e registrar primeiras execuções.
4. **Alta prioridade:** executar primeira revisão por pares com ata, responsáveis e evidência de aprovação.
5. **Antes da apresentação:** repetir auditoria, registrar cada item como conforme/não conforme com links e anexar resultados do experimento comparativo IA × manual.

## 4. Evidências verificáveis

- Árvores e commits: [commit do A3-QA](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571) e [commit do Expense Tracker original](https://github.com/chaudhary-lakshay/Expense-Tracker/commit/b35ff1a420499703d0c9ec10851a32468ba31f2a).
- Código financeiro: [`ExpenseTracker.java`](../../src/Expense_Tracker/ExpenseTracker.java), [`ExpenseStorage.java`](../../src/Expense_Tracker/ExpenseStorage.java), [`BudgetStorage.java`](../../src/Expense_Tracker/BudgetStorage.java).
- Provas preliminares: [`metricas_linha_base.json`](../../evidencias/metricas_linha_base.json), [`resultado_piloto_ia.json`](../../evidencias/resultado_piloto_ia.json) e [`resultados_cenarios.json`](../../evidencias/resultados_cenarios.json).

**Conclusão:** o repositório está organizado para iniciar o controle de qualidade; para comprovar cumprimento de SQA, ainda é necessário executar revisões, automação, cobertura e auditorias posteriores, cada uma com evidência própria.

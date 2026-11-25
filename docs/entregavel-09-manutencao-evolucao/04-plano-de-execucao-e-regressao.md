# 4. Plano de execução, avaliação e regressão das mudanças

## 4.1 Sequência recomendada de manutenção

| Onda | Escopo | Entrada | Saída verificável | Status |
|---|---|---|---|---|
| 0 — Linha de base | Fixar código e testes existentes | Commit `5bbc42c` e CI | Snapshot/URL do workflow | Disponível |
| 1 — Validação monetária | CR-09-01, já entregue no E3 | Histórico de correção | Testes financeiros e CI aprovados | Executada anteriormente |
| 2 — Preservação dos dados | CR-09-02 | Critérios de falha e política de backup aprovados | Testes de interrupção de escrita e leitura após falha, PR verde | Proposta |
| 3 — Consistência dos arquivos | CR-09-03 | Política sobre datas inválidas e fixtures | Tests de importação/meses e tratamento sem perda não autorizada | Proposta |
| 4 — Redução do acoplamento | CR-09-04 | API de serviço definida, testes de contrato CLI | Pequenos PRs com testes preservados e diff revisável | Proposta |

## 4.2 Testes de regressão por solicitação

| CR | Testes existentes e sugeridos | Resultado exigido | Evidência esperada |
|---|---|---|---|
| 01 | `ExpenseAmountTest`, `FinancialRulesTest`, `CliFinancialIntegrationTest` | Nenhum `NaN`/infinito aceito; valores válidos preservados; orçamento zero conforme regra adotada | URL do run e relatório Surefire |
| 02 | Novos `ExpenseStorageAtomicWriteTest` e `BudgetStorageAtomicWriteTest` (*nomes propostos*) | Escrita normal mantém registros; falha simulada preserva estado anterior; erro observável pelo chamador | JUnit com arquivo em `@TempDir`, PR e log de erro simulado |
| 03 | Novos testes de leitura de datas inválidas (*a criar*) | `2026-02-30`, texto não data e campos vazios tratados conforme regra aprovada; histórico não some sem registro | Fixtures de `expenses.txt`, logs e testes para resumos mensais |
| 04 | Extração gradual dos serviços com testes de contrato | Mesmas operações/resultados observáveis, formatos CSV e menu; cobertura P1 não cai abaixo do gate | Comparação de saídas e XML JaCoCo |

**Não existe garantia atual de que esses testes novos já foram escritos ou executados.** São critérios futuros, ligados às CRs propostas.

## 4.3 Controle de regressão e rollback

1. Abrir Issue ou registrar ID da CR no PR; aprovar critério de aceite.
2. Salvar fixture **fictícia**, dados locais de teste e referência do commit anterior.
3. Implementar mudança mínima em branch curta `fix/cr-09-02-*` ou `refactor/cr-09-04-*`.
4. Rodar `mvn clean verify` e `python3 scripts/check_coverage.py target/site/jacoco/jacoco.xml`.
5. Comparar saída e persistência antes/depois, sem apagar arquivos reais do usuário.
6. Exigir revisor independente e CI obrigatório; em caso de falha, reverter apenas o PR responsável via commit de `revert`, preservando rastreabilidade.
7. Atualizar a matriz de impactos e registrar resultados reais, data e responsável.

## 4.4 Critérios de conclusão de E9

- [x] Quatro CRs com tipo, risco, impacto, prioridade e estado identificado.
- [x] Comparação das três estratégias de evolução e ADR justificada.
- [x] Plano de regressão e preservação de dados.
- [x] Fonte de cada constatação vinculada ao código ou à execução disponível.
- [ ] Registrar decisão do grupo com ata real e responsáveis.
- [ ] Publicar este pacote por PR aprovado na `main`.

**O professor pede análise e decisão**, não exige que as quatro CRs estejam implementadas. Se o grupo optar por implementar alguma como demonstração, registrar novo commit, testes e status real.

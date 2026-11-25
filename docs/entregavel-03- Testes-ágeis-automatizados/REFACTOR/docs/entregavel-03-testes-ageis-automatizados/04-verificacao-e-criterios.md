# Evidências de execução e critérios de aceite

## Indicadores realmente medidos em 24/11/2026

| Métrica | Red | Green | Refactor | Fonte |
|---|---:|---:|---:|---|
| Compilação com `javac` | Sucesso | Sucesso | Sucesso | Logs locais |
| Verificador autônomo de contrato — aprovações | 2/7 | 7/7 | 7/7 | `log-*.txt` |
| Verificador autônomo de contrato — falhas | 5/7 | 0/7 | 0/7 | `log-*.txt` |
| Execução da CLI sobre entradas isoladas | Não aplicada | Não aplicada | 6 cenários executados, sem falhas do processo | `resultado-cli-local.json` |
| Testes JUnit via Maven | Não executados | Não executados | Não executados | Maven indisponível no ambiente local |
| Cobertura JaCoCo | Não medida | Não medida | Não medida | A medir via E4 |
| Tempo de desenvolvimento humano | Não medido | Não medido | Não medido | A medir para experimento IA |

## Casos CLI efetivamente exercitados

- Cadastro com `NaN` — aplicação rejeitou a entrada sem encerrar inesperadamente.
- Cadastro com `Infinity` — aplicação rejeitou a entrada.
- Cadastro com 12,50 — aceito e persistido.
- Orçamento -10 — entrada rejeitada, sem arquivo de orçamento.
- Orçamento `NaN` — entrada rejeitada, sem arquivo de orçamento.
- Orçamento 0 — aceito e persistido.

## Critérios para aprovação do Entregável 3

1. Três **commits reais e distintos** representando Red, Green e Refactor.
2. Registro de **execução JUnit**: testes Red falhando pela regra funcional, testes Green/Refactor passando, com saída ou relatório.
3. Cenários BDD legíveis e rastreáveis, com revisão por integrante do grupo.
4. Suíte final automatizada e executável via `mvn clean test`.
5. Rastreabilidade entre requisito de domínio, teste, código e evidência.
6. Integrar ao quality gate do Entregável 4 para medir cobertura e bloquear merges abaixo da meta, após configurar proteção da branch.

**Nota ética/metodológica:** todos os testes deste pacote foram criados com assistência de IA. O grupo ainda precisará elaborar testes independentes **sem IA** para a comparação prevista na Carta de Inovação. Não comparar este conjunto consigo mesmo como se fosse manual.

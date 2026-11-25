# Entregável 2 — Estratégia e Plano de Testes (modelo enxuto inspirado na IEEE 829)

**Projeto:** A3-QA — Expense Tracker | **Disciplina:** Gestão e Qualidade de Software (2026/2)  
**Caminho:** Sistema existente ou legado | **Carta de inovação:** IA a serviço da qualidade  
**Identificador:** PT-A3-02 | **Versão:** 1.0 | **Data:** 24/11/2026  
**Repositório do grupo:** https://github.com/Lucas-Gimenes-Piovesam/A3-QA  
**Versão do grupo analisada para desenho dos testes:** [`0188d5ee4c8ca05114c933455d450c4148da5fd5`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/0188d5ee4c8ca05114c933455d450c4148da5fd5)  
**Referência original consultada:** [`b35ff1a420499703d0c9ec10851a32468ba31f2a`](https://github.com/chaudhary-lakshay/Expense-Tracker/commit/b35ff1a420499703d0c9ec10851a32468ba31f2a)  
**Situação:** plano e exploração inicial executados; suíte JUnit, JaCoCo e integração contínua ainda pendentes.

> **Método:** este documento usa a estrutura tradicional de planejamento de testes da IEEE 829 de forma enxuta, como solicitado no A3. Não declara conformidade formal com a norma. A execução exploratória deste entregável foi auxiliada por IA e não constitui a amostra humana independente da comparação de inovação.

## 1. Introdução, propósito e escopo

Planejar e executar testes que avaliem se as regras financeiras do Expense Tracker funcionam conforme expectativas explícitas e reproduzíveis, bem como identificar riscos em entradas inválidas. O produto funciona via terminal em Java, grava despesas em `expenses.txt`, grava orçamentos em `budgets.txt` e exporta CSV. Não utiliza servidor ou banco de dados.

**Objetivos verificáveis:** (a) especificar classes de equivalência e valores-limite; (b) associar casos a decisões do código; (c) definir critérios de cobertura e aceite alinhados ao Plano de Qualidade; (d) fornecer roteiro de execução e resultados reais sem modificar o código; (e) manter separados os conjuntos de testes humanos e gerados por IA para o experimento do A3.

## 2. Itens de teste e rastreabilidade

| Item de teste | Código/fonte | Risco | Requisitos |
|---|---|---|---|
| Cadastro/edição e validação de montantes | [`ExpenseTracker.java`](../../src/Expense_Tracker/ExpenseTracker.java): `addExpense`, `updateExpense` | **P1** | RF-01, RF-02 |
| Controle e alerta de orçamento mensal | `ExpenseTracker.java`: `manageBudget`, `warnIfOverBudget` | **P1** | RF-03, RF-04 |
| Totalização e filtro por mês/categoria | `ExpenseTracker.java`: `monthTotal`, `viewSummary`, `viewMonthlySummary`, `filterByCategory` | **P1** | RF-05 |
| Datas e meses válidos | `readValidDate`, `readValidMonth` | P2 | RF-06 |
| Persistência e exportação | [`ExpenseStorage.java`](../../src/Expense_Tracker/ExpenseStorage.java), [`BudgetStorage.java`](../../src/Expense_Tracker/BudgetStorage.java), [`CsvUtil.java`](../../src/Expense_Tracker/CsvUtil.java) | P2 | RF-07 |
| Índices de exclusão/edição e menu | `deleteExpense`, `updateExpense`, `main` | P2/P3 | RF-08 |

### Requisitos que serão usados como oráculos

- **RF-01 (proposto para validação):** despesas devem conter valores **finitos e estritamente positivos** (`0` e negativos são inválidos; `NaN`, `Infinity` e overflow também). Para testes de limite monetário adotamos incrementos de R$ 0,01, sem afirmar que a aplicação hoje impõe duas casas decimais.
- **RF-02:** edição deve aplicar a mesma regra de valores do cadastro, sem sobrescrever registro quando a entrada é inválida.
- **RF-03 (proposto para validação):** orçamento mensal deve ser **finito e não negativo**; zero representa orçamento zero.
- **RF-04:** alerta de extrapolação ocorre somente quando `gasto > orçamento` (não quando igual).
- **RF-05:** os totais devem somar despesas persistidas corretamente, filtrando por mês/categoria conforme escolha do usuário.
- **RF-06:** aceitar somente datas reais no padrão ISO `YYYY-MM-DD` e meses válidos `YYYY-MM`.
- **RF-07:** gravar/carregar despesas e orçamentos e preservar conteúdo de descrições com vírgulas/aspas na exportação CSV.
- **RF-08:** excluir/editar somente índices existentes; escolhas inválidas de menu são recusadas.

**Natureza dos oráculos:** RF-01 e RF-03 são *regras propostas de segurança dos dados*, coerentes com a finalidade financeira, mas a aprovação dos participantes deve constar da revisão/ata. As demais foram derivadas do comportamento e da documentação do código. Falhas em regras propostas devem ser tratadas inicialmente como **divergências/risco**, até a validação do domínio.

## 3. Funcionalidades a testar e itens fora do escopo

**Incluídos:** cadastro, edição, exclusão, validações de valores e datas, orçamento e alertas, totais, filtros, persistência e CSV. A fase inicial cobre execução pelo terminal e verificação de arquivos, com isolamento de dados entre os casos.

**Fora do escopo deste entregável:** UI web/mobile, banco de dados, usuários reais, performance sob carga, internacionalização, segurança de rede, deploy em produção e comparação de eficácia humano × IA (prevista como experimento posterior). A fase de testes unitários com JUnit e coleta JaCoCo pertence ao Entregável 3/4 e ainda não foi concluída.

## 4. Abordagem e pirâmide de testes

A pirâmide e suas proporções propostas estão em [`02-piramide-testes-e-roteiro.md`](02-piramide-testes-e-roteiro.md). Priorizamos testes unitários de regras financeiras, depois integração com arquivos e um conjunto menor de ponta a ponta pelo terminal. **As proporções são objetivos de distribuição, não números medidos.**

A estratégia utiliza:

1. **Caixa-preta:** classes equivalentes válidas/inválidas e análise de fronteira dos montantes, orçamento, mês/data e índices. A matriz detalhada está em [`03-matriz-caixa-preta.md`](03-matriz-caixa-preta.md).
2. **Caixa-branca:** inspeção dos fluxos condicionais e planejamento da cobertura de decisões/linhas, conforme [`04-caixa-branca-e-cobertura.md`](04-caixa-branca-e-cobertura.md).
3. **Automação reprodutível inicial:** 30 casos de caixa-preta via `tests/planejamento/entregavel-02/executar_caixa_preta.py`, rodando a aplicação real em diretórios temporários. É uma suíte de **planejamento assistido por IA**, não a amostra de testes humanos independentes.
4. **Automação futura:** suíte Java/JUnit + JaCoCo + GitHub Actions; quality gates com metas aprovadas no Entregável 1.

## 5. Critérios de entrada, aceitação e saída

**Entrada:** fonte Java acessível e identificada por commit; JDK disponível; ambiente isolado sem dados pessoais; requisitos RF-01 a RF-08 com estado de aprovação registrado; roteiros e resultados esperados revisados.

**Aceite de um caso:** entrada e estado inicial documentados; saída/arquivo correspondente ao oráculo especificado; retorno normal do processo; evidência anexada ao resultado. A falha de um caso não significa automaticamente uma falha em produção; deve ser triada contra a regra aprovada.

**Saída da etapa de planejamento:** casos especificados, roteiro reproduzível, relatório de execução exploratória e mapa de decisões, mantendo pendências documentadas.

**Critérios de qualidade do produto (meta, NÃO atingimento):** cobertura de decisões P1 **≥ 90%**, linhas P1 **≥ 85%**, 100% das classes críticas documentadas e executadas, zero defeito P1 bloqueador sem tratamento/decisão para entrega. Ver Plano de Qualidade e SQA do Entregável 1.

## 6. Critérios de suspensão e retomada

Suspender a execução se: compilação falhar; ocorrer alteração não registrada no código; os arquivos de dados do teste não estiverem isolados; o oráculo não tiver interpretação acordada; faltarem ferramentas para coletar uma métrica anunciada. Registrar situação, commit e motivo. Retomar após corrigir o ambiente ou aprovar o requisito, executando novamente os casos afetados e as regressões.

## 7. Ambiente e dados de teste

- Linguagem: Java (aplicação requer JDK 8+). Execução exploratória registrada em **OpenJDK 21**.
- Automação externa do planejamento: **Python 3**, bibliotecas padrão; `javac` e `java` instalados.
- Diretório de trabalho: **novo diretório temporário por caso**, evitando que `expenses.txt` e `budgets.txt` contaminem outros cenários.
- Dados: datas fictícias 2024–2026, descrições genéricas e quantias simuladas; não há dados pessoais reais.
- Arquivos gerados e logs: `evidencias/entregavel-02/`.

## 8. Entregáveis desta etapa e tarefas

| Artefato | Local |
|---|---|
| Plano de testes | Este arquivo |
| Pirâmide e roteiro de execução | [`02-piramide-testes-e-roteiro.md`](02-piramide-testes-e-roteiro.md) |
| Matriz de equivalência e valores-limite | [`03-matriz-caixa-preta.md`](03-matriz-caixa-preta.md) |
| Análise de caixa-branca e metas de cobertura | [`04-caixa-branca-e-cobertura.md`](04-caixa-branca-e-cobertura.md) |
| Casos com dados estruturados para revisão | [`../../tests/planejamento/entregavel-02/casos_caixa_preta.csv`](../../tests/planejamento/entregavel-02/casos_caixa_preta.csv) |
| Roteiro automatizado executável | [`../../tests/planejamento/entregavel-02/executar_caixa_preta.py`](../../tests/planejamento/entregavel-02/executar_caixa_preta.py) |
| Relatório e logs de exploração | [`../../evidencias/entregavel-02/`](../../evidencias/entregavel-02/) |

**Sequência de trabalho:** revisar regras → aprovar valores de referência → executar caixa-preta → classificar divergências → implementar testes JUnit sem alterar prematuramente o legado → medir JaCoCo → integrar CI → comparar IA × humanos (duas amostras independentes).

## 9. Responsabilidades e aprovações

| Papel | Responsabilidade | Pessoa / situação |
|---|---|---|
| Autor do plano | Especificar casos, riscos e resultados esperados | **Redação com apoio de IA — a validar pelo grupo** |
| Revisor de requisitos | Confirmar RF-01/RF-03 e fronteiras financeiras | Integrante do grupo **a designar** |
| Executor | Executar/registrar casos e defeitos | Automação exploratória executada; equipe **a designar** para reexecução no GitHub |
| Responsável por cobertura | Configurar JaCoCo, conferir classes instrumentadas | **A designar** |
| Aprovador | Registrar aprovação de escopo e critérios em ata | **Pendente** |

Nenhuma assinatura, reunião ou aprovação é presumida.

## 10. Riscos e contingências

| Risco | Resposta planejada |
|---|---|
| Não comparabilidade entre testes humanos e IA | Construir dois conjuntos com escopo e critérios equivalentes; separar autores e guardar prompts/tempos |
| Regras financeiras ambíguas | Validar RF-01 e RF-03 com o grupo antes de afirmar “defeito confirmado” |
| Diferença entre código reconstruído e upstream | Reproduzir no código do repositório identificado por commit; guardar hashes e logs |
| Interface de terminal difícil de automatizar | Executar fluxos isolados por stdin/stdout e conferir arquivos gerados |
| Cobertura não disponível | Declarar **não medida**, nunca “0%” ou meta atingida |
| Dados persistidos contaminam resultados | Um diretório temporário por caso e saída comprovada de cada execução |

## 11. Resultados exploratórios desta versão

Na cópia de trabalho presente em `src/Expense_Tracker` antes de alterações foram executados **30 casos de caixa-preta** por um roteiro produzido com assistência de IA, dos quais **23 satisfizeram os oráculos** e **7 apresentaram divergência**. As divergências estão em CP-06, CP-07, CP-09, CP-15, CP-16, CP-17 e CP-28. **Não é uma taxa de defeitos do sistema nem um resultado de vantagem da IA.** A execução foi sobre a cópia reconstruída das classes, que corresponde ao texto não vazio consultado no repositório, mas não foi demonstrada identidade byte a byte com o upstream. Ver evidências de execução e SHA-256 dos arquivos no JSON.

**Cobertura de linhas e decisões:** ainda **não medida** por JaCoCo. O mapeamento da seção de caixa-branca é estático e não pode ser confundido com cobertura executada.

## 12. Referências

- Documento do professor: *Proposta de Trabalho A3 — Gestão e Qualidade de Software 2026/2*, páginas 2 a 5 (estratégia, evidência, riscos e entregáveis).
- IEEE 829, referência metodológica tradicional para componentes de um plano de teste; adaptação enxuta para o A3.
- [Expense Tracker original](https://github.com/chaudhary-lakshay/Expense-Tracker) — licença MIT.
- [Plano de Qualidade e SQA — Entregável 1](../entregavel-01-plano-qualidade/01-plano-qualidade-sqa.md).

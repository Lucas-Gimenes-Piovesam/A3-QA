A3-QA | Expense Tracker — Qualidade de Software

Projeto acadêmico de Gestão e Qualidade de Software (2026/2), no caminho Sistema existente ou legado e com carta de inovação IA a serviço da qualidade.

Objetivo: analisar e melhorar a qualidade do Expense Tracker original, aplicativo de terminal em Java, e comparar testes elaborados manualmente com testes gerados com apoio de IA. A hipótese de reduzir o tempo total de elaboração, revisão e execução de testes em pelo menos 20%, sem perder capacidade de detectar defeitos, continua pendente de comparação controlada.
Situação de referência (25/11/2026 UTC): a CI compila o projeto e executou 28 testes JUnit sem falhas no workflow 45520193389. O quality gate ficou reprovado por cobertura insuficiente das regras financeiras P1. Uma suíte verde, isoladamente, não significa gate verde, e a branch main ainda precisava de proteção na data da inspeção.

Origem e autoria
- Projeto original: chaudhary-lakshay/Expense-Tracker — licença MIT; consultar LICENSE.
- Referência upstream documentada: commit b35ff1a.
- A cópia inicial de trabalho foi reconstruída a partir dos arquivos públicos e não deve ser descrita como clone byte a byte; consultar [`docs/linha-base-e-piloto.md`](docs/linha-base-e-piloto.md). O código deste repositório já passou por intervenções locais.
Funcionalidades sob avaliação
Cadastro, edição e exclusão de despesas; resumo total, mensal e por categoria; orçamento mensal com alerta; persistência em arquivos locais; leitura e exportação CSV. As regras de maior risco (P1) são validação monetária, cálculos e orçamento.
Requisitos
- JDK 21 recomendado para reproduzir o GitHub Actions (código compilado para Java 17 no Maven);
- Apache Maven 3.9+ para o build e a suíte JUnit;
- Python 3.10+ para o verificador de cobertura, usado no pipeline.
Executar a aplicação
A partir da raiz do repositório:
mvn clean package
java -cp target/classes Expense_Tracker.ExpenseTracker
Atenção: o aplicativo grava expenses.txt, budgets.txt e expenses_export.csv no diretório de execução. Esses arquivos são ignorados por .gitignore. Utilize dados fictícios.
Testes, cobertura e análise estática
# Executa todos os testes JUnit
mvn clean test

# Executa build + JUnit + relatório JaCoCo + Checkstyle
mvn clean verify

# Executa o mesmo gate de cobertura financeira usado no Actions
python3 scripts/check_coverage.py target/site/jacoco/jacoco.xml --output target/quality-gate.json
Critérios declarados no Plano de Qualidade: 100% dos testes aprovados, nenhuma violação das regras Checkstyle configuradas, ≥85% de cobertura de linhas e ≥90% de decisões nos métodos financeiros P1 definidos no verificador. mvn verify pode passar e o gate adicional reprovar. Relatórios gerados localmente ficam em target/ e não são versionados.

Consultar execuções no GitHub Actions.
Estrutura do repositório
.github/workflows/    GitHub Actions: CI e quality gate
config/checkstyle/   regras de análise estática
docs/                planos, estratégia de testes, TDD, CI e gestão de configuração
evidencias/          registros de execução e documentos de suporte
scripts/             verificação automática de cobertura
src/Expense_Tracker/ implementação Java
tests/junit/         suíte executável JUnit 5
tests/bdd/           especificações Gherkin (não executadas por Cucumber)
tests/manuais/       área de testes manuais
tests/ia/            área de testes apoiados por IA
pom.xml              configuração Maven
CONTRIBUTING.md      fluxo de contribuição, branches, commits e revisão
CHANGELOG.md         evolução versionada do projeto
Entregáveis da A3
1. [Plano de Qualidade e SQA](docs/entregavel-01-plano-qualidade/01-plano-qualidade-sqa.md)
2. [Estratégia e Plano de Testes](docs/entregavel-02-estrategia-plano-testes/00-LEIA-ME.md)
3. [Testes Ágeis e Automatizados](docs/entregavel-03-testes-ageis-automatizados/00-LEIA-ME.md)
4. [Pipeline com Quality Gate](docs/entregavel-04-pipeline-quality-gate/00-LEIA-ME.md)
5. [Gestão de Configuração](docs/entregavel-05-gestao-configuracao/00-LEIA-ME.md)
Atenção à rastreabilidade: as evidências de caixa-preta do Entregável 2 foram inicialmente colocadas dentro de docs/entregavel-02-estrategia-plano-testes/tests/ e .../evidencias/, em vez da raiz. O procedimento de revisão final deve avaliar esse ajuste; o README não declara os caminhos corrigidos.
Estratégia Git e releases
Trunk-based development: main como referência de integração, branches de vida curta (docs/, test/, fix/, ci/ ou feat/) e Pull Requests pequenos; revisão por pares quando disponível. A CI deverá ser exigida para merge quando a proteção da branch for configurada. Não afirmar que o bloqueio está ativo antes de verificar a configuração e um PR de demonstração.
- [Como contribuir](CONTRIBUTING.md)
- [Estratégia e justificativa](docs/entregavel-05-gestao-configuracao/01-estrategia-branching.md)
- [Tags, versões e releases](docs/entregavel-05-gestao-configuracao/02-versionamento-tags-releases.md)
- [Histórico auditável](docs/entregavel-05-gestao-configuracao/03-historico-e-rastreabilidade.md)
- [Changelog](CHANGELOG.md)
Licença: consulte o arquivo LICENSE; respeitar os créditos do autor original.

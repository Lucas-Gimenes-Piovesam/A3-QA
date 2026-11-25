# 3. Histórico que conta a história do projeto

A análise foi feita sobre os commits efetivamente públicos do repositório do grupo em 25/11/2026 UTC, tendo como referência o HEAD [`3d37fd5`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/3d37fd58b69cf0f8e719ead78ba7d15680fe3684). O quadro não substitui as URLs reais dos commits.

| Fase / fato | Commit | Evidência | Leitura crítica |
|---|---|---|---|
| Estrutura inicial | [`6b55f9d`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571) | Código Java, docs iniciais, evidências-piloto | Cópia de trabalho reconstruída do código público; não chamar de clone literal |
| Entregável 2 | [`ae8065e`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/ae8065e36f560657139a796b8a45d31a1d3d40b3) | Plano e estratégia de testes | Documentos inseridos; evidências adicionais foram carregadas posteriormente |
| Alteração efetiva de `Expense.java` | [`abb4eec`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/abb4eec05a0bc563a3801779c34290eafaab33d6) | Mudança de código e log GREEN | **Ocorreu antes** do commit RED subsequente |
| Evidência RED na raiz | [`12fda53`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/12fda53f9938a9b0524dba62a3243ebbf8b97d71) | Novos testes, Maven e `log-red.txt` | Demonstra especificação dos testes, mas não um ciclo TDD isolado perfeito |
| Commit rotulado GREEN | [`9fed22f`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/9fed22f954aa3c4cdcf42d7f868817a99218f6a5) | `git show` sem arquivos modificados | Commit **vazio**. Não usar como prova de introdução da correção |
| Refatoração e suíte | [`1935c0d`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/1935c0d187d892174a6bd0eab65ec3f8ae6f0c26) | `FinancialRules`, suíte JUnit, Gherkin, docs | Mudanças efetivas no código e testes principais |
| Pipeline | [`c9eb81e`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/c9eb81e67c215722ed1a3e29b34aee37ba0c00d8) | CI, scripts e documentos | Início da integração automatizada |
| Workflow GitHub Actions | [`41d7425`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/41d74253f47430616009853a87a478480f6ae596) | `.github/workflows/ci-quality-gate.yml` | Permite execução em push/PR |
| Arquivos ignorados | [`3dc593d`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/3dc593d751cd74c47e035116de218c1986e87ba5) | `.gitignore` | Evita versionar saídas temporárias e dados de usuário |
| Correção CI | [`3d37fd5`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/3d37fd58b69cf0f8e719ead78ba7d15680fe3684) | Renomeia variável `java` para `javaExe` | Corrige erro de compilação da suíte |
| Execução da CI após correção | [Run `45520193389`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45520193389) | 28 testes aprovados, gate financeiro reprovado | Evidência de quality gate real **detectando não conformidade** |

## Leituras e implicações de qualidade

- Há um histórico auditável de desenvolvimento, ajustes e correções; algumas mensagens são genéricas ou resultam de reorganizações de upload. A narrativa foi reconstruída **a partir de SHA e diff reais**, não apenas das mensagens dos commits.
- O erro do teste CLI foi corrigido por commit específico e seguido por CI; isso ilustra manutenção rastreável.
- O rótulo GREEN não equivale automaticamente ao comportamento GREEN. Uma prova TDD rigorosa exige um teste falhando antes da correção e passando depois, com mudanças no código rastreáveis. Uma nova branch de demonstração pode ser registrada se houver tempo, mas **não reescrever a história**.
- O gate foi executado e falhou por cobertura; a reprovação é um dado válido da experiência de QA. Porém, ainda não comprova bloqueio de merge, porque a proteção estava desativada durante a inspeção.

## Links para evidências complementares

- [Plano de SQA](../entregavel-01-plano-qualidade/01-plano-qualidade-sqa.md)
- [Matriz de testes](../entregavel-02-estrategia-plano-testes/03-matriz-caixa-preta.md)
- [TDD](../entregavel-03-testes-ageis-automatizados/01-tdd-red-green-refactor.md)
- [Pipeline](../entregavel-04-pipeline-quality-gate/00-LEIA-ME.md)
- [Inspeção de 25/11/2026](../../evidencias/entregavel-05/inspecao-github.json)

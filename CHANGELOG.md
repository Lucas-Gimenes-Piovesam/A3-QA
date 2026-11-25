# Histórico de mudanças — A3-QA

Formato inspirado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/). Este arquivo descreve **fatos rastreáveis** e separa versões propostas de releases efetivamente publicadas.

## [Não lançado] — documentação e gestão de configuração

### Planejado
- README atualizado com instruções de execução, testes, evidências e origem do projeto.
- Estratégia trunk-based, regras de colaboração, tags e documentação de releases.
- Criação de branch curta, Pull Request e política de aprovação por CI.
- Tag/release de linha de base e uma pré-release do piloto, **a publicar pelo grupo**.

## [Desenvolvimento no repositório] — 24/11/2026 a 25/11/2026 UTC

### Adicionado
- Plano de Qualidade SQA e planejamento de testes (Entregáveis 1 e 2).
- Testes JUnit e Gherkin para validação financeira (Entregável 3).
- Pipeline Maven/JUnit/JaCoCo/Checkstyle e verificador de cobertura P1 (Entregável 4).

### Corrigido
- Entrada financeira inválida (`NaN`, infinitos e valores não permitidos), com evidência e testes relacionados; consultar commits da documentação do Entregável 3.
- Conflito de identificador em teste de integração no commit [`3d37fd5`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/3d37fd58b69cf0f8e719ead78ba7d15680fe3684).

### Verificado
- [GitHub Actions #45520193389](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45520193389): **28 testes JUnit aprovados**, Maven `verify` e análise estática executados, **gate de cobertura reprovado**.

### Limitações documentadas
- O commit rotulado GREEN [`9fed22f`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/9fed22f954aa3c4cdcf42d7f868817a99218f6a5) não possui alterações; a modificação efetiva de `Expense.java` ocorreu em outro commit anterior ao RED [`abb4eec`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/abb4eec05a0bc563a3801779c34290eafaab33d6). Assim, o histórico não prova um TDD RED→GREEN puro na raiz sem nova demonstração controlada.
- A suíte do Entregável 3 não comprova comparação controlada entre testes manuais e IA.
- Nenhuma release havia sido publicada na inspeção de 25/11/2026 UTC.

**Não atribuir números de versão liberada a registros acima antes de criar as tags/releases reais.**

# Entregável 4 — Pipeline CI com Quality Gate

**Disciplina:** Gestão e Qualidade de Software — A3 (2026/2)  
**Projeto:** [A3-QA](https://github.com/Lucas-Gimenes-Piovesam/A3-QA) — Expense Tracker  
**Carta:** IA a serviço da qualidade  
**Situação do pacote:** configuração preparada para o estado do repositório em 25/11/2026; execução efetiva Maven/Actions e proteção de merge **pendentes**. O código e os testes do Entregável 3 já constam na raiz.  
**Data:** 25/11/2026

## 1. Objetivo

Automatizar a verificação das alterações do Expense Tracker para impedir que modificações sem compilação, sem testes, com falhas de análise estática ou com cobertura insuficiente das regras financeiras críticas sejam aprovadas no processo de revisão e integradas à branch principal.

A CI verifica o **código**, não prova automaticamente que toda regra financeira está correta. Para concluir a qualidade, são necessários testes de negócio, análise das divergências e revisão humana, conforme Entregáveis 1–3.

## 2. Arquitetura do pipeline

```text
Push / Pull Request para main
          |
          v
Checkout + JDK 21 + cache Maven
          |
          v
mvn clean verify
  | Compilacao Java (release 17)
  | JUnit 5: testes de infraestrutura e futuros conjuntos de teste
  | JaCoCo: cobertura HTML + XML
  | Checkstyle: analise estatica (falha com violacoes)
          |
          v
scripts/check_coverage.py
  | Verifica cobertura LINE >= 85% e BRANCH >= 90%
  | Escopo: 9 metodos financeiros P1 de ExpenseTracker
          |
          v
Job 'ci-quality-gate': sucesso ou falha
          |
          v
Branch protection: exigir job bem sucedido para merge
```

### Justificativa das metas

- **85% das linhas e 90% das decisões/ramos nos métodos P1**: mesmos indicadores do Plano de Qualidade (Entregável 1); evita exigir apenas cobertura global genérica que pode ocultar risco financeiro.
- **Zero testes JUnit reprovados**: nenhum comportamento documentado como esperado pode falhar sem justificativa.
- **Zero violações Checkstyle nas regras adotadas**: identifica tabulações, imports `*` e imports de APIs internas proibidas, sem impor reestilização total do legado nesta primeira fase.
- **Proteção de branch**: o script falhar por si só **não bloqueia merges**; é necessário marcar `ci-quality-gate` como status obrigatório em **Settings > Branches**.

**Observação:** cobertura não mede eficácia do oráculo. Na análise dos resultados finais, também serão exigidos testes negativos para entradas financeiras inválidas e a decisão sobre os defeitos P1 conhecidos. Mesmo o gate aprovado não prova ausência de defeitos.

## 3. Arquivos correspondentes

**Importante:** `pom.xml` e `config/checkstyle/checkstyle.xml` **já estão no GitHub**, vindos do Entregável 3. O ZIP atualizado do Entregável 4 contém apenas os arquivos ainda necessários para a CI, evitando tentar sobrescrever os existentes via upload no navegador.

| Arquivo (a partir da raiz do repositório) | Função |
|---|---|
| [`pom.xml`](../../pom.xml) | Maven: build, JUnit, JaCoCo e Checkstyle |
| [`.github/workflows/ci-quality-gate.yml`](../../.github/workflows/ci-quality-gate.yml) | Automação CI em push, PR e execução manual |
| [`config/checkstyle/checkstyle.xml`](../../config/checkstyle/checkstyle.xml) | Regras de análise estática |
| [`scripts/check_coverage.py`](../../scripts/check_coverage.py) | Gate estrito de cobertura dos métodos P1 |
| [`tests/junit/Expense_Tracker/InfrastructureSmokeTest.java`](../../tests/junit/Expense_Tracker/InfrastructureSmokeTest.java) | Testes JUnit iniciais de infraestrutura, produzidos com IA; **não** são o braço manual independente |
| [`evidencias/entregavel-04/validacao-local.txt`](../../evidencias/entregavel-04/validacao-local.txt) | Verificações locais realmente executadas e limitações |

## 4. Critérios de aceite do Entregável 4

1. [x] Arquivo de workflow com checkout, Java e Maven elaborado.
2. [x] Build Maven configurado com testes, relatórios de cobertura e análise estática.
3. [x] Script de verificação de cobertura P1 preparado e validado usando XMLs **sintéticos** (sucesso, reprovação e ausência de relatório).
4. [x] Testes JUnit de infraestrutura escritos; compilação sintática conferida com stubs (não equivale a rodar JUnit).
5. [ ] Publicar arquivos na raiz correta do repositório e registrar commit.
6. [ ] Executar workflow real no GitHub, examinar logs e corrigir falhas de configuração.
7. [ ] Completar testes das regras P1 para obter as metas de cobertura; manter CI **vermelho** enquanto abaixo dos limites, sem fraudar indicadores.
8. [ ] Exigir o status `ci-quality-gate` em `main` e registrar captura do bloqueio efetivo de um PR não conforme.
9. [ ] Guardar URL do run, relatórios publicados, commit e evidência de PR bloqueado em `evidencias/entregavel-04/`.

## 5. Uso local

**Requisitos:** JDK 21, Maven 3.9+ e Python 3.10+ (Python 3.10+ é uma escolha operacional; o script usa só biblioteca padrão).

```sh
mvn --batch-mode --no-transfer-progress clean verify
python3 scripts/check_coverage.py target/site/jacoco/jacoco.xml --output target/quality-gate.json
```

Relatórios esperados:

- JUnit: `target/surefire-reports/`;
- JaCoCo: `target/site/jacoco/index.html` e `jacoco.xml`;
- Checkstyle: `target/checkstyle-result.xml`;
- Decisão de gate: `target/quality-gate.json`.

Se o comando `mvn verify` falhar em testes ou análise estática, o segundo passo não será executado no workflow. Isso **não é uma aprovação**; o job ficará reprovado.

## 6. Pendências e limitações atuais

- Os arquivos do **Entregável 3** já foram enviados à raiz do repositório, incluindo testes JUnit e cenários BDD. Entretanto, ainda **não há execução Maven/Surefire comprovada nem JaCoCo medido**. Não devemos afirmar que o gate foi aprovado; o primeiro Actions pode reprovar pela cobertura ou pela análise estática do código legado.
- Não foi possível executar Maven nem GitHub Actions no ambiente de preparação. **Não existe evidência de execução bem-sucedida do pipeline neste momento**.
- O código no repositório foi previamente reconstruído; linhas não vazias coincidem com o upstream, mas há pequenas diferenças de formatação/linhas em branco. Ainda recomendamos reconstrução fiel e fixação de versão antes da avaliação final.
- Entrega contínua em produção não se aplica a este aplicativo de terminal sem serviço de hospedagem. O jar do build e os relatórios são publicados como **artefatos de CI**, não como deploy de produção.

## 7. Referências

- [Plano de Qualidade e SQA do grupo](../entregavel-01-plano-qualidade/01-plano-qualidade-sqa.md)
- [Regras de cobertura JaCoCo](https://www.jacoco.org/jacoco/trunk/doc/check-mojo.html)
- [Maven Checkstyle](https://maven.apache.org/plugins/maven-checkstyle-plugin/check-mojo.html)
- [GitHub: branches protegidas](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)

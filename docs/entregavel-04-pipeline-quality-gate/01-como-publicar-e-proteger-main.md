# Procedimento operacional — publicar o Entregável 4 e ativar o bloqueio de merge

## A. Upload inicial (pelo navegador)

1. Abra **a página raiz** de <https://github.com/Lucas-Gimenes-Piovesam/A3-QA> (deve mostrar `README.md`, `src`, `docs`, `tests`, `evidencias`).
2. Extraia o arquivo ZIP. Selecione os itens **dentro** da pasta `A3-QA_entregavel_04`, não a pasta externa.
3. Envie os elementos **presentes no ZIP atualizado**, mantendo os caminhos: `.github`, `docs`, `evidencias`, `scripts`, `tests` e `.gitignore`. **Não reenvie `pom.xml` nem `config/checkstyle/checkstyle.xml`**, pois já existem no repositório com o conteúdo requerido. Se o navegador ocultar a pasta `.github`, use o procedimento B.
4. Verifique o nome de cada caminho na prévia do GitHub: **não pode** ficar `docs/entregavel-04.../pom.xml` ou `A3-QA_entregavel_04/pom.xml`.
5. Confirme o commit: `ci: configurar Maven JUnit JaCoCo Checkstyle e quality gate P1`.

**Atenção:** o GitHub não permite selecionar uma pasta em todos os navegadores de forma uniforme. Se o upload por arrastar não preservar as pastas, use **Add file > Create new file** e informe a rota completa (ex.: `.github/workflows/ci-quality-gate.yml`), colando o conteúdo do arquivo correspondente. Isso é especialmente útil para o arquivo YAML oculto em `.github/`.

## B. Conferência após upload

Confirme a existência de todos os caminhos:

```text
A3-QA/
├── pom.xml
├── .gitignore
├── .github/workflows/ci-quality-gate.yml
├── config/checkstyle/checkstyle.xml
├── scripts/check_coverage.py
├── tests/junit/Expense_Tracker/InfrastructureSmokeTest.java
├── docs/entregavel-04-pipeline-quality-gate/
│   ├── 00-LEIA-ME.md
│   └── 01-como-publicar-e-proteger-main.md
└── evidencias/entregavel-04/validacao-local.txt
```

## C. Executar o CI real

1. Abra a aba **Actions**, selecione `A3 Quality Gate`, clique em **Run workflow** se a automação não iniciou automaticamente.
2. Abra o job `ci-quality-gate`. Confira as etapas: checkout, JDK, Maven, verificação de cobertura, artefatos.
3. Se houver falha, **não remova o gate**. Leia o log e registre o motivo. É normal que falhe por cobertura P1 insuficiente antes do Entregável 3.
4. Em **Artifacts**, confira `relatorios-qa-...` e descarregue relatórios de JUnit, cobertura, Checkstyle e gate, conforme gerados.
5. Grave no relatório da entrega a URL do run, commit, data, resultado e evidências baixadas.

## D. Habilitar a proteção de merge (após o primeiro run aparecer)

1. Vá a **Settings > Branches > Add branch protection rule** (a interface também pode permitir Rules > Rulesets).
2. **Branch name pattern:** `main`.
3. Marque **Require a pull request before merging**.
4. Marque **Require status checks to pass before merging**.
5. Selecione o check exato **`ci-quality-gate`**, de GitHub Actions. Se não existir, execute o workflow ao menos uma vez e volte à tela.
6. Recomendado: impedir bypass dos requisitos, se a opção estiver disponível à conta. Salve a regra.
7. Para comprovar o bloqueio, crie uma branch de teste, abra um PR para `main` com uma alteração que não satisfaça o gate e capture a tela exibindo o merge bloqueado. **Não publique alterações propositadamente inseguras na `main`.**

**IMPORTANTE:** após proteger `main`, não envie próximas entregas diretamente para essa branch; faça os novos uploads numa branch e abra PR. O bloqueio efetivo depende dessa configuração no GitHub, **não apenas** do YAML.

## E. Evidências mínimas para o professor

| Evidência | Arquivo ou URL a registrar | Situação inicial |
|---|---|---|
| Workflow versionado | `.github/workflows/ci-quality-gate.yml` + commit | A publicar |
| Execução real do job | URL da aba Actions/run | Pendente |
| Build/testes | Surefire logs em artifacts | Pendente |
| Cobertura P1 | `target/site/jacoco/` e `target/quality-gate.json` | Pendente |
| Análise estática | `target/checkstyle-result.xml` | Pendente |
| Bloqueio de merge | print + URL do PR com status obrigatório | Pendente |

Não reproduzir relatórios artificiais como se fossem gerados pela CI. O único ensaio sintético deste pacote testa a lógica do verificador, não a cobertura real do Expense Tracker.

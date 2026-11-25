# Atualização, evidências e roteiro de apresentação

## 1. Como demonstrar ao professor (2–3 minutos)

1. Abrir [o painel](01-painel-metricas.md) e explicar a escolha dos métodos P1, com ênfase em valores financeiros.
2. Mostrar o [run verde #45522943713](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713), destacando 33/33 testes, JaCoCo, Checkstyle e gate.
3. Explicar: 100% de linhas e ramos **somente dos nove métodos P1**; as metas originais do grupo são 85% e 90%.
4. Mostrar o histórico de seis runs e interpretar o índice de 1/6 sem confundi-lo com falhas de produção.
5. Mostrar o [PR #1](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/pull/1), a revisão e o bloqueio do merge antes do gate; se já estiver integrado, abrir o SHA de merge.
6. Explicar por que métricas DORA de produção ficam não medidas num projeto sem implantação real.

## 2. O que atualizar depois do merge do PR

Na aba **Conversation** do PR #1, após o review e o gate estarem corretos, concluir o merge seguindo as regras de proteção. Não usar *bypass rules*. Então:

1. Abrir a página do PR e confirmar a indicação **Merged**.
2. Registrar a URL/sha do merge e a data de integração (`merged_at`), conforme a API pública `https://api.github.com/repos/Lucas-Gimenes-Piovesam/A3-QA/pulls/1`.
3. Atualizar o arquivo `evidencias/entregavel-06/coleta-github-2026-11-25.json`, preenchendo `merged_at` e alterando `state_no_snapshot` para `closed` **apenas se confirmado**.
4. Rodar, na raiz do projeto, `python3 scripts/gerar_metricas_06.py`.
5. Revisar os valores de lead time interno do PR e cycle time, atualizar o recorte/data do documento e criar novo commit documental. Manter cópia do recorte histórico anterior se necessário para auditoria.

**Se o PR ainda estiver aberto, não preencha `merged_at`.** O relatório atual representa o estado observado em 25/11/2026 UTC, antes da integração.

## 3. Coleta periódica de CI

Para atualizar os indicadores de processo:

- Consulte `https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions` e abra a lista de runs.
- Para cada run novo concluído, registre em `ci_runs` do JSON: ID, evento, `created_at`, `updated_at`, resultado final e URL.
- Registre as informações da nova execução aprovada no campo `quality_gate_ultima_execucao`, **após confirmar os logs**. Se não houver execução aprovada mais recente, mantenha o último dado verificado e declare a defasagem.
- Execute o gerador para atualizar tabelas e dashboard visual.

**Atenção ao alvo R01:** janela de acompanhamento de dez runs após estabilização, e não apagar os seis runs históricos para parecer que o sistema sempre passou.

## 4. Evidências a capturar para apresentação

- Tela do [GitHub Actions aprovado](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45522943713) com os passos bem-sucedidos.
- Relatórios de JUnit/Surefire e JaCoCo da seção **Artifacts**, quando disponíveis.
- PR mostrando a aprovação por colaborador e, após integração, o status **Merged**.
- Regra de branch mostrando `ci-quality-gate` como requisito obrigatório.
- Página da [pre-release baseline](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases/tag/v0.1.0-baseline).

Não salve print de resultado que não corresponde ao commit/run que está sendo descrito. O histórico dos próprios links é evidência primária.

## 5. Como publicar este Entregável 6 sem interferir no PR #1

**Preferência:** finalizar o PR #1 primeiro e depois criar uma branch curta chamada `docs/entregavel-06-metricas-indicadores` a partir da `main` atualizada. No GitHub:

1. Página inicial `A3-QA`, seletor de branch `main` → criar a branch `docs/entregavel-06-metricas-indicadores`.
2. Com essa branch selecionada, **Add file → Upload files** a partir da raiz; arrastar as três pastas `docs`, `evidencias`, `scripts` do pacote extraído.
3. Commit: `docs(metricas): adicionar painel ISO 25010 e indicadores de processo`.
4. Abrir PR com **base `main`** e **compare `docs/entregavel-06-metricas-indicadores`**.
5. Revisão por outro integrante; check obrigatório verde; merge normal.

No upload, **não entre dentro de `docs` antes de arrastar as pastas**: os caminhos devem começar na raiz do repositório para evitar `docs/docs/`.

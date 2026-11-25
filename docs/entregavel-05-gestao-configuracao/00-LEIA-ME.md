# Entregável 5 — Gestão de configuração

**Projeto:** A3-QA / Expense Tracker  
**Disciplina:** Gestão e Qualidade de Software — A3 (2026/2)  
**Abordagem:** sistema existente ou legado; inovação “IA a serviço da qualidade”  
**Repositório:** https://github.com/Lucas-Gimenes-Piovesam/A3-QA  
**Inspeção da referência:** 25/11/2026, UTC — commit `3d37fd58b69cf0f8e719ead78ba7d15680fe3684`.

## Objetivo

Definir e demonstrar controle de configuração com: repositório Git, estratégia de branches escolhida e justificada, convenção de commits, README, rastreabilidade, tags e releases com evidências reais. Não confundir planejamento da configuração com sua aplicação efetiva no GitHub.

## Matriz da exigência do professor

| Exigência | Artefato / evidência | Estado na inspeção |
|---|---|---|
| Repositório Git | https://github.com/Lucas-Gimenes-Piovesam/A3-QA | Presente |
| Estratégia Git Flow ou trunk-based | [01-estrategia-branching.md](01-estrategia-branching.md) | **Trunk-based escolhido; PR demonstrativo a executar** |
| Tags e releases | [02-versionamento-tags-releases.md](02-versionamento-tags-releases.md) | **Pendente:** nenhuma release observada |
| README claro | [`README.md`](../../README.md) | Atualização preparada neste pacote; conferir commit real |
| Histórico que conte a história do projeto | [03-historico-e-rastreabilidade.md](03-historico-e-rastreabilidade.md), [`CHANGELOG.md`](../../CHANGELOG.md) | Commits existentes, relato verificado e limitações registradas |
| Evidência de aplicação | [04-checklist-evidencias.md](04-checklist-evidencias.md) e `evidencias/entregavel-05/` | Requer PR, tag/release e capturas reais |

## Arquivos deste pacote

- [`README.md`](../../README.md): substitui a versão antiga, desatualizada em relação a Maven, JUnit e CI.
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md): normas de colaboração, branches, commits e revisão.
- [`CHANGELOG.md`](../../CHANGELOG.md): evolução com links, fatos e limitações.
- `docs/entregavel-05-gestao-configuracao/`: justificativa, versões, trilha de auditoria, passos e checklist.
- `evidencias/entregavel-05/inspecao-github.json`: dados verificados da inspeção; **não é evidência de tag/release criada**.

## Estado conhecido dos testes e qualidade

[Run #45520193389](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/actions/runs/45520193389): compilação, 28 testes JUnit sem falhas e análise estática concluídos; check adicional de cobertura **falhou**. O branch `main` não estava protegido durante a inspeção. Antes de declarar conformidade completa, realizar a demonstração de Pull Request bloqueado, corrigir cobertura ou justificar pendência, e registrar release efetiva.

**Escopo de entrega contínua:** sem deploy em produção para um aplicativo CLI; registrar e disponibilizar artefatos/versionamento de código por tag/release como distribuição de versão acadêmica. Uma release de estudo não deve ser chamada de produção homologada.

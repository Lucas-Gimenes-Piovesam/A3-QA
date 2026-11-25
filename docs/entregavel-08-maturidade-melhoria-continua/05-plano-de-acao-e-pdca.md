# 5. Plano de ação e ciclo PDCA

## 5.1 Método PDCA para o A3

- **Plan (Planejar):** a partir do diagnóstico CMMI, priorizar riscos e aprovar OKRs e responsáveis na retrospectiva real.
- **Do (Executar):** abrir branches pequenas para TDD, caminhos das evidências, horas, rastreabilidade e métricas; submetê-las a PR e CI.
- **Check (Verificar):** verificar commits/diffs, logs dos testes, indicadores e checklists nas datas previstas.
- **Act (Agir):** consolidar práticas efetivas no `CONTRIBUTING.md`, manter meta ou replanejar explicitamente o que não funcionou.

## 5.2 Priorização sugerida

| ID | Prioridade | Ação | Evidência esperada |
|---|---|---|---|
| A01 | **P0** | Retrospectiva de grupo com ata verdadeira | Ata assinada/validada |
| A02 | **P0** | Novo ciclo TDD genuíno em branch | 3 commits e logs RED/GREEN/REFACTOR |
| A03 | **P0** | Corrigir paths do E2 e links | Testes reproduzíveis, docs clicáveis |
| A04 | P1 | Baseline upstream fiel | Diff, SHA e logs |
| A05 | P1 | Registrar horas novas | CSV preenchido, metodologia |
| A06 | P1 | Atualizar E6 | Painel e dados após merges |
| A07 | P1 | Matriz de requisitos P1 | Requisito→teste→resultado→commit |
| A08 | P2 | Experimento controlado manual × IA | Protocolo pareado, tempo e defeitos |
| A09 | P2 | Arquivar revisões e checks dos PRs | Links e screenshots com contexto |

**Prioridades P0/P1/P2 são decisões sugeridas**, não aprovadas pelo grupo. O backlog completo possui prazos, papéis e aceite no CSV anexo.

## 5.3 Monitorar ações sem simular progresso

| Campo de controle | Como preencher |
|---|---|
| Dono | Nome de integrante que aceitou a atividade |
| Início/fim | Datas reais, não inferidas por Git |
| Evidência | Link para PR, commit, ata ou log |
| Estado | `não iniciada`, `em andamento`, `concluída`, `cancelada` |
| Verificação | Outra pessoa valida o aceite sempre que possível |

**Não apagar falhas passadas:** elas explicam a evolução do processo e servem à retrospectiva. Correções devem aparecer em novos commits e artefatos.

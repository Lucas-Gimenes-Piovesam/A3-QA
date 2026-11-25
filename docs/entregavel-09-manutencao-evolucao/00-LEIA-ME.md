# Entregável 9 — Manutenção e evolução do sistema legado

**Disciplina:** Gestão e Qualidade de Software · A3/2026.2  
**Projeto:** [Expense Tracker — A3-QA](https://github.com/Lucas-Gimenes-Piovesam/A3-QA)  
**Caminho escolhido:** Sistema existente ou legado  
**Estado inspecionado:** `main` no commit [`5bbc42c`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd), em **25/11/2026 (UTC)**.  
**Tipo de trabalho:** avaliação de mudanças, análise de impacto, decisão arquitetural e planejamento; **não** é uma implementação automática de todas as solicitações.

## Resposta ao enunciado

O professor exige **ao menos 3 solicitações de mudança classificadas por tipo e impacto** e, para sistema legado, uma escolha justificada entre **refatorar, modernizar ou substituir**. Neste pacote há **4 solicitações** com rastreabilidade, cenários de aceitação, riscos, dependências, decisões, esforço relativo e status verdadeiro.

| ID | Natureza | Problema/oportunidade | Situação | Prioridade |
|---|---|---|---|---|
| [CR-09-01](solicitacoes/CR-09-01-validacao-monetaria.md) | **Corretiva** | Bloquear valores financeiros `NaN`, infinitos e inadequados | **Implementada antes do E9**; evidência por código e CI | P1 |
| [CR-09-02](solicitacoes/CR-09-02-persistencia-atomica.md) | **Preventiva** | Evitar perda de arquivo em gravação interrompida/erro de I/O | **Proposta**, não implementada | P1 |
| [CR-09-03](solicitacoes/CR-09-03-datas-importadas.md) | **Corretiva potencial** | Validar datas também ao ler `expenses.txt` | **Proposta**; risco identificado por inspeção, não defeito reproduzido | P2 |
| [CR-09-04](solicitacoes/CR-09-04-separar-interface-dominio.md) | **Perfectiva** | Separar menu, regras e persistência para reduzir acoplamento | **Proposta**, não implementada | P2 |

**Decisão:** [ADR-09 — Refatorar progressivamente](03-adr-decisao-refatorar-modernizar-substituir.md). Modernização pontual poderá ser avaliada depois; substituição total não é proporcional ao produto, evidências e prazo acadêmico.

## Índice dos artefatos

- [01 — Inspeção de código e critérios de classificação](01-inspecao-e-metodo.md)
- [02 — Matriz de mudanças e impactos](02-matriz-solicitacoes-e-impactos.md)
- [03 — Decisão arquitetural registrada (ADR)](03-adr-decisao-refatorar-modernizar-substituir.md)
- [04 — Sequência de evolução, testes e rollback](04-plano-de-execucao-e-regressao.md)
- [05 — Rastreabilidade, evidências e limites](05-evidencias-e-limitacoes.md)
- [06 — Checklist de revisão e aprovação do grupo](06-checklist-e-aprovacao.md)
- [Painel visual estático](painel-manutencao.html)
- [Solicitações detalhadas](solicitacoes/)

**Dados estruturados e verificáveis:** `evidencias/entregavel-09/solicitacoes.csv`, `impactos.csv`, `decisao-alternativas.csv`, `inspecao-repositorio.json`, `validacao-local.txt`. 
**Validador:** `python3 scripts/validar_entregavel_09.py` (biblioteca padrão, não altera o projeto Java).

## Publicação correta

Criar uma branch curta `docs/entregavel-09-manutencao-evolucao` a partir da `main`. Enviar **apenas as pastas `docs/`, `evidencias/` e `scripts/` deste ZIP**, a partir da raiz. Não sobrescrever `src/`, não reenviar código antigo e não alterar o estado das solicitações propostas para "concluído" sem PR de implementação. Abrir PR, solicitar revisão de outro integrante e exigir `ci-quality-gate` verde antes do merge.

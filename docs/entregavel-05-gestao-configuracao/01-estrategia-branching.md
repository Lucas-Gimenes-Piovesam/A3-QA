# 1. Estratégia escolhida: trunk-based development

## 1.1 Critério de escolha

O A3-QA é um projeto de escopo reduzido, conduzido em iterações curtas para estudar qualidade sobre um programa de terminal em Java. Sua principal fonte de mudanças é a implementação de testes, ajustes financeiros, documentação e automação CI. A presença de apenas uma linha de evolução do produto reduz a necessidade de manter branches paralelas de suporte.

Por esse motivo, foi escolhido **trunk-based development** em lugar de **Git Flow**.

| Critério | Trunk-based (adotado como política) | Git Flow (descartado neste contexto) |
|---|---|---|
| Branch principal | Uma `main` como referência de integração | `main`/`develop` e branches de release/hotfix |
| Alteração | Branch curta e PR pequeno | Ramificações mais longas e vários fluxos |
| Integração CI | Frequente; falhas são visíveis cedo | Testes podem ficar afastados da branch principal por mais tempo |
| Custo de coordenação do grupo | Menor | Maior para um sistema acadêmico simples |
| Uso mais apropriado | Evolução incremental única | Várias versões simultâneas e calendário formal de releases |

**Justificativa:** privilegiamos integração frequente, revisões menores, identificação rápida de regressões e rastreabilidade das intervenções. A estratégia **não** dispensa testes ou aprovações; depende de status de CI obrigatório antes de integrar.

## 1.2 Regras do fluxo

1. `main` é a referência estável **desejada**. Por enquanto, a CI está vermelha; não chamá-la de linha estável de produção.
2. Criar uma branch curta desde `main`: `docs/entregavel-05-gestao-configuracao`, `test/validacao-orcamento`, `fix/filtro-categoria`, `ci/melhorar-cobertura`.
3. Fazer commits específicos com mensagens significativas; registrar hipótese, evidência de teste e risco no Pull Request.
4. Abrir PR para `main`, solicitar revisão independente quando houver integrantes disponíveis, checar o job obrigatório `ci-quality-gate`.
5. Somente integrar quando os critérios exigidos forem atendidos; excluir branch após merge.
6. Criar tag **imutável por convenção** em commit identificado de versão; nunca mover tag para mascarar um gate vermelho.

```text
main (referência de integração)
   ├─ docs/entregavel-05-gestao-configuracao ── commit ── PR ── CI ── merge
   ├─ test/novos-casos-financeiros ───────────── commit ── PR ── CI ── merge
   └─ fix/regra-de-orcamento ─────────────────── commit ── PR ── CI ── merge
                                                           |
                                              tag / release após critérios
```

## 1.3 Política de proteção de branch

Configurar em **Settings → Branches** (ou **Settings → Rules → Rulesets**): proteção de `main`, **require a pull request before merging** e **require status checks to pass**, selecionando o check **`ci-quality-gate`**. Se disponível para o plano e permissões, restringir push direto e exigir resolução de conversas de revisão. Registrar captura da regra e um PR não conforme bloqueado. O YAML por si só **não** bloqueia merge.

**Condição real em 25/11/2026 UTC:** API de branches retornou `main` com `protected: false`; GitHub Actions do commit `3d37fd5` apresentou 28 testes aprovados e falha no critério de cobertura. Esta política ainda não está demonstrada como ativa.

## 1.4 Como tratar o histórico já existente

A história atual contém commits diretos em `main`, exclusões de diretórios duplicados e um commit GREEN vazio. **Não reescrever nem apagar esses fatos** para simular um processo perfeito. Descrever que a política trunk-based foi definida no Entregável 5 e demonstrá-la a partir de um PR novo. Esta decisão garante rastreabilidade sem falsificar a cronologia.

# Contribuição e governança — A3-QA

## Estratégia

Adotamos como **estratégia proposta a ser demonstrada** o **trunk-based development**: uma branch principal (`main`) e branches de curta duração para alterações específicas, integradas por Pull Request. Não adotamos Git Flow, pois não há equipes de manutenção e versões paralelas que justifiquem branches `develop`/`release` permanentes.

## Convenções

- Branches: `docs/entregavel-05-gestao-configuracao`, `test/casos-limite-orcamento`, `fix/validacao-despesa`, `ci/cobertura-financeira`, `feat/<resumo>`.
- Commits: prefixos `docs:`, `test:`, `fix:`, `refactor:`, `ci:`, `chore:` e `feat:` com mensagem objetiva e verificável.
- Escopo: um objetivo principal por PR; evitar misturar correção financeira com mera formatação.
- Revisão: descrever problema, impacto, evidência antes/depois, como reproduzir, riscos e relação com requisitos/entregável. Revisão de colega sempre que possível, sem inventar aprovação.
- Segredos: não versionar dados financeiros pessoais, senhas, tokens, `expenses.txt` ou `budgets.txt`.

## Fluxo para o próximo PR

1. Criar branch curta a partir da última `main` usando o menu de branches do GitHub (por exemplo, `docs/entregavel-05-gestao-configuracao`).
2. Alterar somente arquivos do objetivo. Para o Entregável 5: `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `docs/entregavel-05-gestao-configuracao/` e `evidencias/entregavel-05/`.
3. Commitar com mensagem `docs: documentar gestao de configuracao e releases`.
4. Abrir **Pull Request** da branch para `main`, incluindo testes executados, capturas e riscos.
5. Verificar `ci-quality-gate` no PR. Se estiver vermelho, registrar o bloqueio; corrigir as falhas em novos commits. **Não alegar merge protegido ou aprovado enquanto o gate estiver vermelho.**
6. Após a CI verde e revisão, fazer merge; apagar a branch temporária; registrar a URL do PR no relatório.

## Modelo de descrição de Pull Request

```markdown
### Objetivo
Qual requisito da A3 este PR atende?

### Alterações
- Arquivos e comportamento alterados

### Evidências
- Run do GitHub Actions: [URL]
- Testes executados: [comando e resultado]
- Cobertura real: [valores] ou não medida
- Revisão por pares: [pessoa/data] ou pendente

### Riscos e limitações
- [descrição]

### Checklist
- [ ] O PR é focado
- [ ] Os links de arquivos funcionam
- [ ] Compilação e JUnit conferidos
- [ ] O gate exigido passou, antes do merge
- [ ] README/changelog atualizados se aplicável
```

## Política para falhas de CI

Falha de build, testes, Checkstyle ou cobertura não será ocultada com aprovação manual falsa. Se o gate impedir o merge, corrigir a causa real ou registrar a limitação e manter o PR aberto. Alteração de limites exige justificativa explícita e revisão do Plano de Qualidade.

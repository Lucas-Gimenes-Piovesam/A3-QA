# 4. Execução no GitHub, critérios de aceite e evidências

## 4.1 Preparação dos arquivos

No repositório, garantir que `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md` fiquem na **raiz**, e que as pastas `docs/entregavel-05-gestao-configuracao/` e `evidencias/entregavel-05/` permaneçam no nível correto. A atualização do README pode exigir **Edit this file** no GitHub, pois já existe arquivo com mesmo caminho.

## 4.2 Demonstração de trunk-based: branch → PR

1. Ir à página principal do repositório e clicar no seletor de branch que mostra `main`.
2. Digitar `docs/entregavel-05-gestao-configuracao`; selecionar **Create branch ... from main**.
3. **Trocar para essa nova branch** antes do upload. Conferir que o seletor mostra o nome dela, não `main`.
4. Clicar **Add file → Upload files**, enviar apenas os novos arquivos: `CONTRIBUTING.md`, `CHANGELOG.md`, pasta `docs` (com subpasta do Entregável 5) e `evidencias` (subpasta do Entregável 5). Esses uploads não apagam outras pastas quando os caminhos são novos.
5. Para atualizar `README.md`, abrir o arquivo **nessa branch**, clicar no lápis, substituir seu conteúdo pelo `README.md` deste pacote e salvar o commit **na branch**. Conferir que não foi alterada a `main` diretamente.
6. Mensagens sugeridas: `docs: adicionar politica de branching e releases` e `docs: atualizar readme e changelog do projeto`.
7. Acessar **Pull requests → New pull request**; `base: main`, `compare: docs/entregavel-05-gestao-configuracao`; título `docs: Entregável 5 — gestão de configuração`. Descrever a finalidade e anexar links para os commits.
8. Registrar URL do PR e dos runs de CI; solicitar revisão por um colega se possível. **Não marcar como aprovado o PR que ainda tem gate vermelho.**

## 4.3 Demonstrar o bloqueio de merge

- Em **Settings → Branches** ou **Rules → Rulesets**, proteger a `main` exigindo **PR** e o status `ci-quality-gate`.
- No PR aberto, confirmar que o status foi executado e está vermelho por cobertura, e que o GitHub indica que o merge não está permitido.
- Guardar captura que contenha nome do PR, status e mensagem de bloqueio. Isso constitui evidência prática do gate; somente o arquivo YAML não basta.
- Para concluir a integração, aumentar a cobertura de verdade e corrigir eventuais falhas, sem diminuir a meta somente para ficar verde.

**Cuidado:** o bloqueio pode depender das permissões/plano e do escopo das regras. Se a tela de Rules estiver indisponível, registrar o impedimento como limitação real e não inventar prova.

## 4.4 Tags e releases

- Seguir [02-versionamento-tags-releases.md](02-versionamento-tags-releases.md) para criar `v0.1.0-baseline` no SHA inicial certo e publicar uma **pre-release**.
- Copiar [05-notas-da-release-baseline.md](05-notas-da-release-baseline.md) como descrição.
- Registrar URL da tag, URL da release, SHA alvo e captura da página de releases.
- Adiar `v0.2.0-qa-piloto` até existir uma versão de corte documentada.

## 4.5 Checklist de avaliação

- [x] GitHub inicial e histórico de commits existente, inspecionado em 25/11/2026 UTC.
- [x] Trunk-based escolhido e justificado em documento.
- [x] Convenções de branches, commits, PR, tags e releases **documentadas** neste pacote.
- [x] README/CHANGELOG/CONTRIBUTING **preparados** neste pacote.
- [ ] Arquivos do Entregável 5 realmente publicados nos caminhos corretos.
- [ ] Branch curta criada e PR aberto para `main`, com URL registrada.
- [ ] Proteção de branch exigindo status `ci-quality-gate` configurada.
- [ ] Merge de PR não conforme comprovadamente bloqueado.
- [ ] Tag real `v0.1.0-baseline` criada sobre o commit certo.
- [ ] GitHub Release experimental publicada e referenciada.
- [ ] Revisão do grupo/ata preenchida com nomes e datas reais.
- [ ] `CHANGELOG.md` atualizado com a URL da release real, quando publicada.

## 4.6 Registro final para o relatório acadêmico

```text
Branch demonstrativa: [nome]
Commit do README: [SHA/link]
Pull Request: [URL]
Revisor: [pessoa e data reais / pendente]
Workflow no PR: [URL e status]
Prova de bloqueio: [arquivo/URL]
Tag de baseline: [URL + SHA]
GitHub Release: [URL + classificação pre-release]
Decisão de manter/corrigir gate: [fato e justificativa]
```

**Nenhum campo acima deve ser preenchido com resultados presumidos.**

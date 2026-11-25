# 2. Versionamento, tags e releases

## 2.1 Política de versões

Utilizar [SemVer](https://semver.org/lang/pt-BR/) como convenção acadêmica: `vMAJOR.MINOR.PATCH[-identificador]`.

- `MAJOR`: mudanças incompatíveis nos contratos externos, se aplicável.
- `MINOR`: funcionalidades e evolução compatível relevante.
- `PATCH`: correções e ajustes compatíveis.
- Sufixos `-baseline` e `-qa-piloto`: identificam **pré-releases de estudo**, não produtos homologados.

Uma tag identifica **um commit específico**. Uma GitHub Release publica notas relativas àquela tag. A existência de um arquivo `CHANGELOG.md` não substitui nenhum dos dois objetos no GitHub.

## 2.2 Tags e releases propostas — NÃO CRIADAS

| Objeto | Commit pretendido | Motivo | Condição |
|---|---|---|---|
| `v0.1.0-baseline` | [`6b55f9d`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571) | Marco inicial do grupo, antes dos entregáveis 1–5 | Release marcada **Pre-release**, deixando explícita a cópia reconstruída e a ausência de cobertura |
| `v0.2.0-qa-piloto` | SHA do futuro merge/commit verificado, **a preencher** | Consolidação de testes, CI e documentação | Publicar somente quando a equipe decidir pela versão, registrando o resultado real do gate e as pendências |

> **Rastreabilidade:** a primeira referência é um **marco da versão de trabalho do grupo**, não uma prova de clone literal do repositório original. Para o segundo marco, ainda não existe SHA definido. Não criar uma release `stable` enquanto o quality gate estiver vermelho.

## 2.3 Como criar uma tag/release pelo site (sem terminal)

1. Acessar https://github.com/Lucas-Gimenes-Piovesam/A3-QA/releases.
2. Clicar em **Draft a new release** (ou **Create a new release**).
3. Em **Choose a tag**, digitar `v0.1.0-baseline` e selecionar **Create new tag**.
4. Conferir o campo **Target**: apontar para o **commit `6b55f9d3f38012f1bcf1e05b272740bdb0ce8571`**, e não automaticamente para a versão mais recente de `main`. Se a interface não permitir selecionar esse SHA, **não publicar com o alvo errado**: usar o procedimento local com Git abaixo.
5. Título: `v0.1.0-baseline — marco inicial da A3-QA`.
6. Descrição: utilizar o texto de `05-notas-da-release-baseline.md`.
7. Marcar **Set as a pre-release**.
8. Publicar e registrar a URL real e a página da tag em `evidencias/entregavel-05/`.

### Alternativa: tag exata pelo Git (quando a interface não aceita SHA)

```bash
git fetch origin --tags
git tag -a v0.1.0-baseline 6b55f9d3f38012f1bcf1e05b272740bdb0ce8571 \
  -m "Marco inicial A3-QA: codigo reconstruido para estudo"
git push origin v0.1.0-baseline
```

Depois, criar a GitHub Release escolhendo a **tag existente** `v0.1.0-baseline`, com a opção **pre-release** habilitada. Não usar `--force` em tags de versão.

## 2.4 Release de evolução

A tag `v0.2.0-qa-piloto` só deve ser criada depois de identificar o SHA de corte, registrar execução real do gate e aprovar as notas. Exemplo de roteiro a seguir **apenas após** os pré-requisitos:

```bash
# exemplo de comando — substituir <SHA_APROVADO> pelo commit verificado
git tag -a v0.2.0-qa-piloto <SHA_APROVADO> -m "Piloto QA A3"
git push origin v0.2.0-qa-piloto
```

A Release deve declarar explicitamente: escopo, o que mudou, testes executados, percentuais reais, problemas conhecidos, limitações da análise IA × manual, instruções de execução e links do CI. Se o gate reprovar, classificar o pacote como **experimental e não aprovado**, nunca como `stable`.

## 2.5 Entrega contínua: aplicabilidade ao produto

O Expense Tracker é um **programa CLI** com dados locais, sem servidor/ambiente de produção. Não há necessidade de deploy automático. Faz sentido disponibilizar versão de estudo via **GitHub Release e código-fonte do commit tagueado**; o workflow pode entregar os relatórios do build como artefatos de CI. Isso é distribuição/versionamento, **não** deploy contínuo de serviço.

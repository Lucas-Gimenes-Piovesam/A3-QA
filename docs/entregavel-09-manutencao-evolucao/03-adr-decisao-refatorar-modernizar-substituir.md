# ADR-09 — Escolha de evolução para o legado: refatoração incremental

**Status:** proposta técnica justificada, sujeita à validação do grupo.  
**Data da proposta:** 25/11/2026 (UTC).  
**Base analisada:** [5bbc42c](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/5bbc42c25735d6e6c54bb9e81ea3f03db34ff7bd).

## Contexto

O Expense Tracker é um programa Java de terminal, com armazenamento simples em arquivos, regras de orçamento, somas, exportação CSV e uma suíte JUnit executável. A CI já roda Maven, JaCoCo e Checkstyle. O escopo acadêmico prioriza corretude de valores, preservação dos dados e manutenção, **não** uma nova interface web ou implantação em produção. O projeto tem prazo curto até a apresentação no início de dezembro.

## Opções consideradas

### A — Refatorar o código atual (*recomendado agora*)

Separar gradualmente as responsabilidades da classe `ExpenseTracker`, fortalecer testes, padronizar regras de entrada e robustecer persistência **preservando a CLI e os formatos de arquivos sempre que possível**.

**Benefícios:** mudanças menores e reversíveis; reaproveita funcionalidades existentes, testes e histórico; menor custo de migração. **Custos:** coexistência temporária com partes legadas; limitações do armazenamento/`double` não desaparecem por mágica.

### B — Modernizar a arquitetura e a plataforma (*etapa futura condicionada*)

Avaliar modularização mais profunda, `BigDecimal`/representação em centavos, armazenamento transacional/banco de dados ou distribuição empacotada. **Benefícios:** maior suporte a precisão/escala e integrações; **custos:** conversão de dados existentes, mudança de contratos, novas falhas e testes de migração. Não há demanda externa validada que obrigue essa mudança neste momento.

### C — Substituir o sistema integralmente (*não recomendada agora*)

Reescrever a aplicação inteira ou trocar por outra solução. **Benefício potencial:** arquitetura nova sem restrições estruturais; **custos:** perda do valor do legado testado, retrabalho, regressão de funções antigas, custo de migração e prazo acadêmico desproporcional ao ganho demonstrado.

## Matriz de decisão multicritério (julgamento inicial, não medição factual)

Escala: 1 = muito desfavorável; 5 = muito favorável. Critérios e pesos refletem **prioridades propostas**. O escore é uma ferramenta transparente para discussão, não prova matemática de superioridade.

| Critério | Peso | Refatorar | Modernizar | Substituir |
|---|---:|---:|---:|---:|
| Preservar funcionalidades e dados | 25% | 5 | 4 | 2 |
| Esforço e prazo acadêmico | 25% | 5 | 3 | 1 |
| Menor risco de regressão | 20% | 4 | 3 | 1 |
| Aumentar testabilidade futura | 20% | 4 | 5 | 4 |
| Baixo risco de migração | 10% | 5 | 3 | 1 |
| **Pontuação ponderada** | **100%** | **4,60/5** | **3,65/5** | **1,85/5** |

**Cálculo:** soma de `peso × nota` (pesos em fração). Pesos e notas devem ser discutidos/ratificados em ata do grupo.

## Decisão recomendada e justificativa

**Escolher A — refatorar incrementalmente**, começando por persistência e validação de entrada, seguida de extração de serviços de domínio. A decisão preserva o investimento em testes e evita ampliar o escopo antes de medir custo/benefício. Considerar modernização direcionada somente se aparecerem requisitos documentados de precisão decimal, concorrência, volume de dados ou distribuição. **Não há evidência que justifique substituição total** agora.

## Consequências, restrições e critérios de revisão da ADR

- Mudanças em código só entram em `main` por PR, revisão e quality gate.
- Antes de alterar CSV ou dados existentes, criar backup de teste e plano de compatibilidade; exigir teste de leitura de arquivo antigo.
- Não associar “modernizar” automaticamente a “melhorar”: mensurar impacto em defeitos, regressão, custo, requisitos e testabilidade.
- **Reabrir a decisão** caso haja (a) requisito de múltiplos usuários/concorrência, (b) inconsistência monetária reproduzida que exija novo modelo, (c) crescimento dos arquivos inviável ou (d) custo de refatoração superior ao de migração comprovado por estimativa revisada.
- A decisão ainda não significa que CR-09-02 a 04 foram executadas.

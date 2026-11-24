# Entregável 1 — Plano de Qualidade e Garantia da Qualidade de Software (SQA)

**Disciplina:** Gestão e Qualidade de Software — A3 (2026/2)  
**Caminho:** Sistema existente ou legado  
**Projeto:** Expense Tracker — análise de qualidade e geração de testes com IA  
**Carta de Inovação:** IA a serviço da qualidade  
**Repositório do grupo:** https://github.com/Lucas-Gimenes-Piovesam/A3-QA  
**Software original:** https://github.com/chaudhary-lakshay/Expense-Tracker  
**Versão do plano:** 1.0 — 24/11/2026  
**Status:** plano proposto; execução e aprovação do grupo ainda pendentes.

> **Rastreabilidade.** O estado do repositório descrito neste documento foi inspecionado no commit [`6b55f9d`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571), de 24/11/2026. A referência pública do código-fonte é o commit [`b35ff1a`](https://github.com/chaudhary-lakshay/Expense-Tracker/commit/b35ff1a420499703d0c9ec10851a32468ba31f2a). Os seis arquivos Java do grupo apresentam as mesmas linhas **não vazias** dos respectivos arquivos originais, mas diferem em formatação/quebras de linha; por isso, a cópia atual não deve ser descrita como clone byte a byte. Não foram alteradas aqui as regras de negócio do código.

## 1. Objetivo, escopo e princípios

### 1.1 Objetivo geral

Estabelecer práticas, critérios de aceitação, revisões, medições e evidências que permitam **avaliar e melhorar a confiabilidade** do Expense Tracker, concentrando o esforço nos riscos das funcionalidades financeiras e fornecendo uma base controlada para comparar testes elaborados manualmente e testes gerados com auxílio de IA.

### 1.2 Objetivos específicos

1. Registrar a condição inicial do sistema antes de modificações e manter a identificação do commit avaliado.
2. Especificar e verificar regras de cadastro, atualização e validação de despesas, resumos financeiros e orçamento mensal.
3. Implantar testes automatizados reproduzíveis e acompanhar cobertura de decisões nos módulos críticos.
4. Definir um fluxo mínimo de revisão, rastreabilidade de alterações e auditoria de processo.
5. Comparar testes manuais e testes gerados com IA sob os mesmos requisitos e critérios de medição.
6. Registrar falhas, limitações, correções e decisões com evidências acessíveis no GitHub.

**Dentro do escopo:** aplicação Java de terminal, armazenamento em arquivos locais, regras financeiras, testes, documentação, métricas e integração contínua.  
**Fora do escopo nesta etapa:** desenvolver uma aplicação web, trocar a persistência por banco de dados, certificar conformidade ISO ou declarar desempenho superior da IA sem teste comparativo.

### 1.3 Política de qualidade

Adotamos como proposta de política que **nenhuma conclusão seja apresentada sem referência verificável** e que **alterações nas regras críticas não sejam incorporadas à branch principal antes de revisão e testes**. Em particular:

- **Evidência acima de declaração:** toda medição do relatório deverá apontar para arquivo, commit, execução de workflow, registro de teste ou ata. Resultados não medidos aparecerão como “não medido”, nunca como zero.
- **Preservação do referencial:** a versão inicial e os dados dos experimentos serão identificados por commit; correções serão feitas em commits posteriores, sem reescrever resultados antigos.
- **Revisão independente:** sempre que possível, quem revisar uma mudança será pessoa diferente de quem a desenvolveu; divergências ficam registradas na ata.
- **Prevenção de regressões:** uma correção de defeito financeiro deverá ter teste que falhe antes da correção e passe depois, com evidência reproduzível.
- **Uso responsável da IA:** prompts e saídas serão guardados; sugestões não serão consideradas corretas apenas por terem sido geradas pela IA. O grupo validará resultados esperados e registrará erros, retrabalho e alucinações.
- **Dados de teste:** utilizar apenas dados fictícios e não incluir informações financeiras pessoais, senhas ou tokens no repositório.
- **Não conformidade:** falhas classificadas como bloqueadoras não poderão ser tratadas como “concluídas” apenas porque a cobertura de código aumentou.

## 2. Módulos críticos e priorização baseada em risco

A prioridade foi definida **antes do experimento**, por avaliação qualitativa do impacto potencial no usuário e dos caminhos de entrada existentes no código. Os riscos são hipóteses de revisão, não frequência de incidentes observada em produção.

| Prioridade | Módulo / regra | Motivo da prioridade | Evidência de código para investigar |
|---|---|---|---|
| **P1 — crítica** | Validação de valores no cadastro/edição | Valores especiais ou impróprios podem contaminar os totais; uso de `Double.parseDouble` e comparação `amount <= 0` | [`ExpenseTracker.java`](../src/Expense_Tracker/ExpenseTracker.java): `addExpense` e `updateExpense` |
| **P1 — crítica** | Orçamento mensal e alerta de limite | Comparações incorretas podem deixar de alertar um gasto excessivo; orçamento é armazenado como `double` | [`ExpenseTracker.java`](../src/Expense_Tracker/ExpenseTracker.java): `manageBudget`, `warnIfOverBudget`; [`BudgetStorage.java`](../src/Expense_Tracker/BudgetStorage.java) |
| **P1 — crítica** | Resumo total/mensal e filtros | Totais incorretos comprometem a finalidade principal da aplicação | [`ExpenseTracker.java`](../src/Expense_Tracker/ExpenseTracker.java): `viewSummary`, `viewMonthlySummary`, `monthTotal`, `filterByCategory` |
| **P2 — importante** | Persistência de despesas e orçamento | Perda ou interpretação equivocada de arquivo compromete continuidade e consistência | [`ExpenseStorage.java`](../src/Expense_Tracker/ExpenseStorage.java), [`BudgetStorage.java`](../src/Expense_Tracker/BudgetStorage.java) |
| **P2 — importante** | CSV, exportação e leitura | Vírgulas e aspas precisam ser preservadas sem corromper os registros | [`CsvUtil.java`](../src/Expense_Tracker/CsvUtil.java), [`CsvUtilTest.java`](../src/Expense_Tracker/CsvUtilTest.java) |
| **P3 — secundária** | Mensagens e navegação no terminal | Influenciam a compreensão e a experiência, mas têm impacto indireto sobre os cálculos | [`ExpenseTracker.java`](../src/Expense_Tracker/ExpenseTracker.java): menu e tratamento de entradas |

**Critério de priorização:** P1 = possibilidade de produzir resultado financeiro errado; P2 = perda, corrupção ou inconsistência de registros; P3 = clareza/experiência do usuário. As prioridades serão reavaliadas após os primeiros testes.

## 3. Características da ISO/IEC 25010 priorizadas

Utilizamos como referência o **modelo de qualidade do produto da ISO/IEC 25010:2023**. A versão 2023 contém nove características; o projeto não reivindica certificação ou avaliação completa conforme a norma. Referência oficial: https://www.iso.org/standard/78176.html.

| Característica | Prioridade | Aplicação ao Expense Tracker | Como será avaliada |
|---|---|---|---|
| **Adequação funcional (functional suitability)** | **Muito alta** | Correção das regras de despesas, cálculos, filtros e orçamentos | Casos de teste com resultados esperados definidos previamente, incluindo limites e entradas inválidas; defeitos por regra |
| **Confiabilidade (reliability)** | **Muito alta** | Manter resultados previsíveis em execução repetida, reabertura e persistência | Reexecução da suíte, testes de gravação/leitura, rastreamento de regressões e falhas |
| **Manutenibilidade (maintainability)** | **Alta** | Permitir entender e modificar código legado e testar sem regressões | Revisão de código, análise estática, duplicações observadas, rastreabilidade de alterações e cobertura de decisões |
| **Capacidade de interação (interaction capability)** | **Média** | Mensagens claras de erro e tratamento de entradas via terminal | Inspeção orientada por cenários de entrada válida/inválida; checklist e registro de observações |
| **Segurança (security)** | **Média** | Evitar publicação de dados pessoais e entrada indevida em arquivos de teste | Revisão de dados usados, ignorados pelo Git e dos arquivos versionados; verificações simples de validação |

**Justificativa:** o programa gerencia registros financeiros locais; cálculos corretos e persistência confiável são mais relevantes que recursos novos. Manutenibilidade é importante porque o projeto envolve testes e mudanças em código existente. Interação e segurança serão verificadas sem ampliar desnecessariamente o escopo.

**Características não priorizadas nesta fase:** eficiência de desempenho, compatibilidade, flexibilidade e segurança operacional (*safety*). Não foram descartadas; somente não serão métricas principais sem necessidade demonstrada.

## 4. Padrões, ferramentas e convenções adotados

| Referência / ferramenta | Emprego no projeto | Estado em 24/11/2026 |
|---|---|---|
| **ISO/IEC 25010:2023** | Selecionar e justificar características de qualidade do produto | Referência definida neste plano |
| **SQA com revisão por pares e auditoria leve** | Prevenir erros de processo e manter evidência de aprovação | Processo definido; revisões formais ainda não registradas |
| **Git/GitHub, commits e pull requests** | Versionar fonte, requisitos, testes, resultados e aprovações | Repositório e commit inicial existentes; PRs/revisões pendentes |
| **Java / JDK** | Executar aplicação e testes | Código Java presente; execução do clone oficial ainda requer confirmação |
| **JUnit 5** | Automatizar testes unitários e de comportamento | A configurar; `CsvUtilTest.java` é uma verificação executável própria, não uma suíte JUnit |
| **Maven** | Padronizar build e execução de testes | A configurar |
| **JaCoCo** | Medir cobertura de linhas e decisões | A configurar; cobertura inicial não medida |
| **GitHub Actions** | Executar build, testes e verificações a cada contribuição | A configurar; nenhum workflow identificado no commit inspecionado |
| **Markdown, CSV/JSON e logs** | Preservar documentação e resultados reproduzíveis | Parte dos documentos e registros do piloto já existe |

As ferramentas planejadas **não serão descritas como já implantadas** até que os commits e os registros de execução comprovem sua configuração.

## 5. Metas de qualidade, critérios de aceite e justificativas

As metas são **propostas do grupo** e poderão ser revistas em ata após a linha de base reproduzível. Não representam resultados já alcançados.

| Indicador | Meta inicial | Justificativa e medição | Evidência exigida |
|---|---|---|---|
| **Cobertura de decisões — regras P1** | **≥ 90%** | Concentra o esforço nos desvios das regras financeiras em vez de impor uma meta genérica a todo código; relatório JaCoCo no escopo P1 | Relatório de cobertura por classe/método + commit |
| **Cobertura de linhas — regras P1** | **≥ 85%** | Complementa a análise de decisões; não substitui testes de comportamento | Relatório JaCoCo + suíte identificada |
| **Casos de entrada crítica** | **100% das classes de entrada P1 documentadas e executadas** | Não deixar sem verificação as fronteiras previamente especificadas (zero, negativos, números finitos e valores especiais) | Matriz requisito × teste × resultado |
| **Defeitos bloqueadores P1 abertos na entrega** | **0** | Não entregar uma melhoria com defeito conhecido que produza cálculo financeiro incorreto | Registro de defeitos e reexecução de regressões |
| **Mudanças nas regras P1** | **100% com revisão registrada** | Exige validação humana de alteração de alto risco | PR/ata com revisor, decisão e referência de execução |
| **Execução de CI nos commits candidatos a entrega** | **100% aprovados** | Evitar aceitar alteração que não compila ou quebre regressão | URL do workflow associado ao commit |
| **Hipótese da IA** | **Reduzir em ≥ 20% o tempo total, sem perder defeitos detectados** | Verificar benefício prático; tempo inclui geração, revisão, correção e execução | Registros cronometrados, testes das duas condições e comparativo |

**Regra de interpretação:** percentuais de cobertura não medem sozinhos eficácia dos testes. As metas de cobertura somente serão consideradas atendidas se os testes verificarem as respostas corretas do programa, incluindo comportamentos de risco.

## 6. Processo de SQA e revisões planejadas

### 6.1 Papéis mínimos

- **Autor da alteração:** documenta o objetivo, desenvolve e executa os testes.
- **Revisor (outro integrante):** verifica requisitos, riscos, testes, evidências, consistência e aprova ou solicita ajustes.
- **Responsável por SQA / registro:** mantém atas, acompanha pendências e verifica links das evidências. Os papéis podem alternar entre integrantes; nomear responsáveis no primeiro encontro do grupo.

### 6.2 Ciclo de revisão por pares (obrigatório para mudanças P1)

1. Abrir uma alteração identificando módulo, regra de negócio, risco e evidência existente.
2. Verificar requisitos e resultados esperados **antes** de aceitar testes gerados pela IA.
3. Fazer **inspeção de código**: tratamento de valores inválidos, cálculos, mensagens, alterações em persistência e regressões possíveis.
4. Fazer **walkthrough dos testes**: autor demonstra caso de entrada, expectativa e resultado real; revisor verifica qualidade do oráculo do teste.
5. Executar testes e conferir os relatórios de cobertura/CI (quando a infraestrutura estiver pronta).
6. Registrar **ata de revisão** com participantes, commit, não conformidades, responsáveis, decisão e links. Usar [`docs/atas/modelo-ata-revisao.md`](atas/modelo-ata-revisao.md).
7. Somente então classificar como aprovado, aprovado com pendências não bloqueadoras ou reprovado.

**Periodicidade:** pelo menos uma revisão por módulo P1 concluído, uma revisão dos materiais do experimento IA versus manual e uma revisão final antes da apresentação. As datas e os nomes devem ser preenchidos pelo grupo, não presumidos.

### 6.3 Critérios mínimos de aprovação

- O escopo da alteração e a regra de negócio estão descritos.
- O resultado esperado foi validado por integrante, não simplesmente copiado da IA.
- Há casos positivos, negativos e de fronteira pertinentes à regra alterada.
- Os resultados, logs e eventuais defeitos têm caminhos/URLs verificáveis.
- Não há defeito bloqueador P1 conhecido sem decisão explícita do grupo.
- A ata registra **aprovado**, **aprovado com ressalvas** ou **reprovado**; o estado do workflow não substitui a revisão humana.

## 7. Auditoria simples do processo

**Método:** conferir, no GitHub, existência e rastreabilidade de: (i) fonte e licença; (ii) identificação de versão; (iii) plano e riscos; (iv) testes; (v) cobertura; (vi) CI; (vii) revisões; (viii) evidências dos experimentos. Cada critério terá estado **Conforme / Parcial / Não conforme / Não aplicável**, com link e ação corretiva.

**Auditoria inicial executada — 24/11/2026:** inspeção documental/estrutural do commit [`6b55f9d`](https://github.com/Lucas-Gimenes-Piovesam/A3-QA/commit/6b55f9d3f38012f1bcf1e05b272740bdb0ce8571). O registro de achados está em [`docs/auditorias/01-auditoria-inicial.md`](auditorias/01-auditoria-inicial.md).

**Reauditoria planejada:** depois de configurar Maven/JUnit/JaCoCo e GitHub Actions, e antes da entrega final. Não serão inventados resultados de reauditoria.

### 7.1 Condições que bloqueiam a aprovação final

- Ausência de rastreabilidade da origem e do commit sob teste.
- Ausência de registros de execução dos testes e de revisão das mudanças P1.
- Metas informadas como cumpridas sem evidência correspondente.
- Cobertura não medida apresentada como 0% ou como meta já alcançada.
- Defeitos financeiros bloqueadores conhecidos sem tratamento/decisão formal.

## 8. Plano de evidências e organização no repositório

| Item de SQA | Local indicado | Situação na elaboração deste plano |
|---|---|---|
| Proposta de projeto | [`docs/proposta-inicial.md`](proposta-inicial.md) | Já disponível |
| Relatório exploratório de linha de base e piloto | [`docs/linha-base-e-piloto.md`](linha-base-e-piloto.md) | Já disponível; **não é resultado comparativo definitivo** |
| Medições exploratórias | [`evidencias/`](../evidencias/) | Já disponíveis; exigem reprodução no código oficial |
| Plano SQA | `docs/01-plano-qualidade-sqa.md` | Este documento |
| Auditoria inicial | `docs/auditorias/01-auditoria-inicial.md` | Registro de inspeção de 24/11/2026 |
| Atas de revisão | `docs/atas/ATA-YYYY-MM-DD-assunto.md` | Ainda não realizadas; modelo disponível |
| Casos manuais | `tests/manuais/` | A desenvolver |
| Casos gerados por IA, prompts e critérios de validação | `tests/ia/` | A desenvolver para o estudo controlado |
| Relatórios de cobertura e CI | `evidencias/cobertura/` + GitHub Actions | A gerar após integração |
| Registro de defeitos | `docs/defeitos/` | A abrir à medida que regras e resultados forem confirmados |

## 9. Critério para conclusão deste entregável

O **Plano de Qualidade e SQA** estará documentalmente preparado quando (a) este arquivo e a auditoria inicial estiverem versionados, (b) o grupo preencher os responsáveis e aprovar as metas, e (c) ao menos uma revisão efetiva produzir sua ata assinada/validada pelos participantes. **Ter o plano escrito não significa que todo o processo foi executado.**

## 10. Referências e origem

- Enunciado da disciplina: **Proposta de Trabalho A3 — Gestão e Qualidade de Software 2026/2**, Jessé Guimarães; entregável 1: plano de qualidade e SQA.
- ISO/IEC. **ISO/IEC 25010:2023 — Product quality model**. https://www.iso.org/standard/78176.html
- Código original: https://github.com/chaudhary-lakshay/Expense-Tracker (MIT), commit `b35ff1a420499703d0c9ec10851a32468ba31f2a`.
- Código e dados do grupo: https://github.com/Lucas-Gimenes-Piovesam/A3-QA, commit de inspeção `6b55f9d3f38012f1bcf1e05b272740bdb0ce8571`.

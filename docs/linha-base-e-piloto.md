# A3 — Expense Tracker: linha de base e experimento-piloto com IA

**Data da análise:** 24/11/2026  
**Caminho:** Sistema existente ou legado  
**Carta de inovação:** IA a serviço da qualidade  
**Repositório consultado:** https://github.com/chaudhary-lakshay/Expense-Tracker  
**Escopo:** cadastro, validação de valores, resumos financeiros, orçamento mensal e CSV.

> **IMPORTANTE — PROVENIÊNCIA:** foi possível consultar todos os seis arquivos Java da branch `main` publicada no GitHub, mas o ambiente não permitiu clonar/baixar automaticamente o repositório. Os arquivos da pasta `src` foram reconstruídos localmente a partir do conteúdo público consultado. A reprodução dos testes nesta cópia **não comprova identidade byte a byte com um commit oficial**. Para uma entrega científica definitiva, o grupo deve clonar o repositório, registrar o SHA do commit, reexecutar os scripts e guardar os logs.

## 1. Hipótese mensurável

Acreditamos que usar IA para sugerir e implementar testes automatizados reduzirá em pelo menos **20% o tempo total de criação, revisão e execução de testes**, **sem reduzir a capacidade de detectar defeitos**, em comparação com testes elaborados manualmente para as mesmas funcionalidades. A meta de 20% ainda **não foi avaliada**, porque o tempo de produção de testes por uma equipe humana independente não foi coletado.

## 2. Linha de base — evidências medidas

| Indicador | Medição | Método / observação |
|---|---:|---|
| Arquivos Java | 6 | Contagem de `.java` na estrutura pública |
| Linhas totais nos arquivos Java | 603 | Inclui linhas em branco e comentários; não é LOC funcional |
| Compilação | 7/7 bem-sucedidas | `javac` (OpenJDK 21), compilação limpa em diretórios temporários |
| Tempo médio de compilação | **0,880 s** | 7 medições: 0,7616; 0,8343; 0,8040; 0,9802; 0,8087; 0,9991; 0,9714 s |
| Teste existente de CSV | **4/4 cenários concluídos** | `CsvUtilTest.main` imprime `All CSV round-trip checks passed.` |
| Testes exploratórios externos | **17 cenários observados** | Script Python externo, código-fonte da aplicação inalterado |
| Comportamentos que merecem análise | **5 observações** | 4 de validade financeira + descrição vazia (regra a confirmar) |
| Cobertura de linhas/ramos | **Não medida** | Sem JaCoCo ou equivalente neste ambiente; não confundir com 0% |
| Lead time do grupo | **Não medido** | Não existe fluxo de PR/issue do grupo avaliado nesta análise |
| Pipeline CI | **Não identificado** | Branch publicada não exibe diretório/configuração de workflow |

### Comportamentos encontrados

1. **Despesa `NaN`**: o cadastro aceita o valor, grava a despesa e o total passa a mostrar `NaN`.
2. **Despesa `Infinity`**: o cadastro aceita o valor, grava a despesa e o total passa a mostrar `Infinity`.
3. **Orçamento `NaN`**: o cadastro do orçamento aceita e persiste o valor inválido para comparações financeiras.
4. **Orçamento negativo**: o cadastro aceita `-100.0`; requer confirmar com os responsáveis se o domínio proíbe orçamentos negativos.
5. **Descrição vazia**: uma despesa sem descrição é aceita; confirmar se isso contraria os requisitos pretendidos.

Os itens 1–3 configuram evidências de falta de validação de números não finitos. Itens 4–5 dependem da formalização das regras de negócio antes de serem classificados como defeitos confirmados. Não significa que encontramos cinco bugs independentes.

**Observação sobre os 17 cenários:** todos produziram as saídas que o script exploratório procurava. Isso é *conformidade da observação*, não aprovação do requisito. Alguns testes tinham como objetivo justamente demonstrar que o sistema aceita entradas inadequadas.

## 3. Experimento — piloto de testes gerados por IA

O assistente gerou **dez testes de caixa-preta**, executados por automação externa (Python chamando o programa Java). Eles verificam comportamento das entradas e saídas no console, sem alterar o código original.

| ID | Cenário | Resultado do teste |
|---|---|---|
| IA-01 | Despesa positiva válida | Passou |
| IA-02 | Despesa zero deve ser rejeitada | Passou |
| IA-03 | Despesa negativa deve ser rejeitada | Passou |
| IA-04 | Texto não numérico deve ser rejeitado | Passou |
| IA-05 | Despesa `NaN` deve ser rejeitada | **Falhou** |
| IA-06 | Despesa `Infinity` deve ser rejeitada | **Falhou** |
| IA-07 | Orçamento `NaN` deve ser rejeitado | **Falhou** |
| IA-08 | Orçamento negativo deve ser rejeitado | **Falhou** — regra a confirmar |
| IA-09 | Gastos acima do orçamento devem gerar aviso | Passou |
| IA-10 | Soma mensal deve considerar somente o mês escolhido | Passou |

**Resultado do piloto:** dez testes executáveis, seis aprovados e quatro com falha de comportamento sob as regras de negócio propostas. O tempo de **1,12 s** refere-se somente à execução dos dez cenários, **não** ao tempo de geração ou revisão dos testes pela IA.

**Importante:** os quatro testes que falharam **não são quatro erros da IA**. Eles encontraram quatro desvios da aplicação em relação a regras propostas. Para identificar alucinações da IA, será necessária uma avaliação separada das sugestões e de suas premissas.

Os testes do piloto estão em `evidencias/testes_gerados_ia_piloto.py`; os resultados estão no JSON correspondente. Este piloto **não** usa JUnit nem possui integração com CI. Essas etapas técnicas ainda não foram concluídas.

## 4. Resultado e comparação

| Aspecto | Antes — projeto original | Depois — piloto com IA |
|---|---|---|
| Testes documentados/executáveis | 4 cenários de CSV | 10 casos adicionais em outras funcionalidades |
| Resultado da execução | 4 cenários concluídos | 6 aprovações; 4 falhas sob regras propostas |
| Problemas de validade financeira evidenciados | Não exercitados pelos testes CSV | `NaN`, `Infinity`, orçamentos inválidos |
| Cobertura de código | Não medida | Não medida |
| Tempo de desenvolvimento dos testes | Não medido | Não medido |
| Erros/alucinações da IA | Não se aplica | Não medidos |

**Limitação essencial:** como os conjuntos têm escopos diferentes, esta tabela não é um experimento controlado manual × IA e **não autoriza concluir que a IA é superior**, que aumentou a cobertura em determinado percentual ou que economizou 20% de tempo. É uma linha de base e um piloto de identificação de comportamentos sob teste.

## 5. Próximos passos para completar o A3

1. Clonar o GitHub original e identificar o **SHA exato** do commit usado.
2. Formalizar as regras de negócio (principalmente valores financeiros finitos e limites de orçamento).
3. Escolher um módulo único e gerar conjuntos independentes de testes **manuais** e **com IA**, com a mesma especificação e orçamento de tempo.
4. Criar testes automatizados executáveis em Java/JUnit e configurar Maven/Gradle + JaCoCo.
5. Registrar cobertura de linhas/ramos, defeitos detectados, testes inválidos/alucinações, tempo de criação/revisão/execução, além de logs.
6. Integrar os testes ao pipeline e versionar tudo no repositório do grupo.
7. Calcular o resultado frente à meta de redução de 20% e apresentar conclusões sem extrapolar os dados.

## Como reproduzir localmente

Exige Java/JDK 8+ e Python 3. A compilação foi realizada com OpenJDK 21.

```bash
cd A3_ExpenseTracker_linha_base
mkdir -p build
javac -encoding UTF-8 -d build src/Expense_Tracker/*.java
java -cp build Expense_Tracker.CsvUtilTest
python3 evidencias/testar_linha_base.py
python3 evidencias/testes_gerados_ia_piloto.py
```

A execução de `testar_linha_base.py` repete sete builds, usa pastas temporárias e sobrescreve o JSON de evidências com as novas medições locais; tempos vão variar com a máquina.

## Arquivos de evidência

- `evidencias/metricas_linha_base.json`: valores observados.
- `evidencias/resultados_cenarios.json`: entradas, saídas e resultados dos 17 cenários exploratórios.
- `evidencias/saida_teste_nativo.txt`: saída do teste já existente.
- `evidencias/resultado_piloto_ia.json`: resultados dos dez testes do piloto.
- `evidencias/testar_linha_base.py`: automação de medição de baseline.
- `evidencias/testes_gerados_ia_piloto.py`: testes gerados neste piloto.

**Licença do código original:** MIT, Copyright (c) 2024 Lakshay; consultar `LICENSE`.

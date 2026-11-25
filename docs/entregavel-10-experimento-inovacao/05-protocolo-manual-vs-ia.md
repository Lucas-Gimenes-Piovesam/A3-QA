# 5. Protocolo complementar — IA versus testes manuais

Este protocolo foi preparado para o grupo **executar**, e **não representa resultados já obtidos**. Ele responde à parte da carta que requer medir **acertos, erros e alucinações** e à hipótese de **redução de ≥20% do tempo** de produção e revisão de testes.

## 5.1 Preparação e cuidado com viés

1. **Congelar o alvo**: fixar o código `v0.1.0-baseline` e uma lista de requisitos aprovada pelo grupo (despesa positiva e finita, orçamento não negativo e finito, totais por mês, alerta acima do teto). Registrar SHAs.
2. **Revisor independente**: integrante que não criou os casos de IA revisa os requisitos **antes** de avaliar cada suíte; especialmente a regra de orçamento negativo.
3. **Separar braços**: um integrante escreve testes manualmente; o braço IA usa um prompt padronizado com a **mesma especificação, tempo e acesso ao código**. Quem escrever testes manuais não deve consultar os casos IA-01 a IA-10 (se os viu, registrar contaminação).
4. **Mesmo orçamento**: por exemplo, 30 minutos para criação e 15 para revisão/correção, medidos com início/fim reais, sem estimar de memória. Se o tempo acabar, registrar suíte parcial sem alterar retrospectivamente a meta.
5. **Revisor cego para origem quando possível**: trocar identificadores de autoria por `A`/`B` para julgar oráculos e defeitos sem preferência pela IA.
6. **Execução pareada**: rodar os testes contra as **mesmas versões e mesmos defeitos**, mantendo a correspondência por requisito. Repetir se possível com novo conjunto ou segundo integrante para avaliar variação.

**Aviso sobre este projeto:** o conjunto IA já está público desde o piloto; um estudo realmente cego pode não ser possível. É aceitável declarar essa limitação e usar uma nova especificação ainda não compartilhada para uma segunda rodada.

## 5.2 Como medir o esforço

Para cada braço registrar minutos de **especificar/escrever** + **revisar/ajustar** + **executar/diagnosticar**. A execução de Java em segundos não substitui essas etapas.

- `tempo_total_manual_min = soma das três etapas manuais`.
- `tempo_total_ia_min = soma de elaboração de prompt/geração + revisão/correção + execução/diagnóstico`.
- `economia_% = 100 × (manual − ia) / manual`.
- `capacidade_deteccao = número de falhas de referência distintas comprovadas pelo braço`.
- `taxa_oraculos_corretos = casos validados pelo revisor / casos avaliados`, quando há parecer.
- `alucinacoes = casos com requisito/API/funcionalidade inventada e não identificada explicitamente como proposta`, confirmados por revisor.

Um caso com `NaN` que **falha na baseline** pode ter um oráculo válido; não deve ser marcado como erro da IA automaticamente. Um teste que passa por coincidir com uma mensagem sem conferir persistência pode ter **oráculo fraco**; registrar essa deficiência.

## 5.3 Instrumentos (arquivos inicialmente sem julgamentos/tempos)

- [`registro_comparacao_manual_ia.csv`](../../evidencias/entregavel-10/registro_comparacao_manual_ia.csv): cronometria e rastreabilidade das duas suítes.
- [`revisao_oraculos.csv`](../../evidencias/entregavel-10/revisao_oraculos.csv): resultado da auditoria caso a caso, com classificação de possíveis erros e alucinações.
- [`modelo_ata_validacao.md`](../../evidencias/entregavel-10/modelo_ata_validacao.md): validação do experimento pelo grupo e consentimento sobre regras de domínio.

## 5.4 Prompt para uma rodada NOVA, não apresentado como prompt histórico

> Você está testando um Expense Tracker Java em terminal. A partir da especificação e dos arquivos de código anexados, gere no máximo dez casos automatizados para validar: despesa positiva e finita; rejeição de entradas inválidas; orçamento mensal não negativo e finito; alerta por excesso; total de um mês. Em cada caso forneça: requisito, entrada, saída esperada, classe de equivalência/limite e código reproduzível. **Não invente funções nem regras não apresentadas; quando houver lacuna, sinalize hipótese a validar**. Não edite o software. Identifique explicitamente qualquer incerteza.

Salvar **data, modelo usado, prompt integral e resposta integral** em evidências da nova rodada. O prompt acima **não é atribuído retroativamente** ao piloto de novembro.

## 5.5 Decisão final possível

A hipótese dos 20% só será **apoiada** se houver cronometrias comparáveis e a suíte IA não tiver pior detecção de falhas sob requisitos aceitos. Caso contrário, registrar **rejeitada** ou **inconclusiva**; resultados negativos continuam úteis para o aprendizado de SQA.

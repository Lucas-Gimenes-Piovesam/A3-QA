# 1. Hipótese e desenho experimental

## 1.1 Carta e problema investigado

A carta **IA a serviço da qualidade** propõe usar IA para gerar, priorizar ou revisar testes e código, medindo o que a IA **acerta, erra ou alucina**. Nosso problema é a aceitação de entradas financeiras inválidas em uma aplicação Java de despesas. Os erros podem contaminar totais, orçamentos e alertas.

## 1.2 Hipótese mensurável originalmente registrada

> Acreditamos que o uso de IA para gerar testes automatizados **reduzirá em pelo menos 20% o tempo total de elaboração, revisão e execução**, sem diminuir a capacidade de identificar defeitos em comparação com testes elaborados manualmente para as mesmas regras.

**H0:** a redução de esforço de IA versus manual é inferior a 20%, ou a IA detecta menos defeitos de referência.  
**H1:** a redução de esforço é de **pelo menos 20%**, sem perda de detecção de defeitos.

Regra de decisão proposta: `ganho_% = (tempo_manual_min - tempo_ia_min) / tempo_manual_min × 100`. A hipótese será considerada apoiada apenas se `ganho_% >= 20` **e** `defeitos_unicos_detectados_ia >= defeitos_unicos_detectados_manual` sobre as mesmas falhas de referência, com validação independente dos oráculos. Se o tempo manual for zero, a comparação é inválida. Tempos de execução de processos Java **não** são tempos de criação/revisão.

**Status desta hipótese:** **INCONCLUSIVA**, porque a equipe ainda não cronometrara o desenvolvimento/revisão de uma suíte manual independente. Este pacote não simula pessoas nem inventa horas.

## 1.3 Subexperimento efetivamente realizado: antes × depois

| Elemento | Protocolo operacional |
|---|---|
| Unidade experimental | Uma execução isolada de CLI por cenário IA-01…IA-10 |
| Entrada | Sequência de opções e dados de teste fixa, documentada em `experimento_10.py` |
| Oráculo | Trechos esperados/proibidos na saída + código de retorno igual a zero |
| Variável modificada | Versão do **software**: `v0.1.0-baseline` versus `main@f4abe2d` |
| Variáveis controladas | Mesmo script, mesmos dez casos, mesmo `javac`/`java`, pastas temporárias isoladas |
| Resultado | Quantos casos satisfazem o oráculo, quais desvios desapareceram, quantas regressões houve |
| Reprodutibilidade | Script compila a versão histórica e a atual isoladamente; resultados JSON e CSV |

**Diferença entre os dois desenhos:** o subexperimento avalia conformidade do **software** após intervenção; a hipótese principal avalia **produtividade/qualidade da geração de testes pela IA comparada à humana**. Não se pode usar a melhoria do software para provar superioridade da IA.

## 1.4 Critérios de qualidade das sugestões de IA

Cada caso de IA deve ser revisado por integrante humano quanto a: (i) requisito rastreável; (ii) entrada executável; (iii) resultado esperado plausível; (iv) independência dos dados; (v) potencial de detectar um defeito real; (vi) redundância e premissas inventadas.

Classificações sugeridas:

- **Correto:** oráculo confirmado por requisito/decisão de domínio e execução tecnicamente válida.
- **Erro de geração:** teste incorreto, não executável, resultado esperado tecnicamente errado ou código com defeito.
- **Alucinação:** IA afirma existir uma funcionalidade, regra, API ou requisito **não sustentado** pela especificação/código e não marcado como proposta.
- **Regra proposta, não validada:** o teste pode ser útil, mas demanda confirmação do grupo; **não** classificar automaticamente como alucinação.
- **Divergência do software:** o programa não atende ao oráculo aceito; **não** confundir com erro da IA.

A planilha [`revisao_oraculos.csv`](../../evidencias/entregavel-10/revisao_oraculos.csv) inicia **em branco** para evitar fingir julgamento humano.

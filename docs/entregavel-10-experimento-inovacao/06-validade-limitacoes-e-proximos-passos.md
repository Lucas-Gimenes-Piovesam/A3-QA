# 6. Validade, limitações e próximos passos

## 6.1 Limitações e ameaças à validade

| Risco | Consequência | Mitigação proposta |
|---|---|---|
| Regras de domínio assumidas | Oráculo IA-08 pode ser julgado indevidamente como defeito | Aprovar a restrição de orçamento em ata real |
| Tamanho pequeno (10 casos) | Resultados não generalizam para todo o sistema | Ampliar cenário de persistência, CSV, data e valores-limite |
| Mesmos casos para antes/depois | Demonstra conformidade do software, **não** eficiência da IA versus humanos | Experimento independente pareado em duas suítes |
| Defeitos correlacionados | Rejeição de `NaN`/`Infinity` é a mesma família de regras | Contar **casos divergentes**; só contar defeitos únicos após triagem |
| Histórico do grupo com uploads/commit GREEN vazio | A narrativa temporal TDD não é totalmente limpa | Referenciar diffs reais; corrigir a demonstração sem reescrever história |
| Snapshot do upstream reconstruído | Não garante identidade com commit do autor original | Limitar baseline à tag do grupo, conferir SHA do upstream se usar como referência externa |
| Oráculo baseado em mensagens | Pode passar mesmo com persistência errada | Testes adicionais devem ler arquivos e validar estado |
| Testes escritos/avaliados com IA | Revisão do oráculo pode compartilhar o mesmo viés | Introduzir especialista ou revisor independente |
| Tempos curtos variáveis | Execução Java não mede ganho de produtividade | Usar cronômetro humano, amostras repetidas e mesma máquina |
| Cobertura 100% restrita aos métodos P1 | Uma alta cobertura não impede erro semântico | Complementar com casos de requisitos, análise manual e testes mutantes |

## 6.2 O que sabemos e o que não sabemos

**Sabemos:** o programa inicial atendeu a seis de dez oráculos; na versão final atendeu aos dez. Os casos IA-05 a IA-08 foram responsáveis pelas quatro divergências da baseline e a versão corrigida eliminou essas divergências sob o mesmo conjunto de entradas. A intervenção é versionada em commits e a integração do projeto possui CI com JUnit/JaCoCo/Checkstyle e gate.

**Não sabemos:** se IA economizou 20% de tempo, quantos oráculos são corretos após revisão independente, quantas alucinações houve, se o mesmo efeito ocorreria com outra equipe, ou se os outros caminhos não exercitados da aplicação estão corretos.

## 6.3 Plano para mais um semestre

1. **Mês 1 — requisitos e dados:** especificação formal das regras financeiras com exemplos limítrofes; criar conjunto cego de defeitos de referência validados por revisor.
2. **Mês 2 — comparação justa:** 2–3 ciclos pareados manual × IA com novos cenários, prompt versionado, tempo registrado e auditoria dos oráculos; publicar inclusive casos incorretos e alucinações.
3. **Mês 3 — detecção efetiva:** ampliar testes com *mutation testing* de regras monetárias e persistência para distinguir execução de teste de eficácia na detecção.
4. **Mês 4 — evolução do legado:** incorporar mudanças CR-09-02 e CR-09-03 em PRs separados, com dados temporários, rollback e testes para gravação segura e validação de datas.
5. **Mês 5 — replicação:** rodar o mesmo protocolo em outro utilitário Java e comparar sensibilidade à ferramenta e dificuldade do domínio.
6. **Mês 6 — difusão:** disponibilizar um kit reutilizável (CSV de casos, script `experimento_10.py`, protocolo de revisão e painel), com tutorial e limites conhecidos.

## 6.4 Reutilização por outra equipe

A equipe seguinte deverá clonar o repositório, escolher **duas revisões fixas**, executar `experimento_10.py`, revisar oráculos e registrar tempos humanos em instrumentos separados. O script fornece um padrão reprodutível de antes/depois; para avaliar outra IA, adicionar nova rodada com prompt, versão do modelo e suite da comparação, sem sobrescrever arquivos históricos.

## 6.5 Conclusão acadêmica

A carta foi aplicada para propor e exercitar testes que encontraram **quatro divergências observadas** no legado sob critérios explícitos. Após correções, os dez casos passaram. A abordagem trouxe **evidência útil para qualidade**, mas não demonstra sozinha produtividade superior da IA, precisão total ou ausência de alucinações. A hipótese original de ganho de 20% permanece **inconclusiva** até a coleta pareada do grupo.

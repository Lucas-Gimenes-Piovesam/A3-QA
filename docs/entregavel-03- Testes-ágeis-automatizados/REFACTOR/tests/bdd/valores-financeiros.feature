# A3-QA | Entregável 3 | Critérios legíveis para negócio e testadores
# Cada cenário foi relacionado a testes JUnit no documento de rastreabilidade.
# ESTE .feature É DOCUMENTAÇÃO BDD, NÃO É EXECUTADO AUTOMATICAMENTE POR CUCUMBER.
# Decisão de domínio do grupo sujeita a validação humana: orçamento igual a zero é válido.

# language: pt
Funcionalidade: Validação dos valores financeiros no Expense Tracker
  Como pessoa que registra despesas pessoais
  Quero impedir valores financeiros inválidos
  Para que os totais e os alertas de orçamento sejam confiáveis

  Cenário: Registrar uma despesa válida
    Dado que estou na opção de cadastrar despesa
    Quando informo um valor de 12,50
    Então a despesa deve ser cadastrada
    E o registro deve ser salvo com o valor informado

  Esquema do Cenário: Rejeitar despesas inválidas
    Dado que estou na opção de cadastrar despesa
    Quando informo o valor "<valor>"
    Então a despesa não deve ser cadastrada
    E uma mensagem de valor inválido deve ser exibida

    Exemplos:
      | valor     |
      | 0         |
      | -0.01     |
      | NaN       |
      | Infinity  |
      | -Infinity |

  Cenário: Definir orçamento mensal de zero
    Dado que estou na opção de orçamento mensal
    Quando informo o valor 0 para o mês "2026-11"
    Então o orçamento deve ser salvo com valor zero

  Esquema do Cenário: Rejeitar orçamento inválido
    Dado que estou na opção de orçamento mensal
    Quando informo o valor "<valor>" para o mês "2026-11"
    Então o orçamento não deve ser salvo
    E a aplicação deve informar que o valor é inválido

    Exemplos:
      | valor    |
      | -10      |
      | NaN      |
      | Infinity |

  Cenário: Ignorar um registro antigo com valor não finito
    Dado que existe uma despesa persistida com valor NaN
    Quando o sistema inicia
    Então o registro inválido deve ser ignorado
    E o total de despesas deve permanecer válido

  Cenário: Atualização inválida preserva o valor anterior
    Dado que existe uma despesa cadastrada no valor de 12,50
    Quando tento atualizá-la informando NaN
    Então a atualização deve ser rejeitada
    E a despesa deve permanecer com o valor original

  Cenário: Ignorar orçamento antigo inválido
    Dado que existe um orçamento persistido com valor NaN
    Quando o sistema inicia
    Então esse orçamento deve ser ignorado

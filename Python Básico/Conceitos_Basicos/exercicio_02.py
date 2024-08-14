# Peça ao usuário para informar o ano de nascimento. Em seguida, calcule e imprima a idade atual.

# Solicita o ano de nascimento
ano_nascimento = int(input("Digite o ano de seu nascimento: "))

# Calcula a idade
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

# Imprime a idade
print("Você tem", idade, "anos.")

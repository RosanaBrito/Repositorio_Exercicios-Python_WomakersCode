"""
Escreva um programa que calcule o salário líquido. Lembrando de declarar o salário bruto e o percentual de desconto do Imposto de Renda.
Renda até R$ 1.903,98: isento de imposto de renda;
Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
Renda entre R$ 3.751,06 e R4 4.664,68: alíquota de 22,5%:
Renda acima R$ 4.664,68: alíquota máxima de 27,5%
"""
def calcular_salario_liquido():
  """
  Calcula o salário líquido de um funcionário com base no salário bruto e nas regras do Imposto de Renda.
  """

  try:
    salario_bruto_str = input("Digite o salário bruto: R$ ")
    salario_bruto_str = salario_bruto_str.replace(",", ".")  # Substitui vírgula por ponto
    salario_bruto = float(salario_bruto_str)

    if salario_bruto <= 1903.98:
      aliquota = 0
    elif salario_bruto <= 2826.65:
      aliquota = 0.075
    elif salario_bruto <= 3751.05:
      aliquota = 0.15
    elif salario_bruto <= 4664.68:
      aliquota = 0.225
    else:
      aliquota = 0.275

    imposto_renda = salario_bruto * aliquota
    salario_liquido = salario_bruto - imposto_renda

    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Alíquota do Imposto de Renda: {aliquota * 100:.1f}%")
    print(f"Imposto de Renda: R$ {imposto_renda:.2f}")
    print(f"Salário líquido: R$ {salario_liquido:.2f}")

  except ValueError:
    print("Entrada inválida. Digite um número para o salário bruto, usando ponto (.) como separador decimal.")

# Calcula o salário líquido
calcular_salario_liquido()



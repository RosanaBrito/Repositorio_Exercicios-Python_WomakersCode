# Faça um Programa que peça dois números e imprima o maior deles

def encontrar_maior():
  """Pede dois números ao usuário e imprime o maior deles."""

  num1 = float(input("Digite o primeiro número: "))
  num2 = float(input("Digite o segundo número: "))

  if num1 > num2:
    print(f"O maior número é: {num1}")
  elif num2 > num1:
    print(f"O maior número é: {num2}")
  else:
    print("Os números são iguais.")

# Chama a função para executar o programa
encontrar_maior()

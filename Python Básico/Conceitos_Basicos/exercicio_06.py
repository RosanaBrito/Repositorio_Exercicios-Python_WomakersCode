# Solicite ao usuário o peso em kg e a altura em metros.
# Calcule e imprime o Índice de Massa Corporal (IMC) usando a fórmula
# IMC = peso / (altura x altura)

# Solicita os dados ao usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura * altura)

# Imprime o resultado
print("Seu IMC é:", imc)

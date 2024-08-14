# Faça um programa que peça a quantidade de quilômetros, transforme em metros, centímetros e milímetros

# Solicita a quantidade de quilômetros
quilometros = float(input("Digite a quantidade de quilômetros: "))

# Converte para metros, centímetros e milímetros
metros = quilometros * 1000
centimetros = metros * 100
milimetros = centimetros * 10

# Imprime os resultados
print(quilometros, "km equivalem a:")
print(metros, "metros")
print(centimetros, "centímetros")
print(milimetros, "milímetros")

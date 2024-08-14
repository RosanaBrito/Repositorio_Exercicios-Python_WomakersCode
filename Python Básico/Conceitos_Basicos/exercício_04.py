''' Receba do usuário a quantidade de litros de combustível consumidos e a distância percorrida. 
    Calcule e imprima o consumo médio em km/l.
'''

# Solicita os dados ao usuário
litros_consumidos = float(input("Digite a quantidade de litros consumidos: "))
distancia_percorrida = float(input("Digite a distância percorrida em km: "))

# Calcula o consumo médio
consumo_medio = distancia_percorrida / litros_consumidos

# Imprime o resultado
print("O consumo médio foi de", consumo_medio, "km/l")

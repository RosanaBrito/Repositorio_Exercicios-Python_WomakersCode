''' Escreva um programa ue calcule o tempo de uma viagem. Faça um comparativo do mesmo percurso de avião, 
carro e ônibus. Levando em consideração:
Avião = 600 km/h
carro = 100 km/h
ônibus = 80 km/h
'''
# Solicita a distância ao usuário
distancia = float(input("Digite a distância da viagem em km: "))

# Calcula o tempo para cada meio de transporte
tempo_aviao = distancia / 600
tempo_carro = distancia / 100
tempo_onibus = distancia / 80

# Imprime os resultados
print("Tempo de viagem para", distancia, "km:")
print("Avião:", tempo_aviao, "horas")
print("Carro:", tempo_carro, "horas")
print("Ônibus:", tempo_onibus, "horas")

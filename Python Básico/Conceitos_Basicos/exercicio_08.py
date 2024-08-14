# Solicite ao usuário o número de horas de exercício físico por semana.
# Calcule o total de calorias queimadas em um mês, considerando uma média de 5 calorias por minuto de exercício.

# Solicita as horas de exercício
horas_exercicio = float(input("Digite o número de horas de exercício por semana: "))

# Calcula o total de minutos de exercício por mês
minutos_exercicio_mes = horas_exercicio * 60 * 4 

# Calcula o total de calorias queimadas
calorias_queimadas = minutos_exercicio_mes * 5

# Imprime o resultado
print("Você queima aproximadamente", calorias_queimadas, "calorias por mês com seus exercícios.")

# calcule a média dos valores digitados pelo usuário

def calcular_media(valores):
    tamanho = 0  # Inicializa tamanho com 0
    soma = 0.0
    for valor in valores:  # Não precisa usar enumerate 
        soma += valor
        tamanho += 1  # Incrementa tamanho a cada interação
    if tamanho == 0:
        return 0  # Evita divisão por zero se nenhum valor for inserido
    else:
        return soma / tamanho

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False
    else:
        try:
            valores.append(float(valor))  # Converte a entrada para float e adiciona à lista
        except ValueError:
            print("Entrada inválida. Digite um número ou 'ok'.")

media = calcular_media(valores)
print('A média calculada para os valores {} foi de {:.2f}'.format(valores, media))
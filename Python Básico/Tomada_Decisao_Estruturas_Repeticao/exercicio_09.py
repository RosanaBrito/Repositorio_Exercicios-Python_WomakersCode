"""
Crie um programa que calcule e apresente a quantidade de números pares e ímpares inseridos. 
O processo de leitura deve ser encerrado quando o usuário informar o valor zero.
Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.
"""

def contar_pares_impares():
    """
    Solicita números ao usuário, conta pares e ímpares, e encerra quando 0 é digitado.
    """

    pares = 0
    impares = 0

    while True:
        try:
            numero = int(input("Digite um número inteiro (0 para sair): "))
            if numero == 0:
                break  # Encerra o loop se 0 for digitado
            elif numero % 2 == 0:
                pares += 1
            else:
                impares += 1
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    print(f"Quantidade de números pares: {pares}")
    print(f"Quantidade de números ímpares: {impares}")

# Executa a contagem de pares e ímpares
contar_pares_impares()

"""
Crie um programa em Python que solicite três números ao usuário, 
utilize estruturas condicionais para determinar o maior entre eles e
apresente o resultado.
"""

def encontrar_maior_numero():
    """
    Solicita três números ao usuário e encontra o maior entre eles.
    """

    numeros = []
    for i in range(3):
        while True:
            try:
                numero = float(input(f"Digite o {i+1}º número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Digite um número.")

    maior_numero = max(numeros)
    print(f"O maior número é: {maior_numero}")

# Encontra o maior número entre os três fornecidos
encontrar_maior_numero()

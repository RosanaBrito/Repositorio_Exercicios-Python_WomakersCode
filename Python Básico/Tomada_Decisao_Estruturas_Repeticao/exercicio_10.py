# Faça um programa que lê três números inteiros e os mostra em ordem crescente.

def ordenar_numeros():
    """
    Solicita três números inteiros ao usuário e os imprime em ordem crescente.
    """

    numeros = []
    for i in range(3):
        while True:
            try:
                numero = int(input(f"Digite o {i + 1}º número inteiro: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

    numeros.sort()  # Ordena a lista em ordem crescente
    print("Números em ordem crescente:", numeros)

# Executa a ordenação dos números
ordenar_numeros()


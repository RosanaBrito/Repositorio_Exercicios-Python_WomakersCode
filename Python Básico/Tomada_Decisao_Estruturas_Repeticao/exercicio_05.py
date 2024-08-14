'''Desenvolva um programa que solicite ao usuário os comprimentos dos três lados de um triângulo e classifique-o como equilátero,
isóceles ou escaleno.
equilátero: todos os lados com o mesmo valor
isóceles: dois lados com o mesmo valor
escaleno: todos os lados com medidas distintas
'''

def classificar_triangulo():
    """
    Solicita os comprimentos dos lados de um triângulo e o classifica.
    """

    while True:
        try:
            lado1 = float(input("Digite o comprimento do primeiro lado: "))
            lado2 = float(input("Digite o comprimento do segundo lado: "))
            lado3 = float(input("Digite o comprimento do terceiro lado: "))

            if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                print("Os comprimentos dos lados devem ser positivos.")
            elif lado1 + lado2 <= lado3 or lado1 + lado3 <= lado2 or lado2 + lado3 <= lado1:
                print("Os comprimentos fornecidos não formam um triângulo válido.")
            else:
                if lado1 == lado2 == lado3:
                    print("O triângulo é equilátero.")
                elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                    print("O triângulo é isósceles.")
                else:
                    print("O triângulo é escaleno.")
                break  # Sai do loop após a classificação
        except ValueError:
            print("Entrada inválida. Digite números para os comprimentos dos lados.")

# Classifica o triângulo
classificar_triangulo()

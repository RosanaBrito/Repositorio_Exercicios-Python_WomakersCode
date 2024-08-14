# Faça uma programa que peça uma nota entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido

def obter_nota_valida():
    """
    Solicita ao usuário uma nota entre 0 e 10 e continua pedindo até que uma nota válida seja fornecida.
    """

    while True:  # Loop infinito até que uma nota válida seja inserida
        try:
            nota = float(input("Digite uma nota entre 0 e 10: "))
            if 0 <= nota <= 10:
                return nota  # Sai do loop se a nota for válida
            else:
                print("Valor inválido. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Obtém uma nota válida do usuário
nota_valida = obter_nota_valida()
print(f"Você digitou a nota: {nota_valida}")

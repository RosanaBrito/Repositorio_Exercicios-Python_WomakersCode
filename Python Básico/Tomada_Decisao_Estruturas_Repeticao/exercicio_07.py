# Desenvolva um programa que solicite a idade do usuário e identifique se ele é uma criança, um adolescente, adulto ou idoso.

def identificar_faixa_etaria():
    """
    Solicita a idade do usuário e identifica a faixa etária correspondente.
    """

    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if idade < 0:
                print("Idade inválida. Digite um número positivo.")
            elif idade < 12:
                print("Você é uma criança.")
            elif idade < 18:
                print("Você é um adolescente.")
            elif idade < 60:  # Ajuste para considerar adultos até 59 anos
                print("Você é um adulto.")
            else:
                print("Você é um idoso.")
            break  # Sai do loop após a identificação
        except ValueError:
            print("Entrada inválida. Digite um número inteiro para a idade.")

# Identifica a faixa etária do usuário
identificar_faixa_etaria()



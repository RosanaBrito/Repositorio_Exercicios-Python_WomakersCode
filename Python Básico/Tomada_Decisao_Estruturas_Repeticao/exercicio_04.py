'''
Implemente um programa que classifique um aluno com base em sua pontuação em um exame. O programa deverá solicitar uma 
nota entre 0 a 10. Se a pontuação for maior ou igual a 7, o aluno é aprovado; caso contrário, é reprovado.
'''

def classificar_aluno():
    """
    Solicita a nota de um aluno e o classifica como aprovado ou reprovado.
    """

    while True:
        try:
            nota = float(input("Digite a nota do aluno (entre 0 e 10): "))
            if 0 <= nota <= 10:
                if nota >= 7:
                    print("Aluno aprovado!")
                else:
                    print("Aluno reprovado.")
                break  # Sai do loop após a classificação
            else:
                print("Nota inválida. A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

# Classifica o aluno
classificar_aluno()

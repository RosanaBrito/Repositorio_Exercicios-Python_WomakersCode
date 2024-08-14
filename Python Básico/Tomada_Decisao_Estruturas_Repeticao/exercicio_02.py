'''Faça um programa que pergunte em que turno você estuda. Peça para digitar M-matutino, V-vespertino ou N-Noturno.
Imprima a mensagem "Bom dia!", "Boa tarde!" ou "Boa noite!" ou "Valor inválido!", conforme o caso.
'''

def saudar_aluno():
    """
    Pergunta o turno de estudo do aluno e imprime uma saudação apropriada.
    """

    turno = input("Em que turno você estuda? Digite M-matutino, V-Vespertino ou N-Noturno: ").upper()

    if turno == 'M':
        print("Bom Dia!")
    elif turno == 'V':
        print("Boa Tarde!")
    elif turno == 'N':
        print("Boa Noite!")
    else:
        print("Valor Inválido!")

# Chama a função para executar o programa
saudar_aluno()

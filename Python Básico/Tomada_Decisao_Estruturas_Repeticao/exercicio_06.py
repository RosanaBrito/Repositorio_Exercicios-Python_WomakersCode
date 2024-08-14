# Crie um programa que soliciteao usuário um login e uma senha. 
# O programa deve permitiro acesso apenas se o usuário for "admin" e  senha for "admin123", caso contrário, imprima uma mensagem de erro

def autenticar_usuario():
    """
    Solicita login e senha ao usuário e verifica se são válidos.
    """

    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login == "admin" and senha == "admin123":
        print("Acesso permitido!")
    else:
        print("Acesso negado. Login ou senha incorretos.")

# Executa a autenticação
autenticar_usuario()

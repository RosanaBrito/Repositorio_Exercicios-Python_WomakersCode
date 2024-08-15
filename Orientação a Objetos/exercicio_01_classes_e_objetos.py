'''
crie um classe que modele o objeto"carro" com os seguintes atributos: ligado, cor, modelo, velocidade.
o carro tem os seguintes comportamentos: liga, desliga, acelera. desacelera.
crie uma instância da classe carro.
faça o carro "andar" utilizando os métodos da sua classe.
faça o carro "parar" utilizando os métodos da sua classe.
'''

class Carro:
    def __init__(self, cor, modelo):
        self.ligado = False
        self.cor = cor  # Atributo cor
        self.modelo = modelo  # Atributo modelo
        self.velocidade = 0

    def liga(self):
        if not self.ligado:
            self.ligado = True
            print("O carro foi ligado.")
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado:
            if self.velocidade == 0:
                self.ligado = False
                print("O carro foi desligado.")
            else:
                print("O carro não pode ser desligado em movimento.")
        else:
            print("O carro já está desligado.")

    def acelera(self, incremento):
        if self.ligado:
            self.velocidade += incremento
            print(f"O carro acelerou para {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para acelerar.")

    def desacelera(self, decremento):
        if self.ligado:
            self.velocidade -= decremento
            if self.velocidade < 0:
                self.velocidade = 0
            print(f"O carro desacelerou para {self.velocidade} km/h.")
        else:
            print("O carro precisa estar ligado para desacelerar.")

# Criando uma instância da classe Carro
meu_carro = Carro("Vermelho", "Fusca")

# Fazendo o carro "andar"
meu_carro.liga()
meu_carro.acelera(30)
meu_carro.acelera(20)

# Fazendo o carro "parar"
meu_carro.desacelera(50)
meu_carro.desliga()

# Criando uma instância da classe Carro
meu_carro = Carro(input("Digite a cor do carro: "), input("Digite o modelo do carro: "))

while True:
    acao = input("\nO que você deseja fazer? (ligar, desligar, acelerar, desacelerar, sair): ")

    if acao.lower() == "ligar":
        meu_carro.liga()
    elif acao.lower() == "desligar":
        meu_carro.desliga()
    elif acao.lower() == "acelerar":
        incremento = int(input("Digite o quanto você quer acelerar: "))
        meu_carro.acelera(incremento)
    elif acao.lower() == "desacelerar":
        decremento = int(input("Digite o quanto você quer desacelerar: "))
        meu_carro.desacelera(decremento)
    elif acao.lower() == "sair":
        break
    else:
        print("Ação inválida. Tente novamente.")
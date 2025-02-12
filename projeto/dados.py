import random

class jogador:
    def __init__(self,pontos):
        self.pontos = pontos

    def Jogar(self):
        dados = random.randint(1,6)
        print(dados)

class adversário:
    def __init__(self,pontos):
        self.pontos = pontos

    def Jogar(self):
        dadospc = random.randint(1,6)


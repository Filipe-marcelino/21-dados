import random

class Jogador:
    def __init__(self,pontosplayer: int):
        self.pontosplayer = pontosplayer

    def Jogar(self):
        dados = random.randint(1,6)
        self.pontosplayer += dados
        print(dados)
        print(self.pontosplayer)

class Adversario:
    def __init__(self,pontospc: int):
        self.pontospc = pontospc

    def Jogar(self):
        dadospc = random.randint(1,6)
        self.pontospc += dadospc

player1 = Jogador(0)
player2 = Adversario(0)
rodada = str(input('Você deseja jogar um dado (s/n)? '))
while rodada.upper() == "S":
    player1.Jogar()
    player2.Jogar()
    rodada = str(input('Você deseja jogar outro dado (s/n)? '))

    if player1.pontosplayer >= 21:
        break

if player1.pontosplayer == 21:
    print('Você venceu!!')

elif player2.pontospc == 21:
    print('Você perdeu')

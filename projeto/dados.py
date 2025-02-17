import random

class Jogador:
    def __init__(self,pontosplayer: int): # Atributo(s): pontosplayer (pontos dp jogador)
        self.pontosplayer = pontosplayer

    def Jogar(self): # Método Jogar do jogador
        dados = random.randint(1,6)
        self.pontosplayer += dados
        print(f"Dados do player: {dados}")
        print(f"Pontos do player: {self.pontosplayer}")

class Adversario: 
    def __init__(self,pontospc: int): # Atributo(s): pontospc (pontos do pc)
        self.pontospc = pontospc

    def Jogar(self): # Método Jogar do pc
        dadospc = random.randint(1,6)
        self.pontospc += dadospc
        print(f"Dados do pc: {dadospc}")
        print(f"Pontos do pc: {self.pontospc}")

player1 = Jogador(0)
player2 = Adversario(0)
rodada = str(input('Você deseja jogar um dado (s/n)? '))

while rodada.upper() != 'SIM':
    rodada = str(input('Você deseja jogar um dado (s/n)? '))

while rodada.upper() == "S":
    player1.Jogar()
    print('---------------------------------')
    player2.Jogar()

    if player1.pontosplayer > 21:
        print('\nPC WINS!')
        break

    elif player1.pontosplayer == 21:
        print('\nPLAYER WINS!')
        break

    elif player2.pontospc > 21:
        print('\nPLAYER WINS!')
        break

    elif player2.pontospc == 21:
        print('\nPC WINS!')
        break
    
    # EM CASO DE EMPATE
    elif player1.pontosplayer > 21 and player2.pontospc > 21:
        if player2.pontospc == player1.pontosplayer:
            print('EMPATE!')
        elif player2.pontospc > player1:
            print('PLAYER WINS!')
        else:
            print('PC WINS!')

    rodada = str(input('\nVocê deseja jogar um dado (s/n)? '))

elif player2.pontospc == 21:
    print('Você perdeu')

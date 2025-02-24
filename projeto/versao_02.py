# EM DESENVOLVIMENTO !!!!!!!!!!

import random
from colorama import Fore, Back, Style

def desenhar_dado(valor: int):
    dados = {
        1: ["┌─────┐", "│     │", "│  ●  │", "│     │", "└─────┘"],
        2: ["┌─────┐", "│ ●   │", "│     │", "│   ● │", "└─────┘"],
        3: ["┌─────┐", "│ ●   │", "│  ●  │", "│   ● │", "└─────┘"],
        4: ["┌─────┐", "│ ● ● │", "│     │", "│ ● ● │", "└─────┘"],
        5: ["┌─────┐", "│ ● ● │", "│  ●  │", "│ ● ● │", "└─────┘"],
        6: ["┌─────┐", "│ ● ● │", "│ ● ● │", "│ ● ● │", "└─────┘"],
        7: ["    / \\", "   /   \\", "  /  7  \\", " /_______\\"],
        8: ["    / \\", "   /   \\", "  /  8  \\", " /_______\\"],
        9: ["    / \\", "   /   \\", "  /  9  \\", " /_______\\"],
        10: ["    / \\", "   /   \\", "  / 10  \\", " /_______\\"]
    }

    for linha in dados[valor]:
        print(Fore.WHITE + linha)

class Jogador: # Classe Jogador
    def __init__(self, nome:str,aposta): # Atributo(s): pontos (pontos dp jogador)
        self.nome = nome
        self.pontos = 0
        self.fichas = 5
        self.aposta = aposta

    def apostar(self):
        aposta = int(input(f'Você tem {self.fichas} fichas.Quantas fichas você vai apostar? '))
        while aposta > self.fichas:
            aposta = int(input('Fichas insuficentes, tente novamente. '))
        self.fichas = self.fichas - aposta

    def Jogar(self): # Método Jogar do jogador
        # ROLAGEM DE DADOS
        dado = input('Que dado desejas rolar (d4, d6 ou d10)? ')
        if dado == 'd4':
            dado = random.randint(1,3)

        elif dado == 'd6':
            dado = random.randint(1,6) 
            
        elif dado == 'd10':
            dado = random.randint(1,10)

        else:
            print('Ops! Não pode rolar esse dado! Escolha entre um d4, d6 ou d10!')
            return self.Jogar()

        # Soma dos pontos e print dos resultados
        self.pontos += dado 
        print(f"Dados do {self.nome}: {dado}")
        print(f"Pontos do {self.nome}: {self.pontos}")
        desenhar_dado(dado)

class Computador(Jogador): 
    def __init__(self):
        self.fichaspc = 5
        super().__init__("Computador")
    

    def pagar(self):
        self.fichaspc = self.fichaspc - self.fichas 
        return ('Eu pago a aposta')

    def Jogar(self):
        # ESTRATÉGIA DO COMPUTADOR PARA ESCOLHER OS DADOS
        if self.pontos <=10:
            dado = "d10"
        
        elif self.pontos <=15:
            dado = "d6"
        
        else:
            dado = 'd4'
        
        # ROLAGEM DE DADOS
        if dado == 'd4':
            dado = random.randint(1,4)

        elif dado == 'd6':
            dado = random.randint(1,6) 
            
        elif dado == 'd10':
            dado = random.randint(1,10)

        self.pontos += dado 
        #print(f"\nDados do {self.nome}: {dado}")
        #print(f"Pontos do {self.nome}: {self.pontos}\n")

def main():
    jogador = Jogador(input("Digite seu nome: "))
    computador = Computador()

    posta = str(input('Você quer fazer uma aposta (s/n)? '))
    if posta.upper() == 'S':
        rodada = str(input('Você deseja jogar um dado (s/n)? '))

        while rodada.upper() != 'S':
            rodada = str(input('Você deseja jogar um dado (s/n)? '))

        while rodada.upper() == "S":
            jogador.apostar()
            jogador.Jogar()
            print('---------------------------------')
            computador.pagar()
            computador.Jogar()

            if jogador.pontos > 21:
                computador.fichaspc = computador.fichaspc + (jogador.aposta*2)
                print('\nPC WINS!')
                print('')
                break

            elif jogador.pontos == 21:
                jogador.fichas = jogador.fichas + (jogador.aposta*2)
                print('\nPLAYER WINS!')
                break

            elif computador.pontos > 21:
                jogador.fichas = jogador.fichas + (jogador.aposta*2)
                print('\nPLAYER WINS!')
                break

            elif computador.pontos== 21:
                computador.fichaspc = computador.fichaspc + (jogador.aposta*2)
                print('\nPC WINS!')
                break
            
            # EM CASO DE EMPATE
            elif jogador.pontos > 21 and computador.pontospc > 21:
                if computador.pontos == jogador.pontos:
                    print('EMPATE!')
                elif computador.pontospc > jogador:
                    jogador.fichas = jogador.fichas + (jogador.aposta*2)
                    print('PLAYER WINS!')
                else:
                    computador.fichaspc = computador.fichaspc + (jogador.aposta*2)
                    print('PC WINS!')
            else:
                continue  # Se ninguém ganhou, continua o jogo

            # PONTUAÇÃO FINAL
        print("\nPontuação Final:")
        print(f"{jogador.nome}: {jogador.pontos} pontos")
        print(f"Computador: {computador.pontos} pontos")  
    else:
        rodada = str(input('Você deseja jogar um dado (s/n)? '))

        while rodada.upper() != 'S':
            rodada = str(input('Você deseja jogar um dado (s/n)? '))

        while rodada.upper() == "S":
            jogador.Jogar()
            print('---------------------------------')
            computador.Jogar()

            if jogador.pontos > 21:
                print('\nPC WINS!')
                print('')
                break

            elif jogador.pontos == 21:
                print('\nPLAYER WINS!')
                break

            elif computador.pontos > 21:
                print('\nPLAYER WINS!')
                break

            elif computador.pontos== 21:
                print('\nPC WINS!')
                break
            
            # EM CASO DE EMPATE
            elif jogador.pontos > 21 and computador.pontospc > 21:
                if computador.pontos == jogador.pontos:
                    print('EMPATE!')
                elif computador.pontospc > jogador:
                    print('PLAYER WINS!')
                else:
                    print('PC WINS!')
            else:
                continue  # Se ninguém ganhou, continua o jogo

            # PONTUAÇÃO FINAL
        print("\nPontuação Final:")
        print(f"{jogador.nome}: {jogador.pontos} pontos")
        print(f"Computador: {computador.pontos} pontos")  

if __name__ == "__main__":
    main()

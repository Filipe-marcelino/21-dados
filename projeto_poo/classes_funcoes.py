import random
from colorama import init, Fore, Back, Style

init(autoreset=True)

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

    print(Style.RESET_ALL)
    for linha in dados[valor]:
        print(Fore.WHITE + linha + Style.RESET_ALL)

class Jogador: # Classe Jogador
    def __init__(self, nome:str): # Atributo(s): pontos (pontos dp jogador)
        self.nome = nome
        self.pontos = 0
        self.fichas = 5
        self.apostadas = 0

    def aposta(self): # Função que só é chamada se o jogador quiser apostar
        f_apostadas = input(f'Você tem {self.fichas} fichas. Quantas fichas você vai apostar? ')
        while not f_apostadas.isdigit():
            print('\nOps! Precisa ser um número... Tente novamente! :)')
            f_apostadas = input(f'Você tem {self.fichas} fichas. Quantas fichas você vai apostar? ')
        f_apostadas = int(f_apostadas)
        self.apostadas += f_apostadas
        while f_apostadas > self.fichas:
            f_apostadas = input('Fichas insuficentes, tente novamente. ')
        self.fichas -= f_apostadas

    def Jogar_dado(self): # Método Jogar_dado do jogador
        # ROLAGEM DE DADOS
        print(Style.RESET_ALL + '\n', Back.WHITE + ' 🎲 ESCOLHA UM DADO! 🎲 \nOPÇÕES: 🎲D4 - 🎲D6 - 🎲D10' + Style.RESET_ALL)
        dado = input(Style.RESET_ALL+'\nDigite aqui: ')
        if dado == 'd4':
            dado = random.randint(1,4)

        elif dado == 'd6':
            dado = random.randint(1,6) 
            
        elif dado == 'd10':
            dado = random.randint(1,10)

        else:
            print('Ops! Você não pode rolar esse dado... 😕')
            return self.Jogar_dado()

        # Soma dos pontos e print dos resultados
        self.pontos += dado 
        print(f"Dados do {self.nome}: {dado}")
        print(f"Pontos do {self.nome}: {self.pontos}")
        desenhar_dado(dado)

class Computador(Jogador): 
    def __init__(self):
        self.fichaspc = 5
        super().__init__("Computador")
    
    def aposta(self):
        self.fichaspc = self.fichaspc - self.fichas 
        return 'Eu pago a aposta'

    def Jogar_dado(self):
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

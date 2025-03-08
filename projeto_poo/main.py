import random
from colorama import init, Fore, Back, Style
from classes_funcoes import desenhar_dado, Jogador, Computador

init(autoreset=True)

def main():
    print('\n\n\n')
    print(Back.WHITE + '    ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ' )
    print(Fore.YELLOW + ' ▦ ',' ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓',Fore.YELLOW + ' ▦ ')
    print(Back.WHITE + '    ','▓▓▓▓▓▓▓         ░▓  ░▓▓▓▓        ░▓▓▓        ░▓▓        ░▓▓▓        ░▓▓         ░▓▓▓           ░▓▓▓▓▓▓',Back.WHITE + '    ')
    print(Back.WHITE + '    ','▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ░▓  ░▓▓▓▓   ▓▓░   ░▓▓   ▓▓░  ░▓▓   ▓▓░   ░▓▓   ▓▓░  ░▓▓  ░▓▓▓▓▓▓▓▓▓▓  ●     ●  ░▓▓▓▓▓▓',Back.WHITE + '    ')
    print(Fore.RED + ' ▦ ',' ▓▓▓▓▓▓▓         ░▓  ░▓▓▓▓   ▓▓░   ░▓▓        ░▓▓   ▓▓░   ░▓▓   ▓▓░  ░▓▓         ░▓▓▓     ●     ░▓▓▓▓▓▓',Fore.RED + ' ▦ ')
    print(Back.WHITE + '    ','▓▓▓▓▓▓▓  ░▓▓▓▓▓▓▓▓  ░▓▓▓▓   ▓▓░   ░▓▓   ▓▓░  ░▓▓   ▓▓░   ░▓▓   ▓▓░  ░▓▓▓▓▓▓▓▓▓  ░▓▓▓  ●     ●  ░▓▓▓▓▓▓',Back.WHITE + '    ')
    print(Back.WHITE + '    ','▓▓▓▓▓▓▓         ░▓  ░▓▓▓▓        ░▓▓▓   ▓▓░  ░▓▓        ░▓▓▓        ░▓▓         ░▓▓▓           ░▓▓▓▓▓▓',Back.WHITE + '    ')
    print(Fore.YELLOW + ' ▦ ','▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓', Fore.YELLOW + ' ▦ ')
    print(Back.WHITE + '    ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.RED + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ' )
    
    print(Fore.RED + '________________________________________________________________________________________________________________')
    jogador = Jogador(input(Back.GREEN + "\nDIGITE SEU NOME:" + Style.RESET_ALL + ' '))
    computador = Computador()
    print(Fore.RED + '________________________________________________________________________________________________________________')
    print('\nÓTIMO, ' + Back.GREEN + jogador.nome + Style.RESET_ALL + '! ESTES SÃO OS MODOS DE JOGAR:')
    print(Back.YELLOW + ' CLÁSSICO ', 'ou', Back.RED + '  APOSTA!  ')
    modo = str(input('\n👀 ESCOLHA UM MODO: '))

    while modo.upper() not in ['APOSTA','CLÁSSICO','CLASSICO']:
        print('Ops! Acho que você digitou algo errado... Vamos tentar novamente!')
        modo = str(input('\n👀 ESCOLHA UM MODO: '))

    if modo.upper() == 'APOSTA':
        print('\n' + Back.WHITE + '    ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '    ')

        print(Fore.YELLOW + ' ▦ '," ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",Fore.YELLOW + ' ▦ ')
        print(Back.WHITE + '    ', "▓▓▓▓▓▓▓▓▓        ░▓▓        ░▓▓        ░▓▓         ░▓▓       ░▓▓        ░▓▓  ▓  ▓  ▓▓▓▓▓▓▓▓▓",Back.WHITE + '    ')
        print(Back.WHITE + '    ', "▓▓▓▓▓▓▓▓▓   ▓▓░  ░▓▓   ▓▓░  ░▓▓   ▓▓░  ░▓▓   ░▓▓▓▓▓▓▓▓▓▓   ░▓▓▓▓   ▓▓░  ░▓▓  ▓  ▓  ▓▓▓▓▓▓▓▓▓",Back.WHITE + '    ')
        print(Fore.YELLOW + ' ▦ ', " ▓▓▓▓▓▓▓▓▓        ░▓▓        ░▓▓   ▓▓░  ░▓▓         ░▓▓▓▓   ░▓▓▓▓        ░▓▓  ▓  ▓  ▓▓▓▓▓▓▓▓▓",Fore.YELLOW + ' ▦ ')
        print(Back.WHITE + '    ',  "▓▓▓▓▓▓▓▓▓   ▓▓░  ░▓▓   ░▓▓▓▓▓▓▓   ▓▓░  ░▓▓▓▓▓▓▓▓   ░▓▓▓▓   ░▓▓▓▓   ▓▓░  ░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",Back.WHITE + '    ')
        print(Back.WHITE + '    ', "▓▓▓▓▓▓▓▓▓   ▓▓░  ░▓▓   ░▓▓▓▓▓▓▓        ░▓▓         ░▓▓▓▓   ░▓▓▓▓   ▓▓░  ░▓▓  ▓  ▓  ▓▓▓▓▓▓▓▓▓",Back.WHITE + '    ')
        print(Fore.YELLOW + ' ▦ ', " ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓",Fore.YELLOW + ' ▦ ')
        print(Back.WHITE + '    ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '     ', Fore.YELLOW + '▦ ', Back.WHITE + '    ')

        num_rodadas = input('\nEm quantas rodadas você acha que vai ganhar? ')
        while not num_rodadas.isdigit():
            print('\nOps! Precisa ser um número... Tente novamente! :)')
            num_rodadas = input('Em quantas rodadas você acha que vai ganhar? ')
        
        num_rodadas = int(num_rodadas)
        for n in range(0, num_rodadas+1):
            jogador.aposta()
            computador.aposta()

            if n > 1:
                if jogador.fichas == 0:
                    print('PC WINS!')
                    print(Style.RESET_ALL + Back.RED + "\nPONTUAÇÃO FINAL:" + Style.RESET_ALL)
                    print(f"{jogador.nome}: {jogador.pontos} pontos")
                    print(f"Computador: {computador.pontos} pontos")
                    break
                
                elif computador.fichaspc == 0:
                    print('PLAYER WINS!')
                    print(Style.RESET_ALL + Back.RED + "\nPONTUAÇÃO FINAL:" + Style.RESET_ALL)
                    print(f"{jogador.nome}: {jogador.pontos} pontos")
                    print(f"Computador: {computador.pontos} pontos")
                    break

                else:
                    continue

            jogador.pontos = 0
            computador.pontos = 0

            while True:
                jogador.Jogar_dado()
                print(Style.RESET_ALL + Fore.YELLOW + '_________________________________' + Style.RESET_ALL)

                computador.Jogar_dado()

                if jogador.pontos > 21:
                    computador.fichaspc = computador.fichaspc + (jogador.apostadas*2)
                    print('\n🖥️ PC WINS!')
                    print('')
                    break                   

                elif jogador.pontos == 21:
                    jogador.fichas = jogador.fichas + (jogador.apostadas*2)
                    print('\nPLAYER WINS!')
                    break

                elif computador.pontos > 21:
                    jogador.fichas = jogador.fichas + (jogador.apostadas*2)
                    print('\nPLAYER WINS!')
                    break

                elif computador.pontos== 21:
                    computador.fichaspc = computador.fichaspc + (jogador.apostadas*2)
                    print('\n🖥️ PC WINS!')
                    break
                    
                    # EM CASO DE EMPATE
                elif jogador.pontos > 21 and computador.pontos > 21:
                    if computador.pontos == jogador.pontos:
                        print('EMPATE!')
                    elif computador.pontos > jogador:
                        jogador.fichas = jogador.fichas + (jogador.apostadas*2)
                        print('PLAYER WINS!')
                    else:
                        computador.fichaspc = computador.fichaspc + (jogador.apostadas*2)
                        print('🖥️ PC WINS!')
                else:
                    continue  # Se ninguém ganhou, continua o jogo
            
            print(Style.RESET_ALL)
            print(Back.RED + "PONTUAÇÃO FINAL:", Style.RESET_ALL)
            print(f"{(jogador.nome).upper()}: {jogador.pontos} pontos")
            print(f"COMPUTADOR: {computador.pontos} pontos")  

    elif modo.upper() == "CLASSICO" or modo.upper() == "CLÁSSICO":

        while True:
            jogador.Jogar_dado()
            print(Style.RESET_ALL + Fore.YELLOW + '_________________________________' + Style.RESET_ALL)
            computador.Jogar_dado()

            if jogador.pontos > 21:
                print('\n🖥️ PC WINS!')
                print('')
                break

            elif jogador.pontos == 21:
                print('\nPLAYER WINS!')
                break

            elif computador.pontos > 21:
                print('\nPLAYER WINS!')
                break

            elif computador.pontos== 21:
                print('\n🖥️ PC WINS!')
                break
            
            # EM CASO DE EMPATE
            elif jogador.pontos > 21 and computador.pontos > 21:
                if computador.pontos == jogador.pontos:
                    print('EMPATE!')
                elif computador.pontos > jogador:
                    print('PLAYER WINS!')
                else:
                    print('🖥️ PC WINS!')
            else:
                continue  # Se ninguém ganhou, continua o jogo

            # PONTUAÇÃO FINAL
        
        print()
        print(Back.RED + "PONTUAÇÃO FINAL:", Style.RESET_ALL)
        print(f"{(jogador.nome).upper()}: {jogador.pontos} pontos")
        print(f"COMPUTADOR: {computador.pontos} pontos")  

if __name__ == "__main__":
    main()

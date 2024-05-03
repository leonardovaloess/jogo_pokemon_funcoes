import random

import subprocess

def limpar_terminal():
    # Utiliza o comando apropriado para limpar o terminal dependendo do sistema operacional
    subprocess.call('cls' if subprocess._mswindows else 'clear', shell=True)

pokemons = []
pokemons_da_rota = []
rota = ''

def introducao():
    limpar_terminal()
    print(30*'-')
    nome = input('Olá!! Seja bem vindo ao mundo pokemon!! Os Pokémons são criaturas incríveis que compartilham o mundo com os seres humanos\n\nPara começar, diga seu nome: \n\n')
    limpar_terminal()
    print(f'\nSeja bem vindo {nome}!!\n' + 30*'-')

def inicial():
    while True: 
        opcao = input(f'Para começar sua jornada, escolha seu pokemon inicial, ele será seu parceiro nessa sua aventura!\n\n 1 - Charmander\n 2 - Squirtle\n 3 - Bulbassauro \n\n')

        if opcao != '1' and opcao != '2' and opcao != '3':
            print('\nOpção inválida\n')
        elif opcao == '1':
            pokemon_inicial = 'Charmander'
            pokemons.append(pokemon_inicial)
            limpar_terminal()
            print(f'\nMuito bem!!! {pokemon_inicial} Será seu parceiro daqui pra frente, lute, explore e capture novos pokemons!!\n' )
            break
        elif opcao == '2':
            pokemon_inicial = 'Squirtle'
            pokemons.append(pokemon_inicial)
            limpar_terminal()
            print(f'\nMuito bem!!! {pokemon_inicial} Será seu parceiro daqui pra frente, lute, explore e capture novos pokemons!!\n')
            break
        elif opcao == '3':
            pokemon_inicial = 'Bulbassauro'
            pokemons.append(pokemon_inicial)
            limpar_terminal()
            print(f'\nMuito bem!!! {pokemon_inicial} Será seu parceiro daqui pra frente, lute, explore e capture novos pokemons!!\n' )
            break

def interacao():
    while True:
        
        opcao = int(input('Aonde deseja ir?\n\n1 - Caverna\n2 - Mato\n3 - Ver pokedex\n4 - Sair do jogo\n\n'))
        
        if opcao == 1:
            rota = 'Caverna'
            limpar_terminal()
            print(f"\nVocê Agora está na Caverna\n" + 30*'-')
            pokemons_da_rota = ["Zubat", "Geodude", "Onix", "Cubone", "Machop"]
            
        elif opcao == 2:
            rota = 'mato'
            limpar_terminal()
            print('\nVocê Agora está no Mato\n' + 30*'-' )
            pokemons_da_rota = ["Pidgey", "Rattata", "Caterpie", "Weedle", "Oddish"]
            
        elif opcao == 3:
            limpar_terminal()
            print(30*'-')
            print(f"\nPokedex - {pokemons}\n")
            print(30*'-')

        elif opcao == 4:
            print("\nSaindo do jogo...\n")
            print(30*'-')
            break
        else:
            print('\nOps, acho q n da pra ir por aí amigão\n')

        if opcao == 1 or opcao == 2:
            while True:
                
                pokemon_encontrado = pokemons_da_rota[random.randint(0, len(pokemons_da_rota) - 1)]
                opcao = int(input(f'\nlocal: {rota}\n\nVocê encontrou um {pokemon_encontrado}!, o que deseja fazer?\n\n1 - Capturar\n2 - Ignorar\n\n' ))
                if opcao == 2:
                    print(30*'-')
                    limpar_terminal()
                    print(f'Você ignorou o {pokemon_encontrado}')
                    print(30*'-')
                    break
                elif opcao == 1 and rota == 'mato':
                    limpar_terminal()
                    tentativas_de_captura = 3
                    capturar = None
                    while tentativas_de_captura > 0:
                        limpar_terminal()
                        print(30*'-')
                        print(f'\nTentando capturar {pokemon_encontrado}\n\ntentativas: {tentativas_de_captura}\n' )
                        probabilidade = random.random()
                            
                        if probabilidade <= 0.5:
                            capturar = True
                            break
                        else:
                            print(30*'-')
                            tentarNovamente = int(input(f'{pokemon_encontrado} escapou da pokeball!\n\nTentar novamente?\n\n1 - sim\n2 - nao\n\n'))
                            
                            if tentarNovamente == 2:
                                print('\nVocê desistiu!')
                                capturar = False
                                

                                break
                                

                            elif tentarNovamente == 1:
                                limpar_terminal()
                                tentativas_de_captura -= 1
                                
                                if tentativas_de_captura == 0:
                                    limpar_terminal()
                                    capturar = False
                                    break
                                print('\nTentando novamente...\n')
                                
                    
                    if capturar:
                        limpar_terminal()
                        print(30*'-')
                        print(f'\nVocê capturou o {pokemon_encontrado}!\n' )
                        print(30*'-')
                        pokemons.append(pokemon_encontrado)
                        break
                    if capturar == False:
                        print(30*'-')
                        print(f'\n{pokemon_encontrado} escapou!' )
                        print(30*'-')
                        break
                elif opcao == 1 and rota == 'Caverna':
                    tentativas_de_captura = 3
                    capturar = None
                    while tentativas_de_captura > 0:
                        limpar_terminal()
                        print(30*'-')
                        print(f'\nTentando capturar {pokemon_encontrado}\n\ntentativas: {tentativas_de_captura}\n' )
                        probabilidade = random.random()
                        print(30*'-')
                        if probabilidade <= 0.35:
                            capturar = True
                            break
                        else:
                            
                            tentarNovamente = int(input(f'{pokemon_encontrado} escapou da pokeball!\n\nTentar novamente?\n\n1 - sim\n2 - nao\n\n'))
                            
                            if tentarNovamente == 2:
                                print(30*'-')
                                print('\nVocê desistiu!')
                                capturar = False
                                print(30*'-')

                                break
                                

                            elif tentarNovamente == 1:
                                
                                tentativas_de_captura -= 1
                                
                                if tentativas_de_captura == 0:
                                    capturar = False
                                    break
                                print('\nTentando novamente...\n')
                                
                    
                    if capturar:
                        limpar_terminal()
                        print(30*'-')
                        print(f'\nVocê capturou o {pokemon_encontrado}!\n' )
                        print(30*'-')
                        pokemons.append(pokemon_encontrado)
                        break
                    if capturar == False:
                        limpar_terminal()
                        print(30*'-')
                        print(f'\n{pokemon_encontrado} escapou!' )
                        print(30*'-')
                        break
                else:
                    print('Opçao inválida!')

def executar_jogo():
    while True:
        #INTRODUÇÃO
        
        introducao()

        #Escolhendo inicial
        
        inicial()
        
        # Interface de interação
        
        interacao()
            
        break


executar_jogo()
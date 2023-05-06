# aula 
# Listas são feitos com []

import os

os.system('cls')

lista = []

while True:
    
    print('Selecione uma opção: ')

    opcao = input('[i]nserir [a]pagar [l]istar | [s]air: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
        print('\n')
        
    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Digite oque vc quer apagar: ')
        print('\n')

        try:
            indice = int(indice_str)
            del lista[indice]
            os.system('cls')
            print('Apagado com sucesso!\n')
        except ValueError:
            os.system('cls')
            print('Não foi possivel apagar esse índice, favor digitar um numero.\n')

        except IndexError:
            os.system('cls')
            print('Favor digitar um número que esteja dentro da lista.\n')

        except Exception:
            os.system('cls')
            print('Erro Desconhecido.\n')
        
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar\n')

        
        for i, valor in enumerate(lista):
            print(i, valor)
                      
        print("\n")

    if opcao == 's':
        os.system('cls')
        break
from random import randint
from menus import espaços

def menu_listas():
        print('\033[4:31mListas\033[m')
        print(
            'As Listas são variáveis compostas e \033[1:31mmutáveis\033[m diferente das tuplas, que permitem armazenar')
        print(
            '\033[1:31mvários\033[m valores em uma mesma estrutura, acessíveis por \033[1:31mchaves individuais\033[m[].\n\033[1mExemplos\033[m:')

        while True:
            opcao_listas = int(input('[1] como remover um objeto da lista\n'
            '[2] formas de remover um objeto\n'
            '[3] sair'))
            espaços.lin4()
            # Remoção com remove
            if opcao_listas == 1:
                print('Exemplo: ')
                lista = [randint(0, 5),
                         randint(0, 5),
                         randint(0, 5),
                         randint(0, 5)]

                if 5 in lista:
                    lista.remove(5)

                print(f'foram lidos {len(lista)} valores da lista:\n{lista}')

                continuar_exemplo = str(input('Deseja ver outro exemplo? SIM/NÃO')).lower().strip()[0]
                if continuar_exemplo == 's':
                    continue
                elif continuar_exemplo=='n':
                    break

            # Outras formas de remover itens
            elif opcao_listas == 2:
                print(
                    'na lista existem 3 metodos: 1° \033[1:31mdel lista[0]\033[m (sem espaço) 2° \033[1:31mlista.pop(0)\033[m\ne a 3° que consiste em excluir um objeto'
                    ' espefico da lista, sendo ele \033[1:31mlista.remove()\033[m em casos de escassez do item utiliza se o if')

                exemplo = str(input('Ver como funciona? [S/N]')).lower().strip()[0]
                if exemplo == 's':
                    print('''lista= [1,2,3,4]
a= (f'{lista.append(10)}')
R: [1, 2, 3, 4, 10] ''')
                elif exemplo=='n':
                    break
                continuar_exemplo = str(input('ver outro exemplo? [S/N]')).lower().strip()[0]
                if continuar_exemplo == 's':
                    continue
                elif continuar_exemplo=='n':
                    break
            elif opcao_listas==3:
                break
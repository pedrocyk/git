from time import sleep
from random import randint

def lin1():
    print ('='*30)
def lin2():
    print('~'*30)
def lin3():
    print('-'*30)
def lin4():
    print('_'*30)
opcao_menu_principal = opcao_funcoes = opcao_listas = 0

# loop (menu principal)
while True:
    lin1()

    print(f'{'\033[1:35mBiblioteca em Python\033[m':^40}\n'
          f'{'\033[3mCurso em video\033[m':^35}')
    lin1()

    print('\033[3mBem vindo a sua Biblioteca Python\033[m')

    # Menu principal
    print('''[1] aula 17 \033[1mlistas\033[m
[2] aula 16 \033[1mtuplas\033[m
[3] aula 15
[4] funções  
[5] sair
''')

    # Tratamento de erro para garantir que o usuário digite um número
    while True:
        try:
            opcao_menu_principal = int(input('Qual item deseja relembrar?'))
        except ValueError:
            opcao_menu_principal = int(input('\033[1:31mErro\033[m...\nQual item deseja relembrar?'))
        if opcao_menu_principal in range (1,6):
            break
    lin2()
    # Opção para sair do programa
    if opcao_menu_principal == 5:
        break

    # ==================== MENU DE FUNÇÕES ====================
    if opcao_menu_principal == 4:
        while True:
            print('[1] localização\033[34m Index\033[m\n'
                  '[2] contagem \033[36mlen\033[m\n'
                  '[3] inverção\033[32m Reverse\033[m\n'
                  '[5] \033[1:31msair\033[m')

            opcao_funcoes = int(input('Qual função quer visualizar? '))
            # Opção 1 - Localização (index)
            if opcao_funcoes == 1:
                lin3()
                print('\033[1:36m[index]\033[m \033[36mMétodo usado para encontrar a posição (índice)\n'
                      'em listas, tuplas ou strings.\033[m')
                print ('''Exemplo:
\033[1mnomes = ['Ana', 'João', 'Maria']\033[m
\033[1mposicao = nomes.index('Maria')\033[m
\033[1mprint(posicao)\033[m''')  # saída: 2

                continuar_exemplo= str(input ('Quer ver outra função? [S/N]')).lower().strip()[0]
                lin3()
                if continuar_exemplo== 's':
                    continue
                elif continuar_exemplo== 'n':
                    break
            # Opção 2 - Contagem com len()
            if opcao_funcoes == 2:
                lin3()
                print('Para realizar uma contagem usa-se \033[1:35mlen\033[m\n\033[1mExemplo...\033[m')

                # Pergunta se o usuário quer ver como funciona
                ver_exemplo = str(input('Deseja ver o exemplo? [s/n] ')).lower().strip()[0]

                if ver_exemplo == 's':
                    lin4()
                    print('''lista = ['Sebastian','Jorge']
for cont in lista:
    print (f'{cont}')  ''')
                    print ( '[Sebastian , jorge] ')
                    continuar_exemplo = str(input('\nQuer ver outro exemplo? [sim/não]')).strip().lower()[0]
                    if continuar_exemplo == 'n':
                        break

            if opcao_funcoes==3:
                lin4()
                print ('Para inverter uma \033[32mstring\033[m é comum usado "[::-1]" \n\033[1mExemplo\033[m: ')
                print ("nome=pedro\nnome_inverso=nome{::-1} #ordep ")
                continuar_exemplo= str (input ('Quer ver outra função? [S/N]')).lower().strip()[0]
                lin2()
                if continuar_exemplo=='s':
                    continue
                elif continuar_exemplo=='n':
                    break

            if opcao_funcoes==5:
                break

    # ==================== OPÇÃO EM OBRAS ====================
    if opcao_menu_principal == 3:
        print('Em obras...')
        break

    # ==================== MENU DE TUPLAS ====================
    if opcao_menu_principal == 2:
        print('\033[4:34mtuplas\033[m')
        print('As tuplas são variáveis compostas e \033[1:34mimutáveis\033[m que permitem armazenar')
        print(
            '\033[1:34mvários\033[m valores em uma mesma estrutura, acessíveis por \033[1:34mchaves individuais\033[m{}.\n\033[1mExemplos\033[m:')

        while True:
            opcao_tuplas = int(input('[1] Números por extenso.\n'
                            '[2] Maior e menor/random\n'
                            '[3] Localização em tuplas\n'
                            '[4] sair'))
            # Opção 1 - Números por extenso
            if opcao_tuplas == 1:
                numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                         'onze', 'doze',
                         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

                numero = int(input('digite um valor entre 0 e 20:'))
                print(f'\033[34m{numeros_extenso[numero]}\033[m')

                exe1 = int(input('Para ver o exercício digite 0 ou se não 1: '))
                lin3()
                # Mostra o código do exercício
                if exe1 == 0:
                    print('''[tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = int(input('digite um valor entre 0 e 20:'))
print(f'{tupla[resp]}')''')

            # Opção 2 - Maior e menor valor da tupla
            if opcao_tuplas == 2:
                tuplas_numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
                print(f'O maior número sorteado foi {max(tuplas_numeros)}')
                print(f'O menor número sorteado foi {min(tuplas_numeros)}')

                continuar_exemplo = str(input('Deseja ver outro exemplo? SIM/NÃO')).lower().strip()[0]
                lin3()
                if continuar_exemplo == 'n':
                    break

            # Opção 3 - Contagem e localização dentro da tupla
            if opcao_tuplas == 3:
                cont = 0
                tupla_valores = (
                    int(input('Digite um valor: ')),
                    int(input('Digite outro valor: ')),
                    int(input('Digite mais um valor: ')),
                    int(input('Digite o último valor: '))
                )
                print(f'9 apareceu {tupla_valores.count(9)} vezes')

                # Verifica se o número 3 existe na tupla

                if 3 in tupla_valores:
                    print(f'O valor 3 está na {tupla_valores.index(3) + 1}° posição ')
                else:
                    sleep(0.5)
                    print('\033[1:31mAcabou!!\033[m')

                mostrar_exemplo = str (input('Visualizar antes de continuar? (visualizar/continuar): ')).strip().lower()[0]
                if mostrar_exemplo == 'v':
                    lin2()
                    print('''cont = 0
tuplas = (int(input('digite um valor: ')),
int(input('Digite outro valor: ')),
int(input('Digite mais um valor: ')),
int(input('digite o ultimo valor ')))
print(f'9 apareceu {t.count(9)} vezes')
    if 3 in t:
    print(f'O valor 3 está na {t.index(3) + 1}° posição ')
else:
    sleep(0.5)''')
                perg = str(input('Deseja ver outro exemplo? SIM/NÃO')).lower().strip()[0]
                if perg == 'n':
                    break

            if opcao_tuplas == 4:
                break
    # ==================== MENU DE LISTAS ====================
    if opcao_menu_principal == 1:
        print('\033[4:31mListas\033[m')
        print(
            'As Listas são variáveis compostas e \033[1:31mmutáveis\033[m diferente das tuplas, que permitem armazenar')
        print(
            '\033[1:31mvários\033[m valores em uma mesma estrutura, acessíveis por \033[1:31mchaves individuais\033[m[].\n\033[1mExemplos\033[m:')

        while True:
            opcao_listas = int(input('[1] como remover um objeto da lista\n'
            '[2] formas de remover um objeto\n'
            '[3] sair'))
            lin4()
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

    continuar = str(input('Deseja continuar com a biblioteca? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break

print('\033[1mFinalizando...\033[m')
sleep(1)
print('Biblioteca finalizada, tenha um bom dia!!!')

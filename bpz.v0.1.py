from time import sleep  # Importa a função sleep para pausas no programa
from random import randint  # Importa randint para gerar números aleatórios

# Variáveis que controlam os menus
opcao_menu_principal = opcao_funcoes = opcao_listas = 0

# Loop principal do programa (menu principal)
while True:
    print('=' * 30)
    # Título formatado com cores ANSI
    print(f'{'\033[1:35mBIBLIOTECA PYTHON\033[m':^40}\n'
          f'{'\033[3mDo Pedro\033[m':^35}')
    print('=' * 30)

    print('\033[3mBem vindo a sua Biblioteca Python\033[m')

    # Menu principal
    print('''[1] aula 17 \033[1mlistas\033[m
[2] aula 16 \033[1mtuplas\033[m
[3] aula 15
[4] funções  
[5] sair
''')

    # Tratamento de erro para garantir que o usuário digite um número
    try:
        opcao_menu_principal = int(input('Qual item deseja relembrar?'))
        print('~' * 30)
    except ValueError:
        opcao_menu_principal = int(input('\033[1:31mErro\033[m...\nQual item deseja relembrar?'))

    # Opção para sair do programa
    if opcao_menu_principal == 5:
        break

    # ==================== MENU DE FUNÇÕES ====================
    if opcao_menu_principal == 4:
        while True:
            print('[1] localização\n'
                  '[2] contagem \033[1:35mlen\033[m\n'
                  '[3] inverção ')

            # Garante que a opção seja válida
            if opcao_funcoes not in range(1, 4):
                opcao_funcoes = int(input('Qual função quer visualizar?'))

            # Opção 1 - Localização
            if opcao_funcoes == 1:
                print('-' * 30)
                print('Para localizar um item ')

            # Opção 2 - Contagem com len()
            if opcao_funcoes == 2:
                print('-' * 30)
                print('Para realizar uma contagem usa-se \033[1:35mlen\033[m\n\033[1mExemplo\033[m:')

                # Lista de exemplo
                listaop4 = ['Sebastian', 'Jorge', 'Cristovam''e', 'josépi']

                # Mostra os valores da lista
                for nome in listaop4:
                    print(f'{nome}', end=' ')

                # Pergunta se o usuário quer ver como funciona
                ver_exemplo = str(input('\nDigite S para ver como funciona')).lower().strip()[0]

                if ver_exemplo == 's':
                    print('_' * 30)
                    print('''listaop4= ['Sebastian','Jorge', 'Cristovam''e','josépi']
                    for c in listaop4:
                        print (f'{c}',end=' ')''')

                    continuar_exemplo = str(input('\nQuer ver outro exemplo? [sim/não]')).strip().lower()[0]
                    if continuar_exemplo == 'n':
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
                            '[3] Localização em tuplas'))
            # Opção 1 - Números por extenso
            if opcao_tuplas == 1:
                numeros_extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                         'onze', 'doze',
                         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

                numero = int(input('digite um valor entre 0 e 20:'))
                print(f'\033[34m{numeros_extenso[numero]}\033[m')

                exe1 = int(input('Para ver o exercício digite 0 ou se não 1: '))
                print('-' * 30)

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
                print('-' * 20)
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

                exe1 = int(input('Para ver o exercício digite 0 ou se não 1: '))
                if exe1 == 0:
                    print('''cont = 0
    t = (int(input('digite um valor: ')),
     int(input('Digite outro valor: ')),
     int(input('Digite mais um valor: ')),
     int(input('digite o ultimo valor ')))
    print(f'9 apareceu {t.count(9)} vezes')
    if 3 in t:
        print(f'O valor 3 está na {t.index(3) + 1}° posição ')
    else:
        sleep(0.5)
    print('\033[1:31mAcabou!!\033[m')''')

                perg = str(input('Deseja ver outro exemplo? SIM/NÃO')).lower().strip()[0]
                if perg == 'n':
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
                            '[2] formas de remover um objeto'))
            print('_' * 30)

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
            if continuar_exemplo == 'n':
                break

            # Outras formas de remover itens
            if opcao_listas == 2:
                print(
                    'na lista existem 3 metodos: 1° \033[1:31mdel lista[0]\033[m (sem espaço) 2° \033[1:31mlista.pop(0)\033[m\ne a 3° que consiste em excluir um objeto'
                    ' espefico da lista, sendo ele \033[1:31mlista.remove()\033[m em casos de escassez do item utiliza se o if')

                exemplo = str(input('Ver como funciona? [S/N]')).lower().strip()[0]
                if exemplo == 's':
                    print('''lista= [1,2,3,4]
a= (f'{lista.append(10)}')
R: [1, 2, 3, 4, 10] ''')

            continuar_exemplo = str(input('ver outro exemplo? [S/N]')).lower().strip()[0]
            if continuar_exemplo == 'n':
                break

    continuar = str(input('Deseja continuar com o estudo? [S/N] ')).lower()
    if continuar == 'n':
        break

print('\033[1mFinalizando...\033[m')
sleep(1)
print('Biblioteca finalizada, tenha um bom dia!!!')

# organização para separar melhor os codigos um dos outros
# fazer comentarios grandes para eu entender o codigo

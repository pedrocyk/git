from random import randint
from time import sleep
from menus import espaços
def tuplas():
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
            espaços.lin3()
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
            espaços.lin3()
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
                espaços.lin2()
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
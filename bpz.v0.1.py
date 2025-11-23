from time import sleep
from random import randint

opçoes=opc=opx=0

while True:
    print('=' * 30)
    print(f'{'\033[1:35mBIBLIOTECA PYTHON\033[m':^40}\n'
          f'{'\033[3mCurso em video\033[m':^35}')
    print('=' * 30)
    print('\033[3mBem vindo a sua Biblioteca Python\033[m')
    print('''[1] aula 17 \033[1mlistas\033[m
[2] aula 16 \033[1mtuplas\033[m
[3] aula 15
[4] funções  
[5] nenhum
''')

    try:
        opçoes = int(input('Qual item deseja relembrar?'))
        print('~' * 30)
    except valorerro:
        opçoes= int (input('Erro...\n Qual item deseja relembrar?'))
    if opçoes==5:
        break
    if opçoes==4:
        while True:
            print ('[1] localização\n'
                   '[2] contagem \033[1:35mlen\033[m\n'
                   '[3] inverção ')
            if opc not in range (1,4):
                opc = int (input ('Qual função quer visualizar?'))
            if opc == 1:
                print ('-'*30)
                print ('Para localizar um item ')
            if opc ==2:
                print ('-'*30)
                print ('Para realizar uma contagem usa-se \033[1:35mlen\033[m\n\033[1mExemplo\033[m:')
                listaop4= ['Sebastian','Jorge', 'Cristovam''e','josépi']
                for c in listaop4:
                    print (f'{c}',end=' ')
                intopc2 = str (input ('\nDigite S para ver como funciona')).lower().strip()[0]
                if intopc2=='s':
                    print ('_'*30)
                    print ('''listaop4= ['Sebastian','Jorge', 'Cristovam''e','josépi']
                    for c in listaop4:
                        print (f'{c}',end=' ')''')
                    contin=str (input ('\nQuer ver outro exemplo? [sim/não]')).strip().lower()[0]
                    if contin == 'n':
                        break

    if opçoes==3:
        print ('Em obras...')
        break

    if opçoes == 2:
        print('\033[4:34mtuplas\033[m')
        print('As tuplas são variáveis compostas e \033[1:34mimutáveis\033[m que permitem armazenar')
        print('\033[1:34mvários\033[m valores em uma mesma estrutura, acessíveis por \033[1:34mchaves individuais\033[m{}.\n\033[1mExemplos\033[m:')
        while True:
            opç = int(input('[1] Números por extenso.\n'
                            '[2] Maior e menor/random\n'
                            '[3] Localização em tuplas'))
            if opç == 1:
                tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
                         'onze', 'doze',
                         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
                resp = int(input('digite um valor entre 0 e 20:'))
                print(f'\033[34m{tupla[resp]}\033[m')
                exe1 = int(input('Para ver o exercício digite 0 ou se não 1: '))
                if exe1 == 0:
                    print('''[tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
resp = int(input('digite um valor entre 0 e 20:'))
print(f'{tupla[resp]}')''')
            if opç == 2:
                tuplas = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
                print(f'O maior número sorteado foi {max(tuplas)}')
                print(f'O menor número sorteado foi {min(tuplas)}')
                perg = str(input('Deseja ver outro exemplo? SIM/NÃO')).lower().strip()[0]
                if perg == 'n':
                    break
            if opç==3:
                cont = 0
                t = (int(input('digite um valor: ')),
                     int(input('Digite outro valor: ')),
                     int(input('Digite mais um valor: ')),
                     int(input('digite o ultimo valor ')))
                print(f'9 apareceu {t.count(9)} vezes')
                if 3 in t:
                    print(f'O valor 3 está na {t.index(3) + 1}° posição ')
                else:
                    sleep(0.5)
                    print('\033[1:31mAcabou!!\033[m')
                exe1 = int(input('Para ver o exercício digite 0 ou se não 1: '))
                if exe1 == 0:
                    print ('''cont = 0
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

    if opçoes ==1:
            print('\033[4:31mListas\033[m')
            print('As Listas são variáveis compostas e \033[1:31mmutáveis\033[m diferente das tuplas, que permitem armazenar')
            print('\033[1:31mvários\033[m valores em uma mesma estrutura, acessíveis por \033[1:31mchaves individuais\033[m[].\n\033[1mExemplos\033[m:')
            while True:

                opx = int(input('[1] como remover um objeto da lista\n'
                        '[2] formas de remover um objeto'))
                print('_' * 30)
                if opx == 1:
                    print ('Exemplo: ')
                    lista= [randint (0,5),
                    randint (0,5),
                    randint (0,5),
                    randint (0,5)]
                    if 5 in lista:
                        lista.remove(5)
                    print (f'foram lidos {len(lista)} valores da lista:\n{lista}')
                    cont1=str (input ('Deseja ver outro exemplo? SIM/NÃO')).lower().strip()[0]
                    if cont1=='n':
                        break
                if opx==2:
                    print ('na lista existem 3 metodos: 1° \033[1:31mdel lista[0]\033[m (sem espaço) 2° \033[1:31mlista.pop(0)\033[m\ne a 3° que consiste em excluir um objeto' 
' espefico da lista, sendo ele \033[1:31mlista.remove()\033[m em casos de escassez do item utiliza se o if')
                    exemplo= str (input ('Ver como funciona? [S/N]')).lower().strip()[0]
                    if exemplo== 's':
                        print ('''lista= [1,2,3,4]
a= (f'{lista.append(10)}')
print (lista) ''')
                whilecont= str (input ('ver outro exemplo? [S/N]')).lower().strip()[0]
                if whilecont=='n':
                    break


    continuar = str(input('Deseja continuar com o estudo? [S/N] ')).lower()
    if continuar == 'n':
        break

print ('\033[1mFinalizando...\033[m')
sleep (1)
print ('Biblioteca finalizada, tenha um bom dia!!')
#arrumei o item dois das listas
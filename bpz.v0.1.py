from time import sleep
from random import randint
while True:
    print ('='*30)
    print (f'{'\033[1:35mBIBLIOTECA PYTHON\033[m':^40}\n'
             f'{'\033[3mCurso em video\033[m':^35}')
    print ('='*30)
    print ('\033[3mBem vindo a sua Biblioteca Python\033[m')
    print ('''[1] aula 17
[2] aula 16
[3] aula 15
''')
    opçoes= int (input ('Qual aula deseja relembrar?'))
    print ('~'*30)
    if opçoes ==3:
        print ('\033[1:33mEM OBRAS\033[m')
        break
    if opçoes == 2:
        print ('\033[4:34mtuplas\033[m')
        print ('As tuplas são variáveis compostas e \033[1:34mimutáveis\033[m que permitem armazenar')
        print ('\033[1:34mvários\033[m valores em uma mesma estrutura, acessíveis por \033[1:34mchaves individuais\033[m{}.\n\033[1mExemplos\033[m:')
        while True:
            opç=int (input ('[1] Números por extenso.\n'
                            '[2] Maior e menor/random '))
            if opç ==1:
                    tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
                         'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
                    resp = int(input('digite um valor entre 0 e 20:'))
                    print(f'{tupla[resp]}')
            if opç ==2:
                tuplas=(randint (1,10), randint (1,10), randint(1,10) , randint (1,10), randint (1,10))
                print (f'O maior número sorteado foi {max(tuplas)}')
                print (f'O menor número sorteado foi {min(tuplas)}')
                resposta= str (input ('Desejar ver outro exemplo?')).strip().lower()
            res=str (input ('Deseja ver outra aula?')).lower().strip ()
            if res == 's':
                break
    if opçoes ==1:
        print('\033[4:31mListas\033[m')
        print ('[1] como remover um objeto da lista\n')
        op=int (input ('Qual método deseja ver? '))
        print ('_'*30)
        if op == 1:
            print ('''na lista existem 3 metodos: 1° \033[1:31mdel lista[0]\033[m (sem espaço) 2° \033[1:31mlista.pop(0)\033[m e a 3° que consiste em excluir um objeto 
espefico da lista, sendo ele \033[1:31mlista.remove()\033[m em casos de escassez do item utiliza se o if''')
            opx= int (input ('[1]ex 1°'))
            while True:
                if opx == 1:
                    print ('Exemplo: ')
                    lista= [randint (0,5),
                    randint (0,5),
                    randint (0,5),
                    randint (0,5)]
                    if 5 in lista:
                        lista.remove(5)
                    print (f'foram lidos {len(lista)} valores da lista:\n{lista}')
                    continuar = str(input('Quer relembrar o exemplo? [S/N] ')).lower()
                    if continuar == 'n':
                        break
            continuar= str (input ('Deseja continuar com o estudo? [S/N] ')).lower ()
            if continuar == 'n':
                break
print ('\033[1mFinalizando...\033[m')
sleep (1)
print ('Banco de dados finalizado, tenha um bom dia!!')
#07/11/2025 16:32 sexta-feira
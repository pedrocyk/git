from menus import espaços
def funcao():
    while True:
        print('[1] localização\033[34m Index\033[m\n'
              '[2] contagem \033[36mlen\033[m\n'
              '[3] inverção\033[32m Reverse\033[m\n'
              '[5] \033[1:31msair\033[m')

        opcao_funcoes = int(input('Qual função quer visualizar? '))
        # Opção 1 - Localização (index)
        if opcao_funcoes == 1:
            espaços.lin3()
            print('\033[1:36m[index]\033[m \033[36mMétodo usado para encontrar a posição (índice)\n'
                  'em listas, tuplas ou strings.\033[m')
            print ('''Exemplo:
\033[1mnomes = ['Ana', 'João', 'Maria']\033[m
\033[1mposicao = nomes.index('Maria')\033[m
\033[1mprint(posicao)\033[m''')  # saída: 2

            continuar_exemplo= str(input ('Quer ver outra função? [S/N]')).lower().strip()[0]
            espaços.lin3()
            if continuar_exemplo== 's':
                continue
            elif continuar_exemplo== 'n':
                break
        # Opção 2 - Contagem com len()
        if opcao_funcoes == 2:
            espaços.lin3()
            print('Para realizar uma contagem usa-se \033[1:35mlen\033[m\n\033[1mExemplo...\033[m')

            # Pergunta se o usuário quer ver como funciona
            ver_exemplo = str(input('Deseja ver o exemplo? [s/n] ')).lower().strip()[0]

            if ver_exemplo == 's':
                espaços.lin3()
                print('''lista = ['Sebastian','Jorge']
for cont in lista:
print (f'{cont}')  ''')
                print ( '[Sebastian , jorge] ')
                continuar_exemplo = str(input('\nQuer ver outro exemplo? [sim/não]')).strip().lower()[0]
                if continuar_exemplo == 'n':
                    break

        if opcao_funcoes==3:
            espaços.lin4()
            print ('Para inverter uma \033[32mstring\033[m é comum usado "[::-1]" \n\033[1mExemplo\033[m: ')
            print ("nome=pedro\nnome_inverso=nome{::-1} #ordep ")
            continuar_exemplo= str (input ('Quer ver outra função? [S/N]')).lower().strip()[0]
            espaços.lin2()
            if continuar_exemplo=='s':
                continue
            elif continuar_exemplo=='n':
                break

        if opcao_funcoes==5:
            break
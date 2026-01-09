from time import sleep
from menus import espaços,menu_listas, menu_principal, menu_tuplas, menu_funcao

opcao_menu_principal = opcao_funcoes = opcao_listas = 0

# loop (principal)
while True:
    menu_principal.menu_princ()
    # Tratamento de erro para garantir que o usuário digite um número
    while True:
        try:
            opcao_menu_principal = int(input('Qual item deseja relembrar?'))
        except ValueError:
            opcao_menu_principal = int(input('\033[1:31mErro\033[m...\nQual item deseja relembrar?'))
        if opcao_menu_principal in range (1,6):
            break
    espaços.lin2()

    # Opção para sair do programa
    if opcao_menu_principal == 5:
        break

    # ==================== MENU DE FUNÇÕES ====================
    if opcao_menu_principal == 4:
        menu_funcao.funcao()
    # ==================== MENU DE DICIONARIOS ====================
    #if opcao_menu_principal == 3:
    # ==================== MENU DE TUPLAS ====================
    if opcao_menu_principal==2:
        menu_tuplas.tuplas()
    # ==================== MENU DE LISTAS ====================
    if opcao_menu_principal ==1:
        menu_listas.menu_listas()

    continuar = str(input('Deseja continuar com a biblioteca? [S/N] ')).strip().lower()[0]
    if continuar == 'n':
        break

print('\033[1mFinalizando...\033[m')
sleep(1)
print('Biblioteca finalizada, tenha um bom dia!!!')
#total 260 linhas :D
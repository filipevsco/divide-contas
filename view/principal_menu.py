from time import sleep
from controller.UsuarioController import listar_usuarios
from controller.DespesaController import cadastrar_despesa, listar_despesas
from .secundario_editar import menu_editar_dados
from .secundario_resumo import menu_resumo

def menu():
    print("=====================================")
    print("========= DIVIDE CONTAS =============")
    print("=====================================")

    print("[ 1 ] NOVA DESPESA")
    print("[ 2 ] RESUMOS")
    print("[ 3 ] LISTA DE USUÁRIOS")
    print("[ 4 ] EDITAR DADOS")
    print("[ 5 ] LISTA DE DESPESAS")
    print("[ 0 ] SAIR")

    opcao = int(input("DIGITE UMA OPÇÂO: "))

    if opcao == 1:
        cadastrar_despesa()
    elif opcao == 2:
        menu_resumo()
    elif opcao == 3:
        listar_usuarios()
    elif opcao == 4:
        menu_editar_dados()
    elif opcao == 5:
        listar_despesas()
    elif opcao == 0:
        exit()
    else:
        print("Opção invalida, tente novamente.")
        sleep(1)
        menu()

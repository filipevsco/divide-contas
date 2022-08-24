from time import sleep

from controller.UsuarioController import cadastrar_usuario, listar_usuarios, deletar_usuario
from controller.DespesaController import cadastrar_despesa, listar_despesas, deletar_despesa
from .secundario_editar import menu_editar_dados
from .secundario_resumo import menu_resumo

def menu():
    print("\n")
    print("=====================================")
    print("========= DIVIDE CONTAS =============")
    print("=====================================")

    print("[ 1 ] NOVA DESPESA")
    print("[ 2 ] LISTA DE DESPESAS")
    print("[ 3 ] LISTSA DE USUÁRIOS")
    print("[ 4 ] EDITAR DADOS")
    print("[ 5 ] RESUMOS")
    print("[ 0 ] SAIR")

    opcao = int(input("DIGITE UMA OPÇÂO: "))

    if opcao == 1:
        cadastrar_despesa()
    elif opcao == 2:
        listar_despesas()
    elif opcao == 3:
        listar_usuarios()
    elif opcao == 4:
        menu_editar_dados()
    elif opcao == 5:
        menu_resumo()
    elif opcao == 0:
        exit()
    else:
        print("Opção invalida, tente novamente.")
        sleep(1)
        menu()

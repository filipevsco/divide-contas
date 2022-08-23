from time import sleep

from controller.UsuarioController import cadastrar_usuario, listar_usuarios, deletar_usuario
from controller.DespesaController import cadastrar_despesa, listar_despesas, deletar_despesa
from .secundario_editar import menu_editar_dados

def menu():
    print("\n"*3)
    print("=====================================")
    print("========= DIVIDE CONTAS =============")
    print("=====================================")

    print("Por favor, selecione uma opção:")
    print("[ 1 ] Cadastrar Despesa")
    print("[ 2 ] Listar Despesas")
    print("[ 3 ] Listar Usuários")
    print("[ 4 ] Menu edicao")
    print("[ 0 ] Sair do Programa")

    opcao = int(input("DIGITE UMA OPÇÂO: "))

    if opcao == 1:
        cadastrar_despesa()
    elif opcao == 2:
        listar_despesas()
    elif opcao == 3:
        listar_usuarios()
    elif opcao == 4:
        menu_editar_dados()
    elif opcao == 0:
        exit()
    else:
        print("Opção invalida, tente novamente.")
        sleep(1)
        menu()
from time import sleep
from controller.UsuarioController import cadastrar_usuario, deletar_usuario
from controller.DespesaController import deletar_despesa
from controller.CategoriaController import cadastrar_despesa
import view.principal_menu as principal_menu

def menu_editar_dados():
    print("=====================================")
    print("=========== MENU EDIçÃO =============")

    print("[ 1 ] NOVA CATEGORIA")
    print("[ 2 ] EXCLUIR CATEGORIA ")
    print("[ 3 ] NOVO USUÁRIO")
    print("[ 4 ] EDITAR USUÁRIO")
    print("[ 5 ] EXCLUIR USUÁRIO")
    print("[ 6 ] ESCLUIR DESPESA")
    print("[ 0 ] MENU ANTERIOR")
    
    opcao = int(input("OPÇÃO: "))
    
    if opcao == 1:
        cadastrar_despesa()
    elif opcao == 2:
        pass
    elif opcao == 3:
        cadastrar_usuario()
    elif opcao == 4:
        pass
    elif opcao == 5:
        deletar_usuario()
    elif opcao == 6:
        deletar_despesa()
    elif opcao == 0:
        principal_menu.menu()
    else:
        print("opção inválida")
        sleep(1)
        menu()

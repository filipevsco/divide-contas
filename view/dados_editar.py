from time import sleep

from controller.UsuarioController import cadastrar_usuario, deletar_usuario
from controller.DespesaController import deletar_despesa


def menu_editar_dados():
    print("--------------------")
    print("---MENU DE EDIÇÃO---")
    
    print(" [1] - Cadastrar nova categoria")
    print(" [2] - Excluir categoria")
    print(" [3] - Cadastrar novo usuário")
    print(" [4] - Editar usuário")
    print(" [5] - Excluir usuário")
    print(" [6] - Excluir despesa")
    print(" [0] - Retornar ao menu anterior")
    
    opcao = int(input("Digite uma opção: "))
    
    if opcao == 1:
        pass
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
        exit()
    else:
        print("opção inválida")

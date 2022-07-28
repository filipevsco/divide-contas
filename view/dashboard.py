from time import sleep

# from controller.UsuarioController import cadastrar_usuario, listar_usuario, deletar_usuario
# from controller.DespesasController import cadastrar_despesa, listar_despesas, deletar_despesa

def menu():
    print("=====================================")
    print("========= DIVIDE CONTAS ============")
    print("=====================================")

    print("Por favor, selecione uma opção:")
    print("[ 1 ] Cadastrar Novo Usuário")
    print("[ 2 ] Cadastrar Despesa")
    print("[ 3 ] Listar Despesas")
    print("[ 4 ] Listar Usuários")
    print("[ 5 ] Deletar Despesa")
    print("[ 6 ] Deletar Usuário")
    print("[ 0 ] Sair do Programa")

    opcao = int(input("DIGITE UMA OPÇÂO: "))

    if opcao == 1:
        cadastrar_usuario()
    elif opcao == 2:
        cadastrar_despesa()
    elif opcao == 3:
        listar_despesas()
    elif opcao == 4:
        listar_usuarios()
    elif opcao == 5:
        deletar_despesa()
    elif opcao == 6:
        deletar_usuario()
    elif opcao == 0:
        exit()
    else:
        print("Opção invalida, tente novamente.")
        sleep(1)
        menu()

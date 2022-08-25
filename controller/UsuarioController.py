from time import sleep
import view.principal_menu as menu
import db.usuario


def cadastrar_usuario():
    print("=========== NOVO USUÁRIO ============")
    nome = input("NOME: ").upper()
    salario_medio = float(input("SALÁRIO MÉDIO: "))

    db.usuario.cadastrar_usuario(nome, salario_medio)
    print("Criando....")
    sleep(1)
    print("Usuário criado com sucesso")
    sleep(1)
    menu.menu()


def listar_usuarios():
    print("========= LISTA DE USUÁRIOS ==========")
    sleep(1)
    db.usuario.listar_usuario()
    sleep(1)
    print("ENTER PARA CONTINUAR")
    input()
    menu.menu()


def deletar_usuario():

    id = int(input("Digite o ID de usuario que deseja deletar: "))
    id_cofirma = int(input("Confirme o ID de usuário que deseja deletar: "))

    if id == id_cofirma:
        db.usuario.deletar_usuario(id)
    else:
        print("nome invalido, tente novamente")
    sleep(1)
    menu.menu()

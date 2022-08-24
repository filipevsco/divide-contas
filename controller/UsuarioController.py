from time import sleep
import view.principal_menu as menu
import db.usuario


def cadastrar_usuario():
    print("=====================================")
    print("=========== NOVO USUÁRIO ============")
    nome = input("Nome: ")
    salario_medio = float(input("Salário Médio: "))

    db.usuario.cadastrar_usuario(nome, salario_medio)
    print("Criando....")
    sleep(1)
    print("Usuário criado com sucesso")
    sleep(1)


def listar_usuarios():

    print("Carregando lista de usuarios....")
    sleep(1)
    db.usuario.listar_usuario()
    sleep(1)
    print("Tecle ENTER para voltar ao menu")
    input()
    menu.menu()


def deletar_usuario():
    listar_usuarios()

    id = int(input("Digite o ID de usuario que deseja deletar: "))
    id_cofirma = int(input("Confirme o ID de usuário que deseja deletar: "))

    if id == id_cofirma:
        db.usuario.deletar_usuario(id)
    else:
        print("nome invalido, tente novamente")


from time import sleep

from model.UsuarioModel import usuario_db


def cadastrar_usuario():
    print("================+======")
    print("=== NOVO USUÁRIO ======")
    nome = input("Nome: ")
    salario_medio = float(input("Salário Médio: "))

    usuario_db("nome", "salario_medio")
    print("Criando....")
    sleep(1)
    print("Usuário criado com sucesso")
#    print(usuario)
    sleep(1)
    menu()


def listar_usuarios():
    if not usuarios:
        print("Sem usuários cadastrados")
    else:
        for usuario in usuarios:
            print("------------------")
            print(usuario)
            print("------------------")
        print("Fim da Lista")
    sleep(1)
    menu()


def deletar_usuario():
    pass

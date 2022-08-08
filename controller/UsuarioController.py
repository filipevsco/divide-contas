from time import sleep

import model.UsuarioModel as ModelUser

def cadastrar_usuario():
    print("================+======")
    print("=== NOVO USUÁRIO ======")
    nome = input("Nome: ")
    salario_medio = float(input("Salário Médio: "))

    ModelUser.cadastrar_usuario_db(nome, salario_medio)
    print("Criando....")
    sleep(1)
    print("Usuário criado com sucesso")
#    print(usuario)
    sleep(1)


def listar_usuarios():

    print("Pesquisando....")
    sleep(2)
    print("pronto!")
    sleep(1)
    ModelUser.listar_usuario_db()
    sleep(1)


def deletar_usuario():
    pass

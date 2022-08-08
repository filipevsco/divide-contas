from time import sleep

import model.UsuarioModel as ModelUser

def cadastrar_usuario():
    print("=======================")
    print("=== NOVO USUÁRIO ======")
    nome = input("Nome: ")
    salario_medio = float(input("Salário Médio: "))

    ModelUser.cadastrar_usuario_db(nome, salario_medio)
    print("Criando....")
    sleep(1)
    print("Usuário criado com sucesso")
    sleep(1)


def listar_usuarios():

    print("Carregando lista de usuarios....")
    sleep(1)
    ModelUser.listar_usuario_db()
    sleep(1)


def deletar_usuario():
    listar_usuarios()

    id = int(input("Digite o ID de usuario que deseja deletar: "))
    id_cofirma = int(input("Confirme o ID de usuário que deseja deletar: "))
    if id == id_cofirma:
        ModelUser.deletar_usuario_db(id)
    else:
        print("nome invalido, tente novamente")
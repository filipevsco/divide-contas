from time import sleep

# from model.usuario import Usuario

usuarios = []


def cadastrar_usuario():
    print("================+======")
    print("=== NOVO USUÁRIO ======")
    nome = input("Nome: ")
    salario_medio = float(input("Salário Médio: "))

    usuario = Usuario("nome", "salario_medio")
    usuarios.append(usuario)
    print("Criando....")
    sleep(1)
    print("Usuário criado com sucesso")
    print(usuario)
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

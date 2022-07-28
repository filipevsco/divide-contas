from time import sleep

# from model.usuario import Usuario

def cadastrar_usuario():
    print("================+======")
    print("=== NOVO USUÁRIO ======")
    nome = input("Nome: ")
    salario_medio = float(input("Salário Médio: "))

    usuario = Usuario("nome", "salario_medio")
    print("Criando....")
    sleep(1)
    print("Usuário criado com sucesso")
    print(usuario)
    sleep(1)
    menu()

def listar_usuarios():
    pass

def deletar_usuario():
    pass

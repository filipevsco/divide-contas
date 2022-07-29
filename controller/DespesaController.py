from time import sleep

# from model.despesa import Despesa
# from model.usuario import Usuario

def cadastrar_despesa():
    print("=== CADASTRAR DESPESA ===")
    print("-------------------------")
    user = input("Digite o nome de usuario: ")
    for usuario in Usuario:
        if usuario.name == user:
            pagante = usuario
        else:
            print("Usuario invalido. tente novamente")
            sleep(2)
            cadastrar_despesa()
    nome = input("Nome Despesa: ")
    categoria = input("Categoria: ")
    valor = float(input("valor: "))
    coop = int(input("compartilhado? (S/N"))

def listar_despesas():
    pass

def deletar_despesa():
    pass

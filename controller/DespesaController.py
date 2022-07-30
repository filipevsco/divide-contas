from time import sleep

# from model.despesa import Despesa

def cadastrar_despesa():
    print("=== CADASTRAR DESPESA ===")
    print("-------------------------")
    print("-------------------------")
    pagante = int(input("Digite o nome de usuario: "))
    if pagante == usuario.name:
        pagante = usuario
    nome = input("Nome Despesa: ")
    categoria = input("Categoria: ")
    valor = float(input("valor: "))
    coop = int(input("compartilhado? (S/N"))
    
    despesa = Despesa(pagante, nome, categoria, valor, coop)
    print("Despesa cadastrada com sucesso!")
    sleep(1)
    print(despesa)

def listar_despesas():
    pass

def deletar_despesa():
    pass

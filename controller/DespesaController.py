from time import sleep

# from model.despesa import Despesa

despesas = []

def cadastrar_despesa():
    print("=== CADASTRAR DESPESA ===")
    print("-------------------------")
    pagante = input("Digite o nome de usuario: ")
    if pagante == usuario.name:
        pagante = usuario
    nome = input("Nome Despesa: ")
    categoria = input("Categoria: ")
    valor = float(input("valor: "))
    coop = int(input("compartilhado? (S/N"))
    
    despesa = Despesa(pagante, nome, categoria, valor, coop)
    despesas.append(despesa)
    print("Despesa cadastrada com sucesso!")
    sleep(1)
    print(despesa)
    sleep(2)
    menu()

def listar_despesas():
<<<<<<< HEAD
    print("=== LISTAGEM DE DESPESAS ===")
    print("----------------------------")
    for despesa in despesas:
        print(despesa)
    print("----------------------------")
    print("Fim da Lista")
    sleep(2)
    menu()

def deletar_despesa():
    pass

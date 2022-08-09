from time import sleep


def cadastrar_despesa():
    print("=== CADASTRAR DESPESA ===")
    pagante = input("Digite o nome de usuario: ")
    descricao = input("Descrição despesa: ")
    categoria = input("Categoria: ")
    valor = float(input("valor: "))
    coop = int(input("compartilhado?(S/N): "))
    
    db.cadastrar_despesa(pagante, descricao, categoria, valor, coop)
    print("Despesa cadastrada com sucesso!")
    sleep(1)

def listar_despesas():

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

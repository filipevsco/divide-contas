from time import sleep


def cadastrar_despesa():
    print("=== CADASTRAR DESPESA ===")
    id_usuario = input("Digite o nome de usuario: ")
    descricao = input("Descrição despesa: ")
    categoria = input("Categoria: ")
    valor = float(input("valor: "))
    coop = int(input("compartilhado?(S/N): "))
    
    db.cadastrar_despesa(id_usuario, descricao, categoria, valor, coop)

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

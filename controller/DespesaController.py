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
    listar_despesas()

    id = int(input("Digite o ID da despesa que deseja deletar: "))
    id_cofirma = int(input("Confirme o ID da despesa que deseja deletar: "))

    if id == id_cofirma:
        db.despesa.deletar_despesa(id)
    else:
        print("nome invalido, tente novamente")
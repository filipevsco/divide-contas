from time import sleep
import view.principal_menu as menu
import db.despesa


def cadastrar_despesa():
    print("=== CADASTRAR DESPESA ===")
    id_usuario = input("Digite o ID de usuário: ")
    descricao = input("Descrição despesa: ")
    categoria = input("Categoria: ")
    mes = input("mes(XX): ")
    valor = float(input("valor: "))
    coop = input("compartilhado?(S/N): ")
    if coop == "S" or "s":
        coop = 1
    elif coop == "N" or "n":
        coop = 0
    
    db.despesa.cadastrar_despesa(id_usuario, descricao, categoria, mes, valor, coop)

def listar_despesas():

    print("Carregando lista de despesas....")
    sleep(1)
    db.despesa.listar_despesas()
    sleep(1)
    print("Tecle ENTER para voltar ao menu")
    input()
    menu.menu()

def deletar_despesa():
    listar_despesas()

    id = int(input("Digite o ID da despesa que deseja deletar: "))
    id_cofirma = int(input("Confirme o ID da despesa que deseja deletar: "))

    if id == id_cofirma:
        db.despesa.deletar_despesa(id)
    else:
        print("nome invalido, tente novamente")
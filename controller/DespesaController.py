from time import sleep
import view.principal_menu as menu
import db.despesa


def cadastrar_despesa():
    print("=========== NOVA DESPESA ============")
    id_usuario = input("ID USUÁRIO: ")
    descricao = input("DESPESA: ")
    categoria = input("CATEGORIA: ")
    mes = input("MÊS(XX): ")
    valor = float(input("VALOR: "))
    coop = input("COMPARTILHADO?(S/N): ").upper()
    if coop == "S":
        coop = 1
    elif coop == "N":
        coop = 0
    
    db.despesa.cadastrar_despesa(id_usuario, descricao, categoria, mes, valor, coop)
    menu.menu()

def listar_despesas():

    print("========== LISTA DESPESA ============")
    sleep(1)
    db.despesa.listar_despesas()
    sleep(1)
    print("ENTER PARA CONTINUAR")
    input()
    menu.menu()

def deletar_despesa():

    id = int(input("ID da despesa que deseja deletar: "))
    id_cofirma = int(input("Confirme o ID da despesa que deseja deletar: "))

    if id == id_cofirma:
        db.despesa.deletar_despesa(id)
    else:
        print("Nome invalido, tente novamente")
    input("ENTER PARA CONTINUAR")
    menu.menu()
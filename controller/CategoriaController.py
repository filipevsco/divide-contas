from time import sleep
import db.categoria
import view.principal_menu as menu

def cadastrar_categoria():
    print("========= NOVA CATEGORIA ============")
    categoria = input("DIGITE A NOVA CATEGORIA: : ").upper()

    db.categoria.cadastrar_categoria(categoria)
    sleep(2)
    menu.menu()


def deletar_categoria():
    print("=====    DELETAR CATEGORIA     ====")
    categoria = input("DIGITE O NOME DA CATEGORIA: ").upper()

    db.categoria.deletar_categoria(categoria)
    sleep(1)
    menu.menu()
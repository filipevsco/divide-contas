from time import sleep
import db.categoria
import view.principal_menu as menu

def cadastrar_despesa():
    print("========= NOVA CATEGORIA ============")
    categoria = input("DIGITE A NOVA CATEGORIA: : ")

    db.categoria.cadastrar_categoria(categoria)
    sleep(2)
    menu.menu()

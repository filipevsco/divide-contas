from time import sleep
import db.categoria
import view.principal_menu as menu

def cadastrar_despesa():
    print("Cadastrar nova categoria")
    print("------------------------")
    categoria = input("Digite o nome da categoria: ")

    db.categoria.cadastrar_categoria(categoria)
    sleep(2)
    menu.menu()

from time import sleep
import db.categoria


def cadastrar_despesa():
    print("Cadastrar nova categoria")
    print("------------------------")
    categoria = input("Digite o nome da categoria: ")

    db.categoria.cadastrar_categoria(categoria)

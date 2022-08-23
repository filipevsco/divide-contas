from db import mysql

def cadastrar_categoria(categoria):
    '''
    cadastrar nova categoria
    '''
    conexao = mysql.conectar()
    cursor = conexao.cursor()

    cursor.execute(f"INSERT INTO categoria (nome) VALUES ('{categoria}');")
    conexao.commit()

    if cursor.rowcount == 1:
        print("Cadastro realizado com sucesso")
    else:
        print("Erro ao efetuar cadastro")

    mysql.desconectar(conexao)
from db import mysql


def listar_despesas():
    '''
    lista todas as despesas cadastradas
    '''
    conexao = mysql.conectar()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT * FROM despesas")
    despesas = cursor.ferchall()
    for despesa in despesas:
        print(f"ID: {despesa[0]}")


def cadastrar_despesa():
    pass


def deletar_despesa(id):
    pass
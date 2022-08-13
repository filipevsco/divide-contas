from db import mysql


def listar_despesas():
    '''
    lista todas as despesas cadastradas
    '''
    conexao = mysql.conectar()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT * FROM despesas")
    despesas = cursor.ferchall()
    if despesas:
        print("== LISTA DE DESPESAS ==")
        for despesa in despesas:
            print(f"ID: {despesa[0]} ")
    else:
        print("Não existem despesas cadastradas")
    
    mysql.desconectar(conexao)


def cadastrar_despesa(id_usuario, descricao, categoria, valor, coop):
    '''
    cadastrar nova despesa 
    '''
    conexao. mysql.conectar()
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO despesa")
    
    # codigo inclusao 
    
    mysql.desconectar(conexao)


def deletar_despesa(id):
    pass
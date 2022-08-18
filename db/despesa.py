from db import mysql


def listar_despesas():
    '''
    lista todas as despesas cadastradas
    '''
    conexao = mysql.conectar()
    cursor = conexao.cursor()
    
    cursor.execute(f"SELECT * FROM despesa")
    despesas = cursor.fetchall()
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
    """
    deletar usuario
    """
    conexao = mysql.conectar()
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM despesa WHERE id={id}")
    conexao.commit()

    if cursor.rowcount == 1:
        print("Usuario deletado com sucesso")
    else:
        print("Erro ao tentar deletar usuario")

    mysql.desconectar(conexao)
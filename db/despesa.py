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
            print(f"ID: {despesa[0]} - {despesa[2]} - {despesa[5]}")
    else:
        print("Não existem despesas cadastradas")
    
    mysql.desconectar(conexao)


def cadastrar_despesa(id_usuario, descricao, categoria, mes, valor, coop):
    '''
    cadastrar nova despesa 
    '''
    conexao = mysql.conectar()
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO despesa (id_usuario, descricao, categoria, mes, valor, coop) VALUES ('{id_usuario}', '{descricao}', '{categoria}', '{mes}', '{valor}', '{coop}');")
    conexao.commit()

    if cursor.rowcount == 1:
        print(f"Despesa {descricao} cadastrada com sucesso")
    else:
        print("erro ao efetuar cadastro")

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
        print("Despesa deletada com sucesso")
    else:
        print("Erro ao tentar deletar despesa")

    mysql.desconectar(conexao)
from db import mysql


def total_despesas_mes(mes):
    conexao = mysql.conectar()
    cursor = conexao.cursor()

    cursor.execute(f"SELECT * FROM despesa WHERE mes={mes};")
    despesas_mes = cursor.fetchall()
    mysql.desconectar(conexao)
    return despesas_mes


def despesas_por_usuario(id_usuario, mes):
    conexao = mysql.conectar()
    cursor = conexao.cursor()

    cursor.execute(f"SELECT * FROM despesa WHERE id_usuario={id_usuario} AND mes={mes}")
    despesas_usuario = cursor.fetchall()
    mysql.desconectar()
    return despesas_usuario



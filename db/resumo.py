from db import mysql


def total_despesas_mes(mes):
    conexao = mysql.conectar()
    cursor = conexao.cursor()

    cursor.execute(f"SELECT * FROM despesa WHERE mes={mes};")
    despesas_mes = cursor.fetchall()
    mysql.desconectar(conexao)
    return despesas_mes


def despesas_por_usuario(id_usuario, mes):
    pass


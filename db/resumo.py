from db import mysql


def total_despesas_mes(mes):
    conexao = mysql.conectar()
    cursor = conexao.cursor()

    cursor.execute(f"SELECT * FROM despesa WHERE mes={mes};")
    despesas_mes = cursor.fetchall()
    mysql.desconectar(conexao)
    return despesas_mes


def total_despesa_coop(mes):
    conexao = mysql.conectar()
    cursor = conexao.cursor()

    total_coop = 0
    cursor.execute(f"SELECT valor FROM despesa WHERE coop=1 AND mes={mes}")
    valores = cursor.fetchall()
    for valor in valores:
        total_coop += valor[0]
    return total_coop


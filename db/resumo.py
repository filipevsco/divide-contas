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
    mysql.desconectar(conexao)
    return total_coop

def proporcional_por_usuario():
    conexao = mysql.conectar()
    cursor = conexao.cursor()

    lista = []
    cursor.execute(f"SELECT SUM(salario_medio) FROM usuario")
    soma_salario = cursor.fetchall()[0][0]
    cursor.execute(f"SELECT nome, salario_medio FROM usuario")
    salario_medio = cursor.fetchall()
    for salario in salario_medio:
        lista.append([salario[0],salario[1]/soma_salario])
    return lista
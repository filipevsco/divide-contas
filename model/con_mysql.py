import MySQLdb

def conectar():
    try:
        conn = MySQLdb.connect(
            db='divide_contas',
            host='localhost',
            user='root',
            passwd='root'
        )
        return conn
    except MySQLdb.error as e:
        print("erro ao conectar ao banco de dados.")
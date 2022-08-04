import MySQLdb

def conectar():
    try:
        conn = MySQLdb.connect(
            db='divide_contas',
            host='localhost',
            user='admin',
            passwd='admin'
        )
        return conn
    except MySQLdb.Error as e:
        print("erro ao conectar ao banco de dados.")
    

import MySQLdb


def conectar():
    '''
    conectar com o banco de dados
    '''
    try:
        conn = MySQLdb.connect(
            db='divide_contas',
            host='localhost',
            user='admin',
            passwd='admin'
        )
        return conn
    except MySQLdb.Error as e:
        print(f"erro ao conectar ao banco de dados: {e}")
    
def desconectar():
    """
    desconectar do servidor Mysql
    """
    if conn:
        conn.close()
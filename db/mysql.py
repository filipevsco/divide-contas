import MySQLdb

def conectar():
    '''
    conectar ao banco de dados / connect to database
    '''
    try:
        conexao = MySQLdb.connect(
            db='divide_contas',
            host='localhost',
            user='admin',
            passwd='admin'
            )
        return conexao
    except MySQLdb.Error as erro:
        print(f'Erro ao conectar no banco de dados: {erro}')


def desconectar(conexao):
    '''
    desconectar do banco de dados / desconnect to database
    '''
    if conexao:
        conexao.close()
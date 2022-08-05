import MySQLdb

def conexao():
    '''
    conectar ao banco de dados
    '''
    try:
        conectar = MySQLdb.connect(
            db='divide_contas',
            host='localhost',
            user='admin',
            passwd='admin'
            )
        return conectar
    except MySQLdb.Error as erro:
        print(f'Erro ao conectar no banco de dados: {erro}')


def desconectar():
    '''
    deeconectar do banco de dados
    '''
    if conectar:
        conectar.close()
        

def cadaatrar_usuario_db(nome, salario_medio):
     conectar = conexao()
    
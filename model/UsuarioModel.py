import MySQLdb

def conectar():
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

def usuario_db(nome, salario_medio):
     
    
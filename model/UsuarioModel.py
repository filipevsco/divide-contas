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


def desconectar(conexao):
    '''
    deeconectar do banco de dados
    '''
    if conexao:
        conexao.close()
        

def cadaatrar_usuario_db(nome, salario_medio):

    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute(f"INSERT INTO usuarios (nome, salario_medio)) VALUE ('{nome}', {salario_medio})
    
def listar_usuario_db():
    
    conectar = conexao()
    cursor = conectar.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.ferchall()
    
    if usuarios:
        for usuario in usuarios:
            print(f'ID: {usuario[0]}')
            print(f'nome: {usuario[1]')
            print("----------------")
    else:
        print("lista vazia")
    
    desconectar(conexao)
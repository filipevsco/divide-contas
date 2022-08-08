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
        

def cadastrar_usuario_db(nome, salario_medio):
    '''
    cadastrar novo usuario / add new user
    '''
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO usuario (nome, salario_medio) VALUES ('{nome}', {salario_medio})")
    conexao.commit()
    
    if cursor.rowcount == 1:
        print(f"Usuario {nome} cadastrado com sucesso")
    else:
        print("erro ao efetuar cadastro")
    desconectar(conexao)
    
def listar_usuario_db():
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuario")
    usuario = cursor.fetchall()
    
    if usuario:
        for user in usuario:
            print('----LISTANDO USUÁRIOS----')
            print(f'ID: {user[0]}')
            print(f'Nome: {user[1]}')
            print(f'Salário: {user[2]}')
            print('-------------------------')
    else:
        print("lista vazia")
    
    desconectar(conexao)

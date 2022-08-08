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
    cursor.execute(f"INSERT INTO usuarios (nome, salario_medio)) VALUE ('{nome}', {salario_medio}")
    conexao.commit()
    
    if cursor.rowcount == 1:
        print(f"Usuario {nome} cadastrado com sucesso")
    else:
        print("erro ao efetuar cadastro")
    desconectar(conexao)
    
def listar_usuario_db():
    
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.ferchall()
    
    if usuarios:
        for usuario in usuarios:
            print('----LISTANDO USUÁRIOS----')
            print(f'ID: {usuario[0]}')
            print(f'Nome: {usuario[1]}')
            print(f'Salário: {usuario[2]}')
            print('-------------------------')
    else:
        print("lista vazia")
    
    desconectar(conexao)

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
        print('----LISTANDO USUÁRIOS----')
        for user in usuario:
            print(f'ID: {user[0]} - {user[1]} - {user[2]}')
            print('-------------------------')
    else:
        print("lista vazia")

    desconectar(conexao)

def deletar_usuario_db(id):

    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM usuario WHERE id={id}")
    conexao.commit()

    if cursor.rowcount == 1:
        print("Usuario deletado com sucesso")
    else:
        print("Erro ao tentar deletar usuario")

    desconectar(conexao)
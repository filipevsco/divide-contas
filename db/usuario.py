from db import mysql

def cadastrar_usuario(nome, salario_medio):
    '''
    cadastrar novo usuario / add new user
    '''
    conexao = mysql.conectar()
    cursor = conexao.cursor()
    cursor.execute(f"INSERT INTO usuario (nome, salario_medio) VALUES ('{nome}', {salario_medio})")
    conexao.commit()
    
    if cursor.rowcount == 1:
        print(f"Usuario {nome} cadastrado com sucesso")
    else:
        print("erro ao efetuar cadastro")
    mysql.desconectar(conexao)
    
def listar_usuario():
    
    conexao = mysql.conectar()
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

    mysql.desconectar(conexao)

def deletar_usuario(id):

    conexao = mysql.conectar()
    cursor = conexao.cursor()
    cursor.execute(f"DELETE FROM usuario WHERE id={id}")
    conexao.commit()

    if cursor.rowcount == 1:
        print("Usuario deletado com sucesso")
    else:
        print("Erro ao tentar deletar usuario")

    mysql.desconectar(conexao)
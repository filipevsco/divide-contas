from time import sleep

# from model.despesa import Despesa

def cadastrar_despesa():
    print("=== CADASTRAR DESPESA ===")
    print("-------------------------")
    print
    ##### PENDENTE LISTAR USUÁRIOS 
  #  for usuario in usuarios:
  #     print(f'{usuario.id} - {usuario.nome}')
    print("-------------------------")
    codigo = int(input("Digite o código: "))
    
    for usuario in usuarios:
        if usuario.id == codigo:
            usuario = usuario
    nome = input("Nome Despesa: ")
    categoria = input("Categoria: ")
    valor = float(input("valor: "))
    

def listar_despesas():
    pass

def deletar_despesa():
    pass

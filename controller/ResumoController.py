from time import sleep

import view.principal_menu as menu
from db.resumo import total_despesas_mes, total_despesa_coop, proporcional_por_usuario, despesa_nao_coop


def resumo_mes_atual():
    pass


def resumo_outros_meses():
    '''
    recebe o mes e devolve o valor proporcional por usuario
    '''
    mes = int(input("DIGITE O MÊS(XX): "))
    total_coop = total_despesa_coop(mes)
    lista_porporcional = proporcional_por_usuario()
    total_nao_coop = despesa_nao_coop(0)
    print(f"TOTAL COMPARTILHADO: \tR$ {total_coop}")
    print(f"TOTAL NÃO-COMPARTILHADO: \tR$ {total_nao_coop}")
    for usuario in lista_porporcional:
        nome = usuario[0]
        proporcao = usuario[1]
        id = usuario[2]
        nao_coop = despesa_nao_coop(id)
        if not nao_coop:
            print("{}: \tR$ {:.2f}".format(nome, proporcao*total_coop))
        else:
            print("{}: \tR$ {:.2f}".format(nome, proporcao*total_coop + nao_coop))
    # falta calcular a diferenca para pagar



def resumo_total_despesas():
    mes = int(input("MÊS PARA CONSULTA(XX): "))
    despesas = total_despesas_mes(mes)
    if despesas:
        total = 0
        print("========= TOTAL DESPESAS ============")
        for despesa in despesas:
            print(f"{despesa[2]} - {despesa[5]}")
            total += despesa[5]
        print("_____________________")
        print(f"Valor total: {total}")
    else:
        print("Não foram encontrada despesas")
    input("ENTER PARA RETORNAR")
    menu.menu()


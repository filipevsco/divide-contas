from time import sleep

import view.principal_menu as menu
from db.resumo import total_despesas_mes, total_despesa_coop, proporcional_por_usuario


def resumo_mes_atual():
    pass


def resumo_outros_meses():
    '''
    recebe o mes e devolve o valor proporcional por usuario

    ***************falta somar o nao coop
    '''
    mes = int(input("DIGITE O MÊS(XX): "))
    total_coop = total_despesa_coop(mes)
    # com o total coop divide proporcional
    lista_porporcional = proporcional_por_usuario()
    print(f"TOTAL COMPARTILHADO: R${total_coop}")
    for usuario in lista_porporcional:
        print(f"{usuario[0]}: {usuario[1]*total_coop}")

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


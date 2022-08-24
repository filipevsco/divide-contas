from time import sleep

import view.principal_menu as menu
from db.resumo import total_despesas_mes, total_despesa_coop


def resumo_mes_atual():
    pass


def resumo_outros_meses():
    '''
    somar todos coop do mes e
    dividir
    proporcional por usuario
    somar o nao-coop de outro usuario
    '''
    mes = int(input("DIGITE O MÊS(XX): "))
    total_coop = total_despesa_coop(mes)
    print(f"TOTAL COMPARTILHADO: R${total_coop}")


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


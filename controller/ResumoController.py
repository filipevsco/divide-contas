from time import sleep

import view.principal_menu as menu
from db.resumo import total_despesas_mes, despesas_por_usuario


def resumo_mes_atual():
    pass


def resumo_outros_meses():

    mes = int(input("DIGITE O MÊS(XX): "))




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


from time import sleep

import view.principal_menu as menu
from db.resumo import total_despesas_mes, despesas_por_usuario


def resumo_mes_atual():
    pass


def resumo_outros_meses():
    pass


def resumo_total_despesas():
    mes = int(input("Digite o mes para consulta(XX): "))
    despesas = total_despesas_mes(mes)
    if despesas:
        print(f"{despesas[0]}")
    else:
        print("Não foram encontrado despesas")

from time import sleep
import view.principal_menu as principal_menu
from controller.ResumoController import  resumo_total_despesas, resumo_outros_meses


def menu_resumo():
    print("=====================================")
    print("============= RESUMOS ===============")

    print("[ 1 ] BALANÇO MÊS ATUAL")
    print("[ 2 ] BALANÇO OUTROS MESES")
    print("[ 3 ] TOTAL DESPESAS DO MÊS")
    print("[ 0 ] MENU ANTERIOR")

    opcao = int(input("OPçÃO: "))

    if opcao == 1:
        resumo_mes_atual()
    elif opcao == 2:
        resumo_outros_meses()
    elif opcao == 3:
        resumo_total_despesas()
    elif opcao == 0:
        principal_menu.menu()
    else:
        print("opcao inválida. Tente novamente")
        sleep(1)
        menu_resumo()

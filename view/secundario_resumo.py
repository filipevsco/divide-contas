from time import sleep
import view.principal_menu as principal_menu
from controller.ResumoController import resumo_mes_atual, resumo_outros_meses(), resumo_total_despesas()


def menu_resumo():
    print("======= EMITIR RESUMOS ======")
    print("\n")
    print("[1] Balanço mês atual")
    print("[2] Balanço outros meses")
    print("[3] Total despesas por mês")
    print("[0] Retornar ao menu anterior")

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

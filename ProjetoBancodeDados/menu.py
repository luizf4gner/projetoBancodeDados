import os
from inserirUsuario import inserirUsuario
from excluirUsuario import excluirUsuario
from inserirFilmesESeries import inserirFilmeSerie
from excluirFilmeESerie import excluirFilmeSerie
from inserirAssinatura import inserirAssinatura
from excluirAssinaturas import excluirAssinatura
from listarUsuario import listarUsuarios
from listarAssinatura import listarAssinaturas
from listarFilmesESeries import listarFilmesESeries
from inserirHistorico import inserirHistorico
from listarHistorico import listarHistorico
from excluirHistorico import excluirHistorico
from inserirRecomendacao import inserirRecomendacao
from listarRecomendacao import listarRecomendacoes
from excluirRecomendacoes import excluirRecomendacao

def menu():
    while True:
        os.system("cls")
        print("=== cineflix - menu principal ===")
        print("1. cadastrar usuario")
        print("2. listar usuarios")
        print("3. excluir usuario")
        print("4. cadastrar filme/serie")
        print("5. listar filmes/series")
        print("6. excluir filme/serie")
        print("7. cadastrar assinatura")
        print("8. listar assinatura")
        print("9. excluir assinatura")
        print("10. registrar historico de vizualizacao")
        print("11. listar historico de vizualizacao")
        print("12. excluir historico de vizualizacao")
        print("13. adicionar recomendacao")
        print("14. listar recomendacoes")
        print("15. excluir recomendacao")
        print("0. sair")

        opcao = input("\nEscolha uma opcao:")

        if opcao == "1":
            inserirUsuario()
        elif opcao == "2":
            listarUsuarios()
        elif opcao == "3":
            excluirUsuario()
        elif opcao == "4":
            inserirFilmeSerie()
        elif opcao == "5":
            listarFilmesESeries()
        elif opcao == "6":
            excluirFilmeSerie()
        elif opcao == "7":
            inserirAssinatura()
        elif opcao == "8":
            listarAssinaturas()
        elif opcao == "9":
            excluirAssinatura()
        elif opcao == "10":
            inserirHistorico()
        elif opcao == "11":
            listarHistorico()
        elif opcao == "12":
            excluirHistorico()
        elif opcao == "13":
            inserirRecomendacao()
        elif opcao == "14":
            listarRecomendacoes()
        elif opcao == "15":
            excluirRecomendacao()
        elif opcao == "0":
            print("saindo do sistema...")
            break
        else:
            print("opção invalida. tente novamente.")

        input("\npressione enter para voltar ao menu....")

if __name__ == "__main__":
    menu()
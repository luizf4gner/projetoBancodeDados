import os
from login import login  
from inserirUsuario import inserirUsuario
from excluirUsuario import excluirUsuario
from listarUsuario import listarUsuarios
from inserirFilmesESeries import inserirFilmeSerie
from excluirFilmeESerie import excluirFilmeSerie
from inserirAssinatura import inserirAssinatura
from excluirAssinaturas import excluirAssinatura
from listarAssinatura import listarAssinatura
from listarFilmesESeries import listarFilmesESeries
from inserirHistorico import inserirHistorico
from listarHistorico import listarHistorico
from excluirHistorico import excluirHistorico
from inserirRecomendacao import inserirRecomendacao
from listarRecomendacao import listarRecomendacoes
from excluirRecomendacoes import excluirRecomendacao

def menu(id_usuario, tipo_usuario):
    while True:
        os.system("cls")  
        print(f"===  Cineflix - Menu ({'Admin' if tipo_usuario == 'admin' else 'Usuário'}) ===")

        if tipo_usuario == "admin":
            print("1. Cadastrar usuário")
            print("2. Listar usuários")
            print("3. Excluir usuário")
            print("4. Cadastrar filme/série")
            print("5. Excluir filme/série")
            print("6. Listar filmes/séries")
            print("7. Cadastrar assinatura")
            print("8. Listar todas as assinaturas")  
            print("9. Excluir qualquer assinatura")  
            print("10. Registrar histórico de visualização")
            print("11. Listar todo o histórico")  
            print("12. Excluir qualquer histórico")  
            print("13. Adicionar recomendação")
            print("14. Listar todas as recomendações")
            print("15. Excluir qualquer recomendação")

        else:
            print("1. Listar filmes/séries")
            print("2. Cadastrar assinatura")
            print("3. Listar minha assinatura")  
            print("4. Excluir minha assinatura")  
            print("5. Registrar histórico de visualização")
            print("6. Listar meu histórico de visualização")  
            print("7. Excluir meu histórico de visualização")  
            print("8. Adicionar recomendação")
            print("9. Listar minhas recomendações")
            print("10. Excluir recomendação")

        print("0. Logout")

        opcao = input("\nEscolha uma opção: ")

        if tipo_usuario == "admin":
            if opcao == "1":
                inserirUsuario()
            elif opcao == "2":
                listarUsuarios()
            elif opcao == "3":
                excluirUsuario()
            elif opcao == "4":
                inserirFilmeSerie()
            elif opcao == "5":
                excluirFilmeSerie()
            elif opcao == "6":
                listarFilmesESeries()
            elif opcao == "7":
                inserirAssinatura()
            elif opcao == "8":
                listarAssinatura()
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
                print("Saindo do menu e voltando para o login...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        else:
            if opcao == "1":
                listarFilmesESeries()
            elif opcao == "2":
                inserirAssinatura()
            elif opcao == "3":
                listarAssinatura(id_usuario)  
            elif opcao == "4":
                excluirAssinatura(id_usuario)  
            elif opcao == "5":
                inserirHistorico(id_usuario)  
            elif opcao == "6":
                listarHistorico(id_usuario)  
            elif opcao == "7":
                excluirHistorico(id_usuario)  
            elif opcao == "8":
                inserirRecomendacao(id_usuario)  
            elif opcao == "9":
                listarRecomendacoes(id_usuario)  
            elif opcao == "10":
                excluirRecomendacao(id_usuario)  
            elif opcao == "0":
                print("Saindo do menu e voltando para o login...")
                break
            else:
                print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para voltar ao menu...")

while True:
    id_usuario, tipo_usuario = login()
    if id_usuario:
        menu(id_usuario, tipo_usuario)  
    else:
        print("Encerrando o sistema...")
        break
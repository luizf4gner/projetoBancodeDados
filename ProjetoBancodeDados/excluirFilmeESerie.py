import mysql.connector
import os

def excluirFilmeSerie():
    os.system("cls")
    print("---- Excluir Filme/Série ----")
    
    titulo = input("Insira o título do filme ou série que deseja excluir:\n")

    try:
        conexao = mysql.connector.connect(
            user="root",
            password="luiz123",
            host="localhost",
            unix_socket="/data/data/com.termux/files/usr/var/run/mysqld.sock"
        )
        cursor = conexao.cursor()

        cursor.execute(f"select id from series_filmes where titulo = '{titulo}';")
        resultado = cursor.fetchone()

        if resultado is None:
            print("Filme/Série não encontrado. Verifique o título e tente novamente.")
        else:
            confirmacao = input(f"Tem certeza que deseja excluir '{titulo}'? (s/n): ").strip().lower()
            if confirmacao == 's':
                id_filme = resultado[0]

                cursor.execute(f"delete from historico where id_filme = '{id_filme}';")
                cursor.execute(f"delete from recomendacao where id_filme = '{id_filme}';")

                cursor.execute(f"delete from series_filmes where id = '{id_filme}';")
                conexao.commit()
                print(f"Filme/Série '{titulo}' excluído com sucesso!")
            else:
                print("Exclusão cancelada.")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir filme/série: {err}")

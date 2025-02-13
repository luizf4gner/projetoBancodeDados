import mysql.connector
import os

def excluirRecomendacao():
    os.system("cls")
    print("---- Excluir Recomendação ----")

    nome_usuario = input("Insira o nome do usuário:\n")
    titulo = input("Insira o título do filme/série para remover a recomendação:\n")

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()

        cursor.execute(f"select id from usuarios where username = '{nome_usuario}';")
        usuario = cursor.fetchone()

        if usuario is None:
            print("Usuário não encontrado.")
            return

        id_usuario = usuario[0]

        cursor.execute(f"select id from series_filmes where titulo = '{titulo}';")
        filme_serie = cursor.fetchone()

        if filme_serie is None:
            print("Filme ou série não encontrado.")
            return

        id_filme = filme_serie[0]

        confirmacao = input(f"Tem certeza que deseja excluir a recomendação de '{nome_usuario}' para '{titulo}'? (s/n): ").strip().lower()
        if confirmacao != 's':
            print("Exclusão cancelada.")
            return

        comando = f"delete from recomendacao where id_usuario = '{id_usuario}' and id_filme = '{id_filme}';"
        cursor.execute(comando)
        conexao.commit()
        print(f"Recomendação de '{titulo}' feita por '{nome_usuario}' removida com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir recomendação: {err}")

if __name__ == "__main__":
    excluirRecomendacao()
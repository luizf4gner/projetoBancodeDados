import mysql.connector
import os

def listarRecomendacoes():
    os.system("cls")
    print("---- Lista de Recomendações ----")

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()

        comando = """
        select usuarios.username, series_filmes.titulo, recomendacao.nota
        from recomendacao
        inner join usuarios on recomendacao.id_usuario = usuarios.id
        inner join series_filmes on recomendacao.id_filme = series_filmes.id
        order by recomendacao.nota desc;
        """
        cursor.execute(comando)
        recomendacoes = cursor.fetchall()

        if not recomendacoes:
            print("Nenhuma recomendação encontrada.")
        else:
            for recomendacao in recomendacoes:
                print(f"Usuário: {recomendacao[0]}, Filme/Série: {recomendacao[1]}, Nota: {recomendacao[2]}")

    except mysql.connector.Error as err:
        print(f"Erro ao listar recomendações: {err}")
import mysql.connector
import os

def listarFilmesESeries():
    os.system("cls")
    print("---- Lista de Filmes e Séries ----")

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()

        cursor.execute("select titulo, genero, data_lancamento, duracao from series_filmes;")
        filmes_series = cursor.fetchall()

        if not filmes_series:
            print("Nenhum filme ou série encontrado.")
            return

        for titulo, genero, data_lancamento, duracao in filmes_series:
            print(f"Título: {titulo}, Gênero: {genero}, Lançamento: {data_lancamento}, Duração: {duracao}")

    except mysql.connector.Error as err:
        print(f"Erro ao listar filmes e séries: {err}")

    finally:
        cursor.close()
        conexao.close()

    input("\nPressione ENTER para continuar...")

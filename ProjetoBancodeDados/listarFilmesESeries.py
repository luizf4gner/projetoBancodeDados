import mysql.connector
import os

def listarFilmesESeries():
    os.system("cls")
    print("---- Lista de Filmes/Séries ----")

    comando = "select titulo, genero, data_lancamento, duracao from series_filmes;"

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )

        cursor = conexao.cursor()
        cursor.execute(comando)
        series_filmes = cursor.fetchall()

        if not series_filmes:
            print("Nenhum filme ou série encontrado.")
        else:
            for serie_filme in series_filmes:
                print(f"título: {serie_filme[0]}, Gênero: {serie_filme[1]}, Data de lançamento: {serie_filme[2]}, Duração: {serie_filme[3]}")
    
    except mysql.connector.Error as err:
        print(f" Erro ao listar Filmes e séries: {err}")
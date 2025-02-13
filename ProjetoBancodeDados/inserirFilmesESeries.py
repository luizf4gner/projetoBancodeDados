import mysql.connector
import os

def inserirFilmeSerie():
    os.system("cls")
    print("---- Cadastrar Série/Filme ----")
    
    titulo = input("Insira o título:\n")
    genero = input("Insira o gênero:\n")
    data_lancamento = input("Insira a data de lançamento (YYYY-MM-DD):\n")
    duracao = input("Insira a duração em minutos:\n")

    comando = f"insert into series_filmes (titulo, genero, data_lancamento, duracao) values ('{titulo}', '{genero}', '{data_lancamento}', '{duracao}');"

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
        conexao.commit()
        print(f"'{titulo}' cadastrado com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao cadastrar série/filme: {err}")
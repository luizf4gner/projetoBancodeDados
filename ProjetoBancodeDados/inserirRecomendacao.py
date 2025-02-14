import mysql.connector
import os

def inserirRecomendacao():
    os.system("cls")
    print("---- Adicionar Recomendação ----")
    
    nome_usuario = input("Insira o nome do usuário:\n")
    titulo = input("Insira o título do filme ou série:\n")
    
    try:
        nota = float(input("Insira a nota (0.0 a 5.0):\n"))
        if nota < 0 or nota > 5:
            print("Nota inválida! Insira um valor entre 0.0 e 5.0.")
            return
    except ValueError:
        print("Entrada inválida! Insira um número decimal.")
        return

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

        comando = f"insert into recomendacao (id_usuario, id_filme, nota) values ('{id_usuario}', '{id_filme}', '{nota}');"
        cursor.execute(comando)
        conexao.commit()
        print(f"Recomendação registrada para '{nome_usuario}' no filme/série '{titulo}' com nota {nota}!")

    except mysql.connector.Error as err:
        print(f"Erro ao registrar recomendação: {err}")
import mysql.connector
import os

def inserirHistorico():
    os.system("cls")
    print("---- Registrar Histórico de Visualização ----")
    
    nome_usuario = input("Insira o nome do usuário:\n")
    titulo = input("Insira o título do filme ou série assistido:\n")
    progresso = input("Insira o progresso (minutos assistidos):\n")

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

        comando = f"insert into historico (id_usuario, id_filme, progresso) values ('{id_usuario}', '{id_filme}', '{progresso}');"
        cursor.execute(comando)
        conexao.commit()
        print(f"Histórico registrado para '{nome_usuario}' assistindo '{titulo}'!")

    except mysql.connector.Error as err:
        print(f"Erro ao registrar histórico: {err}")
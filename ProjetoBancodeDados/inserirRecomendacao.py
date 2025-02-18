import mysql.connector
import os

def inserirRecomendacao(id_usuario, tipo_usuario):
    os.system("cls")
    print("---- Adicionar Recomendação ----")

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()

        if tipo_usuario == "admin":
            nome_usuario = input("Insira o nome do usuário para a recomendação: ").strip()
            cursor.execute("select id from usuarios where username = %s;", (nome_usuario,))
            usuario = cursor.fetchone()

            if usuario is None:
                print("Usuário não encontrado. Verifique o nome e tente novamente.")
                return

            id_usuario = usuario[0]

        cursor.execute("select id, titulo from series_filmes;")
        filmes_series = cursor.fetchall()

        if not filmes_series:
            print("Nenhum filme ou série disponível para recomendação.")
            return

        print("\nEscolha um filme/série para recomendar:")
        for id_filme, titulo in filmes_series:
            print(f"{id_filme}. {titulo}")

        id_filme = input("\nDigite o ID do filme/série recomendado: ").strip()
        nota = input("Dê uma nota para a recomendação (0 a 5): ").strip()

        cursor.execute(
            "insert into recomendacao (id_usuario, id_filme, nota) values (%s, %s, %s);",
            (id_usuario, id_filme, nota)
        )
        conexao.commit()

        print("Recomendação registrada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao registrar recomendação: {err}")

    finally:
        cursor.close()
        conexao.close()

    input("\nPressione ENTER para continuar...")
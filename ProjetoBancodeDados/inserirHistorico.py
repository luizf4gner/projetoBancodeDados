import mysql.connector
import os

def inserirHistorico(id_usuario, tipo_usuario):
    os.system("cls")
    print("---- Registrar Histórico de Visualização ----")

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
            nome_usuario = input("Insira o nome do usuário para registrar o histórico: ").strip()
            cursor.execute("select id from usuarios where username = %s;", (nome_usuario,))
            usuario = cursor.fetchone()

            if usuario is None:
                print("Usuário não encontrado. Verifique o nome e tente novamente.")
                return

            id_usuario = usuario[0]

        cursor.execute("select id, titulo from series_filmes;")
        filmes_series = cursor.fetchall()

        if not filmes_series:
            print("Nenhum filme ou série disponível.")
            return

        print("\nEscolha um filme/série para registrar no histórico:")
        for id_filme, titulo in filmes_series:
            print(f"{id_filme}. {titulo}")

        id_filme = input("\nDigite o ID do filme/série assistido: ").strip()
        progresso = input("Digite o progresso do vídeo (em minutos): ").strip()

        cursor.execute(
            "insert into historico (id_usuario, id_filme, progresso) values (%s, %s, %s);",
            (id_usuario, id_filme, progresso)
        )
        conexao.commit()

        print("Histórico registrado com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao registrar histórico: {err}")

    finally:
        cursor.close()
        conexao.close()

    input("\nPressione ENTER para continuar...")
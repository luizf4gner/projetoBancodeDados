import mysql.connector
import os

def excluirRecomendacao(id_usuario, tipo_usuario):
    os.system("cls")
    print("---- Excluir Recomendação ----")

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
            nome_usuario = input("Insira o nome do usuário para excluir a recomendação: ").strip()
            cursor.execute("select id from usuarios where username = %s;", (nome_usuario,))
            usuario = cursor.fetchone()

            if usuario is None:
                print("Usuário não encontrado. Verifique o nome e tente novamente.")
                return

            id_usuario = usuario[0]

        cursor.execute("""
            select recomendacao.id, series_filmes.titulo, recomendacao.nota 
            from recomendacao 
            inner join series_filmes on recomendacao.id_filme = series_filmes.id 
            where recomendacao.id_usuario = %s;
        """, (id_usuario,))
        recomendacoes = cursor.fetchall()

        if not recomendacoes:
            print("Nenhuma recomendação encontrada para este usuário.")
            return

        print("\nEscolha uma recomendação para excluir:")
        for id_recomendacao, titulo, nota in recomendacoes:
            print(f"{id_recomendacao}. {titulo} (Nota: {nota})")

        id_recomendacao = input("\nDigite o ID da recomendação a ser excluída: ").strip()

        if input("Tem certeza que deseja excluir essa recomendação? (s/n): ").strip().lower() != "s":
            print("Exclusão cancelada.")
            return

        cursor.execute("delete from recomendacao where id = %s;", (id_recomendacao,))
        conexao.commit()

        print("Recomendação excluída com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir recomendação: {err}")

    finally:
        cursor.close()
        conexao.close()

    input("\nPressione ENTER para continuar...")
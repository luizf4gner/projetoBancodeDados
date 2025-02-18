import mysql.connector
import os

def excluirHistorico(id_usuario, tipo_usuario):
    os.system("cls")
    print("---- Excluir Histórico de Visualização ----")

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
            nome_usuario = input("Insira o nome do usuário para excluir o histórico: ").strip()
            cursor.execute("select id from usuarios where username = %s;", (nome_usuario,))
            usuario = cursor.fetchone()

            if usuario is None:
                print("Usuário não encontrado. Verifique o nome e tente novamente.")
                return

            id_usuario = usuario[0]

        if input("Tem certeza que deseja excluir o histórico? (s/n): ").strip().lower() != "s":
            print("Exclusão cancelada.")
            return

        cursor.execute("delete from historico where id_usuario = %s;", (id_usuario,))
        conexao.commit()

        print("Histórico excluído com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir histórico: {err}")

    finally:
        cursor.close()
        conexao.close()

    input("\nPressione ENTER para continuar...")

import mysql.connector
import os

def excluirAssinatura(id_usuario=None, tipo_usuario="admin"):
    os.system("cls")
    print("---- Excluir Assinatura ----")

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
            nome_usuario = input("Insira o nome do usuário para excluir a assinatura: ").strip()
            cursor.execute("select id from usuarios where username = %s;", (nome_usuario,))
            usuario = cursor.fetchone()

            if usuario is None:
                print("Usuário não encontrado. Verifique o nome e tente novamente.")
                return

            id_usuario_excluir = usuario[0]

        else:
            id_usuario_excluir = id_usuario

        if input(f"Tem certeza que deseja excluir a assinatura? (s/n): ").strip().lower() != "s":
            print("Exclusão cancelada.")
            return

        cursor.execute("delete from assinaturas where id_usuario = %s;", (id_usuario_excluir,))
        conexao.commit()

        print("Assinatura excluída com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir assinatura: {err}")

    finally:
        cursor.close()
        conexao.close()

    input("\nPressione ENTER para continuar...")
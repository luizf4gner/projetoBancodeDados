import mysql.connector
import os

def excluirUsuario(id_usuario, tipo_usuario):
    os.system("cls")
    print("---- Excluir Usuário ----")

    try:
        conexao = mysql.connector.connect(
            user="root",
            password="luiz123",
            host="localhost",
            unix_socket="/data/data/com.termux/files/usr/var/run/mysqld.sock"
        )
        cursor = conexao.cursor()

        if tipo_usuario == "admin":
            nome_usuario = input("Insira o nme do usúario que deseja excluir: ").strip()
            cursor.execute("select id from usuarios where username = %s;", (nome_usuario,))
            usuario = cursor.fetchone()

            if usuario is None:
                print("Usúario não encontrado. Verifique o nome e tente novamente.")
                return
            
            id_usuario_excluir = usuario[0]

            if input(f"Tem certeza que deseja excluir '{nome_usuario}'? (s/n): ").strip().lower() != "s":
                print("Exclusão cancelada.")
                return
            
        else: 
            if input("Tem certeza que deseja deletar sua conta? (s/n): ").strip().lower() != "s":
                print("Exclusão cancelada.")
                return
            
            id_usuario_excluir = id_usuario[0]

        cursor.execute("delete from historico where id_usuario = %s;", (id_usuario_excluir,))
        cursor.execute("delete from recomendacao where id_usuario = %s;", (id_usuario_excluir,))
        cursor.execute("delete from assinaturas where id_usuario = %s;", (id_usuario_excluir,))

        cursor.execute("delete from usuarios where id = %s;", (id_usuario_excluir,))
        conexao.commit()

        print("Conta deletada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir usúario: {err}")

    input("Tecle ENTER para sair...")

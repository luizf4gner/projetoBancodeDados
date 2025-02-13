import mysql.connector
import os

def login():
    os.system("cls")
    print("==== 🎬 Cineflix - Login ====")

    username = input("Usuário: ").strip()
    senha = input("Senha: ").strip()

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()

        comando = "select id from usuarios where username = %s and senha = %s"
        cursor.execute(comando, (username, senha))
        usuario = cursor.fetchone()

        if usuario:
            id_usuario = usuario[0]
            print(f"Login bem-sucedido! Bem-vindo, {username}!")
            return id_usuario
        else:
            print("Usuário ou senha incorretos.")
            return None

    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None
import mysql.connector
import os

def login():
    os.system("cls")
    print("====  Cineflix - Login ====")

    while True:
        username = input("Usuário: ").strip()
        senha = input("Senha: ").strip()

        if not username or not senha:
            print("Nome de usuário e senha não podem estar vazios. Tente novamente.\n")
            continue

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                port="3307",
                database="cineflix"
            )
            cursor = conexao.cursor()

            comando = "select id, tipo from usuarios where username = %s and senha = %s"
            cursor.execute(comando, (username, senha))
            usuario = cursor.fetchone()

            if usuario:
                id_usuario, tipo = usuario
                print(f"Login bem-sucedido! Bem-vindo, {username} ({tipo}).")
                return id_usuario, tipo
            else:
                print("Usuário ou senha incorretos. Tente novamente.\n")

        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None, None
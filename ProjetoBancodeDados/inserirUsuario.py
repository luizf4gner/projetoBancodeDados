import mysql.connector
import os

def inserirUsuario(tipo_usuario_logado="usuario"):
    os.system("cls")
    print("---- Cadastrar Usuário ----")

    while True:
        username = input("Insira o nome de usuário:\n").strip()
        if not username:
            print("O nome de usuário não pode estar vazio!")
            continue
        break

    while True:
        senha = input("Insira a senha de acesso:\n").strip()
        if not senha:
            print("A senha não pode estar vazia!")
            continue
        break

    while True:
        email = input("Insira o seu email:\n").strip()
        if not email:
            print("O email não pode estar vazio!")
            continue
        break

    if tipo_usuario_logado == "admin":
        while True:
            tipo_novo_usuario = input("O novo usuário será 'admin' ou 'usuario'? ").strip().lower()
            if tipo_novo_usuario in ["admin", "usuario"]:
                break
            print("Opção inválida! Digite 'admin' ou 'usuario'.")

    else:
        tipo_novo_usuario = "usuario"

    comando = "insert into usuarios (username, senha, email, tipo) values (%s, %s, %s, %s)"
    valores = (username, senha, email, tipo_novo_usuario)

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()
        cursor.execute(comando, valores)
        conexao.commit()

        print(f"Usuário '{username}' cadastrado com sucesso como {tipo_novo_usuario}!")

    except mysql.connector.Error as err:
        print(f"Erro ao inserir usuário: {err}")
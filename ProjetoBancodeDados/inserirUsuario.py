import mysql.connector
import os

def inserirUsuario():
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

    comando = f"insert into usuarios (username, senha, email) values ('{username}', '{senha}', '{email}')"

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()
        cursor.execute(comando)
        conexao.commit()

        print("Usuário inserido com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao inserir usuário, verifique os dados e tente novamente: {err}")
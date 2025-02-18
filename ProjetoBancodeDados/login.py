import mysql.connector
import os
from inserirUsuario import inserirUsuario

def login():
    while True:
        os.system("cls")
        print("===  Cineflix - Bem vindo! ===")
        print("1. Já tenho uma conta (Fazer login)")
        print("2. Não tenho uma conta (Fazer cadastro)")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            break
        elif opcao == "2":
            inserirUsuario()
        elif opcao == "0":
            print()
            return None, None
        else:
            print("Opção inválida. Tente Novamente.")

    while True:
        os.system("cls")
        print("===  Cineflix - Login ===")

        username = input("Usúario: ").strip()
        senha = input("Senha: ").strip()

        if not username or not senha:
            print("Nome de usúario e senha não podem estar vazios. Tente novamente.\n")
            continue

        try:
            conexao = mysql.connector.connect(
                host ="localhost",
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
                print(f"Login bem sucedido! Bem vindo, {username} ({tipo}).")
                return id_usuario, tipo
            else:
                print("Usúario ou senha incorretos. Tente novamente.\n")

        except mysql.connector.Error as err:
            print(f"Erro ao conectar ao banco de dados: {err}")
            return None, None
        
        input()
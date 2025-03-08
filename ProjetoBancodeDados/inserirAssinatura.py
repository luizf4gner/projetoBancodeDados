import mysql.connector
import os

def inserirAssinatura():
    os.system("cls")
    print("---- Cadastrar Assinatura ----")
    
    nome_usuario = input("Insira o nome do usuário:\n")
    data_inicial = input("Insira a data de início (YYYY-MM-DD):\n")
    data_final = input("Insira a data de fim (YYYY-MM-DD):\n")

    try:
        conexao = mysql.connector.connect(
            user="root",
            password="luiz123",
            host="localhost",
            unix_socket="/data/data/com.termux/files/usr/var/run/mysqld.sock"
        )
        cursor = conexao.cursor()

        cursor.execute("select id from usuarios where username = %s;", (nome_usuario,))
        resultado = cursor.fetchone()

        if resultado is None:
            print("Usuário não encontrado. Verifique o nome e tente novamente.")
        else:
            id_usuario = resultado[0]
            comando = f"insert into assinaturas (id_usuario, data_inicial, data_final) values ('{id_usuario}', '{data_inicial}', '{data_final}');"
            cursor.execute(comando)
            conexao.commit()
            print(f"{nome_usuario} sua assinatura foi realizada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao realizar assinatura: {err}")

    input()

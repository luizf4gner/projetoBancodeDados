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
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()

        cursor.execute(f"select id from usuarios where username = '{nome_usuario}';")
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
import mysql.connector
import os

def listarUsuarios():
    os.system("cls")
    print("---- Lista de Usuários ----")

    comando = "select id, username, email, data_criacao from usuarios;"

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
        usuarios = cursor.fetchall()

        if not usuarios:
            print("Nenhum usuário encontrado.")
        else:
            for usuario in usuarios:
                print(f"ID: {usuario[0]}, Nome: {usuario[1]}, Email: {usuario[2]}, Criado em: {usuario[3]}")
    
    except mysql.connector.Error as err:
        print(f" Erro ao listar usuários: {err}")
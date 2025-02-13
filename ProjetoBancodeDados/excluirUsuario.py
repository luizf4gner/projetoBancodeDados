import mysql.connector
import os

def excluirUsuario():
    os.system("cls")
    print("---- Excluir Usuário ----")
    
    nome_usuario = input("Insira o nome do usuário que deseja excluir:\n")

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
        usuario = cursor.fetchone()

        if usuario is None:
            print("Usuário não encontrado. Verifique o nome e tente novamente.")
            return
        
        id_usuario = usuario[0]

        confirmacao = input(f"Tem certeza que deseja excluir '{nome_usuario}'? (s/n):").strip().lower()
        if confirmacao != 's':
            print("Exclusão cancelada")
            return 
        
        cursor.execute(f"delete from assinaturas where id_usuario = '{id_usuario}';")

        cursor.execute(f"delete from usuarios where id = '{id_usuario}';")
        conexao.commit()

        print(f"Usuário '{nome_usuario}' excluído com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir usuario: {err}")
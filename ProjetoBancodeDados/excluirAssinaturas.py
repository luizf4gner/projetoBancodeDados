import mysql.connector
import os

def excluirAssinatura():
    os.system("cls")
    print("---- Excluir Assinatura ----")
    
    nome_usuario = input("Insira seu nome de usuario:\n")

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
            print("Usuario não encontrada. Verifique o nome e tente novamente.")
            return
        
        id_usuario = usuario[0]

        cursor.execute(f"select id from assinaturas where id_usuario = '{id_usuario}';")
        assinatura = cursor.fetchone()

        if assinatura is None:
            print(f"{nome_usuario} não possui uma assinatura ativa.")
            return
        
        id_assinatura = assinatura[0]

        comfirmacao = input(f"Tem certeza que deseja cancelar a assinatura de {nome_usuario}? (s/n):\n").strip().lower()
        if comfirmacao != 's':
            print("Exclusão cancelada.")
            return

        cursor.execute(f"delete from assinaturas where id = '{id_assinatura}';")
        conexao.commit()
        print(f"Assinatura de {nome_usuario} cancelada com sucesso!")

    except mysql.connector.Error as err:
        print(f"Erro ao excluir assinatura: {err}")
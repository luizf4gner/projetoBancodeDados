import mysql.connector
import os

def listarAssinatura(id_usuario):
    os.system("cls")
    print("---- Sua Assinatura ----")

    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port="3307",
            database="cineflix"
        )
        cursor = conexao.cursor()

        comando = """
        select data_inicial, data_final
        from assinaturas
        where id_usuario = %s;
        """
        cursor.execute(comando, (id_usuario,))
        assinatura = cursor.fetchall()

        if not assinatura:
            print("Você não tem nenhuma assinatura ativa.")
        else:
            for registro in assinatura:
                print(f"Data Inicial: {registro[0]} | Data Final: {registro[1]}")

    except mysql.connector.Error as err:
        print(f"Erro ao listar assinatura: {err}")
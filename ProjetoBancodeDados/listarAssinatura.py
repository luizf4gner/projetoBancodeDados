import mysql.connector
import os

def listarAssinatura(id_usuario):
    os.system("cls")
    print("---- Sua Assinatura ----")

    try:
        conexao = mysql.connector.connect(
            user="root",
            password="luiz123",
            host="localhost",
            unix_socket="/data/data/com.termux/files/usr/var/run/mysqld.sock"
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

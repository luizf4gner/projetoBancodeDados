import mysql.connector
import os

def listarAssinaturas():
    os.system("cls")
    print("---- Listar Assinaturas ----")

    comando = """ 
    select assinaturas.id, usuarios.username, assinaturas.data_inicial, assinaturas.data_final
    from assinaturas
    inner join usuarios on assinaturas.id_usuario = usuarios.id;
    """

    try:
        conexao = mysql.connector.connect(
            host="127.0.0.1",
            port="3307",
            user="root",
            password="",
            database="cineflix"
        )

        cursor = conexao.cursor()
        cursor.execute(comando)
        assinaturas = cursor.fetchall()

        if not assinaturas:
            print("Assinaturas não encontradas.")
        else:
            for assinatura in assinaturas:
                print(f"id: {assinatura[0]}, Usuário: {assinatura[1]}, Início: {assinatura[2]}, Fim: {assinatura[3]}")

    except mysql.connector.Error as err:
        print(f"Ocorreu um erro ao listar as assinaturas: {err}")
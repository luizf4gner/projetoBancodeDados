import mysql.connector
import os

def listarHistorico(id_usuario, tipo_usuario):
    os.system("cls")
    print("---- Seu Histórico de Visualização ----")

    try:
        conexao = mysql.connector.connect(
            user="root",
            password="luiz123",
            host="localhost",
            unix_socket="/data/data/com.termux/files/usr/var/run/mysqld.sock"
        )
        cursor = conexao.cursor()

        comando = """
        select series_filmes.titulo, historico.data_visualizacao, historico.progresso
        from historico
        inner join series_filmes on historico.id_filme = series_filmes.id
        where historico.id_usuario = %s
        order by historico.data_visualizacao desc;
        """
        cursor.execute(comando, (id_usuario,),(tipo_usuario,))
        historico = cursor.fetchall()

        if not historico:
            print("Nenhum histórico encontrado para você.")
        else:
            for registro in historico:
                print(f"Título: {registro[0]} | Data: {registro[1]} | Progresso: {registro[2]} minutos")

    except mysql.connector.Error as err:
        print(f"Erro ao listar histórico: {err}")

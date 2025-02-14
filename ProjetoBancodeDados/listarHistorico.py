import mysql.connector
import os

def listarHistorico(id_usuario):
    os.system("cls")
    print("---- Seu Histórico de Visualização ----")

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
        select series_filmes.titulo, historico.data_visualizacao, historico.progresso
        from historico
        inner join series_filmes on historico.id_filme = series_filmes.id
        where historico.id_usuario = %s
        order by historico.data_visualizacao desc;
        """
        cursor.execute(comando, (id_usuario,))
        historico = cursor.fetchall()

        if not historico:
            print("Nenhum histórico encontrado para você.")
        else:
            for registro in historico:
                print(f"Título: {registro[0]} | Data: {registro[1]} | Progresso: {registro[2]} minutos")

    except mysql.connector.Error as err:
        print(f"Erro ao listar histórico: {err}")
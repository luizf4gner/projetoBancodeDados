import mysql.connector
import os

def listarHistorico():
    os.system("cls")
    print("---- Histórico de Visualização ----")

    

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
        select usuarios.username, series_filmes.titulo, historico.data_visualizacao, historico.progresso
        from historico
        inner join series_filmes on historico.id_filme = series_filmes.id
        inner join usuarios on historico.id_usuario = usuarios.id
        where historico.id_usuario = id_usuario
        order by historico.data_visualizacao desc;
        """
        cursor.execute(comando)
        historico = cursor.fetchall()

        if not historico:
            print("Nenhum histórico encontrado para este usuário.")
        else:
            for registro in historico:
                print(f"Usúario: {registro[0]}: Título: {registro[1]}, Data: {registro[2]}, Progresso: {registro[3]} minutos")

    except mysql.connector.Error as err:
        print(f"Erro ao listar histórico: {err}")
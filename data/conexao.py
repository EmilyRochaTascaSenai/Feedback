import mysql.connector


class  Conexao:
    # Criando a conexão 
    def criar_conexao():
            if True:
                conexao = mysql.connector.connect(host="10.110.134.2",
                                            port=3306,
                                            user="3ds",
                                            password="banana",
                                            database="db_feedback")
                return conexao
        

    #    conexao = mysql.connector.connect(host="localhost",
    #                                     port=3306,
    #                                     user="3ds",
    #                                     password="banana",
    #                                     database="db_feedback")
    #         return conexao
       
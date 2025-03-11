import  datetime
from data.conexao import Conexao

class Mensagem:

    def  cadastro_mensagem(usuario,mensagem):
        data_hora=datetime.datetime.today()


        # Cadastrando as informações no banco de dados

     # Criando a conexão
        conexao = Conexao.criar_conexao()
     #    O cursor será responsavel por manipular o bcd

        cursor =conexao.cursor()
        #  Criando o sql que será executado

        sql="""INSERT INTO tbComentarios
        (Nome,DataPostagem,Comentario)
        VALUES
        (%s, %s, %s)"""  
        valores = (usuario,data_hora,mensagem)

        #    Executando o comenado sql
        cursor.execute(sql,valores)

        # Confirmo a alteração 

        conexao.commit()

        # Fecho a conexão com o banco

        cursor.close()
        conexao.close()



    def recuperar_mensagens():
       
     
        conexao = Conexao.criar_conexao()
        
        cursor=conexao.cursor(dictionary=True)
        # Criano o SQL  será executado

        sql="""SELECT Nome as usuario,
        Comentario as mensagem ,
        DataPostagem as data_hora 
        FROM tbcomentarios"""

        # Executando o comando SQL
        cursor.execute(sql)
        # Recuperando os dados e guardando em uma variavel
        resultado=cursor.fetchall()

        # Fecho a conexão com o banco
        cursor.close()
        conexao.close()
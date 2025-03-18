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

        sql="""INSERT INTO tb_Comentarios
        (nome,data_hora,comentario)
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

        sql="""SELECT cod_comentario,
          nome as usuario,
        comentario as mensagem ,
        data_hora as data_hora,
        curtidas
        FROM tb_comentarios"""

        # Executando o comando SQL
        cursor.execute(sql)
        # Recuperando os dados e guardando em uma variavel
        resultado=cursor.fetchall()

        # Fecho a conexão com o banco
        cursor.close()
        conexao.close()

        return resultado
    
    def delete_mensagem(codigo):
        conexao = Conexao.criar_conexao()
        
        cursor=conexao.cursor()

        # Criano o SQL  será executado

        sql="delete from tb_comentarios where cod_comentario = %s;"

        valores=(int(codigo),)
        # Executando o comando SQL
        cursor.execute(sql, valores)

        # Comitand para gravar as alterações
        conexao.commit()

        # Fechando a conexao

        conexao.close()


    


         

         


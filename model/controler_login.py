from data.conexao import Conexao

class  Login :

    def  cadastrar(login,senha):
        # Cadastrando as informações no banco de dados
        # Criando a conexão
        conexao = Conexao.criar_conexao()
        #    O cursor será responsavel por manipular o bcd

        cursor =conexao.cursor()
        #  Criando o sql que será executado

        #  Criando o sql que será executado

        sql="""INSERT  tb_login
        (login,senha)
        VALUES
        (%s, %s, %s)"""  
        valores = (login,senha)

        #    Executando o comenado sql
        cursor.execute(sql,valores)
        # Confirmo a alteração 

        conexao.commit()

        # Fecho a conexão com o banco

        cursor.close()
        conexao.close()


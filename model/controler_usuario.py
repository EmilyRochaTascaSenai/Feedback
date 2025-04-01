from hashlib import sha256
from data.conexao import Conexao


class  Usuario :

    def  cadastrar(login,senha,nome):
        # Criptografando a senha
        senha=sha256(senha.encode()).hexdigest()
        # Cadastrando as informações no banco de dados
        # Criando a conexão
        conexao = Conexao.criar_conexao()
        #    O cursor será responsavel por manipular o bcd

        cursor =conexao.cursor()
        #  Criando o sql que será executado

        #  Criando o sql que será executado

        sql="""INSERT  tb_usuarios
        (login,senha,nome)
        VALUES
        (%s, %s, %s)"""  
        valores = (login,senha,nome)

        #    Executando o comenado sql
        cursor.execute(sql,valores)
        # Confirmo a alteração 

        conexao.commit()

        # Fecho a conexão com o banco

        cursor.close()
        conexao.close()


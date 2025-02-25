from flask  import Flask,render_template,form,request,redirect
import datetime
import _mysql_connector
app = Flask(__name__)

#CRIANDO A ROTA incial

@app.route("/")
def pagina_incial():
    return  render_template("index.html")



# Criando rota cadastro
@app.route("/post/cadastro",methods=["POST"])
def pagina_cadstro():
    #Peguei as informações vinda do formulario
   usuario = request.form.get("usuario")
   mensagem= request.form.get("mensagem")
   data_hora=datetime.datetime.today()
    # Cadastrando as informações no banco de dados
    # Criando a conexão
   
#    conexao = mysql.connector.connect(hostname="localhost",
#                                         port=3306,
#                                          user="root"
#                                          password="root",
#                                          database=dbFeedback)
#    O cursor será responsavel por manipular o bcd
   
    # cursor =conexao.cursor()
# Criando o sql que será executado
   
#    sql="""INSERT INTO tbComentarios
#    (Nome,DataPostagem,Comentario)
#    VALUES
#    (%s, %s, %s)"""  
   valores = (usuario,data_hora,mensagem)

#    Executando o comenado sql
#    cursos.execute(sql,valores)
   
# Confirmo a alteração 

#    conexao.commit()
   
# Fecho a conexão com o banco
   
    # cursor.close()
#    conexao.close()
   
# Redireciona para o index
   return redirect("/")
app.run(debug=True)
from flask  import Flask,render_template,request,redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem  import Mensagem

app = Flask(__name__)

#CRIANDO A ROTA incial

@app.route("/")
def pagina_incial():
    # Recuperando as mensagens
    mensagens=Mensagem.recuperar_mensagens()

    # Enviar as mensagens para o template
    return  render_template("index.html",mensagens=mensagens)



# Criando rota cadastro
@app.route("/post/cadastro",methods=["POST"])
def pagina_cadstro():
    #Peguei as informações vinda do formulario
    usuario = request.form.get("usuario")
    mensagem= request.form.get("mensagem")

    # Cadastrando a mensagem usando a classe mensagem
    Mensagem.cadastro_mensagem(usuario,mensagem)

    # Redireciona para o index
    return redirect("/")



app.run(debug=True)
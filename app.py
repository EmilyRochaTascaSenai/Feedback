from flask  import Flask,render_template,request,redirect
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem  import Mensagem
from model.controler_usuario import Usuario

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

# Criando rota excluir
@app.route("/delete/mensagem/<codigo>")
def pagina_delete(codigo):
   Mensagem.delete_mensagem(codigo)
   return redirect("/")
# Criando rota curtida
@app.route("/put/mensagem/adicionar/curtidas/<codigo>")
def adicionar_curtida(curtida):
    Mensagem.curtidas_mensagens(curtida)
    return redirect("/")
# Criando a rota cadastro para exibir a pagina
@app.route("/cadstro_usuario")
def pagina_cadastro_usuario():
    return render_template ("usuario.html")
# Criando para cadastar
@app.route("/post/cadstro_usuario",methods=["Post"])
def  post_cadastar_usaurio():
    login=request.form.get("usuario")
    senha=request.form.get("senha")
    nome=request.form.get("nome")
   
   
    Usuario.cadastrar(login,senha,nome)

    return redirect("/login")
    

# Criando a rota de login
@app.route("/login_usuario")
def pagina_login_usuario():
    return render_template("login.html")
app.run(debug=True)
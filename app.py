from flask  import Flask,render_template
app = Flask(__name__)

#CRIANDO A ROTA incial

@app.route("/")
def pagina_incial():
    return  render_template("index.html")

app.run(debug=True)

# Criando rota cadastro
@app.route("/post/cadastro")
def pagina_cadstro():

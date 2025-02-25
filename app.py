from flask  import Flask
app = Flask(__name__)

#CRIANDO A ROTA teste

@app.route("/")
def pagina_teste():
    return "Pagina Principal" 

app.run(debug=True)
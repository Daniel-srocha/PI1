from flask import Flask, render_template

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Configuração e extensões (se necessário)

# Rotas
@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/vacinas_disponiveis")
def vdisponiveis():
    return render_template("vdisponiveis.html")

@app.route("/quem_pode_se_vacinar")
def qpsvacinar():
    return render_template("quem_pode_se_vacinar.html")

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")

@app.route("/locais")
def locais():
    return render_template("locais.html")

if __name__ == "__main__":
    app.run(debug=True)

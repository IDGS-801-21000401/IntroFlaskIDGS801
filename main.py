from flask import Flask,render_template

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos")
def alumnos():
    titulo="UTL"
    nombres = ["Angel Roberto", "Pedro Morales","Johan Doe"]
    return render_template("alumnos.html",titulo=titulo,listaNombres=nombres)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

@app.route("/hola")
def hola():
    return """
            <h1>Saludos mi desde FLASK</h1>
            """

@app.route("/Saludo")
def saludo():
    return """
            <h1>Saludos</h1>
            """

@app.route("/nombre/<string:nom>")
def nombre(nom):
    return """
            <h1>Saludos """ + nom +"""</h1>
            """

@app.route("/numero/<int:n1>")
def numero(n1):
    return """
            <h1>Tu telefono es: {} """.format(n1) +"""</h1>
            """

@app.route("/user/<int:id>/<string:nom>")
def numeroNombre(id,nom):
    return """
            <h1>Tu telefono es: {}, tu nombre es: {} """.format(id,nom)


@app.route("/suma/<float:num1>/<float:num2>")
def suma(num1,num2):
    return """
            <h1>la suma {} + {} = {}""".format(num1,num2, num1+num2)

@app.route("/default")
@app.route("/default/<string:d>")
def default(d="user-not:default"):
    return """
            <h1>el nombre del Usuario es: """ + d + """
            """



if __name__ == "__main__":
    app.run(debug=True)
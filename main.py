from flask import Flask,render_template,request
from forms import UserForm

app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos",methods=["GET","POST"])
def alumnos():
    alumno_clase = UserForm(request.form)
    nombre = ""
    apaterno = ""
    amaterno = ""
    edad = ""
    email = ""
    if request.method == "POST":
        nombre = alumno_clase.nombre.data
        apaterno = alumno_clase.apaterno.data
        amaterno = alumno_clase.amaterno.data
        edad = alumno_clase.edad.data
        email = alumno_clase.email.data
    return render_template("alumnos2.html",form=alumno_clase,nombre=nombre,apaterno=apaterno,amaterno=amaterno,edad=edad,email=email)

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


@app.route("/calcular",methods=["GET","POST"])
def calcular():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicación de {} y {} = {}".format(num1, num2, str(int(num1)* int(num2)))
    else:
        return '''
            <form action="/calcular" method="POST">

                <label>Numero 1: </label>
                <input type="text" name="n1"><br>
                
                <label>Numero 2: </label>
                <input type="text" name="n2"><br>
                <input type="submit">
            </form>
        '''

@app.route("/OperasBas",methods=["GET","POST"])
def operaBas():
    return render_template("OperasBas.html")

@app.route("/resultado",methods=["GET","POST"])
def result():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicación de {} y {} = {}".format(num1, num2, str(int(num1)* int(num2)))
    

if __name__ == "__main__":
    app.run(debug=True)
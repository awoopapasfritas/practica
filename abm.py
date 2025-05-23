from flask import Flask, render_template, request, redirect

app = Flask(__name__)
usuarios = []

@app.route("/")
def index():
    return render_template("index.html", usuarios=usuarios)

@app.route("/agregar", methods=["POST"])
def agregar():
    nombre = request.form["nombre"]
    email = request.form["email"]
    usuarios.append({"nombre": nombre, "email": email})
    return redirect("/")

@app.route("/eliminar/<int:indice>", methods=["POST"])
def eliminar(indice):
    if 0 <= indice < len(usuarios):
        usuarios.pop(indice)
    return redirect("/")

@app.route("/modificar/<int:indice>", methods=["GET", "POST"])
def modificar(indice):
    if request.method == "GET":
        usuario = usuarios[indice]
        return f'''
        <form action="/modificar/{indice}" method="POST">
            Nombre: <input type="text" name="nombre" value="{usuario['nombre']}" required><br>
            Email: <input type="email" name="email" value="{usuario['email']}" required><br>
            <button type="submit">Guardar Cambios</button>
        </form>
        '''
    else:
        usuarios[indice] = {
            "nombre": request.form["nombre"],
            "email": request.form["email"]
        }
        return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)


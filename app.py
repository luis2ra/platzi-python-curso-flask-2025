from flask import Flask, request, jsonify, render_template, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    role = "normal"
    notes = ["Nota 1", "Nota 2", "Nota 3"]
    return render_template("home.html", role=role, notes=notes)

@app.route("/acerca-de")
def about():
    return "Esto es una app de notas"

@app.route("/contacto", methods=['GET', 'POST'])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctamente", 201
    return "Pagina de contacto"


@app.route("/api/info")
def api_info():
    data = {
        "nombre": "Notes App",
        "version": "1.1.1"
    }
    return jsonify(data), 200

@app.route("/confirmacion")
def confirmation():
    return "Prueba"

@app.route("/crear-nota", methods=["GET", "POST"])
def create_note():
    if request.method == "POST":
        note = request.form.get("note", "No encontrada") 
        return redirect(url_for("confirmation", note=note))
    return render_template("note_form.html")

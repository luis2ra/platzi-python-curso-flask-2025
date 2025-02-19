from flask import Flask, request

from config import Config
from models import db
from notes.routes import notes_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
app.register_blueprint(notes_bp)


@app.route("/acerca-de")
def about():
    return "Esto es una app de notas"


@app.route("/contacto", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        return "Formulario enviado correctamente", 201
    return "Pagina de contacto"

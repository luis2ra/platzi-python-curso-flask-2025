from flask import Flask, request, jsonify

from config import Config
from models import db
from notes.routes import notes_bp
from auth.routes import auth_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    app.register_blueprint(notes_bp)
    app.register_blueprint(auth_bp)

    @app.route("/acerca-de")
    def about():
        return "Esto es una app de notas"

    @app.route("/contacto", methods=["GET", "POST"])
    def contact():
        if request.method == "POST":
            return "Formulario enviado correctamente", 201
        return "Pagina de contacto"

    @app.route("/api/info")
    def api_info():
        data = {
            "name": "Notas API",
            "version": "1.0.0",
            "description": "API para gestionar notas",
        }
        return jsonify(data), 200

    return app

from flask import Flask, jsonify, request
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Ruta que consulta el API de Dragon Ball
@app.route("/personaje/<id>")
def get_personaje(id):
    url = f"https://dragonball-api.com/api/characters/{id}"
    
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "Personaje no encontrado"}), 404

    data = response.json()
    return jsonify(data)  # Retornamos al frontend

@app.route("/")
def index():
    return open("templates/index.html").read()

if __name__ == "__main__":
    app.run(debug=True)

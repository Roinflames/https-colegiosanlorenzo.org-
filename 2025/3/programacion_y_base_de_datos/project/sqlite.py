import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

# --- Función para conectar DB ---
def get_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

# --- Crear tabla si no existe ---
def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

init_db()

# --- Rutas de API ---

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    conn = get_db()
    rows = conn.execute("SELECT * FROM usuarios").fetchall()
    conn.close()

    return jsonify([dict(row) for row in rows])

@app.route("/usuarios", methods=["POST"])
def agregar_usuario():
    data = request.json
    nombre = data.get("nombre")

    conn = get_db()
    conn.execute("INSERT INTO usuarios (nombre) VALUES (?)", (nombre,))
    conn.commit()
    conn.close()

    return jsonify({"mensaje": "Usuario agregado correctamente"}), 201

if __name__ == "__main__":
    app.run(debug=True)

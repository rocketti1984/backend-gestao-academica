from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    if data["usuario"] == "admin" and data["senha"] == "123":
        return jsonify({"msg": "Login autorizado"})
    return jsonify({"msg": "Login inválido"}), 401

@app.route("/api/notas")
def notas():
    return jsonify([
        {"nome": "João", "nota": 8.5},
        {"nome": "Maria", "nota": 9.0},
        {"nome": "Carlos", "nota": 7.2}
    ])

if __name__ == "__main__":
    app.run()

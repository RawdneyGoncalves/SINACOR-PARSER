# src/controller/main_controller.py
from flask import Flask, jsonify

app = Flask(__name__)




@app.route('/')
def home():
    return jsonify({"message": "Pagina Teste"})

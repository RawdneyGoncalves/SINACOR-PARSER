# src/router/main_router.py
from flask import Flask
from src.controller.main_controller import MainController

main_controller = MainController(Flask(__name__))

# Defina suas rotas aqui
@main_controller.app.route('/')
def index():
    return main_controller.hello_world()

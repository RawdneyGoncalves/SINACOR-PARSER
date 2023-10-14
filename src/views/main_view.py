
from flask import Flask
from src.controller.main_controller import MainController

main_controller = MainController(Flask(__name__))


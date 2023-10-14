# src/controller/main_controller.py
from flask import Flask

class MainController:
    def __init__(self, app: Flask):
        self.app = app

    def hello_world(self):
        return "Hello, World!"

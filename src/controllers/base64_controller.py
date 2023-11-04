from flask import Flask
from src.controllers.base64_controller import base64_controller  
from main_controller import app 

app.register_blueprint(base64_controller, url_prefix='/base64')

if __name__ == '__main__':
    app.run()

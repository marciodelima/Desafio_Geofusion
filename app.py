# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring
# Importando as bibliotecas
from flask import Flask, render_template
from flask_restful import Api
from models.predict import Predict

#Criando a aplicacao
APP = Flask(__name__)
API = Api(APP)

#Endpoint - GET
API.add_resource(Predict, '/predict/<string:lat>&<string:lng>')

#Default
@APP.route('/')
def home():
    return render_template('index.html')

#Main
if __name__ == '__main__':
    APP.run(debug=False)
    APP.run(port=5000)

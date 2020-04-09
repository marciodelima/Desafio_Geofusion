# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

#Importando as bibliotecas
from flask_restful import Resource
import models.retorno as ret
import utils.funcoes as func

#Classe
class Predict(Resource):

    # Metodo get
    @staticmethod
    def get(lat, lng):
        return ret.gerarpredicao(func.getvalues(lat), func.getvalues(lng))

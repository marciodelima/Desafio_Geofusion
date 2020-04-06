#Importando as bibliotecas
from flask_restful import Resource

#Classe
class Predict(Resource):

    #Obtendo valores
    def getvalues(self, value):
        return float((value.split('=')[1]))

    # Metodo get
    def get(self, lat, lng):
        resposta = {"latitude": self.getvalues(lat), \
"longitude": self.getvalues(lng), \
"predicao":96040.6114295958, "n_grandes_redes":0.0, \
"n_pequeno_varejista":1.0}
        return resposta

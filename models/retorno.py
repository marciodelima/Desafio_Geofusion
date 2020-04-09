# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

#Importando as bibliotecas
import os
import pickle
import pandas as pd
from shapely.geometry import Point
import utils.funcoes as func

PATH = os.getcwd() + '/models/'
METROS = 1000
METROS_CONCORRENTES = 50

def loadmodelo():
    return pickle.load(open(PATH + 'model_campifarma.pickle', 'rb'))

def gerarretorno(lat, lng, predicao, n_grandes_redes, n_pequeno_varejista):
    return {"latitude": lat, "longitude": lng, \
"predicao": predicao, "n_grandes_redes": float(n_grandes_redes), \
"n_pequeno_varejista": float(n_pequeno_varejista)}


def gerarpredicao(lat, lng):
    #Checando se geolocalidade esta no Mapa
    if not func.isdentromapa(lat, lng):
        return gerarretorno(lat, lng, -1, -1, -1)
    #Load dos dados
    df_pois = func.loadpois()

    #Gerando IsoCotas
    ponto_procura = func.criarponto(lat, lng)
    isocota_geral = func.gera_isocota(ponto_procura, METROS)
    isocota_concorrentes = func.gera_isocota(ponto_procura, METROS_CONCORRENTES)

    #Montando e marcando os points através do isocota
    df_pois['filtro'] = list(map(lambda x, y: Point(x, y).intersects(isocota_geral), \
df_pois.longitude, df_pois.latitude))
    df_intersecao = pd.DataFrame(df_pois[df_pois.filtro == True].values, \
columns=['index', 'latitude', 'longitude', 'tipo_POI', 'filtro'])

    #Montando e marcando dos points de concorrencia - 50 METROS
    df_pois['filtroConcorrentes'] = list(map(lambda x, y: Point(x, y).\
intersects(isocota_concorrentes), df_pois.longitude, df_pois.latitude))
    df_concorrentes = pd.DataFrame(df_pois[df_pois.filtroConcorrentes == True].values, \
columns=['index', 'latitude', 'longitude', 'tipo_POI', 'filtro', 'filtroConcorrentes'])

    #Gerando dados para o modelo preditivo
    data_model = df_intersecao.groupby('tipo_POI').count().T[0:1]
    for i in func.obtem_configuracao():
        if i not in data_model:
            data_model[i] = 0.0

    data_model.reset_index(drop=True, inplace=True)
    data_model = data_model[sorted(data_model.columns)]

    data_model_concorrentes = df_concorrentes.groupby('tipo_POI').count().T[0:1]
    for i in func.obtem_configuracao_concorrentes():
        if i not in data_model_concorrentes:
            data_model_concorrentes[i] = 0.0
    data_model_concorrentes.reset_index(drop=True, inplace=True)

    #Gerando a Previsao
    previsao = loadmodelo().predict(data_model.values)[0]

    return gerarretorno(lat, lng, previsao, \
float(data_model_concorrentes['concorrentes__grandes_redes']), \
float(data_model_concorrentes['concorrentes__pequeno_varejista']))

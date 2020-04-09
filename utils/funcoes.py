# -*- coding: utf-8 -*-
# pylint: disable=missing-docstring

import os
from functools import partial
from shapely.geometry import Point
from shapely.ops import transform
from shapely.wkt import loads
import pandas as pd
import pyproj

document_path = os.getcwd() + '/data/'

def lat_lng_to_utm(lat_lng_geom):
    project = partial(pyproj.transform,\
    pyproj.Proj(init='epsg:4326'), \
    pyproj.Proj(init='epsg:3857'))
    utm_geom = transform(project, lat_lng_geom)
    return utm_geom

def utm_to_lat_lng(utm_geom):
    project = partial(pyproj.transform,\
    pyproj.Proj(init='epsg:3857'), \
    pyproj.Proj(init='epsg:4326'))
    lat_lng_geom = transform(project, utm_geom)
    return lat_lng_geom

def gera_isocota(ponto, raio):
    raio_ponto_de_estudo_utm = lat_lng_to_utm(ponto).buffer(raio)
    raio_ponto_de_estudo_lat_lng = utm_to_lat_lng(raio_ponto_de_estudo_utm)
    return raio_ponto_de_estudo_lat_lng

def obtem_configuracao():
    return {'faculdades', 'escolas', 'ponto_de_onibus', 'concorrentes__grandes_redes', \
'concorrentes__pequeno_varejista', 'minhas_lojas', 'agencia_bancaria', \
'padaria', 'acougue', 'restaurante', 'correio', 'loterica'}

def obtem_configuracao_concorrentes():
    return {'concorrentes__grandes_redes', 'concorrentes__pequeno_varejista'}

def criarponto(lat, lng):
    return Point(lng, lat)

def isdentromapa(lat, lng):
    return loadmapa().intersects(criarponto(lat, lng))

def loadmapa():
    data = ""
    with open(document_path + 'campinas.wkt') as arq:
        for line in arq:
            data = line
    return loads(data)

def loadpois():
    return pd.read_csv(document_path + 'pois.csv')

def getvalues(value):
    return float((value.split('=')[1]))

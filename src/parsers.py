# -*- coding:utf-8 -*-
'''
Created on 25 ene 2022

@author: willi
'''
from datetime import datetime

def parsea_fecha(cadena):
    return datetime.strptime(cadena,'%d/%m/%Y').date()
def parsea_booleano(cadena):
    res=None
    cadena = cadena.upper()
    if cadena == 'SI':
        res =True
    elif cadena == 'NO':
        res =False
    return res
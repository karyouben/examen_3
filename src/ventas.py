# -*- coding:utf-8 -*-
'''
Created on 25 ene 2022

@author: willi
'''
import csv
from collections import namedtuple
from collections import Counter
import statistics
from parsers import *
from _datetime import date


Ventas = namedtuple('Ventas', 'fecha,ciudad,modelo,precio,unidades,financiado')

def lee_ventas(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector= csv.reader(f)
        next(lector)
        res=[]
        for fecha,ciudad,modelo,precio,unidades,financiado in lector:
            tupla_ventas = Ventas(parsea_fecha(fecha),ciudad,modelo,float(precio),int(unidades),parsea_booleano(financiado))
            res.append(tupla_ventas)
        return res

def esta_en_rango(fecha,fecha1,fecha2):
    fecha1 = datetime.strptime(fecha1, '%d/%m/%Y').date()
    fecha2 = datetime.strptime(fecha2, '%d/%m/%Y').date()
    res = True
    if fecha1 ==None and fecha2 ==None:
        res=True
    elif fecha1==None:
        res = fecha<=fecha2
    elif fecha2==None:
        res= fecha>=fecha1
    else:
        res= fecha1<=fecha<=fecha2
    return res
    
def unidades_vendidas(ventas,modelo,fecha1,fecha2):
    return sum(t.unidades for t in ventas if t.modelo in modelo and esta_en_rango(t.fecha,fecha1,fecha2))

def dicc_beneficios_por_modelo_año(ventas,año):
    dicc={}
    for t in ventas:
        if t.fecha.year ==año:
            clave=t.modelo
            if clave in dicc:
                dicc[clave]+= beneficio(t)
            else:
                dicc[clave]= beneficio(t)
    return dicc
        
def beneficio(venta):
    if venta.financiado:
        beneficio = venta.unidades*venta.precio*0.15
    else:
        beneficio = venta.unidades*venta.precio*0.1
    return beneficio


def dias_de_mas_unidades(ventas):
    maximo = max(ventas, key=lambda x:x.unidades)
    return [t.fecha for t in ventas if t.unidades==maximo.unidades]

            
def dicc_unidades_por_mes(ventas):
    dicc={}
    for t in ventas:
        clave =t.fecha.month
        if clave in dicc:
            dicc[clave]+=t.unidades
        else:
            dicc[clave] = t.unidades
    return dicc

def lista_dif_unidades_mes(ventas):
    dicc = dicc_unidades_por_mes(ventas)
    ventas = sorted(dicc.items())
    res=[]
    for indx in range (len(ventas)-1):
        ventas1 = ventas[indx][1]
        ventas2 = ventas[indx+1][1]
        diferencia = (ventas2-ventas1)
        res.append(diferencia)
    return res


def modelos_vendidos_mas_n_en_año(ventas,año,n):
    dicc = agrupa_por_modelo(ventas, año, n)
    return {clave for clave,valor in dicc.items() if len(valor)>n}

def agrupa_por_modelo(ventas,año,n):
    dicc={}
    for t in ventas:
        if t.fecha.year==año:
            clave=t.modelo
            if clave in dicc:
                dicc[clave].append(t.ciudad)
            else:
                dicc[clave] = [t.ciudad]
    return dicc

        

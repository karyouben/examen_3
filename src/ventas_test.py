# -*- coding:utf-8 -*-
'''
Created on 25 ene 2022

@author: willi
'''
from ventas import *
from datetime import datetime



def test_lee_ventas(fichero):
    res= lee_ventas(fichero)
    print(f"Leídas {len(res)} ventas")
    print("")
    print(f"Las tres primeras son: {res[:3]}")
    print("")
    print(f"Las tres últimas son: {res[-3:]}")
    print("")



def test_unidades_vendidas(ventas,modelo,fecha1=None,fecha2=None):
    res = unidades_vendidas(ventas,modelo,fecha1,fecha2)
    print(f"El número de unidades vendidas de los modelos {modelo} entre el {fecha1} y el {fecha2} es: {res}")
    print("")
def test_dicc_beneficios_por_modelo_año(ventas,año):
    res = dicc_beneficios_por_modelo_año(ventas,año)
    print(f"El beneficio por modelo en el año {año} es: {res}")
    print("")
    
def test_dias_de_mas_unidades(ventas):
    res = dias_de_mas_unidades(ventas)
    print(f"Las fechas de las ventas con más unidades vendidas fueron {len(res)} y son: {res}")
    print("")
    
def test_lista_dif_unidades_mes(ventas):
    res = lista_dif_unidades_mes(ventas)
    print(f"La lista de diferencia de ventas por mes es: {res}")
    print("")
    
def test_modelos_vendidos_mas_n_en_año(ventas,año,n):
    res = modelos_vendidos_mas_n_en_año(ventas,año,n)
    print(f"Los modelos vendidos en {año} en mas de {n} ciudades fueron: {res}")
    print("")


def main():
    fichero=('../data/concesionarios.csv')
    VENTAS = lee_ventas(fichero)
    test_lee_ventas(fichero)
    test_unidades_vendidas(VENTAS,{'MODELO-A','MODELO-C'},'1/1/2017','1/3/2017')
    test_dicc_beneficios_por_modelo_año(VENTAS,2016)
    test_dias_de_mas_unidades(VENTAS)
    test_lista_dif_unidades_mes(VENTAS)
    test_modelos_vendidos_mas_n_en_año(VENTAS,2012,2)
if __name__=="__main__":
    main()
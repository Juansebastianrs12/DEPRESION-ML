# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:41:51 2020

@author: sthef
"""
from modelo2 import Biosenal
from vista2 import InterfazGrafico
import sys
from PyQt5.QtWidgets import QApplication
class Principal(object):
    def __init__(self):        
        self.__app=QApplication(sys.argv)
        self.__mi_vista=InterfazGrafico()
        self.__mi_biosenal=Biosenal()
        self.__mi_controlador=Coordinador(self.__mi_vista,self.__mi_biosenal)
        self.__mi_vista.asignar_Controlador(self.__mi_controlador)
    def main(self):
        self.__mi_vista.show()
        sys.exit(self.__app.exec_())
    
class Coordinador(object):
    def __init__(self,vista,biosenal):
        self.__mi_vista=vista
        self.__mi_biosenal=biosenal
    def recibirDatosSenal(self,data):
        self.__mi_biosenal.asignarDatos(data)
    def devolverDatosSenal(self,c,x_min,x_max):
        return self.__mi_biosenal.devolver_segmento(c,x_min,x_max)
    
    def devolverDatos(self,c,c1,x_min,x_max):
        return self.__mi_biosenal.devolver_segmento2(c,c1,x_min,x_max)
    def funciones(self):
        return self.__mi_biosenal.funciones()
    def verificar1(self,a,b,c):
        return self.__mi_biosenal.verificar(a,b,c)
    # def escalarSenal(self,x_min,x_max,escala):
    #     return self.__mi_biosenal.escalar_senal(x_min,x_max,escala)
p=Principal()
p.main()
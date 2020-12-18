# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:41:51 2020

@author: sthef
"""
#%%ñibrerias
import sys
#Qfiledialog es una ventana para abrir yu gfuardar archivos
#Qvbox es un organizador de widget en la ventana, este en particular los apila en vertcal
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog, QMessageBox
from PyQt5 import QtCore, QtWidgets

from matplotlib.figure import Figure

from PyQt5.uic import loadUi
from scipy.io import loadmat
from numpy import arange, sin, pi
#contenido para graficos de matplotlib
from matplotlib.backends. backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import os
import scipy.io as sio
import numpy as np
from modelo2 import Biosenal
from scipy.signal import welch 
# clase con el lienzo (canvas=lienzo) para mostrar en la interfaz los graficos matplotlib, el canvas mete la grafica dentro de la interfaz
class MyGraphCanvas(FigureCanvas):
    #constructor
    def __init__(self, parent= None,width=4, height=3, dpi=80):
        
        #se crea un objeto figura
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #el axes en donde va a estar mi grafico debe estar en mi figura
        self.axes = self.fig.add_subplot(111)
        #llamo al metodo para crear el primer grafico
        self.compute_initial_figure()
        
        #se inicializa la clase FigureCanvas con el objeto fig
        FigureCanvas.__init__(self,self.fig)
        
    #este metodo me grafica al senal senoidal que yo veo al principio, mas no senales
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s)
#        self.axes_welch.plot(0,0)

    #hay que crear un metodo para graficar lo que quiera
    def graficar_datos(self,datos):
        #primero se necesita limpiar la grafica anterior
        self.axes.clear()      
        self.axes.plot(datos)
        #ingresamos los datos a graficar
        #y lo graficamos
        print("datos")
        print(datos)
        #voy a graficar en un mismo plano varias senales que no quecden superpuestas cuando uso plot me pone las graficas en un mismo grafico
        for c in range(datos.shape[0]):    
            print(c)
            self.axes.plot(datos[c,:]+c*10)
         
        self.axes.set_xlabel("Tiempo")
        self.axes.set_ylabel("Amplitud")
        self.axes.set_title("Graficación de señales")
        #self.axes.set
        #ordenamos que dibuje
        self.axes.figure.canvas.draw()

    
class MyGraphCanvas2(FigureCanvas):
    #constructor
    def __init__(self, parent= None,width=4, height=3, dpi=80):
        
        #se crea un objeto figura
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        #el axes en donde va a estar mi grafico debe estar en mi figura
        self.axes = self.fig.add_subplot(111)
        #llamo al metodo para crear el primer grafico
        self.compute_initial_figure()
        
        #se inicializa la clase FigureCanvas con el objeto fig
        FigureCanvas.__init__(self,self.fig)
        
    #este metodo me grafica al senal senoidal que yo veo al principio, mas no senales
    def compute_initial_figure(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)
        self.axes.plot(t,s)
#        self.axes_welch.plot(0,0)

    #hay que crear un metodo para graficar lo que quiera
    def graficar_datos2(self,datos):
        #primero se necesita limpiar la grafica anterior
        self.axes.clear()      
        self.axes.plot(datos)
        #ingresamos los datos a graficar
        #y lo graficamos
        contador=1
        print("datos")
        print(datos)
        #voy a graficar en un mismo plano varias senales que no quecden superpuestas cuando uso plot me pone las graficas en un mismo grafico
        for c in range(datos.shape[0]):           
            self.axes.plot(datos[c,:]+c*10)
            contador = contador +1
         
        self.axes.set_xlabel("Tiempo")
        self.axes.set_ylabel("Amplitud")
        self.axes.set_title("Graficación de señales")
        
        #self.axes.set
        #ordenamos que dibuje
        self.axes.figure.canvas.draw()

#%%
        #es una clase que yop defino para crear los intefaces graficos
class InterfazGrafico(QMainWindow):
    #condtructor
    def __init__(self):
        #siempre va
        super(InterfazGrafico,self).__init__()
        #se carga el diseno
        loadUi ('principal.ui',self)
        #se llama la rutina donde configuramos la interfaz
        self.setup()
        #se muestra la interfaz
        self.show()
    def setup(self):
        #los layout permiten organizar widgets en un contenedor
        #esta clase permite añadir widget uno encima del otro (vertical)
        layout = QVBoxLayout()
        #se añade el organizador al campo grafico
        self.campo_grafico.setLayout(layout)
        #se crea un objeto para manejo de graficos
        self.__sc = MyGraphCanvas(self.campo_grafico, width=4, height=3, dpi=80)
        #se añade el campo de graficos
        layout.addWidget(self.__sc)
        
        
        self.campo2.setLayout(layout)
        #se crea un objeto para manejo de graficos
        self.__sc2 = MyGraphCanvas2(self.campo2, width=4, height=3, dpi=80)
        #se añade el campo de graficos
        layout.addWidget(self.__sc2)
        
        #se organizan las señales 
        self.BotonAceptar.clicked.connect(self.cargar_senal);
        self.BotonCancelar.clicked.connect(self.cancelar)
        self.mostrar.clicked.connect(self.mostrar_Seg)
        self.BotonAdelante.clicked.connect(self.adelante)
        self.BotonAtras.clicked.connect(self.atras)
        self.BotonAceptar_2.clicked.connect(self.aceptar2)
        self.BotonSumar.clicked.connect(self.sumar)

        self.BotonAdelante.setEnabled(False)
        self.BotonAdelante.setEnabled(False)

    def asignar_Controlador(self,controlador):
        self.__coordinador=controlador
        
    def funciones1(self):
        estadistica=self.__coordinador.funciones()
        
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setText(estadistica)
        msg.show()
        
    def adelante(self):
        self.__x_min=self.__x_min+2000
        self.__x_max=self.__x_max+2000
        self.__sc.graficar_datos(self.__coordinador.devolverDatosSenal(self.c,self.__x_min,self.__x_max))
    def atras(self):
        #que se salga de la rutina si no puede atrazar
        if self.__x_min<2000:
            return
        self.__x_min=self.__x_min-2000
        self.__x_max=self.__x_max-2000
        self.__sc.graficar_datos(self.__coordinador.devolverDatosSenal(self.c,self.__x_min,self.__x_max))

    def cargar_senal(self):

        archivo_cargado, _ = QFileDialog.getOpenFileName(self, "Abrir señal","","Todos los archivos (*);;Archivos mat (*.mat)*")
        if archivo_cargado != "":
            print(archivo_cargado)
            
            #la senal carga exitosamente entonces habilito los botones
            data = sio.loadmat(archivo_cargado)
           # print(data["pnts"])
            print(data.keys())
            print(type(data))
           # print(data)
            

            f = data["EEG"]
            x=(np.array(f))
            print(x.shape)
            j=(x[0,0])
    
            data=(j[15])
           
            #volver continuos los datos
            self.c=self.canales.value()
            self.__x_min=0
            self.__x_max=2000
           # sensores,self.puntos,self.ensayos=data.shape
            #senal_continua=np.reshape(data,(sensores,self.puntos*self.ensayos),order="F")
            self.__coordinador.recibirDatosSenal(data)   
            self.__sc.graficar_datos(self.__coordinador.devolverDatosSenal(self.c,self.__x_min,self.__x_max))
            self.BotonAdelante.setEnabled(True)
            self.BotonAdelante.setEnabled(True)
            self.funciones1() 
            

            
    def mostrar_Seg(self):
        
        self.c=self.canales.value()
        self.__x_min=0
        self.__x_max=2000
        self.__sc.graficar_datos(self.__coordinador.devolverDatosSenal(self.c,self.__x_min,self.__x_max))
        self.BotonAdelante.setEnabled(True)
        self.BotonAdelante.setEnabled(True)
        self.funciones1() 
        
    def cancelar(self):
        self.hide()
    def aceptar2(self):
        self.__x_max=int(self.Texto_maximo.text())
        self.__x_min=int(self.Texto_minimo.text())
        print(self.__x_min)
        print(self.__x_max)
        self.c=int(self.canales.value())
        self.c1=int(self.canales_4.value())
        self.e2=int(self.canales_3.value())
        
        print(self.c)
        x=self.__coordinador.verificar1(self.c1,self.e2,self.__x_max)
        if x==True:
            self.__sc2.graficar_datos2(self.__coordinador.devolverDatos(self.c,self.c1,self.__x_min,self.__x_max))     
    #def cancelar(self):
        if x==False:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("datos por fuera del rango")
            msg.show()
            
        

            
    def sumar (self) :
        self.__x_max=int(self.Texto_maximo.text())
        self.__x_min=int(self.Texto_minimo.text())
        print(self.__x_min)
        print(self.__x_max)
        self.c=int(self.canales.value())
        self.d=int(self.canales_2.value())
        
        self.c1=int(self.canales_4.value())
        self.f=self.c1+self.d
        self.e=int(self.canales_3.value())
        print(self.c)
        x=self.__coordinador.verificar1(self.c1,self.e,self.__x_max)
        if x==True:
        #punto=self.Texto_puntos.text()
            self.__sc2.graficar_datos2(self.__coordinador.devolverDatos(int(self.c),self.f,int(self.__x_min),int(self.__x_max)))
    #def cancelar(self):
        if x==False:
             msg = QMessageBox(self)
             msg.setIcon(QMessageBox.Information)
             msg.setText("datos por fuera del rango,tenga en cuenta que si la dimension es 2, la epoca se tomara como 1")
             msg.show()
       
        
        
        
        
        
        
        
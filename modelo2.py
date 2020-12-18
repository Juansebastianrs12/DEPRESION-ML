# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 13:41:51 2020

@author: sthef
"""
import numpy as np
class Biosenal(object):
    def __init__(self,data=None):
        if not data==None:
            self.asignarDatos(data)
        else:
            self.__data=np.asarray([])
            self.__canales=0
            self.__puntos=0
    def asignarDatos(self,data):
        self.__data=data
        #self.__canales=data.shape[0]
        #self.__puntos=data.shape[1]
    #necesitamos hacer operacioes basicas sobre las senal, ampliarla, disminuirla, trasladarla temporalmente etc
    def devolver_segmento(self,c,x_min,x_max):
        #prevengo errores logicos
        if x_min>=x_max:
            return None
        #cojo los valores que necesito en la biosenal
        return self.__data[:,x_min:x_max]
    def devolver_segmento2(self,c,c1,x_min,x_max):
        #prevengo errores logicos
        if x_min>=x_max:
            return None
        #cojo los valores que necesito en la biosenal
        return self.__data[c:c1,x_min:x_max]
    
    def funciones(self):
        
        media=np.mean(self.__data)
        desviacion=np.std(self.__data)
        minimo=np.amin(self.__data)
        maximo=np.amax(self.__data)
        dimension= self.__data.ndim
        valores=self.__data.shape
        canal= valores[0]
        puntos=valores[1]
        if dimension==3:
            epoca=valores[2]
        else :
            epoca=1
            j="la señal no esta formada por canales x puntos x épocas, la epoca se tomara como 1"
    
        #canales= valores[0]
        #puntos= valores[1]
        #epocas= valores[2]
        
        print("Dimensiones de los datos cargados: " + str(self.__data.shape));
        print("Numero de dimensiones: " + str(self.__data.ndim));
        estadistica=("Numero de dimensiones: " + str(self.__data.ndim)+"\n"+ j+"\n"+"canales:"+str(canal)+"\n"+"puntos: "+str(puntos)+"\n"+"epoca"+str(epoca)+"\n"+"La media de la señal es: " + str(media) + "\n"+"La desviacion estandar de la señal es: " + str(desviacion) + "\n"+"El valor minimo de la señal es: " + str(minimo) + "\n"+"El valor maximo de la señal es: " + str(maximo))
        print("La media es: " + str (media))
        print("La desviacion estandar es: "+ str(desviacion))
        print ("El valor minimo es:" + str(minimo ))
        print ("El valor maximo es:" + str(maximo))
        return estadistica
    
    def verificar(self,a,b,c):
        valores=self.__data.shape
        canal= valores[0]
        puntos=valores[1]
        dimension= self.__data.ndim
        if dimension==3:
            epoca=valores[2]
        else :
             epoca=1
        if int(a)>canal or int(a)<0:
            return(False)
        if int(c)>int(puntos) or int(c)<int(0):
            return (False)
        if int(b)>int(epoca) or int(b)<int(0) :
            return (False)
        else : 
            return(True)
    
    


 
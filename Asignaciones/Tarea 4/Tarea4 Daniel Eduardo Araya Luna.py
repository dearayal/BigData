###################################################################
# FILENAME :        Tarea4_DEAL.c             
#
# DESCRIPTION :     Exercises Dataframe
#       
#		Universidad Fidelitas - Python Analysis
#		IIQ 2020 
#
# AUTHOR :    Daniel Eduardo Araya Luna  
#
# HISTORY:
# DATE    	WHO     	        DETAIL
# 6/21/2020     Daniel E. Araya Luna    Initial commit
#
###################################################################

#                                 IMPORTANT!!!
#  Current source code was tested from command line, from IDLE was 
#  not possible import pandas even tough it was installed


# Import modules
import math as mt
import pandas as pd 
import os 
print(os.getcwd())
# Local Working Directoy 
os.chdir('D:\\Fidelitas\\Análisis con Python\\Asignaciones\\Tarea 4')  
print(os.getcwd())

#Cargue en un DataFrame el archivo EjemploAlgoritmosRecomendacion.csv y haga lo siguiente: 
datos = pd.read_csv("EjemploAlgoritmosRecomendacion.csv", delimiter = ';', decimal = ",", header = 0, index_col = 0 )

# • Calcule la dimensión de la Tabla de Datos.
datos.shape

# • Despliegue las primeras 2 columnas de la tabla de datos (Usando solamente []). 
datos[1:3]

# • Despliegue las primeras 2 columnas de la tabla de datos (Usando solamente iloc).
datos.iloc[1:3,:]

# • Despliegue las primeras 2 columnas de la tabla de datos (Usando solamente loc). 
datos.loc['Adam':'Anna', :]

# • Ejecute un info() de los datos.
datos.info

# • Calcule la Media para todas las variables 
datos.median()



# Cargue la tabla de datos que está en el archivo SAheartv.csv haga lo siguiente:
datos = pd.read_csv("SAheart.csv", delimiter = ';', decimal = ".", header = 0, index_col = 0 )

# • Calcule la dimensión de la Tabla de Datos.
datos.shape

# • Despliegue las primeras 3 columnas de la tabla de datos (Usando solamente []). 
datos[1:4]

# • Despliegue las primeras 3 columnas de la tabla de datos (Usando solamente iloc). 
datos.iloc[1:4,:]

# • Ejecute un info() de los datos.
datos.info

# • Calcule la suma de las columnas con variables cuantitativas (numéricas). 
datos.sum(axis=1)

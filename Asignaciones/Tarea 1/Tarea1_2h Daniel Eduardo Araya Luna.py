###################################################################
# FILENAME :        Tarea1_DEAL.py             
#
# DESCRIPTION :     Exercises for data analysis and transformation 
#       
#		Universidad Fidelitas - Python
#		IIQ 2020 
#
# AUTHOR :    Daniel Eduardo Araya Lun  
#
# HISTORY:
# DATE    	WHO     	        DETAIL
# 5/30/2020     Daniel E. Araya Luna    Initial commit
#
###################################################################

# Import modules
import math as mt

# Ejercicios de análisis y transformación de datos

# h) Dados dos puntos en el espacio, en coordenadas (X,Y), calcule la distancia
#    entre los dos puntos.
#    La fórmula de la distancia es:
#    d = sqrt( (X1 – X2) ** 2 + (Y1 – Y2) ** 2 )


print("\nEste programa determina la distancia entre dos puntos.")

print("\nDatos para el punto 1 (X1,Y1)")
X1 = int (input("Digite el valor de X1: "))
Y1 = int (input("Digite el valor de Y1: "))


print("\nDatos para el punto 2 (X2,Y2)")
X2 = int (input("Digite el valor de X2: "))
Y2 = int (input("Digite el valor de Y2: "))

d = mt.sqrt( (X1 - X2) ** 2 + (Y1 - Y2) ** 2 )

print("\nLa distancia d calculada es: " + str(d))



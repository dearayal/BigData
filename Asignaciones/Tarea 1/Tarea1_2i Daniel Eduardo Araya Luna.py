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

# i) Se desea leer la hora actual del día (en hora, minutos, segundos) y determinar
#    cuántas horas, minutos y segundos restan para culminar el día.
#    Asuma un formato de 24 horas. 

print("\nEste programa determina cuántas horas, minutos y segundos restan para culminar el día.")

print("\nIngrese la hora actual (HH:MM::SS)")
HH = int (input("Ingrese las horas HH: "))
MM = int (input("Ingrese los minutos MM: "))
SS = int (input("Ingrese los segundos SS: "))

print("\nPara terminar el dia faltan:")
print(str(23 - HH) + " Horas, " + str(59 - MM) + " Minutos y " + str(60 - SS) + " Segundos")



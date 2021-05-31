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

# j) Se desea sumar dos tiempos dados en horas, minutos y segundos

print("\nEste programa determina la sumatoria de dos horas en formato HH:MM:SS")

print("\nIngrese la hora (HH:MM::SS)")
HH1 = int (input("Ingrese las horas HH: "))
MM1 = int (input("Ingrese los minutos MM: "))
SS1 = int (input("Ingrese los segundos SS: "))

print("\nIngrese la hora (HH:MM::SS)")
HH2 = int (input("Ingrese las horas HH: "))
MM2 = int (input("Ingrese los minutos MM: "))
SS2 = int (input("Ingrese los segundos SS: "))

SS =  int ((SS1 + SS2) % 60)
rem = int (SS1 + SS2 / 60) 
MM =  int ((MM1 + MM2 + rem) % 60)
rem = int ((MM1 + MM2 + rem) / 60)
HH =  int (HH1 + HH2 + rem)

print("\n La sumatoria es " + str(HH) + ":" + str(MM) + ":" + str(SS))





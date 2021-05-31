###################################################################
# FILENAME :        Tarea1_DEAL.py             
#
# DESCRIPTION :     Exercises for math Lib use
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

# a) Desarrolle el código respectivo en Python para determinar el porcentaje
#    de varones y de mujeres que hay en un salón de clases
female = int (input("Digite un numero de estudiantes mujeres: "))
male = int (input("Digite un numero de estudiantes varones: "))
total = male + female;

print("\nEl total de estudiantes es: " +  str(total)+ "%")
print("LAS estudiantes representan el " +  str((male/total)*100) + "%")
print("LOS estudiantes representan el " +  str((female/total)*100) + "%")

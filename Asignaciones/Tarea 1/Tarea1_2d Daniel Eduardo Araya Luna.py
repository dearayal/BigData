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

# d) Desarrolle el código respectivo en Python para intercambiar las cifras
#    de las unidades de dos números naturales.

print("\nEste programa intercambia las unidades de dos numeros naturales\n")


num1 = int (input("Digite el primer numero: "))
num2 = int (input("Digite el segundo numero: "))

# Obtener unidades de cada numero
unit1 = num1 % 10
unit2 = num2 % 10

num1 = num1 - unit1 + unit2
num2 = num2 - unit2 + unit1

print("\nLos nuevos numeros son " + str(num1) + " y " + str(num2) +"\n")

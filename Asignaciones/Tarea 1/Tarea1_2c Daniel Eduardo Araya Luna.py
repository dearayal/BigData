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

# c) En una gasolinera, las maquinas expresan lo vendido en galones, pero el
#    precio está definido por litro. Determine la cantidad de litros vendida
#    al cliente y el monto que el cliente debe pagar. Considere que un galón
#    son 3.785 litros y cada litro de combustible vale 598 colones.

Gallon2Liter = 3.785;
precioLitro = 598

print("\nEste programa calcula el precio a pagar en una gasolinera de ")
print("acuerdo a la cantidad de galones vendidos\n")


galones  = int (input("Digite la cantidad de galones vendidos: "))
venta =  galones * Gallon2Liter * precioLitro

print("\n El total a pagar por esta venta es: " + str(venta) + " colones\n")

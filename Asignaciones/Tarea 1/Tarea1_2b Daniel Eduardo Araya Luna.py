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

# b) Calcule el área y el volumen de un cilindro, conociendo su radio
#    y su altura. Las fórmulas son:
#       área = 2 * PI * radio * altura 
#       volumen = PI * radio * 2 * altura.
#    (PI es una constante real cuyo valor es 3.1415)

PI = 3.1415;

print("\nEste programa calcula el area y volumen de un cilindro\n")

radio  = int (input("Digite el radio del cilindro(cm): "))
altura = int (input("Digite la altura del cilidro(cm): "))

area = 2 * PI * radio * altura 
volumen = PI * radio**2 * altura

print("\nEl area es: " +  str(area)+ "cm2")
print("El volumen es: " +  str(volumen)+ "cm3")

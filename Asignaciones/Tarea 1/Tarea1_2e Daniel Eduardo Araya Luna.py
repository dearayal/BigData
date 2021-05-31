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

# e) En países de habla inglesa es común dar la estatura de una persona como
# la suma de una cantidad entera de pies más una cantidad entera de pulgadas.
# Así, la estatura de una persona podría ser 3' 2" (3 pies 2 pulgadas).
# Determine la estatura de una persona en metros, conociendo su estatura en
# el formato inglés. Considere que: 1 pie = 12 plg, 1 plg = 2.54 cm, 1 m = 100 cm

print("\nEste programa determina la altura de una persona en metros a partir del sistema ingles\n")

feet = int (input("Digite la altura en pies(feet): "))
inch = int (input("Y pulgadas(in): "))

# Obtener unidades de cada numero
altura = ((feet * 12 + inch) * 2.54)/100

print("\nLa altura equivale a " + str(altura) + "m\n")

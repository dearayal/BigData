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

# f) Se desea expresar la capacidad de un disco duro en megabytes, kilobytes y
#    bytes, conociendo la capacidad del disco en gigabytes. Considere que:
#       1 kilobyte = 1024 bytes
#       1 megabyte = 1024 kilobyte,
#       1 gigabyte = 1024 megabyte


print("\nEste programa determina la capacidad de un disco(GBi) en MB y kB\n")

capacity = int (input("Digite la capacidad de almacenamiento en GBi: "))

print("\nLa capacidad en MBi es: " + str(capacity * 1024) + " MBi")
print("La capacidad en kBi es: " + str(capacity * 1024 * 1024) + " kBi")

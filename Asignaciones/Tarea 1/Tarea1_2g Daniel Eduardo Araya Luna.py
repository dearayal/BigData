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

# g) El sueldo bruto de un vendedor se calcula como la suma de un sueldo básico
#    de 2500 colones por cada venta hecha más el 12% del monto total vendido.
#    Determine el sueldo neto de un vendedor sabiendo la cantidad y el monto
#    de las ventas que hizo en el mes.
#    El salario neto es el salario ganado por el vendedor menos el 9.17%


print("\nEste programa determina el sueldo neto de un vendedor sabiendo la ")
print("cantidad y el monto de las ventas que hizo en el mes\n")

monto = float (input("Digite el monto de las ventas para este mes: "))
cantVentas = int (input("Digite la cantidad de ventas: "))

sueldoBruto = (cantVentas * 2500) + (monto * 0.12)
deducciones =sueldoBruto * 0.0917
sueldoNeto = sueldoBruto - deducciones

print("\nEl salario bruto para este mes es: " + str(sueldoBruto))
print("Las deducciones (9.17%) son: " + str(deducciones))
print("El salario neto para este mes es: " + str(sueldoNeto))


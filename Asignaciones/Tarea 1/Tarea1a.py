###################################################################
# FILENAME :        Tarea1_DEAL.c             
#
# DESCRIPTION :     Exercises for math Lib use
#       
#		Universidad Fidelitas - Big Data
#		IQ 2020 
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

# En un Script de Python resuelva los siguientes ejercicios y imprimar
# los resultados (30 ptos): 

# 1) resultado1 = π·2− √4
n = int (input("Digite un numero entero: "))
resultado1 = n*2 - mt.sqrt(4)
print("El resultado de = n·2− √4 es " +  str(resultado1) + "\n\n")

# 2) resultado2 = 5!
resultado2 = mt.factorial(5)
print("El resultado de 5! es " + str(resultado2) + "\n\n")

# 3) resultado3 = log2(19)
resultado3 = mt.log(19,2)
print("El resultado de log_2(19) es " + str(resultado3) + "\n\n")    

# 4) resultado4 = log(5)
resultado4 =   mt.log(5,10)
print("El resultado de log(5) es " + str(resultado4) + "\n\n")

# 5) resultado5  = e^(0.6931472)
resultado5 =   mt.exp(0.6931472)
print("El resultado de e^(0,6931472) es " + str(resultado5) + "\n\n")


# 6) resultado6 = Calcule el valor de x si x= (1+y)/(1+2z^2)  para y=5 y z=π.
y = 5
z = int (input("Digite un numero entero: "))

resultado6 = x= (1+y) / (1 + 2*z^2)
print("El resultado de x= (1+y)/(1+2z^2) para y = 5, z="+ str(z) + ", es " + str(resultado6) + "\n\n")


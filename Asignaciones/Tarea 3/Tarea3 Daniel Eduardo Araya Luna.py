###################################################################
# FILENAME :        Tarea3_DEAL.c             
#
# DESCRIPTION :     Exercises Loops and Matrices
#       
#		Universidad Fidelitas - Python Analysis
#		IIQ 2020 
#
# AUTHOR :    Daniel Eduardo Araya Luna  
#
# HISTORY:
# DATE    	WHO     	        DETAIL
# 6/13/2020     Daniel E. Araya Luna    Initial commit
#
###################################################################

# Import modules
import math as mt


print("1. Programe en Python una función que recibe dos valores, determinar cual de los dos valores es el menor")
print("   y luego lo retorna.") 
def min2values(num1, num2): 
  if (num1 <= num2): # Si no es gallo entonces...
    return(num1)
  else:  
    return(num2)


print("2. Programe en Python una función que recibe tres valores A, B, y C y retorna el menor")
def min3values(A, B, C):

  if ((A <= B) and (A <= C)):   # A es menor que B y C?
    return(A)
  elif ((B <= A) and (B <= C)): # Si A no es el menor, B es menor que los otros números?
      return(B)
  else:                       # Si ni A ni B son los menores entonces es C
    return(C)


print("3. Programe en Python una función que recibe tres valores A, B, y C y retorna la suma. En caso de que")
print("   alguno de los tres valores no sea numérico retorna 0, use type para obtener el tipo.")
def sum3if(A, B, C):
    if (type(A) == int) and (type(B) == int) and (type(C) == int):  
        return (A + B + C)
    else:
        return 0

print("4. Programe en Python una función que recibe un numero n y retorna la productoria de los números enteros")
print("   comprendidos entre el 1 y el n.")
def factorial(n):
    return (mt.factorial(n))



print("5. Desarrolle una función que realice la sumatoria de los números enteros impares comprendidos entre el 1")
print("   y el n.")
def sumOdd(n):
    i = 1
    total = 0
    while i<=n:
        total = total + i
        i = i+2
    return total


print("6. Desarrolle una función que realice la sumatoria de los números enteros múltiplos de 10, comprendidos")
print("   entre el 1 y el n.")
def sumMult10(n): 
  total = 0
  i = 10
  while i<=n
    total = total + i
    i = i+10
return total

print("7. Desarrolle una función que calcula el costo de una llamada telefónica que ha durado t minutos sabiendo")
print("   que si t < 1 el costo es de 0,4 dólares, mientras que para duraciones superiores el costo es de")
print("   0,4 + (t − 1)/4 dólares, la función debe recibir el valor de t.") 
def CalcPhoneCharges(t):
    # Si t es menor a  1min (pero positivo) el costo es de 0,4 dólares
    if ((t < 1) & (t > 0 )):
        costo = 0.4
    elif (t >= 1): # para duraciones superiores
        costo = 0.4 + (t - 1) / 4 
    else:
        costo = 0
    return(costo)


print("8. Desarrolle una función que reciba un vector de números reales y un numero real x, tal que indique el")
print("    porcentaje de elementos menores a un valor x")
def getPorcInferior(vec, value):
    total = len(vec)
    cont = 0;
    for i in range(total):
        if vec[i] < value:
            cont = cont + 1
    return (cont/total)
        


print("9. Desarrolle una función que recibe una matriz cuadrada A de tamaño n × n y calcula su traza, es decir,")
print("   la suma de los elementos de la diagonal (Utilizando for anidados). Por ejemplo, la traza de la siguiente")
print("   matriz: 
def getTrace(A):

    trace = 0
    for i in range (len(A)): 
        trace = trace + A[i][i]

    return trace

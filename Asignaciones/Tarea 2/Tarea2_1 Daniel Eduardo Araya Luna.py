###################################################################
# FILENAME :        Tarea2_DEAL.c             
#
# DESCRIPTION :     Exercises Tuplas and Dictionary
#       
#		Universidad Fidelitas - Python Analysis
#		IIQ 2020 
#
# AUTHOR :    Daniel Eduardo Araya Luna  
#
# HISTORY:
# DATE    	WHO     	        DETAIL
# 6/7/2020      Daniel E. Araya Luna    Initial commit
#
###################################################################

# Import modules
import math as mt

print("Ejercicios para Listas y Tuplas\n")



print("\n4. Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Progra 1,")
print("Ingles, Algoritmos y Teoría) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura")
print("y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las ")
print("asignaturas que el usuario tiene que repetir.")
# Llenar la lista de materias

myList = []
while True:
    newItem = str (input("Digite una materia ('exit' para salir):  "))
    print (newItem)
    if (newItem == 'exit'):
        break
    else:
        myList.append(newItem)
        
# Nota obtenida
for i in range(len (myList)):
    nota = int (input("Digite una nota obtenida en el curso " + str(myList[i]) + ":  "))
    if (nota<70):
        myList.remove(myList[i])


print("\n5. Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, ")
print("y muestre por pantalla el menor y el mayor de los precios.") 
precios = [50, 75, 46, 22, 80, 65, 8]
print(str(precios))
print("El menor de los precios es: " + min(precios))
print("El mayor de los precios es: " + max(precios))


print("\n6. Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por ")
print("pantalla su producto escalar.")
vec1= (1,2,3)
vec2= (-1,0,2)

print("\n7. Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.")

 
print("\nEjercicios para Diccionario\n\n") 

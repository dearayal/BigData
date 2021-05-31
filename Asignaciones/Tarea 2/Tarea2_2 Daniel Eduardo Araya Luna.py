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
# 6/20/2020     Daniel E. Araya Luna    Added missing code for Dictionaries and Lists
#
###################################################################

# Import modules
import math as mt
import statistics as st
import numpy as np

print("Ejercicios para Listas y Tuplas\n")

print("\n1. Escribir un programa que almacene las asignaturas de un curso (por ejemplo, Matemáticas, Progra 1,")
print("   Ingles, Algoritmos y Teoría) en una lista y la muestre por pantalla.")
myList = []
while True:
    newItem = str (input("Digite una materia ('exit' para salir):  "))
    print (newItem)
    if (newItem == 'exit'):
        break
    else:
        myList.append(newItem)
        myList


print("\n2. Escribir un programa que pregunte al usuario los números ganadores de la lotería, los almacene en una")
print("   lista y los muestre por pantalla ordenados de menor a mayor.")
myList = []
for i in range (5):
  print(newItem = int (input("Digite el "+ i + "/5 numero ganador de la loteria"))
    print(newItem)
    myList.append(newItem)
myList.sort()
print("Los numeros ganadores son: " + str(myList))


print("\n3. Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en ")
print("   orden inverso separados por comas.")
myList = [1, 5 ,4, 3, 2, 9, 7, 8, 6, 10]
myList.sort(reverse = True)        

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
print("    y muestre por pantalla el menor y el mayor de los precios.") 
precios = [50, 75, 46, 22, 80, 65, 8]
print(str(precios))
print("El menor de los precios es: " + str(min(precios)))
print("El mayor de los precios es: " + str(max(precios)))


print("\n6. Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por ")
print("   pantalla su producto escalar.")
vec1= [1, 2, 3]
vec2= [-1, 0, 2]

producto =  vec1[0]*vec2[0] +  vec1[1]*vec2[1] +  vec1[2]*vec2[2]
print("Dado el vector: " + str(vec1))
print("Y dado el vector: " + str(vec2))
print("El producto escalar es: " + str(producto))

print("\n7. Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una ")
print("   lista y muestre por pantalla su media y desviación típica.")
myList = [] 
  
n = int(input("Ingrese la cantidad de elementos (muestra):  y elementos")) 

for i in range(0, n): 
    item = int(input()) 
    myList.append(item)
      
print(myList) 
print("La media de la muestra es: " + str(st.median(myList)))
print("La desviacion estandar de la muestra es: " + str(np.std(myList)))

 
print("\n\nEjercicios para Diccionario\n\n") 

print("\n1. Escribir un programa que guarde en una variable el diccionario  {'Euro':'€','Dollar':'$', 'Yen':'¥'}, ")
print("   pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el ")
print("   diccionario.") 
myDict = {'Euro':'€','Dollar':'$', 'Yen':'¥'}
print(myDict)
keyRequest = str (input("Digite una divisa:  "))

if (myDict.get(keyRequest)=="none"):
    print("Divisa no encontrada)
else:
    myDict[keyRequest]



print("\n2. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un")
print("   diccionario. Después debe mostrar por pantalla el mensaje: <nombre>  tiene <edad> años, vive en")
print("   <dirección> y su número de teléfono es  <teléfono>")
nombre = str (input("Digite su nombre :"))
myDict["Nombre"] = nombre
edad = int (input("Digite su edad :"))
myDict["Edad"] = edad
direccion = str (input("Digite su direccion :"))
myDict["Direccion"] = direccion
telefono = int (input("Digite su telefono :"))
myDict["Telefono"] = telefono

print(str(myDict["Nombre"]) + " tiene " + str(myDict["Edad"]) + " anios, vive en " + str(myDict["Direccion"]) + " y su numero de telefono es " + str(myDict["Telefono"]))  


print("\n3. Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al")
print("   usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.")
print("   Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.")
myFrutas = {"Platano": 1.35, "Manzana": 0.80, "Pera": 0.85, "Naranaja": 0.70}

fruit = str (input("Digite el nombre de la fruta:"))
kilos = int (input("Digite la cantidad de kilos:"))

if (myFrutas.get(fruit)=="none"):
    print("Fruta no encontrada)
else:
    print("El precio de " + str(kilos) + " kilos de " + str(fruit) + " es: " + str(myFrutas[fruit]*kilos))  


print("\n4. Escribir un programa que pregunte una fecha en formato dd/mm/aaaa  y muestre por pantalla la misma")
print("   fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.")
strDate = str (input("Digite una fecha(dd/mm/aaaa):  "))
myList = strDate.split("/")
myYear = {'1': "Enero", '2': "Febrero", '3': "Marzo", '4': "Abril", '5': "Mayo", '6': "Junio", '7': "Julio", '8': "Agosto", '9': "Septiembre", '10': "Octubre", '11': "Noviembre", '12': "Diciembre"}

print("fecha: " + str(myList[0]) + " de " + str(myYear[int(myList[1])]) + " de " + str(myList[2]))



print("\n5. Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso")
print("   {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura")
print("   en el formato <asignatura> tiene <créditos> créditos donde <asignatura>  es cada una de las asignaturas del")
print("   curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.")
myDict= {'Matemáticas': 6, 'Física': 4, 'Química': 5}

print("Matemáticas tiene " + str(myDict['Matemáticas']) + " créditos")
print("Física tiene " + str(myDict['Física']) + " créditos")
print("Química tiene " + str(myDict['Química']) + " créditos")

values = myDict.values()
total = sum(values)


print("\n6. Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona")
print("   (por ejemplo, nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez")
print("   que se añada un nuevo dato debe imprimirse el contenido del diccionario.")
nombre = str (input("Digite su nombre :"))
myDict["Nombre"] = nombre
myDict

edad = int (input("Digite su edad :"))
myDict["Edad"] = edad
myDict

sexo = str (input("Digite su sexo :"))
myDict["Sexo"] = sexo
myDict

telefono = str (input("Digite su telefono :"))
myDict["Telefono"] = telefono
myDict

email = str (input("Digite su email :"))
myDict["Email"] = email
myDict

direccion = str (input("Digite su direccion :"))
myDict["Direccion"] = direccion
myDict

print("\n7. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar")
print("   el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se")
print("   debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato")
myList = []
while True:
    print("Digite el articulo y su precio ('exit' para salir):  "))
    newItem = str (input("Articulo:  "))
    if (newItem == 'exit'):
        break
    else:
        newPrice = int (input("Precio:  "))
        myList[newItem] = newPrice
        myList

  
print("\n8. Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras")
print("   en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa")
print("   debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el")
print("   diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.") 

print("\n9. Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán ")
print("   en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. ")
print("   El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar.")
print("   Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario.")
print("   Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada")
print("   operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.") 

print("\n10. Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán")
print("   en un diccionario en el que la clave de cada cliente será su ID(cédula), y el valor será otro diccionario con los datos")
print("   del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor TRUE si se trata de un")
print("   cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú:")
print("   (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes")
print("    preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:") 


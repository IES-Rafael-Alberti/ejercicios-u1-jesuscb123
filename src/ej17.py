#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
#Pedimos un nombre al usuario.
nombre = input ("Introduce tu nombre: ")
#creamos una variable que contenga el número introducido por el usuario.
num1 = int(input("Introduce un número: "))
#Con el for indiciamos que imprima el nonbre tantas veces como se indica dentro del rango.
for i in range (num1):
    print (nombre)

#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r", donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.
n = int (input("Introduce un número: "))
m = int (input("Introduce un número: "))
division = n / m 
c = n // m
r = n % m
print (f"El resultado de la división es {division}, el cociente es {c} y el resto es {r}")

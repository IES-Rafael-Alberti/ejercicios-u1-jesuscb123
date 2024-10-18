#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número de letras que tienen el nombre.
#Pedimos un nombre al usuario
nombre = input ("Dime un nombre: ")
#Len contará y contendrá el número de caracteres de la frase.
totalcaracteres = len(nombre)
#Creamos una variable para almacenar el nombre en mayúsculas utilizando .upper().
nombremayuscula = nombre.upper()
#Imprimimos el nombre en mayúsculas y el número de caracteres.
print (f"{nombremayuscula} tiene {totalcaracteres} letras")

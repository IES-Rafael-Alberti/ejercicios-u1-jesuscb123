#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
#Creamos una variable que almacene la frase.
frase = input ("Dime una frase: ")
#Creamos otra variable que almacene la vocal en minúscula.
vocal = input ("Dime una vocal: ")
#Si la vocal introducida se encuentra en la frase:
if vocal in frase: 
    #Creamos otra variable que reemplaze la vocal introducida (Que estára en minúsculas) por la misma pero en mayúsculas.
    vocal_mayusculas = vocal.replace(vocal.lower(), vocal.upper())
    #Creamos otra variable que almacene el reemplazo de la frase original que tendrá todas las vocales en minúsculas por las vocales mayúsculas.
    frase_vocal = frase.replace(vocal, vocal_mayusculas)
print (frase_vocal)
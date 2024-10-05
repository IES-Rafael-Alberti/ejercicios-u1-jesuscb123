#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.
#Pedimos al usuario que introduzca una frase: 
frase = input("Dime una frase: ")
#Creamos una variable que contenga la frase pero añadiendo [::-1], esto hará que las letras se inviertan.
alreves = frase [::-1]
#Imprimimos en consola la frase y luego la frase al revés.
print (f"frase original {frase} frase invertida {alreves}")

#--------Otro método-------
#Pedimos al usuario que introduzca la frase:
frase = input ("dime una frase: ")
#Con .split dividimos indicamos las partes de la frase que están separadas por espacios.
partes = frase.split(" ")
#Creamos otra variable que contenga las partes pero cambiando el orden con [::-1]
palabrasinvertidas = partes [::-1]
#Creamos otra variable que contenga las partes pero ahora, formaran una nueva frase separadas por espacios utilizando .join
frasealreves = " ".join(palabrasinvertidas)
#Imprimimos la frase original y luego la frase al revés.
print (f"tu frase origina es {frase} y la frase al reves es {frasealreves}")
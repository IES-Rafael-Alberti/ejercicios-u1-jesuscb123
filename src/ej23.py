#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
#Pedimos un correo al usuario.
correo = input ("Introduce un correo: ")
#creamos una variable que almacene las partes separadas por el @.
arroba = correo.split("@")
#Creamos otra variable que almacene el reemplazo de la segunda parte después del arroba por ceu.es
correo_cambiado = correo.replace(arroba[1], "ceu.es")
print (correo_cambiado)
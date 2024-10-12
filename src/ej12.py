#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales.

#Introducimos un peso, ponemos float debido a que pueden tener decimales.
peso = float (input("Introduce tu peso: ")) 
# mientras peso sea negativo, señalar un error debido a que no existe peso en negativo.
while peso < 0:                             
    peso = float (input("Error, introduce un peso correcto: "))
altura = float (input("Introduce tu altura: ")) 
#Mientras la altura sea negativa, señalar un error debido a que no existe altura en negativa.
while altura < 0:                           
    altura = float (input("Error, introduce una altura correcta: "))
#El indice de masa corporal se mide diviendo el peso (en kg) por la altura (m2)
indicemasa = peso / altura ** 2        
#para redondear, he creado otra variable llamada "redondeado" y round hace que redondees a los decimales que quieras.    
redondeado = round (indicemasa, 2)          
print (f"Tu indice de masa corporal es: {redondeado}") 
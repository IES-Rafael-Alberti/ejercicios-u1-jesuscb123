#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
#Creamos una variable CONSTANTE llamada BARRAPAN (se pone en mayúsculas para indicar al programador que esa nunca debe cambiar)
BARRAPAN = 3.49
#creamos otra variable que contenga la solución a la siguiente operación que nos dará como resultado cuánto dinero se le descuenta a una barra de pan que no es del día.
pannodia = 3.49 * (60 / 100)
#Creamos otra variable que almacene el número de barras que no son del día vendidas.
vendidasnodia = int (input("Dime cuantas barras que no son del día has vendido: "))
#Ahora, creamos otra variable que indique el precio definitivo de la barra de pan que no es del día. Restamos el precio de una barra normal y le restamos lo que se descuenta. 
preciofinalbarra = 3.49 - pannodia 
#Creamos otra variable que contenga el coste final de todo multiplicando las barras vendidas por el precio que vale una barra que no es del día.
costefinal = vendidasnodia * preciofinalbarra
#Imprimimos por pantalla el coste habitual de una barra normal, cuando no es del día el precio con el descuento y el total de las barras vendidas que no son del día.
print (f"El coste habitual de una barra es {BARRAPAN}, como no es fresca el descuento es de {preciofinalbarra} y el coste final es: {costefinal}")
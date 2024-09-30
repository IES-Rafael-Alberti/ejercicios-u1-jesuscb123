#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
BARRAPAN = 3.49
pannodia = 3.49 * (60 / 100)
vendidasnodia = int (input("Dime cuantas barras que no son del día has vendido: "))
descuentobarra = 3.49 - pannodia 
costefinal = vendidasnodia * descuentobarra
print (f"El coste habitual de una barra es {BARRAPAN}, como no es fresca el descuento es de {descuentobarra} y el coste final es: {costefinal}")
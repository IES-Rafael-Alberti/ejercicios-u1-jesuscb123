#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.
#Creamos una variable que contenga el interes pero en decimal, no en porcentaje.
interes = 4 / 100
#Definimos otra variable que contenga el dinero introducido por el usuario.
cuentahorro = int (input("Introduce el dinero que tienes en la cuenta de ahorro: "))
#Creamos una variable que contenga el dinero del usuario por el interes y por los 3 años.
cantidadahorros = cuentahorro * interes * 3
#el ahorro total será el ahorro actual menos la cantidad de ahorros.
ahorrototal = cuentahorro - cantidadahorros
print (f"Cantidad ahorro tras tres años : {ahorrototal}")
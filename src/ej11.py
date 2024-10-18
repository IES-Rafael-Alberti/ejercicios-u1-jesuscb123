#escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
#He creado dos variables: una será contador que valdrá 1 y otro que será suma que vale 0.
contador = 1
suma = 0
#Pedimos al usuario un número.
n = int (input("Introduce un número positivo: "))
#Utilizo un while para indicar que mientras no hayas ingresado un número positivo saltará un error, y te hará introducir un número positivo.
while n < 0:
    n = int(input("Error, introduce otro número"))
#Mientras que contador (que en este caso vale 1) sea menor o igual que el número introducido, que sume uno a la variable suma y lo acumule. Contador también irá sumando 1 para que cuando contador supere al número introducido, salga del bucle. Así conseguimos que suma acumule tantos 1 como se haya indicado en el número introducido.
while contador <= n:
    suma += contador
    contador += 1
print (f"la suma de 1 a {n} es {suma}")


    


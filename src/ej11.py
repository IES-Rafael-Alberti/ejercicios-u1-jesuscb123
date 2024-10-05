#escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
contador = 1
suma = 0
n = int (input("Introduce un número positivo: "))
while n < 0:
    n = int(input("Error, introduce otro número"))
while contador <= n:
    suma += contador
    contador += 1
print (f"la suma de 1 a {n} es {suma}")


    


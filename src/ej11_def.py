#Recibe un número y retorna una cadena de caracteres con el resultado de la función.

#He creado una función que hace que la variable suma almacene el número introducido por la suma de el número +1 y luego lo divida todo entre 2. Luego ese valor se retorna debido a que main hará un print de la función y se mostrará.
def serie (num):
    suma = (num * (num +1)) / 2
    return suma


#Una función para comprobar si el número introducido es positivo, si el número es negativo seguirá pidiendo un número positivo.
def es_positivo(num):
    while num < 0: 
        num = int(input("Error, introduce un número positivo: "))
    return num


    
def main ():
    num = int(input("Introduce un número positivo: "))
    es_positivo(num)
    print (serie(num))


   
if __name__ == "__main__":
    main()

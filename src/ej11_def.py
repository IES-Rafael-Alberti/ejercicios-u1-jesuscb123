#Recibe un número y retorna una cadena de caracteres con el resultado de la función.

def serie (num):
    suma = (num * (num +1)) / 2
    return suma
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

#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
def main():
    precio_introducido = input("Introduce un número con dos dec2imales: ")
#Como los números decimales siempre van a ir separados por "," utilizamos la función .split para separar la parte entera de la decimal.
    enteros_decimales = precio_introducido.split(",")
    print (f"Euros: {enteros_decimales[0]} decimales: 0,{enteros_decimales[1]}")

if __name__ == "__main__":
    main()
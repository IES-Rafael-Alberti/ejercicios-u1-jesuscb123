#Calcular la serie de Fibonacci hasta un número dado.

def fibonacci(maximo: int)-> str:
    num1 = 0
    num2 = 1
    serie = "0 1"
    suma = 0

    while suma <= maximo:
        suma = num1 + num2
        num1 = num2
        num2 = suma
        if suma <= maximo:
            serie+= " " + str(suma)
    return serie

def main():
    numero = int(input("Introduzca un número: "))
    print(fibonacci(numero))

if __name__ == "__main__":
    main()
#Realiza un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuántos números existen entre ellos dos.
#El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
#Si los números son diferentes, por ejemplo, 5 y 12, debe mostrar la frase: "El número menor es el 5 y entre ellos existen 7 números enteros".
def main():
    num1 = int(input("Introduce un número: "))
    num2 = int(input("Introduce otro número: "))
    while num2 == num1:
     num2 = int (input("ERROR, LOS NÚMEROS NO PUEDEN SER IGUALES, INTRODUCE OTRO NÚMERO: "))
    if num1 < num2: 
        diferencia = num1 - num2
        diferencia_positiva = diferencia * -1
        print (f"El número {num1} es el pequeño y entre ellos existen {diferencia_positiva} números. ")
    else:
        diferencia = num1 - num2
        print (f"El número {num2} es el pequeño y entre ellos existen {diferencia} números.")
        



if __name__ == "__main__":
    main()
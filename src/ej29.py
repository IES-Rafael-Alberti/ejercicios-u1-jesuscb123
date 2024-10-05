#Realiza un programa en Python que solicite un nombre y una edad.
#Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirse hasta que introduzca una edad comprendida entre 0 y 125 años.
#El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".
def main():
    nombre = input ("Introduce un nombre: ")
    edad = int(input("Introduce tu edad: "))
    while edad <0 or edad>125:
        edad = int (input("ERROR, INTRODUCE UNA EDAD CORRECTA: "))
    años_restantes = 125 - edad
    print (f"Tu nombre es {nombre} y tienes {edad}. Te quedan {años_restantes} años por cumplir.")

if __name__ == "__main__":
    main()

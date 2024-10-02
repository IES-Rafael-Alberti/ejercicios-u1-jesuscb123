#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def main ():
    fecha_introducida = input("Introduce una fecha en formato dd/mm/aaaa: ")
    fecha = fecha_introducida.split("/")
    print (fecha)
if __name__ == "__main__":
    main()


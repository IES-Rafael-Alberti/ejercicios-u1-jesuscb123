def main():
    numero = dame_entero()
    print ("Escribiste el número {num}")


def comprobar_numero(cadena:str) -> bool:
        cadena = cadena.strip()
        return cadena.isdigit() or (cadena.startswith("-") and  cadena[1:].isdigit())


def dame_entero()-> int:        
    cadena = input ("Dame un entero: ")
    while not comprobar_numero:
         cadena = input ("ERROR NO ES UN ENTERO!!!\n\nDame un entero de verdad!")
    return int(cadena)


if __name__ == "__main__":
    main()
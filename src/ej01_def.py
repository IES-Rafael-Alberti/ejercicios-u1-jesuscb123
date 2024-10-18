def saludo(nombre):
    return f"Hola, {nombre}"

def main():
    nombre = input ("Intro nombre: ")
    print (saludo(nombre))


if __name__ == "__main__":
    main()

#Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.
#El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10
def main():
    num1 = int(input("Introduce un número: "))
    incremento = int(input("Introduce un incremento: "))
    total = int(input("Introduce un total: "))
    while incremento < 0 or total < 0:
        print ("Error, ni el incrmeento ni el total pueden ser menores de 0. Vuelve a introducir un incremento y un total: ")
        incremento = int(input("Introduce un incremento: "))
        total = int(input("Introduce un total: "))
    for serie in range (num1, total +1, incremento):
        print (f"{serie}"+"-")



if __name__ == "__main__":
    main()
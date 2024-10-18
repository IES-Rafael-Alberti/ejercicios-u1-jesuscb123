#Realiza un programa en Python que pida un número de inicio, un incremento y un total de la serie.
#El incremento y el total deben ser mayores que cero. Si no es así, el programa debe finalizar con un error o obligar a que introduzcan un valor correcto para ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes).
#Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10

def comprobar_si_es_positivo(num_inicio,incremento,total_serie):
    while num_inicio < 0 or incremento < 0 or total_serie < 0:
        if num_inicio < 0:
            num_inicio = int(input("ERROR, INTRODUCE UN NÚMERO POSITIVO: "))
        if incremento < 0: 
            incremento = int(input("ERROR, INTRODUCE UN INCREMENTO POSITIVO: "))
        if total_serie < 0:
            total_serie = int(input("ERROR, INTRODUCE UN TOTAL POSITIVO: "))
    


def serie(num_inicio,incremento,total_serie):
        for serie in range(num_inicio,total_serie + 1,incremento):
             print(serie,end="-")



def main():
    num_inicio = int(input("Introduce un nùmero inicial: "))
    incremento = int(input("Introduce un incremento: "))
    total_serie = int(input("Introduce un total: "))
    comprobar_si_es_positivo(num_inicio,incremento,total_serie)
    serie(num_inicio,incremento,total_serie)



if __name__ == "__main__":
    main()
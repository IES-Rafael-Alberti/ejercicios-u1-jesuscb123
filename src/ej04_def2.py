#La función grados_celsius(farenheit: float) -> float recibe los grados farenheit (redondeados a dos posiciones decimales) y retorna los grados celsius (redondeados a dos posiciones).

def grados_celsius(fahrenheit: float):
    celsius = ((fahrenheit - 32) * (5/9))
    return round(celsius,2)

def introduce_numero_fahrenheit():
    fahrenheit = float(input("Introduce número: "))
    return round(fahrenheit,2)



def main():
    fahrenheit = introduce_numero_fahrenheit()
    celsius = grados_celsius(fahrenheit)
    print({f"Los grados en fahrenheit son: {fahrenheit} pasados a celsius son: {celsius}"})

    


if __name__ == "__main__":
    main()
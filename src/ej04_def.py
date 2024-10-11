#NO recibe parámetros y retorna una cadena de caracteres con la temperatura convertida en grados Celsius y entre parántesis la temperatura en grados farenheit... ambas temperaturas con 2 posiciones decimales. Por ejemplo, si introduce 212 debe retornar la cadena "100.00ºC (212.00ºF)". Dentro de la función se pedirá al usuario los grados Farenheit.
def grado ():
    fahrenheit = float (input("Dime los grados en celsius: "))
    celsius = ((fahrenheit - 32) * (5/9))
    return f"{celsius:.2f}({fahrenheit:.2f})"

def main ():
    print (grado())

if __name__=="__main__":
    main()



#La función calcula_precio(importe: float, iva: float) -> str recibe el importe y el iva, si el iva está fuera del rango 0-100 se aplicará el 21%, y retornará una cadena de caracteres con el iva y el precio con iva mostrando solo 2 posiciones decimales. Ejemplo: calcula_precio(100, 21) -> "El precio final del artículo con IVA (21.00) es 121.00€."

def calcular_iva_21(importe,iva):
    importe_con_iva = importe * (21 / 100)
    return f"El precio final con iva 21.00 es: {round(importe_con_iva,2)}"

def calcular_iva(importe,iva):
    importe_con_iva = importe * (iva / 100)
    return f"El precio final con iva {iva} es: {round(importe_con_iva,2)}"

def comprobar_si_21(iva):
    if iva < 0 or iva > 100:
        return True
    else: 
        return False

def pedir_importe_mas_iva():
    importe = float(input("Introduce un importe: "))
    iva = float (input("introduce el iva a aplicar: "))
    return importe,iva

def main():
    importe,iva = pedir_importe_mas_iva()
    if not comprobar_si_21(iva):
        print(calcular_iva(importe,iva))
    else:
        print(calcular_iva_21(importe,iva))






if __name__ == "__main__":
    main()
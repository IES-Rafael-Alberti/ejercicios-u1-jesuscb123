#Recibe el importe del artículo sin iva y el tipo de iva a aplicar, pero no retorna nada, sino que se imprime desde dentro de la función.
def importe_iva (importe_sin_iva,tipo_iva):
    iva_aplicado = importe_sin_iva * (tipo_iva / 100)
    importe_con_iva = importe_sin_iva + iva_aplicado
    print (f"El importe con iva es: {importe_con_iva}")

def main():
    importe_sin_iva = float(input("Dame el importe sin iva: "))
    tipo_iva = float(input("Dime el iva a aplicar: "))
    importe_iva(importe_sin_iva,tipo_iva)

if __name__=="__main__":
    main()

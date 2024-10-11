def coste_horas(horas,preciohora):
   importe_servicio = horas + preciohora
   return f"El importe total {importe_servicio}"
    


def main():
    horas = int (input("Dime las horas: "))
    preciohora = int (input ("Dime precio por hora: "))
    print (coste_horas(horas,preciohora))

if __name__=="__main__":
    main()

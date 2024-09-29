#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
importesiniva = float (input ("Dame el importe sin iva del artículo: "))
tipoiva = float (input ("dime el iva a aplicar: "))
ivaaplicado =  importesiniva * (tipoiva / 100)
importeconiva = importesiniva + ivaaplicado
print (f"el importe con iva es : {importeconiva}")

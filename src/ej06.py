#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
importe_final = int (input("Introduzca importe final"))
iva_aplicado = 10 / 100
importe_sin_iva = importe_final / iva_aplicado
print (f"Iva pagado: {iva_aplicado} importe sin iva: {importe_sin_iva}")


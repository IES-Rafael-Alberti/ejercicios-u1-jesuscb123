#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = input("Introduce un número: ")
precio = float (input("Introduce un precio: "))
unidades = float (input("Dime las unidades: "))
total = precio * unidades
print (f"Nombre del producto: {producto}, precio: {precio:09.2f}, unidades: {unidades:03.0f} coste total: {total:011.2f}")



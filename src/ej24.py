#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio_producto = str (input("Dime un precio"))
entero = str(precio_producto.replace(", "2,00"))
decimal = precio_producto.replace("2,52", "0,52")
print (f"El número entero es: {entero}")
print(f"El número decimal es: {decimal}")

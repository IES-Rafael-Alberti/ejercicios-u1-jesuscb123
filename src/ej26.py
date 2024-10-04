#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
def main():
    #Creamos una variable que almacene los productos separados por ","
    productos_compra = input ("Introducide productos de la compra separados por comas: ")
    #creamos otra variable que almacene cada producto que se encuentre antes de la ",". Esto se consigue gracias a .split
    lista_compra = productos_compra.split(",")
    #Creamos un for en el que indique que si productos_compra se encuentra dentro de la lista, lo imprima uno por uno.
    for productos_compra in lista_compra:
        print (productos_compra)

if __name__ =="__main__":
    main()
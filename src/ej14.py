#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
#Creamos dos variables que contengan el peso de un solo payaso y una sola muñeca.
payaso = float (112)
muñeca = float (75)
#Creamos dos variables que contengan cuantos payasos y muñecas ha vendidos
payasosvendidos = float (input("Cuántos payasos has vendido en el último pedido: "))
muñecasvendidas = float (input("Cuántas muñeas has vendido en el último pedido: "))
#el peso total será los payasos vendidos por el peso de cada payaso más las muñecas vendidas por el peso de cada muñeca.
pesototal = (payasosvendidos * payaso) + (muñecasvendidas * muñeca)
#He creado otra variable que almacene el peso pero en lugar de g en kg.
pesoenkg = pesototal / 1000 
print (f"El peso total del paquete que será enviado es de: {pesoenkg} kg ")

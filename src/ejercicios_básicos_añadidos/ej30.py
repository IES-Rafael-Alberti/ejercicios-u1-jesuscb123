#Escribir un programa que determine si un número es primo

def parimpar(num1):
    par = num1 % 2
    if par == 0:
       es_par_y_primo(num1)
    else:
        es_divisible(num1)




def es_par_y_primo(num1):
    if num1 <= 1 or num1 > 2:
        print ("El número introducido no es primo")
    else:
        if num1 == 2 or num1 > 1:
            print ("El número es primo") 




def es_impar_y_primo(num1):
    if num1 <= 1:
      print ("El número introducido no es primo")
    else:
        if num1 == 2 or num1 > 1:
           es_divisible(num1)




def es_divisible(num1):
    for i in range (1,30,2):
        es_divisible = num1 / i
        es_divisible_str = str(es_divisible)
        encuentra_punto = es_divisible_str.find(".")
    if es_divisible_str.find("."):
        print("El número es primo")
    else: 
        print("El número no 3es primo")
    


def main():
    num1 = int(input("introduce un número: " ))
    parimpar(num1)



if __name__ == "__main__":
    main()
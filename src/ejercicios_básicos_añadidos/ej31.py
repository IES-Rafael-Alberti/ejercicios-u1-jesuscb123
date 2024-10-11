#Mostrar todos los divisores de un número.

def divisores(num1):
    divisores = 0
    for i in range(1,num1,1):
        divisores += num1 / i
        print(divisores)
    

    

def main():
    num1 = int(input("Dame un número: "))
    print (divisores(num1))  



if __name__ == "__main__":
    main()
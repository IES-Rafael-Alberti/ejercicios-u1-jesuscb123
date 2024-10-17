#Cálculo de un número aleatorio entre dos valores.
import random
def num_aleatorio(num,num2):
    return random.randint(num,num2)


def main():
    num = int(input("Dame un número: "))
    num2 = int (input("Dame otro número: "))
    num_aleatorio(num,num2)
    print(num_aleatorio(num,num2))
    
if __name__ == "__main__":
    main()
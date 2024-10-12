import random
 

def adivino_ese_numero(num_user, numero_pc):
    contador = 1
    fin = 0
    while not num_user == numero_pc:
        fin += contador
        if num_user < numero_pc:
                num_user = int(input("MÁS:  "))
        else: 
                num_user = int(input("MENOS: "))
        if fin == 3:
                break
        print ("FALLASTE") 
    print("LO CONSEGUISTE")     

    
    
def main():
    num_user = int(input("Introduce un número del 1 al 100: "))
    numero_pc = random.randint(1,100)
    adivino_ese_numero(num_user,numero_pc)
    


if __name__ == "__main__":
    main()
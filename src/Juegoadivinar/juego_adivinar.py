import random
 


def no_has_adivinado(num_user_str,numero_pc):
        if num_user != numero_pc:
                print("FALLASTE")
        main()




def adivino_ese_numero(num_user_str,numero_pc):
        contador = 1
        fin = 0
        while not num_user == numero_pc:
                fin += contador
                print(f"Vas por el {fin} intento de 5")
                if num_user < numero_pc:
                        num_user = int(input("MÁS:  "))
                else: 
                        num_user =int(input("MENOS: "))
                if fin == 5:
                        no_has_adivinado(num_user,numero_pc)
        return("LO CONSEGUISTE")



def comprobar_si_es_entero(num_user):
        while num_user.find("."):
                num_user = input("ERROR, INTRODUCE OTRO NÚMERO: ")
        return True


def introduce_entero(num_user):
        num_user = input("Introduce un número del 1 al 100: ")
        return comprobar_si_es_entero(num_user)

    
def main():
        numero_pc = random.randint(1,100)
        num_user = introduce_entero("num_ user: ")


if __name__ == "__main__":
    main()
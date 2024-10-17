import random


def mensaje_error(num_user):
    num_user = input("ERROR, INTRODUCE UN NÚMERO VÁLIDO: ")
    return num_user


def adivina(num_user,num_pc):
        diferencia = int(num_pc - num_user)
        diferencia_absoluta = abs(diferencia)
        if num_user == num_pc:
            return True
        elif diferencia < 2:
            print("TE QUEMAS")
        elif diferencia < 5:
            print("ARDIENDO")
        elif diferencia < 10:
            print("CALENTITO...")
        elif diferencia < 20:
            print("Templado...")
        elif diferencia < 50:
            print("Estás cerca y a la vez lejos...")
        elif diferencia < 70 or diferencia > 70: 
            print ("CONGELADO")
        

        
def es_mayor_de_100(num_user):
    num_user = int(num_user)
    if num_user > 100:
        return True



def comprobar_entero(num_user: str):
    if num_user.startswith("-"):
        num_user= num_user[1:]
    elif num_user.count("."):
        return False
    else:
        num_user.strip
        return num_user.isdigit()



def introduce_numero():
    num_user = input("Introduce un número: ")
    while not comprobar_entero(num_user) or es_mayor_de_100(num_user):
        num_user = mensaje_error(num_user)
    num_user = int(num_user)
    return num_user
    
    

def main():
    num_pc = random.randint(0,100)
    num_user = introduce_numero()
    while not adivina(num_user,num_pc):
        num_user = introduce_numero()
    print("LO CONSEGUISTE")

        
        
    







if __name__ == "__main__":
    main()
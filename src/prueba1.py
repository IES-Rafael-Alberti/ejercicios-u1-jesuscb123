
def comrpueba_si_es_mayor(num1,num2):
    if num1 > num2:
        return num1
    elif num1 < num2:
        return num2
    else: 
        return False 
    

def dame_dos_numeros(num1,num2):
    num1 = int(input("Dame el primer número: "))
    num2 = int(input("Dame el segundo número: "))
    return num1,num2

def main():
    num1 = 0
    num2 = 0
    num1,num2 = dame_dos_numeros(num1,num2)
    if not comrpueba_si_es_mayor(num1,num2):
        print("0")
    else:
        print(comrpueba_si_es_mayor(num1,num2))

if __name__ =="__main__":
    main()
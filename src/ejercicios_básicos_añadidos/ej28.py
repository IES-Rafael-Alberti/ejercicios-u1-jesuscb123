
import math 


def tiene_mas_de_un_punto(valor: str):
    pos_primer_punto = valor.find(".")
    
    if pos_primer_punto >= 0:
        if valor.find(".", pos_primer_punto + 1):
            return True
    
    return False


def comprobar_numero_float(valor: str):
    if valor [:1] == "-":
        valor = valor[1:]
    
    if tiene_mas_de_un_punto(valor):
        return False
    
    return contiene_solo_digitos_y_un_punto(valor)


def contiene_solo_digitos_y_un_punto(valor: str):
    for i in range(len(valor)): #esto va a ir de 0 a len(valor) - 1
        if not (valor[i].isdigit() or valor(i) == "."):
            return False
    
    return True


def calcular_area(lado_a, lado_b, lado_c):
    semiperimetro = (lado_a + lado_b + lado_c) / 2
    area = math.sqrt(semiperimetro * (semiperimetro - lado_a) * (semiperimetro - lado_b) * (semiperimetro - lado_c))
    return area


def introduce_numero(msj:str):
    numero = input(msj).strip()
    
    while comprobar_numero_float(numero) == False:
          print ("ERROR NÚMERO INVALIDO")
          numero = input(msj).strip()
    
    return float(numero) 


def main():
    print("Dame los tres lados del triángulo: ")
    lado_a = introduce_numero("Lado 1: ")
    lado_b= introduce_numero("lado 2: ")
    lado_c = introduce_numero("lado 3: ")
    area = calcular_area(lado_a, lado_b, lado_c)
    print(f"{area:.2f}")


if __name__ == "__main__":
    main()
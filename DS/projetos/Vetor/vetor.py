import os
os.system ("cls")
import math

v = [45, -89, 32,-12, 33]

def primeiroElemento() -> int:
    x=v[0]
    # print(f"x vale {v[0]}")
    return x

def achaNega() -> None:
    for i in range (0,5,1):
        if v[i] < 0:
            print(v[i])

def somaVet() -> int:
    soma=0
    for i in range (0,5,1):
        soma = soma + v[i]
    return soma

def mediaVet() -> int:
    # soma = 0
    # for i in range (0,5,1):
    #     soma = soma + v[i]
    # media = soma / 5 
    return somaVet()/5

def achaImpar() -> int:
    impares=0
    for i in range (0,5,1):
        if v[i]%2==1:
            print(v[i]) 

print("""1-Primeiro Elemento
2-Acha Negativos
3-Soma os Valores
4-Media dos Valores
5-Valores Impares""")
opcao=int(input("Escolha: "))
match opcao:
    case 1:
        print(primeiroElemento())

    case 2:
        achaNega()

    case 3:
        print(somaVet())

    case 4:
        print(mediaVet())

    case 5:
        print(achaImpar())

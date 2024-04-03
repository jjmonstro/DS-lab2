import os
os.system ("cls")
import math
from subalgoritimos import *


v = [45, -89, 32,-12, 33]
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]


# def primeiroElemento() -> int:
#     x=v[0]
#     # print(f"x vale {v[0]}")
#     return x

# def achaNega() -> None:
#     for i in range (0,5,1):
#         if v[i] < 0:
#             print(v[i])

# def somaVet() -> int:
#     soma=0
#     for i in range (0,5,1):
#         soma = soma + v[i]
#     return soma

# def mediaVet() -> int:
#     # soma = 0
#     # for i in range (0,5,1):
#     #     soma = soma + v[i]
#     # media = soma / 5 
#     return somaVet()/5

# def achaImpar() -> int:
#     impares=0
#     for i in range (0,5,1):
#         if v[i]%2==1:
#             print(v[i]) 

# def exiba_extremos():
#     print(v[0],v[4])

# def exibe_indice_par():
#     for i in range(5):
#         if i % 2 == 0:
#             print(v[i])

# def existeOuNao(valor):
#     for i in range(5):
#         if valor==v[i]:
#             return True
        
# def ordenaVetor():
#     for i in range(5):
#         print(i)
#         for j in range(5):
#             if v[i]<v[j]:
#                v[j]=v[i]
#             break
#     for y in range(5):
#         print(v[i])




while True:
    os.system("cls")
    print(""" 
    0. S A I R
    1. Primeiro elemento do vetor. 
    2. Exiba somente os números negativos contidos no vetor.
    3. Soma dos elementos do vetor
    4. Média dos elementos do vetos
    5. Numeros ímpares contidos no vetor
    """)
    opcao = input("Escolha: ")
    if not opcao.isnumeric():
        input("Opção inválida!\nPressione alguma tecla para continuar . . .")
        continue
    opcao = int(opcao)

    match opcao:
        case 0:
            break
        case 1:
            print(primeiroElemento(v))

        case 2:
            achaNega()

        case 3:
            print(somaVet(v))

        case 4:
            print(mediaVet(v))

        case 5:
            print(achaImpar())
        case 6:
            print(exiba_extremos())
        case 7:
            print(exibe_indice_par())
        case 8:
            print(existeOuNao(32))
        case 9:
            print("Errado")
            print(ordenaVetor())
        case 10:
            copiaVet(v1,v2)
        case 11:
            inverte_vetor(v1,v2)
        case 12:
            ordenaVetor2()
        case 13:
            ordenaVetorDecrescente()
        case 14:
            ordenaVetorGeral()
        case 15:
            separaParesImpares()
        case 16:
            print(acima_media())
        case 17:
            print(maior_elemento(v1))
        case _:
            ...
    input("Aperte qualquer tecla para continuar . . .")



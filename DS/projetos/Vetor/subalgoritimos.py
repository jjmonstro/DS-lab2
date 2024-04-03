v = [45, -89, 32,-12, 33]
v1 = [41, 72, 39, 4, 35]
v2 = [0, 0, 0, 0, 0]

#EXERCÍCIO 1
def primeiroElemento(v: list) -> int:
    x=v[0]
    return x

#EXERCÍCIO 2
def achaNega() -> None:
    for i in range (0,5,1):
        if v[i] < 0:
            print(v[i])

#EXERCÍCIO 3
def somaVet(vet: list) -> int:
    soma=0
    for i in range (0,5,1):
        soma = soma + vet[i]
    return soma

#EXERCÍCIO 4
def mediaVet(vet) -> int:
    # soma = 0
    # for i in range (0,5,1):
    #     soma = soma + v[i]
    # media = soma / 5 
    return somaVet(vet)/5

#EXERCÍCIO 5
def achaImpar() -> int:
    impares=0
    for i in range (0,5,1):
        if v[i]%2==1:
            print(v[i]) 

#EXERCÍCIO 6
def exiba_extremos():
    print(v[0],v[4])

#EXERCÍCIO 7
def exibe_indice_par():
    for i in range(5):
        if i % 2 == 0:
            print(v[i])

#EXERCÍCIO 8
def existeOuNao(valor):
    for i in range(5):
        if valor==v[i]:
            return True
        
#EXERCÍCIO 9
def ordenaVetor():
    print("em construção...")
    for i in range(5):
        for j in range(5):
            if v[i]>v[j]:
               save = v1[i]
               v1[i] = v1[j]
               v[j] = save
    for y in range(5):
        print(v[i])

#EXERCÍCIO 10
def copiaVet(v1: list, v2: list) -> list:
    for i in range(5):
        v2[i]=v1[i]
    for i in range(5):
        print(f"v2={v2[i]}\n")

#EXERCÍCIO 11
def inverte_vetor(v1: list, v2: list):
    for i in range(5):
        v2[i]=v1[4-i]
    for i in range(5):
       print(f"v1={v1[i]}   v2={v2[i]}\n")

#EXERCÍCIO 12
def ordenaVetor2(vet: list) -> list:
    print("em construção...")


#EXERCÍCIO 13
def ordenaVetorDecrescente():
    print("em construção...")

#EXERCÍCIO 14
def ordenaVetorGeral():
    print("em construção...")

#EXERCÍCIO 15
def separaParesImpares():
    for i in range(5):
        for j in range(5):
            if v1[i]%2==0:
                save=v1[i]
                v1[i]=v1[j]
                v1[j]=save
                
        print(v1[i])
        
#EXERCÍCIO 16
def acima_media():
    x=0
    media=mediaVet(v1)
    for i in range(5):
        if v1[i]>media:
            x=x+1
    return x

#EXERCÍCIO 17
def maior_elemento(vet: list) -> int:
    x=0
    for i in range(5):
        if vet[i] > x:
            x=vet[i]
    return x
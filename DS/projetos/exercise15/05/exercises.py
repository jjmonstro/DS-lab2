import os
os.system("cls")


string="Eu sou maluco doido, avante palestra"
lista=[2,4,5,7,-9]
print(string)
def transformaVogal(s:list):
    string=s.replace('a', 'A')
    string=string.replace('e', 'E')
    string=string.replace('i', 'I')
    string=string.replace('o', 'O')
    string=string.replace('u', 'U')
    print(string)

def inteiroOUnao(l:list) -> bool:
    print(l)
    l=str(l)
    tudoJunto="".join(l)
    print(tudoJunto)
    


inteiroOUnao(lista)
import random
lista=[]
def general():
    i=0
    while i < 5:
        lista.append(random.randint(1,10))
        i+=1

def lista_kiir():
    i=0
    while i <len(lista):
        if i < len(lista)-1:
            print(lista[i],end='!')
        else:
            print(lista[i],end='')
        i+=1

def nagyobb(lista):
    i=0
    nagyobb_db=0
    while i < len(lista):
        if lista[i]>lista[i-1]:
            nagyobb_db+=1
        i+=1
    return nagyobb_db

def konzol_ir(nagyobb):
    print(f"\nNagyobb számok száma: {nagyobb}")

def fajlba_ir(nagyobb_db):
    with open("vegeredmeny.txt","w",encoding="UTF-8") as file:
        file.write(f"Nagyobb számok száma: {nagyobb_db}")
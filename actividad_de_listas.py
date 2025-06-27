#PUNTO1
lista1=[]
lista1.append(100)
lista1.append('Hola Mundo')
#PUNTO2
lista2=[]
lista2.append('Hola y Adios')
lista2.append(300)
#PUNTO3
lista3=lista1
lista3.pop(1)
#PUNTO4
lista4=lista2
lista4.remove('Hola y Adios')
lista4.remove(300)
#PUNTO5
lista5=lista3+lista4
print(lista5)
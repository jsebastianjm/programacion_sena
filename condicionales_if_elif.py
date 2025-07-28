print("Este programa permite convertir un texto en todo minusculas o todo mayusculas")
texto=input("Ingresa el texto: ")
print('''Ingresa:
      1. Si quieres convertir en minusculas
      2. Si quieres convertir en mayusculas''')
opc=int(input())
if opc==1:
    print(texto.lower())
elif opc==2:
    print(texto.upper())
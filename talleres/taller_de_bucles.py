print("\n1. Suma hasta cero.----------")
lista=[]
while True:
    num=int(input("Ingresa un numero entero: "))
    lista.append(num)
    if num==0:
        break
print(f"La suma de todos los numeros ingresados es {sum(lista)}")

print("\n2. Contraseña secreta.----------")
while True:
    con=input("Ingresa la contraseña correcta: ")
    if con=="python123":
        break
    print("Intenta de nuevo...")
print("Contraseña correcta")

print("\n3. Lista de compras.----------")
lista=[]
while True:
    producto=input("Ingresa un producto: ")
    if producto=="fin":
        break
    lista.append(producto)
print(f"Todos los productos en la lista son: {lista}")


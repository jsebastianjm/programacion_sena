print("\n1. Suma hasta cero.----------")
lista=[]
print("PARA TERMINAR LA SUMA INGRESA '0'")
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
print("INGRESA LOS PRODUCTOS A LA LISTA, PARA SALIR INGRESA 'fin'")
while True:
    producto=input("Ingresa un producto: ")
    if producto=="fin":
        break
    lista.append(producto)
print(f"Todos los productos en la lista son: {lista}")

print("\n4. Contador de pares e impares.----------")
pares,impares=([],[])
w=1
while w<=10:
    num=int(input("Ingresa un numero: "))
    if num%2==0:
        pares.append(num)
    else:
        impares.append(num)
    w+=1
print(f"Pares: {pares}")
print(f"Impares: {impares}")

print("\n5. Promedio de calificaciones.----------")
notas=[]
while True:
    nota=input("Ingresa una nota de 0 a 5, o escribe 'salir' para terminar el programa: ")
    if nota=="salir":
        break
    nota=float(nota)
    notas.append(nota)
if len(notas)==0:
    print("No hay notas")
else:
    print(sum(notas)/len(notas))

print("\n6. Tabla de multiplicar interactiva.----------")
num=int(input("Ingresar un número para generar la tabla de multiplicar: "))
i=1
print(f"\nTABLA DEL {num}")
while i<=10:
    print(f"{num}*{i}={num*i}")
    i+=1

print("\n7. Adivina el número.----------")
secreto=67
num=(int(input("Adivina el numero del 1 al 100: ")))
if num!=secreto:
    while True:
        if num>secreto:
            num=(int(input("Mas bajo, intenta de nuevo: ")))
        elif num<secreto:
            num=(int(input("Mas alto, intenta de nuevo: ")))
        else:
            print("¡Correcto!")
            break
else:
    print("¡Felicidades, adivinaste en el primer intento!")

print("\n8. Tupla de frutas.----------")
frutas=("manzana", "pera", "naranja", "piña", "mango", "uva", "fresa")
fruta=input("Adivina una fruta de las que está en la lista (Todo en minuscula): ")
while fruta not in frutas:
    fruta=input("No se encuentra en la lista, intenta de nuevo: ")
print("Bien hecho")

print("\n9. Diccionario de traducción.----------")
dictionary={
    "Traducción":"Translation",
    "Carro":"Car",
    "Metrónomo":"Metronome",
    "Saturno":"Saturn",
    "Es":"Is"
}
while True:
    palabra=input("Ingresa una palabra a traducir: ")
    if palabra in dictionary:
        print(dictionary[palabra])
        break
    else:
        print("Esa palabra no se encuentra en este diccionario: ")

print("\n10. Calculadora basica.----------")
while True:
    print("""----MENU----
    1. Sumar
    2. Restar
    3. Multiplicar
    4. Dividir
    5. SALIR""")
    opc=int(input("Elige una opción: "))
    if opc==5:
        break
    num1=int(input("Ingresa el primer numero a operar: "))
    num2=int(input("Ingresa el segundo numero en la operación: "))
    if opc==1:
        print(f"->{num1}+{num2}={num1+num2}")
    elif opc==2:
        print(f"->{num1}-{num2}={num1-num2}")
    elif opc==3:
        print(f"->{num1}*{num2}={num1*num2}")
    elif opc==4:
        print(f"->{num1}/{num2}={num1/num2}")
    print("")

print("\n11. Registro de edad.----------")
personas={}
print("Ingresa 'salir' como nombre para finalizar")
while True:
    llave=input(("Ingresa un nombre: "))
    if llave=="salir":
        break
    valor=int(input((f"Ingresa la edad de {llave}: ")))
    personas[llave]=valor
print(personas)

print("\n12. Buscar en lista.----------")
colores=["rojo","azul","amarillo","dorado","turquesa"]
color=input("Adivina un color de la lista (En minusculas): ")
while color not in colores:
    color=input("Ese color no está en la lista, adivina de nuevo: ")
print("Correcto")
    
print("\n13. Potencias de un numero.----------")
num=int(input("Ingresar un número para mostrar sus potencias del 1 al 5: "))
i=1
print(f"\nPOTENCIAS DEL {num}")
while i<=5:
    print(f"{num}^{i}={num**i}")
    i+=1

print("\n14. Lista de cuadrados.----------")
cuadrados=[]
print("Este programa permite ingresar 5 numeros para al final mostrar el resultado de elevar cada uno al cuadrado")
w=1
while w<=5:
    cuadrados.append(int(input("Ingresa un numero: "))**2)
    w+=1
print(cuadrados)

print("\n15. Diccionario de estudiantes.----------")
estudiantes={}
print("Ingresa 'fin' como nombre para finalizar")
while True:
    llave=input(("Ingresa el nombre del estudiante: "))
    if llave=="fin":
        break
    valor=int(input((f"Ingresa la nota de {llave}: ")))
    estudiantes[llave]=valor
print(estudiantes)

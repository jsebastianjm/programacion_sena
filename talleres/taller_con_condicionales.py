print("\n1. Verifica si un numero es positivo, negativo o cero.----------")
num=float(input("Ingresa un numero: "))
if num>0:
    print("Es un numero positivo")
elif num<0:
    print("Es un numero negativo")
else:
    print("Es cero")

print("\n#2. Calcula el mayor de dos numeros ingresados.----------")
num=float(input("Ingresa un numero: "))
num2=float(input("Ingresa otro numero: "))
if num>num2:
    print(f"{num} es mayor que {num2}")
elif num2>num:
    print(f"{num2} es mayor que {num}")
else:
    print("Ambos numeros son iguales")

print("\n#3. Determina si un numero es par o impar.----------")
num=float(input("Ingresa un numero: "))
if num%2==0:
    print("El numeros es par")
else:
    print("El numero es impar")

print("\n#4. Dado un numero verifica si esta entre 10 y 20.----------")
num=float(input("Ingresa un numero: "))
if num>=10 and num<=20:
    print("El numero esta entre 10 y 20")
else:
    print("El numero no esta en el rango de 10 a 20")

print("\n#5. Dados tres numeros encuentra el mayor usando condicionales.----------")
num=float(input("Ingresa un numero: "))
num2=float(input("Ingresa otro numero: "))
num3=float(input("Ingresa otro numero: "))
if num>num2:
    if num>num3:
        print(f"El numero {num} es el mayor de todos")
    elif num3>num:
        print(f"El numero {num3} es el mayor de todos")
elif num2>num3:
    print(f"El numero {num2} es el mayor de todos")
else:
    print("Todos los numeros son iguales")

print("\n#6. Calcula el precio final con un 10% de descuento si el total es mayor a $100.----------")
total=float(input("Ingresa el total de los gastos: "))
if total>100:
    total-=total/10
    print(f"Se le aplica un descuento del 10%, su nuevo total es de {total}")
else:
    print(f"Su total es {total}")

print("\n#7. Verifica si una persona puede votar (mayor o igual a 18 años).----------")
edad=int(input("Ingresa su edad: "))
if edad>=18:
    print("Puede votar")
else:
    print("No puede votar")

print("\n#8. Dado el tipo de cliente (VIP o normal), aplica un descuento del 20% solo a VIP.----------")
estatus=int(input("El cliente es VIP? (SI->Ingrese 1) (NO->Ingrese 0): "))
total=float(input("Ingresa el total de los gastos: "))
if total>100:
    if estatus==1:
        total-=total/20
        print(f"Se le aplica un descuento del 20% por ser un estimado cliente VIP, su nuevo total es de {total}")
    else:
        total-=total/10
        print(f"Se le aplica un descuento del 10%, su nuevo total es de {total}")
else:
    print(f"Su total es {total}")

print("\n#9. Verifica si un numero es multiplo de 5 y 3 al mismo tiempo.----------")
num=float(input("Ingresa un numero: "))
if num%5==0 and num%3==0:
    print("El numeros es multiplo de 5 y 3")
else:
    print("El numero no es multiplo de 5 y 3 al mismo tiempo")
    
print("\n#10. Dado un numero, verifica si es divisible entre dos numeros dados.----------")
num=int(input("Ingresa un numero: "))
div1=int(input("Ingresa otro numero, para verificar si es divisor del primero: "))
div2=int(input("Ingresa otro numero para verificar si es divisor: "))
if num%div1==0:
    if num%div2==0:
        print(f"{num} es divisible entre {div1} y {div2}")
    else:
        print(f"{num} es divisible entre {div1}")
elif num%div2==0:
    print(f"{num} es divisible entre {div2}")
else:
    print(f"{num} no es divisible entre {div1} ni entre {div2}")
    
print("\n---------- EJERCICIOS CON LISTAS ----------")
print("\n#11.----------")
numeros=[1,2,3,4,5]
if numeros[2]>10:
    print("Mayor a 10")
else:
    print("Menor a 10")

print("\n#12.----------")
lista=[3,5,7,9]
if 7 in lista:
    print("Esta en la lista")
else:
    print("No esta en la lista")
    
print("\n#13.----------")
lista=[4,6,2,8]
if lista[0]+lista[1]>10:
    print("Suma alta")
else:
    print("Suma baja")
    
print("\n#14.----------")
nombres=["Ana","Luis","Pedro","Marta"]
if nombres[-1]=="Marta":
    print("Nombre correcto")
else:
    print("Nombre incorrecto")
    
print("\n#15.----------")
colores=[input("Ingresa un color (en minusculas): "), input("Otro: "), input("Otro mas: ")]
if colores[1]=="azul":
    colores[1]=input("Ingresa un color diferente de azul: ")
print(colores)

print("\n---------- EJERCICIOS CON TUPLAS ----------")
print("\n#16.----------")
tupla=(5,8,12,20)
if tupla[0]<tupla[-1]:
    print("Orden ascendente")
else:
    print("Orden descendente")
    
print("\n#17.----------")
tupla=(25,32,28)
if tupla[1]>30:
    print("Edad mayor a 30")
else:
    print("Edad menor a 30")
    
print("\n#18.----------")
tupla=(1,2,3)
lista=list(tupla)
if lista[1]==2:
    lista[1]=10
tupla=tuple(lista)
print(tupla)

print("\n#19.----------")
tupla=(4,9)
if tupla[1]>5:
    print("Coordenada alta")
else:
    print("Coordenada baja")
    
print("\n#20.----------")
tupla1,tupla2=((3,4),(3,5))
if tupla1==tupla2:
    print("Tuplas iguales")
else:
    print("Tuplas diferentes")
    
print("\n---------- EJERCICIOS CON DICCIONARIOS ----------")
print("\n#21.----------")
id={
    "nombre":"Juan",
    "edad":17
}
if id["edad"]>=18:
    print("Mayor de edad")
else:
    print("Menor de edad")
    
print("\n#22.----------")
kanye_west={
    "nombre":"Lucia",
    "edad":20
}
if kanye_west["edad"]>18:
    kanye_west.update(edad=21)
print(kanye_west)

print("\n#23.----------")
ye={
    "nombre":"Carlos"    
}
if ye.get("ciudad")==False:
    ye.add(ciudad="Bogota")
print(ye)

print("\n#24.----------")
drake={
    "producto":"pan",
    "precio":1200
}
if "precio" in drake:
    print(drake["precio"])
else:
    print("No hay precio")
    
print("\n#25.----------")
hector_lavoe={
    "pan":1200,
    "leche":2000
}
if "pan" in hector_lavoe:
    print(hector_lavoe["pan"])
else:
    print("Producto no disponible")
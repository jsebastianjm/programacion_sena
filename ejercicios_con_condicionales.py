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
if total/10>100:
    total-=total/10
    print(f"Se le aplica un descuento del 10%, su nuevo total es de {total}")
else:
    print(f"Su total es {total}")
#holaaaaaa

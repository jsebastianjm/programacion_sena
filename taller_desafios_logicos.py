print("\n- EJERCICIO 1")
edad=int(input("Bienvenido usuario, para continuar ingresa tu edad: "))
if edad<18:
    print("Categoria: Menor de edad")
elif edad<65:
    print("Categoria: Mayor de edad")
else:
    print("Categoria: Adulto mayor")

print("\n- EJERCICIO 2")
estatura=float(input("Ingresa tu estatura en metros: "))
if estatura<1.5:
    print("Eres de baja estatura")
elif estatura<=1.8:
    print("Eres de estatura media")
else:
    print("Eres alto")

print("\n- EJERCICIO 3")
num=int(input("Ingresa un numero entero: "))
if num%2==0:
    if num%3==0:
        print(f"El numero {num} es multiplo de 2 y de 3")
    else:
        print(f"El numero {num} es multiplo de 2")
elif num%3==0:
    print(f"El numero {num} es multiplo de 3")
else:
    print(f"El numero {num} no es multiplo de 2 ni de 3")

print("\n- EJERCICIO 4")#No existe
print("""
:)
""")

print("\n- EJERCICIO 5")
paises=("Colombia", "Perú","Argentina", 'México')
pais=input("Ingresa un pais y veremos si esta en nuestra base de datos: ")
if bool(pais in paises)==False:
    print(f"'{pais}' no se encuentra en nuestra base de datos o cometiste un error ortografico")
else:
    print(f"{pais} si está en nuestra base de datos")

print("\n- EJERCICIO 6")
compatibilidad={
    "AB": ("AB","B","A","O"),
    "B": ("B", "O"),
    "A": ("A", "O"),
    "O": ("O")
}
tsangre=input("Ingresa tu tipo de sangre (AB, B, A, O) en mayusculas: ")
print(f"Puedes recibir sangre de donantes con tipo: {compatibilidad[tsangre]}")

print("\n- EJERCICIO 7")
temp=float(input("Ingresa la temperatura del ambiente (°C): "))
if temp<10:
    print("Hace frio")
elif temp<=25:
    print("Hay un clima templado")
else:
    print("Hace calor")

print("\n- EJERCICIO 8")
opc=int(input("Este programa te permite hacer operaciones entre dos numeros, primero ingresa el numero correspondiente a la operacion deseada:\n(1. Suma) (2. Resta) (3. Multiplicacion): "))
if opc==1:
    print("SUMA")
    num1=float(input("Ingresa el primer numero: "))
    num2=float(input("Ingresa el segundo numero: "))
    print(f"El total de {num1}+{num2} es {num1+num2}")
elif opc==2:
    print("RESTA")
    num1=float(input("Ingresa el primer numero: "))
    num2=float(input("Ingresa el segundo numero: "))
    print(f"El resultado de {num1}-{num2} es {num1-num2}")
elif opc==3:
    print("MULTIPLICACION")
    num1=float(input("Ingresa el primer factor: "))
    num2=float(input("Ingresa el segundo factor: "))
    print(f"El total de {num1}*{num2} es {num1*num2}")
else:
    print("Comando no encontrado")

print("\n- EJERCICIO 9")
meses={
    1:"Enero",
    2:"Febrero",
    3:"Marzo",
    4:"Abril",
    5:"Mayo",
    6:"Junio",
    7:'Julio',
    8:'Agosto',
    9:'Septiembre',
    10:'Octubre',
    11:'Noviembre',
    12:'Diciembre'
}
mes=int(input("Ingresa un numero del 1 al 12: "))
print(f"El mes numero {mes} del año es {meses[mes]}")

print("\n- EJERCICIO 10")
num=(input("Ingresa un numero de 4 cifras: "))
num_comienza=num[0]
print(f"El numero {num} comienza por {num_comienza}")

print("\n- EJERCICIO 11")
vocales=("a","e","i","o","u")
consonantes=("b","c","d","f","g","h","j","k","l","m","n","ñ","p","q","r","s","t","v","w","x","y","z")
numeros=("1","2","3","4","5","6","7","8","9","0")
texto=input("Ingresa una palabra o numero: ")
texto_start=texto[0]
if texto_start in vocales:
    print("La palabra comienza por una vocal")
elif texto_start in consonantes:
    print("La palabra comienza por una consonante")
elif texto_start in numeros:
    print("El texto ingresado comienza por un numero")
else:
    print("El texto comienza por un caracter especial")

print("\n- EJERCICIO 12")
frutas=['manzana','pera','piña']
precios={
    "manzana":1000,
    "pera":1200,
    "piña":1500,
}
fruta=input(f"Ingresa la fruta que deseas comprar\n(SOLO NOS QUEDA: {frutas}): ")
if fruta in frutas:
    print(f"Una {fruta} vale {precios[fruta]}")
else:
    print("Ese producto no está disponible")

print("\n- EJERCICIO 13")
nota=float(input("Ingresa tu calificacion (0-5): "))
if nota<3:
    print("Estas reprobado")
elif nota<=4:
    print("Estas aprobado con nota regular")
else:
    print("Apruebas con desempeño excelente")

print("\n- EJERCICIO 14")
num=int(input("Ingresa un numero entero: "))
if num%4==0:
    if num%6==0:
        print(f"El numero {num} es multiplo de 4 y de 6")
    else:
        print(f"El numero {num} es multiplo de 4")
elif num%6==0:
    print(f"El numero {num} es multiplo de 6")
else:
    print(f"El numero {num} no es multiplo de 4 ni de 6")

print("\n- EJERCICIO 15")
registro={
    "usuario":input("Ingresa un usuario: "),
    "contraseña":input("Ingresa una contraseña ")
}

usuario=input("Vuelve a confirmar tu usuario para continuar: ")
contraseña=input("Tambien valida tu contraseña: ")
if usuario==registro["usuario"] and contraseña==registro["contraseña"]:
    print("Acceso permitido")
else:
    print("Usuario o contraseña incorrectos")

print("\n- EJERCICIO 16")
edad=int(input("Bienvenido usuario, para continuar ingresa tu edad: "))
if edad<13:
    print("Categoria: Niño")
elif edad<18:
    print("Categoria: Adolescente")
elif edad<65:
    print("Categoria: Adulto")
else:
    print("Categoria: Adulto mayor")

print("\n- EJERCICIO 17")
capital=("Bogotá","bogotá","Bogota","bogota")
ciudad=input("Ingresa una ciudad de Colombia: ")
if ciudad in capital:
    print("Esa ciudad es la capital de Colombia")
else:
    print("Esa ciudad es una ciudad secundaria")


print("\n- EJERCICIO 18")
valor=float(input("Ingresa el valor de la compra: "))
if valor>200000:
    valor-=valor/100*15
    print("Tiene descuento del 15%")
elif valor>=100000:
    valor-=valor/100*10
    print("Tiene descuento del 10%")
print(f"El valor despues de posibles descuentos es de {valor}")

print("\n- EJERCICIO 19")
nombre=input("Ingrese su nombre: ")
horas=int(input("Ingrese el numero de horas trabajadas: "))
salario=horas*10000
if horas>40:
    salario+=salario*0.2
print(f"Su paga es de {salario}")

print("\n- EJERCICIO 20")
nota=float(input("Ingresa tu puntaje (0-100): "))
if nota<50:
    print("Insuficiente")
elif nota<80:
    print("Aceptable")
else:
    print("Sobresaliente")


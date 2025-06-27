'''print("\n- EJERCICIO 1")
print("Bienvenido usuario, ingresa tres calificaciones para calcular el promedio")
notas = []
notas.append(float(input("")))
notas.append(float(input("")))
notas.append(float(input("")))
promedio=(notas[0]+notas[1]+notas[2])/3
print(f"El promedio es {promedio}")

print("\n- EJERCICIO 2")
precios = {
    "huevos": 700,
    "gaseosa": 2000,
    "galletas": 1800
}
print(f"Los precios actuales de algunos de los productos son\n{precios}")
impuesto=float(input("\nIngrese un porcentaje para elevar los precios: "))
precios["huevos"]+=precios["huevos"]*(impuesto/100)
precios["gaseosa"]+=precios["gaseosa"]*(impuesto/100)
precios["galletas"]+=precios["galletas"]*(impuesto/100)
print(precios)

print("\n- EJERCICIO 3")
print("Ingresa las temperaturas (°C) de los 5 ultimos dias: ")
temp1=float(input(""))
temp2=float(input(""))
temp3=float(input(""))
temp4=float(input(""))
temp5=float(input(""))
temper=(temp1,temp2,temp3,temp4,temp5)
temper=list(temper)
temper[0]=temper[0]*(9/5)+32
temper[1]=temper[1]*(9/5)+32
temper[2]=temper[2]*(9/5)+32
temper[3]=temper[3]*(9/5)+32
temper[4]=temper[4]*(9/5)+32
print(f"Las temperaturas en °F son: {temper}")

print("\n- EJERCICIO 4")
print("Dame las edades de 5 personas: ")
edades=[int(input("")), int(input("")), int(input("")), int(input("")), int(input(""))]
print(f"El mayor es de: {max(edades)}")
print(f"El menor es el de: {min(edades)}")
print(f"El promedio es: {sum(edades)/len(edades)}")

print("\n- EJERCICIO 5")
precios={
    "manzana":10000,
    "pera":12000,
    "papa":20000
}
print("precios por kilo: ", precios)
manzana=float(input("Cuantos kilos vas a llevar de manzana?: "))
pera=float(input("Cuantos kilos vas a llevar de pera?: "))
papa=float(input("Cuantos kilos vas a llevar de papa?: "))
total=manzana*precios["manzana"]+pera*precios["pera"]+papa*precios["papa"]
print(f"El total es de {total}$")

print("\n- EJERCICIO 6")
numeros=(1,2,3,4,5)
total=sum(numeros)
print(f"La suma de {numeros} es: {total}")

print("\n- EJERCICIO 7")
print("Para ingresar los tres nuevos productos ingresa los siguientes datos: ")
print("\nPRODUCTO 1")
producto1={
    "nombre":input("Ingrese el nombre del producto: "),
    "cantidad":int(input("Ingresa la cantidad: ")),
    "precio":float(input("INgresa el precio: "))
}
print("\nPRODUCTO 2")
producto2={
    "nombre":input("Ingrese el nombre del producto: "),
    "cantidad":int(input("Ingresa la cantidad: ")),
    "precio":float(input("INgresa el precio: "))
}
print("\nPRODUCTO 3")
producto3={
    "nombre":input("Ingrese el nombre del producto: "),
    "cantidad":int(input("Ingresa la cantidad: ")),
    "precio":float(input("INgresa el precio: "))
}
print(producto1, producto2, producto3)

print("\n- EJERCICIO 8")
precios = {
    "huevos": 700,
    "gaseosa": 2000,
    "galletas": 1800,
    "doritos": 2200,
    "yogurt": 1500
}
print(f"Los precios actuales de algunos de los productos son\n{precios}")
descuento=float(input("\nIngrese un porcentaje para descontar a los precios: "))
precios["huevos"]-=precios["huevos"]*(descuento/100)
precios["gaseosa"]-=precios["gaseosa"]*(descuento/100)
precios["galletas"]-=precios["galletas"]*(descuento/100)
precios["doritos"]-=precios["doritos"]*(descuento/100)
precios["yogurt"]-=precios["yogurt"]*(descuento/100)
print(precios)

print("\n- EJERCICIO 9")
print("Dame 4 notas: ")
notas=(float(input("")), float(input("")), float(input("")), float(input("")))
print(f"La mayor es de: {max(notas)}")
print(f"La menor es de: {min(notas)}")

print("\n- EJERCICIO 10")
conversiones={
    "km": 1000,
    "hm": 100,
    "dam":10,
    "m":1,
    "dm":1/10,
    "cm":1/100,
    "mm":1/1000
}
cantidad=float(input("Ingresa la cantidad a convertir (numeros): "))
unidad=input("Ingresa de forma abreviada la unidad a convertir a metros (km, hm, dam, m, dm, cm, mm): ")
if unidad=="km":
    print(f"{cantidad} {unidad} es equivalente a {cantidad*conversiones["km"]} m")
elif unidad=="hm":
    print(f"{cantidad} {unidad} es equivalente a {cantidad*conversiones["hm"]} m")
elif unidad=="dam":
    print(f"{cantidad} {unidad} es equivalente a {cantidad*conversiones["hm"]} m")
elif unidad=="m":
    print(f"{cantidad} {unidad} es equivalente a {cantidad*conversiones["m"]} m")
elif unidad=="dm":
    print(f"{cantidad} {unidad} es equivalente a {cantidad*conversiones["dm"]} m")
elif unidad=="cm":
    print(f"{cantidad} {unidad} es equivalente a {cantidad*conversiones["cm"]} m")
elif unidad=="mm":
    print(f"{cantidad} {unidad} es equivalente a {cantidad*conversiones["mm"]} m")
else:
    print("...¿que?")'''
    
print("\n- EJERCICIO 11")
print("Ingresa cinco precios para calcular el IVA")
precios=[int(input("")), int(input("")), int(input("")), int(input("")), int(input(""))]
precios_iva=[precios[0]+(precios[0]/100*19),precios[1]+(precios[1]/100*19),precios[2]+(precios[2]/100*19),precios[3]+(precios[3]/100*19),precios[4]+(precios[4]/100*19)]
print(f"Los precios de:\n{precios}\nPasan a ser:\n{precios_iva}")

print("\n- EJERCICIO 12")
num1=int(input("Ingresa dos numeros para calcular operaciones matemticas entre ellos: "))
num2=int(input(""))
operaciones=(num1+num2,num1-num2,num1*num2,num1/num2)
op=("suma","resta","multiplicacion","division")
print(op)
print(operaciones)

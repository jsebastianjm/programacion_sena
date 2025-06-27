print("\n- EJERCICIO 1")
frutas = []
frutas.append(input("Ingresa una fruta: "))
frutas.append(input("Ingresa otra fruta: "))
frutas.append(input("Ingresa otra fruta: "))
print(frutas)

print("\n- EJERCICIO 2")
edades = []
edades.append(int(input("Ingresa una edad: ")))
edades.append(int(input("Ingresa otra edad: ")))
print(edades)

print("\n- EJERCICIO 3")
notas = []
notas.append(float(input("Ingresa una nota: ")))
notas.append(float(input("Ingresa otra nota: ")))
print(sum(notas)/2)

print("\n- EJERCICIO 4")
productos = []
productos.append(input("Ingresa un producto: "))
productos.append(input("Ingresa otro producto: "))
productos.append(input("Ingresa otro producto: "))
print(productos)

print("\n- EJERCICIO 5")
precios = []
precios.append(float(input("Ingresa el precio de un producto: ")))
precios.append(float(input("Ingresa el precio de otro producto: ")))
precios.append(float(input("Ingresa el precio de otro producto: ")))
print(sum(precios))

print("\n- EJERCICIO 6")
numeros = []
numeros.append(int(input("Ingresa un numero: ")))
numeros.append(int(input("Ingresa otro numero: ")))
numeros.append(int(input("Ingresa otro numero: ")))
numeros.append(int(input("Ingresa otro numero: ")))
print(f"El numero menor es {min(numeros)}")
print(f"El numero mayor es {max(numeros)}")

print("\n- EJERCICIO 7")
nombres = []
nombres.append(input("Ingresa un nombre completo: "))
nombres.append(input("Ingresa otra nombre completo: "))
print(f"Bienvenido de nuevo, {nombres[0]}")
print(f"Bienvenido de vuelta, {nombres[1]}")

print("\n- EJERCICIO 8")
temperaturas = []
temperaturas.append(float(input("Ingresa una temperatura: ")))
temperaturas.append(float(input("Ingresa otra temperatura: ")))
fahr1=temperaturas[0]*9/5+32
fahr2=temperaturas[1]*9/5+32
print(f"La primera temperatura, ({temperaturas[0]}°C) es igual a {fahr1}°F")
print(f"La segunda temperatura, ({temperaturas[1]}°C) es igual a {fahr2}°F")
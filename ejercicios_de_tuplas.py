#Ejercicio1
numeros = (1,2,3,4,5)
#Ejercicio2
print(numeros[1])
#Ejercicio3
print(len(numeros))
#Ejercicio4
print(numeros.index(4))
#Ejercicio5
print(numeros.count(2))
#Ejercicio6
variado = ("computador", 15, 299.31)
#Ejercicio7
tupla_mas_pequeña=(11,21,31,41,51,61,71,81,91)
otra_tupla_mas_pequeña=("a","e","i","o","u")

tupla_mas_grande = (tupla_mas_pequeña, otra_tupla_mas_pequeña)
print(tupla_mas_pequeña[0])
#Ejercicio8
tupla_externa = (1,2,(10,20,30),4)
primer_valor_interno = tupla_externa[2][0]
print(f"El primer valor de la tupla interna es {primer_valor_interno}")
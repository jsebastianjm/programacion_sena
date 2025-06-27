print("\n***************APPEND(X)***************")
print("\n- EJERCICIO 1")
numeros = []
numeros.append(7)
print(numeros)

print("\n- EJERCICIO 2")
nombres = ["Ana", "Luis"]
nombres.append('Carlos')
print(nombres)

print("\n***************INSERT(I, X)***************")
print("\n- EJERCICIO 1")
numeros = [1, 2, 3]
numeros.insert(0, 99)
print(numeros)

print("\n- EJERCICIO 2")
colores = ['azul', 'verde']
colores.insert(1, 'rojo')
print(colores)

print("\n***************EXTEND(ITERABLE)***************")
print("\n- EJERCICIO 1")
numeros = [4, 5, 6]
numeros.extend(numeros)
print(numeros)

print("\n- EJERCICIO 2")
letras = ['a', 'b']
string='ok'
letras.extend(string)
print(letras)

print("\n***************REMOVE(X)***************")
print("\n- EJERCICIO 1")
frutas = ['manzana', 'uva', 'pera']
frutas.remove('uva')
print(frutas)

print("\n- EJERCICIO 2")
numeros = [1, 2, 3, 2]
numeros.remove(2)
print(numeros)

print("\n***************POP(I)***************")
print("\n- EJERCICIO 1")
numeros = [1, 2, 3, 4]
numeros.pop(3)
print(numeros)

print("\n- EJERCICIO 2")
numeros2 = ["uno", "dos", "tres"]
numeros2.pop(0)
print(numeros2)

print("\n***************CLEAR()***************")
print("\n- EJERCICIO 1")
numeros = [1, 2, 3]
numeros.clear()
print(numeros)

print("\n- EJERCICIO 2")
mi_lista = ["abcdefghijklmnopqrstuvwxyz", 97182, "Asus7#", True, 3.14159265368979]
mi_lista.clear()
print(mi_lista)

print("\n***************INDEX(X)***************")
print("\n- EJERCICIO 1")
frutas = ['manzana', 'pera', 'uva']
print(frutas.index('pera'))


print("\n- EJERCICIO 2")
numeros = [4, 5, 6, 7]
print(numeros.index(6))

print("\n***************COUNT(X)***************")
print("\n- EJERCICIO 1")
numeros = [3,1,3,5,3]
print(numeros.count(numeros))


print("\n- EJERCICIO 2")
letras = ['a', 'b', 'a', 'c', 'a']
print(letras.count('a'))

print("\n***************SORT()***************")
print("\n- EJERCICIO 1")
numeros = [5,1,4,2,3]
numeros.sort()
print(numeros)

print("\n- EJERCICIO 2")
letras = ["z", "a", "m", "b"]
letras.sort()
print(letras)

print("\n***************REVERSE()***************")
print("\n- EJERCICIO 1")
numeros = [1,2,3,4]
numeros.reverse()
print(numeros)

print("\n- EJERCICIO 2")
orden = ['inicio', 'medio', 'fin']
orden.reverse()
print(orden)

print("\n***************REVERSE()***************")
print("\n- EJERCICIO 1")
numeros = [1,2,3]
nueva_lista=numeros.copy()
print(nueva_lista)

print("\n- EJERCICIO 2")
letras = ['a', 'b', 'c']
nueva_lista=letras.copy()
nueva_lista.append('d')
print(nueva_lista)
print(letras)
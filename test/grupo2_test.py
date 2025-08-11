cantidad=int(input("Ingrese la cantidad de estudiantes: "))
i=0
print("")


estudiantes=[]
for i in range(cantidad):
    nombre= input("Ingresa el nombre del estudiante: ")
    notas= (float(input("Ingresa la primer nota: ")), float(input("Ingresa la segunda nota: ")), float(input("Ingresa la tercer nota: ")))
    promedio= sum(notas)/len(notas)
    situacion=""
    if promedio>=3.5:
        situacion="Aprobado"
    elif promedio>=2.5:
        situacion="En recuperacion"
    else:
        situacion="Reprobado"
    est1={
        "nombre": nombre,
        "notas": notas,
        "promedio": promedio,
        "situacion": situacion
    }
    estudiantes.append(est1)
    print("")
print(estudiantes)

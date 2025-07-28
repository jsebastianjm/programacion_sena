notas={
    "notas": (int(input("Ingresa 1ra nota: ")), int(input("Ingresa 2da nota: ")), int(input("Ingresa 3ra nota: "))),
    "pesos": (int(input("Ingresa el peso de la primera nota (En porcentaje): ")), int(input("Ingresa peso 2da nota: ")), int(input("Ingresa peso 3ra nota: ")))
}
nota1=notas["notas"][0]*(notas["pesos"][0]/100)
nota2=notas["notas"][1]*(notas["pesos"][1]/100)
nota3=notas["notas"][2]*(notas["pesos"][2]/100)
valores_finales=(nota1,nota2,nota3)
promedio=sum(valores_finales)
print(f"En promedio se saca un puntaje de {promedio}")
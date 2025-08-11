Algoritmo Condicionales_ejercicio5
	definir num,num2,num3 Como Real
	Escribir "Ingresa un numero"
	leer num
	escribir "Otro mas"
	leer num2
	escribir "Otro mas"
	leer num3
	Si num>num2 y num>num3 Entonces
		escribir num," es el mayor"
	Sino
		Si num2>num y num2>num3 Entonces
			escribir num2," es el mayor"
		SiNo
			Si num3>num y num3>num2 Entonces
				escribir num3," es el mayor"
			SiNo
				escribir "Todos son iguales"
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo

Algoritmo Condicionales_ejercicio10
	definir juan, pepito, laura Como Entero
	escribir "Ingresa un numero"
	leer juan
	escribir "Otro"
	leer pepito
	escribir "Otro"
	leer laura
	si juan%pepito==0 Entonces
		Si juan%laura==0 Entonces
			escribir juan," es divisible entre ",pepito," y ", laura
		SiNo
			escribir juan," es divisible entre ",pepito
		Fin Si
	SiNo
		Si juam%laura==0 Entonces
			escribir juan," es divisible entre ",laura
		SiNo
			escribir juan, " no es divisible entre esos numeros"
		Fin Si
	FinSi
FinAlgoritmo

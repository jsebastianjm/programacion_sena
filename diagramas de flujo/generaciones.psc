Algoritmo generaciones
	definir año como entero
	Escribir "Ingrese su año de nacimiento"
	Leer año
	Si año>=1920 y año<=1940 Entonces
		escribir "Es de la generacion silenciosa"
	SiNo
		Si año>=1941 y año<=1964 Entonces
			escribir "Es de la generacion baby boomer"
		SiNo
			Si año>=1965 y año<=1979 Entonces
				escribir "Es de la generacion X"
			SiNo
				Si año>=1980 y año<=2000 Entonces
					escribir "Es de la generacion Y"
				SiNo
					Si año>=2001 y año<=2010 Entonces
						escribir "Es de la generacion Z"
					SiNo
						escribir "Su edad no entra en ninguna de las generaciones registradas"
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo

Algoritmo generaciones
	definir a�o como entero
	Escribir "Ingrese su a�o de nacimiento"
	Leer a�o
	Si a�o>=1920 y a�o<=1940 Entonces
		escribir "Es de la generacion silenciosa"
	SiNo
		Si a�o>=1941 y a�o<=1964 Entonces
			escribir "Es de la generacion baby boomer"
		SiNo
			Si a�o>=1965 y a�o<=1979 Entonces
				escribir "Es de la generacion X"
			SiNo
				Si a�o>=1980 y a�o<=2000 Entonces
					escribir "Es de la generacion Y"
				SiNo
					Si a�o>=2001 y a�o<=2010 Entonces
						escribir "Es de la generacion Z"
					SiNo
						escribir "Su edad no entra en ninguna de las generaciones registradas"
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo

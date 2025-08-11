Algoritmo Condicionales_ejercicio8
	definir AAAAH Como Entero
	definir total como real
	escribir "Es VIP? (Si->Ingrese 1) (No->Ingrese 0)"
	leer AAAAH
	escribir "Ingrese el total de los gastos"
	leer total
	Si total>100 Entonces
		Si AAAAH==1 Entonces
			total<-total-(total*0.2)
		SiNo
			total<-total-(total*0.1)
		Fin Si	
	Fin Si
	escribir "El total queda en ",total
FinAlgoritmo

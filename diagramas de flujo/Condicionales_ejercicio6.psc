Algoritmo Condicionales_ejercicio6
	definir gastos Como Real
	escribir "Ingresa el total de los gastos"
	leer gastos
	Si gastos>100 Entonces
		gastos<-gastos-(gastos*0.1)
		escribir "Se le descuenta el 10%, queda en ",gastos
	SiNo
		"No tiene descuento"
	Fin Si
FinAlgoritmo

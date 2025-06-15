import calculadora_indices as calc
import funciones_importar as utils

peso = utils.pedir_float_positivo("Ingrese su peso en kg: ")
altura = utils.pedir_float_positivo("Ingrese su altura en metros: ")
edad = utils.pedir_int_positivo("Ingrese su edad: ")
genero = utils.pedir_genero()
valor_genero = 10.8 if genero == "m" else 0

grasa = calc.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)
print(f"Su porcentaje de grasa corporal es: {round(grasa, 2)}%")

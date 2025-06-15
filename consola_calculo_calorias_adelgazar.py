import calculadora_indices as calc
import funciones_importar as utils

peso = utils.pedir_float_positivo("Ingrese su peso en kg: ")
altura = utils.pedir_float_positivo("Ingrese su altura en metros: ")
edad = utils.pedir_int_positivo("Ingrese su edad: ")
genero = utils.pedir_genero()

valor_genero = 5 if genero == "m" else -161

rango = calc.consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero)
print(rango)

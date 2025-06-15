import calculadora_indices as calc
import funciones_importar as utils

peso = utils.pedir_float_positivo("Ingrese su peso en kg: ")
altura = utils.pedir_float_positivo("Ingrese su altura en metros: ")
edad = utils.pedir_int_positivo("Ingrese su edad: ")
genero = utils.pedir_genero()

valor_genero = 5 if genero == "m" else -161

tmb = calc.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
print(f"Su Tasa Metabólica Basal es: {round(tmb)} calorías al día")

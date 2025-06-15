import calculadora_indices as calc
import funciones_importar as utils

peso = utils.pedir_float_positivo("Ingrese su peso en kg: ")
altura = utils.pedir_float_positivo("Ingrese su altura en metros: ")

try:
    imc = calc.calcular_IMC(peso, altura)
    categoria = calc.clasificar_IMC(imc)
    print(f"Su IMC es: {round(imc, 2)} - Categoría: {categoria}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")
finally:
    print("Fin del cálculo del IMC.")
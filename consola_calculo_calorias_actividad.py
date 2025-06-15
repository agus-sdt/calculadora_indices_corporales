import calculadora_indices as calc
import funciones_importar as utils

peso = utils.pedir_float_positivo("Ingrese su peso en kg: ")
altura = utils.pedir_float_positivo("Ingrese su altura en metros: ")
edad = utils.pedir_int_positivo("Ingrese su edad: ")
genero = utils.pedir_genero()

print("Seleccione su nivel de actividad física:")
print("1. Poco o ningún ejercicio")
print("2. Ejercicio ligero (1-3 días/semana)")
print("3. Ejercicio moderado (3-5 días/semana)")
print("4. Deportista (6-7 días/semana)")
print("5. Atleta (entrenamientos mañana y tarde)")
op = int(input("Opción: "))

valor_genero = 5 if genero == "m" else -161
valores_actividad = {1: 1.2, 2: 1.375, 3: 1.55, 4: 1.72, 5: 1.9}
valor_actividad = valores_actividad.get(op, 1.2)

tmb_activa = calc.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)
print(f"Su consumo calórico con actividad es: {round(tmb_activa)} calorías al día")
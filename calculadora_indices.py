def calcular_IMC(peso, altura):
    return peso / (altura ** 2)

def clasificar_IMC(imc):
    if imc < 16:
        return "Delgadez severa"
    elif imc < 17:
        return "Delgadez moderada"
    elif imc < 18.5:
        return "Delgadez aceptable"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    elif imc < 35:
        return "Obesidad tipo I"
    elif imc < 40:
        return "Obesidad tipo II"
    elif imc < 50:
        return "Obesidad tipo III o mórbida"
    else:
        return "Obesidad tipo IV o extrema"

def calcular_porcentaje_grasa(peso, altura, edad, valor_genero):
    imc = calcular_IMC(peso, altura)
    valor_imc = 1.2 * imc
    valor_edad = 0.23 * edad
    porcentaje_gc = valor_imc + valor_edad - 5.4 - valor_genero
    return porcentaje_gc

def calcular_calorias_en_reposo(peso, altura, edad, valor_genero):
    altura_cm = altura * 100
    valor_peso = 10 * peso
    valor_altura = 6.25 * altura_cm
    valor_edad = 5 * edad
    tmb = valor_peso + valor_altura - valor_edad + valor_genero
    return tmb

def calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    tmb_actividad = tmb * valor_actividad
    return tmb_actividad

def consumo_calorias_recomendado_para_adelgazar(peso, altura, edad, valor_genero):
    tmb = calcular_calorias_en_reposo(peso, altura, edad, valor_genero)
    min_cal = tmb * 0.80
    max_cal = tmb * 0.85
    mensaje = f"Para adelgazar es recomendado que consumas entre: {round(min_cal)} y {round(max_cal)} calorías al día."
    return mensaje

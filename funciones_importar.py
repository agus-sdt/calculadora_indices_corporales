def pedir_float_positivo(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida. Ingrese un número decimal válido.")

def pedir_int_positivo(mensaje):
    while True:
        try:
            valor = int(input(mensaje))
            if valor > 0:
                return valor
            else:
                print("El número debe ser mayor que cero.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero válido.")

def pedir_genero():
    while True:
        genero = input("Ingrese su género (m/f): ").lower()
        if genero in ["m", "f"]:
            return genero
        print("Solo se admite 'm' para masculino o 'f' para femenino.")
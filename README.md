Objetivo: Diseñar un módulo que de funciones
Temática: A elección del Desarrollador
Modelo de Desarrollo:
- Título/Tema del Módulo
- Objetivo general
- Objetivos específicos
- Descripción de la aplicación
- Codificación de módulos e interfaces de usuario
- Pruebas del funcionamiento

Titulo: Modulo Calculadora de indices corporales

Objetivo general:
El objetivo general de este proyecto es crear una aplicación que permite hacer cálculos
de distintos índices corporales como el índice de masa corporal, la tasa metabólica basal, el gasto calórico según actividad física, y un rango de calorías recomendado para adelgazar.

Objetivos específicos:
1. CCrear funciones que realicen cálculos relacionados con la salud corporal.
2. Llamar funciones con parámetros.
3. Componer funciones, es decir, que una función utilice otra.
4. CCrear y utilizar un módulo en Python.
5. Probar las funciones del módulo creado.
6. Construir interfaces de usuario simples por consola para interactuar con el módulo.

Descripción de la Aplicación
Esta aplicación permite calcular diversos índices corporales que ayudan a comprender mejor el estado de salud física de una persona. 
Los cálculos incluyen:
- Índice de Masa Corporal (IMC): Relación entre peso y altura para determinar si una persona tiene un peso saludable.
- Porcentaje de Grasa Corporal (%GC): Estimación del porcentaje de grasa en el cuerpo, considerando edad, género e IMC.
- Tasa Metabólica Basal (TMB): Calorías mínimas necesarias para mantener funciones vitales en reposo.
- TMB con Actividad Física: Calorías quemadas considerando el nivel de actividad física semanal.
- Calorías recomendadas para adelgazar: Rango de calorías que una persona debería consumir si desea perder peso.

Codificación de módulos e interfaces de usuario:
- calculadora_indices.py: Módulo que contiene todas las funciones de cálculo.
- funciones_importar.py: Archivo que contiene funciones auxiliares para entrada de datos con manejo de excepciones:
    - pedir_float_positivo(): Solicita un número decimal positivo.
    - pedir_int_positivo(): Solicita un número entero positivo.
    - pedir_genero(): Solicita el género del usuario (m/f), validando la entrada.
- consola_calculo_imc.py: Interfaz de usuario para calcular el IMC.
- consola_calculo_porcentaje_grasa.py: Interfaz de usuario para calcular el % de grasa corporal.
- consola_calculo_calorias_reposo.py: Interfaz para calcular la TMB.
- consola_calculo_calorias_actividad.py: Interfaz para calcular la TMB según actividad física.
- consola_calculo_calorias_adelgazar.py: Interfaz para calcular el rango de calorías para adelgazar.

Pruebas del funcionamiento:
- interfaz_pruebas
    - consola_calculo_calorias_actividad.png
    - consola_calculo_calorias_adelgazar.png
    - consola_calculo_calorias_reposo.png
    - consola_calculo_imc.png
    - consola_calculo_porcentaje_grasa.png
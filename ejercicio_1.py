# Archivo: ejercicio_1.py
# Curso: SOFT-01 Principios de Programación 1
# Autor: Daniel Cordero Ramírez
# Fecha: 17/11/2026
# Versión: 1.0
# Descripción: Control de temperatura de cámara experimental

# Entrada
inicio = float(input("Temperatura inicial (°C): "))
objetivo = float(input("Temperatura objetivo (°C): "))
incremento = float(input("Incremento por ciclo (°C): "))

# Validación y proceso
if objetivo <= inicio:
    print("La temperatura objetivo debe superar la inicial.")
elif incremento <= 0:
    print("El incremento debe ser mayor que cero.")
else:
    temperatura_actual = inicio
    ciclos = 0
    while temperatura_actual < objetivo:
        temperatura_actual = temperatura_actual + incremento
        ciclos = ciclos + 1
        print("Ciclo", ciclos, "| Temperatura:", temperatura_actual, "°C")
    print("Temperatura final:", temperatura_actual, "°C")
    print("Total de ciclos:", ciclos)

# Archivo: ejercicio_4.py
# Curso: SOFT-01 Principios de Programación 1
# Autor: Daniel Cordero Ramírez
# Fecha: 17/11/2026
# Versión: 1.0
# Descripción: Control de abastecimiento de expedición

# Constantes e inventario inicial
AGUA_INICIAL = 150
ALIMENTO_INICIAL = 100
agua = AGUA_INICIAL
alimento = ALIMENTO_INICIAL
total_agua = 0
total_alimento = 0
dias_completados = 0

# Validar cantidad de jornadas
jornadas = int(input("Jornadas previstas (1 a 30): "))
while jornadas < 1 or jornadas > 30:
    print("Ingrese un número entre 1 y 30.")
    jornadas = int(input("Jornadas previstas (1 a 30): "))

# Recorrer jornadas planificadas
for dia in range(1, jornadas + 1):
    if agua == 0 or alimento == 0:
        break
    print("\nDía", dia, "| Agua:", agua, "L | Alimento:", alimento, "unidades")
    consumo_agua = int(input("Agua consumida (litros): "))
    while consumo_agua <= 0 or consumo_agua > agua:
        print("Consumo válido: mayor que cero y hasta", agua, "litros.")
        consumo_agua = int(input("Agua consumida (litros): "))
    consumo_alimento = int(input("Alimento consumido (unidades): "))
    while consumo_alimento <= 0 or consumo_alimento > alimento:
        print("Consumo válido: mayor que cero y hasta", alimento, "unidades.")
        consumo_alimento = int(input("Alimento consumido (unidades): "))
    agua = agua - consumo_agua
    alimento = alimento - consumo_alimento
    total_agua = total_agua + consumo_agua
    total_alimento = total_alimento + consumo_alimento
    dias_completados = dias_completados + 1
    print("Saldo | Agua:", agua, "L | Alimento:", alimento, "unidades")
    if (agua == 0 or alimento == 0) and dias_completados < jornadas:
        break

# Informe final
promedio_agua = total_agua / dias_completados
promedio_alimento = total_alimento / dias_completados
print("\nJornadas completadas:", dias_completados)
print("Agua consumida:", total_agua, "L | Restante:", agua, "L")
print("Alimento consumido:", total_alimento, "unidades | Restante:", alimento, "unidades")
print("Promedio de agua:", promedio_agua, "L por jornada")
print("Promedio de alimento:", promedio_alimento, "unidades por jornada")
if dias_completados == jornadas:
    print("Estado: expedición completada.")
else:
    print("Estado: expedición interrumpida por agotamiento de recursos.")

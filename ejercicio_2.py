# Archivo: ejercicio_2.py
# Curso: SOFT-01 Principios de Programación 1
# Autor: Daniel Cordero Ramírez
# Fecha: 17/11/2026
# Versión: 1.0
# Descripción: Registro semanal de consumo de agua

# Constantes y acumuladores
DIAS_SEMANA = 7
UMBRAL_LITROS = 150
consumo_total = 0.0
consumo_mayor = 0.0
dias_superan_umbral = 0

# Repetición de siete registros
for dia in range(1, DIAS_SEMANA + 1):
    consumo = float(input("Consumo del día " + str(dia) + " (litros): "))
    while consumo < 0:
        print("Ingrese un consumo igual o mayor que cero.")
        consumo = float(input("Consumo del día " + str(dia) + " (litros): "))
    consumo_total = consumo_total + consumo
    if consumo > consumo_mayor:
        consumo_mayor = consumo
    if consumo > UMBRAL_LITROS:
        dias_superan_umbral = dias_superan_umbral + 1

# Salida
promedio_diario = consumo_total / DIAS_SEMANA
print("Consumo total semanal:", consumo_total, "litros")
print("Promedio diario:", promedio_diario, "litros")
print("Mayor consumo:", consumo_mayor, "litros")
print("Días con consumo superior a 150 litros:", dias_superan_umbral)

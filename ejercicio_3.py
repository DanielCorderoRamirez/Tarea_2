# Archivo: ejercicio_3.py
# Curso: SOFT-01 Principios de Programación 1
# Autor: Daniel Cordero Ramírez
# Fecha: 17/11/2026
# Versión: 1.0
# Descripción: Administración de estacionamiento privado

# Constantes y estado inicial
CAPACIDAD = 20
TARIFA_HORA = 800
ocupacion = 0
salidas = 0
recaudacion = 0

# Menú repetitivo
while True:
    print("\n1. Registrar ingreso")
    print("2. Registrar salida")
    print("3. Consultar ocupación")
    print("4. Consultar recaudación")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        if ocupacion < CAPACIDAD:
            ocupacion = ocupacion + 1
            print("Ingreso registrado. Ocupación:", ocupacion)
        else:
            print("Estacionamiento lleno. Capacidad:", CAPACIDAD)
    elif opcion == "2":
        if ocupacion > 0:
            horas = int(input("Horas enteras por cobrar: "))
            while horas <= 0:
                print("Las horas deben ser mayores que cero.")
                horas = int(input("Horas enteras por cobrar: "))
            pago = horas * TARIFA_HORA
            ocupacion = ocupacion - 1
            salidas = salidas + 1
            recaudacion = recaudacion + pago
            print("Salida registrada. Pago: ₡", pago)
        else:
            print("Estacionamiento vacío. Sin salidas para registrar.")
    elif opcion == "3":
        print("Ocupados:", ocupacion, "| Libres:", CAPACIDAD - ocupacion)
    elif opcion == "4":
        print("Recaudación: ₡", recaudacion, "| Salidas:", salidas)
    elif opcion == "5":
        print("Resumen final | Ocupación:", ocupacion,
              "| Salidas:", salidas, "| Recaudación: ₡", recaudacion)
        break
    else:
        print("Opción inválida. Intente nuevamente.")

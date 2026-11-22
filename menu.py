"""Laboratorio de Python: match case.

Incluye la Parte A (días y notas), la Parte B (calculadora con
menú sin ciclos) y el reto (conversor de temperatura sin ciclos).
Requiere Python 3.10 o superior.
"""

# ============================================================
# PARTE A - EJERCICIO 1: CLASIFICADOR DE DÍAS
# ============================================================
print("\n=== CLASIFICADOR DE DÍAS ===")
dia = int(input("Ingresa un número de día (1-7): "))

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6 | 7:
        print("Fin de semana")
    case _:
        print("Número de día no válido")

# ============================================================
# PARTE A - EJERCICIO 2: CLASIFICADOR DE NOTAS (GUARDAS)
# ============================================================
print("\n=== CLASIFICADOR DE NOTAS ===")
nota = int(input("Ingresa tu nota (0-100): "))

match nota:
    case n if n < 0 or n > 100:
        print("Nota fuera de rango")
    case n if n >= 90:
        print("Excelente")
    case n if n >= 70:
        print("Aprobado")
    case _:
        print("Reprobado")

# ============================================================
# PARTE B - CALCULADORA CON MENÚ SIN CICLOS
# ============================================================
print("\n===== CALCULADORA =====")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")
print("=======================")

opcion = input("Elige una opción (1-5): ").strip()

match opcion:
    case "1" | "2" | "3" | "4":
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))

        match opcion:
            case "1":
                print("Resultado:", a + b)
            case "2":
                print("Resultado:", a - b)
            case "3":
                print("Resultado:", a * b)
            case "4":
                if b == 0:
                    print("Error: no se puede dividir entre cero")
                else:
                    print("Resultado:", a / b)
    case "5":
        print("Saliendo de la calculadora. ¡Hasta luego!")
    case _:
        print("Opción no válida")

# ============================================================
# RETO FINAL - CONVERSOR DE TEMPERATURA SIN CICLOS
# ============================================================
print("\n===== CONVERSOR DE TEMPERATURA =====")
print("1. Celsius a Fahrenheit")
print("2. Fahrenheit a Celsius")
print("3. Salir")
print("====================================")

opcion_temperatura = input("Elige una opción (1-3): ").strip()

match opcion_temperatura:
    case "1":
        celsius = float(input("Temperatura en Celsius: "))
        fahrenheit = celsius * 9 / 5 + 32
        print(f"{celsius:.2f} °C = {fahrenheit:.2f} °F")
    case "2":
        fahrenheit = float(input("Temperatura en Fahrenheit: "))
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit:.2f} °F = {celsius:.2f} °C")
    case "3":
        print("Saliendo del conversor. ¡Hasta luego!")
    case _:
        print("Opción no válida")

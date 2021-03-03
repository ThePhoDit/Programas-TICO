# Convertir una temperatura dada en Fahrenheit a Celsius y Kelvin.

# Usamos float() porque queremos números con decimales. Si no se introduce un número, dará error.
fahrenheit = float(input("Introduce la temperatura en Fahrenheit:\n"))

# Usamos las funciones para la conversión.
celsius = 5 * (fahrenheit - 32) / 9
kelvin = celsius + 273

print(f"La temperatura en Celsius es de {celsius} grados y en Kelvin es de {kelvin} grados.")
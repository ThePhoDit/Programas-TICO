# Calcular el dinero total en base a la cantidad de monedas de cada tipo.

# Usamos int() para que los números sean enteros. No hay "una moneda y media".
a = int(input("Introduce la cantidad de monedas de 2 euros:\n"))
b = int(input("Introduce la cantidad de monedas de 1 euro:\n"))
c = int(input("Introduce la cantidad de monedas de 50 céntimos:\n"))
d = int(input("Introduce la cantidad de monedas de 20 céntimos:\n"))
e = int(input("Introduce la cantidad de monedas de 10 céntimos:\n"))

total = a * 200 + b * 100 + c * 50 + d * 20 + e * 10 # El resultado son céntimos.

# El operador % nos devuelve el resto de la división.
print(f"En total hay {str(int(total / 100))}.{str(total % 100)} euros.")
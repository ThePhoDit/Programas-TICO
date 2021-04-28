number = int(input("Introduce el número deseado:\n"))

factorial = 1
sumatorio = 0

for i in range (number):
	factorial *= i + 1
	sumatorio += i + 1

print(f"El sumatorio es {sumatorio} y el factorial es {factorial}")
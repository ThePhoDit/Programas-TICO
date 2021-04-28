def factorial(number):
	if number == 1:
		return 1
	return number * factorial(number - 1)

def sumatorio(number):
	if number == 1:
		return 1
	return number + sumatorio(number - 1)

number = int(input("Introduce el número deseado:\n"))
print(f"El sumatorio es {sumatorio(number)} y el factorial es {factorial(number)}")
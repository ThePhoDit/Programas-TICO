def factorial(number):
	if number == 1:
		return 1
	return number * factorial(number - 1)

time = float(input("Introduce el tiempo:\n"))
total = 1

for i in range(10):
	total += ((0.0289 * time) ** (i + 1)) / factorial(i + 1)

print(total)
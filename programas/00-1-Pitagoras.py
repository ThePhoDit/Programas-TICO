# Calcular el área y preímetro de un triángulo rectángulo por su base y altura.

"""
Antes de nada, esto es un comentario. Es dcir, un trozo de código que no se ejecuta. Se puede encontrar así o con # delante.
En todos los lenguajes es importante distinguir entre números y texto.
	Los números pueden ser enteros (integers): 2
	O pueden ser decimales (floats): 2.5

	El texto (strings) son todos ellos que van entre comillas: '2'

	Es importante la diferencia porque 2 + 2 = 4 pero '2' + '2' = '22'

Algunas funciones importantes son:
	str() => El número (integer o float) que pongas dentro se convierte a texto (string).
	int() => El texto que le pases (siempre que dentro solo tenga numeros) se convierte a un número (se ignoran los decimales).
	float() => Igual que int() pero tiene en cuenta decimales.
"""

# Asignar los datos a variables. Como la fun ción input() devuelve un string, usamos int() para convertirlo a un número.
# Si queremos usar números con decimales, hay que usar float() en vez de int().
# \n significa "nueva línea"
base = int(input("Introduce la base del triángulo:\n")) 	# El input() va dentro del int() para convertir a un integer la respuesta, que es un string.
altura = int(input("Introduce la altura del triángulo:\n")) # Si se introduce algo que no es un número, dará error.

"""
Ahora se realizan las operaciones. Las principales son:
	+ => suma
	- => resta
	* => multiplicación
	/ => división
	** => Exponenciación - Elevar a un número.
"""
hipotenusa = (base ** 2 + altura ** 2) ** 0.5 # Para hacer la raíz, se eleva a 1/2 = 0.5. Hay que tener en cuenta la jerarquía de operaciones, po eso se ponen paréntesis.
area = base * altura / 2 					  # Algo a tener en cuenta es que las variables no deben tener tildes ni espacios.
perimetro = base + altura + hipotenusa

"""
Ahora se imprime el resultado en la pantalla.
Si se pone una 'f' delante de las comillas, nos permite poner variables en medio del texto mediante las llaves {} como se ve debajo.
Además, como imprimimos texto, hay que convertir los números (integers) a texto (string) => str()
"""
print(f"El perímetro es {str(perimetro)} y el área es {str(area)}.")
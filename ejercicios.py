#Ejercicio 1:
#materia y quiere saber cuál es su promedio.
#Un estudiante está cursando 5 materias, tiene la nota de cada
nota1 = int(input("Ingrese la nota de la materia 1: "))
nota2 = int(input("Ingrese la nota de la materia 2: "))
nota3 = int(input("Ingrese la nota de la materia 3: "))
nota4 = int(input("Ingrese la nota de la materia 4: "))
nota5 = int(input("Ingrese la nota de la materia 5: "))

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("El promedio de las notas es:", promedio)

#Ejericio 2:
#Un pintor de casas debe hacer un presupuesto para un cliente. Lo
#que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El
#cliente le indica que necesita conocer el costo de mano de obra para pintar una
#pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro
#cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para
#pintar la pared.

alto = float(input("Ingrese la altura de la pared en metros: "))
ancho = float(input("Ingrese el ancho de la pared en metros: "))
costo_por_metro_cuadrado = float(input("Ingrese el costo por metro cuadrado en moneda local: "))
area = alto * ancho
costo_total = area * costo_por_metro_cuadrado
print("El costo total de mano de obra para pintar la pared es:", costo_total)

#Ejercicio 3:
#Un hincha de fútbol desea conocer la cantidad de puntos que su
#equipo lleva acumulados en el campeonato, para ello recibe cada semana la
#información de la cantidad total de partidos, desde el inicio del campeonato, que
#el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado
#recibe un punto, por cada partido ganado tres puntos y por los perdidos cero
#puntos.

partidos_ganados = int(input("Ingrese la cantidad de partidos ganados: "))
partidos_empatados = int(input("Ingrese la cantidad de partidos empatados: "))
partidos_perdidos = int(input("Ingrese la cantidad de partidos perdidos: "))
puntos_ganados = partidos_ganados * 3
puntos_empatados = partidos_empatados * 1
puntos_perdidos = partidos_perdidos * 0
puntos_totales = puntos_ganados + puntos_empatados + puntos_perdidos
print("El equipo ha acumulado", puntos_totales, "puntos en el campeonato.")

#ESTRUCTURAS CONDICIONALES:

#1. Condicional parcial (solo el if) con expresión lógica simple
# IF 
numero = float(input("Ingrese un número: "))
if numero > 0:
    print("El número es positivo.")

#2. Condicional completo (if - else) con expresión lógica simple

numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

#3. Condicional parcial (solo el if) con expresión lógica compuesta (and)


numero = float(input("Ingrese un número: "))
if 10 <= numero <= 20:
    print("El número está en el rango de 10 a 20.")

#4. Condicional completo (if - else) con expresión lógica compuesta (or)


numero = float(input("Ingrese un número: "))
if numero < 0 or numero > 100:
    print("El número es negativo o mayor que 100.")
else:
    print("El número está entre 0 y 100.")



cantidad = int(input("Ingrese la cantidad de leche a comprar: "))
es_jubilado = input("¿Es jubilado? (si/no): ").strip().lower()
costo_unitario = 1000
descuento = 0
if cantidad > 24:
    descuento = 0.15
elif cantidad > 12:
    descuento = 0.10
if es_jubilado == "si":
    descuento += 0.10
costo_total = cantidad * costo_unitario * (1 - descuento)
print("El costo total a pagar es:", costo_total)

#ESTRUCTURAS ITERATIVAS:

# Mostrar los números desde el 0 al número solicitado al usuario
numero = int(input("Ingrese un número: "))
for i in range(numero + 1):
    print(i)

# Mostrar solo los números pares desde 0 hasta el número ingresado
numero = int(input("Ingrese un número: "))
for i in range(numero + 1):
    if i % 2 == 0:
        print(i)

# Pedir que el usuario ingrese nombres de personas y mostrarlos hasta que ingrese “fin”
while True:
    nombre = input("Ingrese un nombre (o 'fin' para terminar): ")
    if nombre.lower() == 'fin':
        break
    print(nombre)

# Calcular el promedio de notas de un curso y determinar el rendimiento
num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
suma_notas = 0
for _ in range(num_estudiantes):
    nota = float(input("Ingrese la nota del estudiante: "))
    suma_notas += nota

promedio = suma_notas / num_estudiantes

if promedio > 8:
    print("Rendimiento elevado")
elif 6 <= promedio <= 8:
    print("Rendimiento aceptable")
else:
    print("Rendimiento bajo")

# Generar la tabla de multiplicar de un número utilizando mientras
numero = int(input("Ingrese un número entre 1 y 10: "))
i = 1
while i <= 10:
    print(f"{numero}x{i}={numero * i}")
    i += 1

# Generar la tabla de multiplicar de un número utilizando para
numero = int(input("Ingrese un número entre 1 y 10: "))
for i in range(1, 11):
    print(f"{numero}x{i}={numero * i}")
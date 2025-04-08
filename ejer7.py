#Intercambiar valor de dos variables numericas usando auxiliar
a = int(input("Ingrese el valor de la primera variable (a): "))
b = int(input("Ingrese el valor de la segunda variable (b): "))

print(f"Valores originales: a = {a}, b = {b}")
aux = a
a = b
b = aux
print(f"Valores intercambiados: a = {a}, b = {b}")
#Calcular salario de u empleado
salario_actual = float(input("Ingrese el salario actual: "))
incremento = 0.08
descuento_servicios = 0.025
nuevo_salario = (salario_actual * (1 + incremento)) * (1 - descuento_servicios)

print(f"Nuevo salario después de aumento y descuento: {nuevo_salario:.2f}")
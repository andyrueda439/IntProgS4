#Calcular el salario de un trabajador
nombre_trabajador = input("Nombre del trabajador: ")
horas_trabajadas = float(input("Horas trabajadas: "))
precio_por_hora = float(input("Precio por hora: "))
sueldo_bruto = horas_trabajadas * precio_por_hora
renta = sueldo_bruto * 0.05
sueldo_neto = sueldo_bruto - renta

print(f"Nombre: {nombre_trabajador}")
print(f"Sueldo bruto: C${sueldo_bruto:.2f}")
print(f"Descuento de renta (5%): C${renta:.2f}")
print(f"Sueldo neto a pagar: C${sueldo_neto:.2f}")
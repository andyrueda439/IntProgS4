#Determinar tiempo promedio que la persona se tarda en correr
print("Ingrese los tres tiempos (en minutos):")
tiempo1 = float(input("Lunes: "))
tiempo2 = float(input("Miércoles: "))
tiempo3 = float(input("Viernes: "))
tiempo_promedio = (tiempo1 + tiempo2 + tiempo3) / 3

print(f"Tiempo promedio: {tiempo_promedio:.2f} minutos")
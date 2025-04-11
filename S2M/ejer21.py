#Calcular numero de pulsaciones
edad = int(input("Ingrese su edad: "))
pulsaciones = (220 - edad) / 10

print(f"Número de pulsaciones por cada 10 segundos: {pulsaciones:.2f}")
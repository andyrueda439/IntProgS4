#Calcular cuanto de propina dejar
total_cuenta = float(input("Total de la cuenta: "))
porcentaje_propina = float(input("Porcentaje de propina (%): ")) / 100
propina = total_cuenta * porcentaje_propina

print(f"Propina: {propina:.2f}")
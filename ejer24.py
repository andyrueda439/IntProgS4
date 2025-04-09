#Obtener la cantidad de dinero que recibirá cada área
presupuesto_total = float(input("Ingrese el presupuesto anual del hospital: "))
urgencias = presupuesto_total * 0.37
pediatria = presupuesto_total * 0.42
traumatologia = presupuesto_total * 0.21

print(f"Urgencias: C${urgencias:.2f}")
print(f"Pediatría: C${pediatria:.2f}")
print(f"Traumatología: C${traumatologia:.2f}")
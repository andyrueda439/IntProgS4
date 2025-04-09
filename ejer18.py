#Calcular calificacion final
tareas = float(input("Nota de tareas (sobre 100): "))
ex_parcial = float(input("Nota de examen parcial (sobre 100): "))
ex_final = float(input("Nota de examen final (sobre 100): "))
calificacion_final = (tareas * 0.3) + (ex_parcial * 0.3) + (ex_final * 0.4)

print(f"Calificación final: {calificacion_final:.2f}")
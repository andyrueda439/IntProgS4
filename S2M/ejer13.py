#Calcular porcentaje de mujeres y varone en un aula
mujeres = int(input("Cantidad de mujeres en el aula: "))
varones = int(input("Cantidad de varones en el aula: "))
total_estudiantes = mujeres + varones
porcentaje_mujeres = (mujeres / total_estudiantes) * 100
porcentaje_varones = (varones / total_estudiantes) * 100

print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
print(f"Porcentaje de varones: {porcentaje_varones:.2f}%")
#Solicitar datos y porcentaje y luego demostrar
nombre_producto = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
descuento = float(input("Porcentaje de descuento (%): ")) / 100
precio_final = precio * (1 - descuento)

print(f"{nombre_producto}: Precio final con descuento: {precio_final:.2f}")
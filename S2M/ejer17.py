#Solicitar el precio y mostrar
precio1 = float(input("Precio del primer producto: "))
precio2 = float(input("Precio del segundo producto: "))
precio3 = float(input("Precio del tercer producto: "))
subtotal = precio1 + precio2 + precio3
iva = subtotal * 0.15
total = subtotal + iva

print(f"Subtotal: {subtotal:.2f}")
print(f"IVA (15%): {iva:.2f}")
print(f"Total a pagar: {total:.2f}")
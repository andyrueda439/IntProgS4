#Pedir datos y mostrar posible correo
nombre = input("Nombre: ")
apellido = input("Apellido: ")
correo = f"{nombre.lower()}.{apellido.lower()}@uamv.edu.ni"

print(f"Correo posible: {correo}")
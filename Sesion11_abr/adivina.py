#adivinar un numero
import random

numero_secreto = random.randint(1,10)
while(True):
    numero_usuario = int(input("Dime un numero del 1 al 10: "))
    if(numero_secreto == numero_usuario):
        print(f"Felicidades, adivinaste el numero: {numero_secreto}")
        break
    else:
        print("Sigue intentando")
    if(numero_usuario > numero_secreto):
        print("Ek numero es menor")
    else:
        print("El numero es mayor") 
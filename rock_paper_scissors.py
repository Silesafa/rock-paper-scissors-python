
import random

def juego():
    # Opciones de juego
    opciones = ["piedra", "papel", "tijera"]

    # Jugador elige opción
    jugador = input("Elige: piedra, papel o tijera: ").lower()

    if jugador not in opciones:
        print("Debes elegir una opción válida")
        return

    # Computadora elige opción
    computadora = random.choice(opciones)

    # Mostrar elecciones
    print(f"Tu elección: {jugador}")
    print(f"La computadora eligió: {computadora}")

    # Determinar resultado
    if jugador == computadora:
        print("Empate")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "papel" and computadora == "piedra") or \
         (jugador == "tijera" and computadora == "papel"):
        print("¡Eres el ganador!")
    else:
        print("Perdiste!")

# Bucle del juego
print("Hola... Vamos a jugar piedra, papel o tijera")

while True:
    juego()
    # Preguntar si quiere jugar de nuevo
    jugar_de_nuevo = input("¿Quieres jugar otra vez? (si/no): ").lower()
    if jugar_de_nuevo != "si":
        print("Gracias por jugar, nos vemos")
        break





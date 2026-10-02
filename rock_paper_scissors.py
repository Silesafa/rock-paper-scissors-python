
import random
 
 
def juego():
# Opciones disponibles
opciones = ["piedra", "papel", "tijera"]
 
# Jugador elige una opción
jugador = input("Elige: piedra, papel o tijera: ").lower()
 
if jugador not in opciones:
print("Debes elegir una opción válida.")
return
 
# Computadora elige una opción aleatoria
computadora = random.choice(opciones)
 
print(f"Tu elección: {jugador}")
print(f"La computadora eligió: {computadora}")
 
# Determinar resultado
if jugador == computadora:
print("Empate.")
elif (
(jugador == "piedra" and computadora == "tijera")
or (jugador == "papel" and computadora == "piedra")
or (jugador == "tijera" and computadora == "papel")
):
print("¡Eres el ganador!")
else:
print("¡Perdiste!")
 
 
def main():
print("Hola... Vamos a jugar piedra, papel o tijera.")
 
while True:
juego()
 
jugar_de_nuevo = input(
"¿Quieres jugar otra vez? (si/no): "
).lower()
 
if jugar_de_nuevo != "si":
print("Gracias por jugar, nos vemos.")
break
 
 
if __name__ == "__main__":
main()

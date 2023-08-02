import random

def adivina_el_numero():
    # Generamos un número aleatorio entre 1 y 100 (puedes ajustar los límites según tu preferencia).
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido al juego de adivinar el número secreto!")
    print("He elegido un número entre 1 y 100. ¡Adivina cuál es!")

    while True:
        try:
            # Pedimos al usuario que ingrese un número como intento.
            intento = int(input("Ingresa tu intento: "))
        except ValueError:
            # Si el usuario ingresa algo que no es un número, mostramos un mensaje de error y continuamos el ciclo.
            print("Por favor, ingresa un número válido.")
            continue

        intentos += 1

        if intento == numero_secreto:
            # Si el intento es igual al número secreto, felicitamos al usuario y mostramos la cantidad de intentos que tomó.
            print(f"¡Felicidades! ¡Has adivinado el número secreto {numero_secreto} en {intentos} intentos!")
            break
        elif intento < numero_secreto:
            # Si el intento es menor que el número secreto, indicamos al usuario que el número secreto es mayor y pedimos un nuevo intento.
            print("El número secreto es mayor. Intenta de nuevo.")
        else:
            # Si el intento es mayor que el número secreto, indicamos al usuario que el número secreto es menor y pedimos un nuevo intento.
            print("El número secreto es menor. Intenta de nuevo.")

if __name__ == "__main__":
    # Llamamos a la función principal para comenzar el juego.
    adivina_el_numero()

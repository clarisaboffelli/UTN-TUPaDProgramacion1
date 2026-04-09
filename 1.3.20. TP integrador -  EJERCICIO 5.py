# Ejercicio 5 — “Escape Room:"La Arena del Gladiador"
# Detallar el nombre y objetivo del juego
print("Escape Room: LA ARENA DEL GLADIADOR")
print("El Gladiador se enfrenta contra el Enemigo. Reduce los puntos de vida del oponente a cero antes de que él lo haga contigo!")
print()
gladiador = input("Gladiador, ingresa tu nombre: ").strip().upper()
while not (gladiador.isalpha()):
    print("Cuidado Gladiador! Solo se permiten letras.")
    gladiador = input("Gladiador, vuelve a ingresar tu nombre: ").strip().upper()
print(f"Gladiador ha elegido el glorioso nombre de {gladiador}.")
# Detallar los valores iniciales de las variables.
vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True
# Establecer un ciclo while: el juego entra en un ciclo que se repite mientras ambos combatientes tengan más de 0 puntos de vida.
print()
while (vida_enemigo > 0 and vida_gladiador > 0):
    if turno_gladiador:
        print(f"Es el turno de {gladiador}.")
        print(f"El Gladiador {gladiador} tiene {vida_gladiador} puntos de vida.")
        print(f"El Enemigo tiene {vida_enemigo} puntos de vida.")
        print(f"Te quedan {pociones_vida} pociones de vida.")
        # Empieza el Gladiador.
        while True:
            print("""
                1. Ataque pesado.
                2. Rafaga veloz.
                3. Curar.
                """)
            opcion = input("Gladiador, elige una acción: ").strip()
            while not (opcion.isdigit() and ((int(opcion) > 0) and (int(opcion) < 4))):
                print("Gladiador, las acciones disponibles son 1, 2 o 3.") 
                opcion = input("Ingresa una de ellas para continuar la batalla: ").strip()
            match opcion:
                case "1":
                    print("Ataque pesado contra el rival!")
                    danio = ataque_pesado
                    if vida_enemigo < 20:
                        danio = danio*1.5
                    vida_enemigo = vida_gladiador-danio
                    print(f"Atacaste al enemigo por {danio} puntos de daño!")
                    print()
                    break
                case "2":
                    print("Rafaga veloz contra el rival!")
                    for i in range(3):
                        vida_enemigo -= 5
                        print("> Golpe conectado por 5 de daño.")
                    print()
                    break
                case "3":
                    if pociones_vida > 0:
                        vida_gladiador += 30
                        pociones_vida -= 1
                    else:
                        print("No quedan pociones!")
                        print("Perdiste el turno!")
                    print()
                    break
        turno_gladiador = False
    else:
        print("Es el turno del Enemigo!")
        vida_gladiador = vida_gladiador - ataque_enemigo
        print("El enemigo te ataco por 12 puntos de daño!")
        turno_gladiador = True
        print()
if vida_gladiador > 0:
    print(f"VICTORIA! {gladiador} ha ganado la batalla!")
else:
    print(f"DERROTA! Has caido en combate!")
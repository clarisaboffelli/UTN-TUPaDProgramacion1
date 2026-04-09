# Ejercicio 4 — “Escape Room: La Bóveda”
# Insertar descripcion del juego
print("ESCAPE ROOM LA BOVEDA")
print()
print("""Eres un agente que intenta abrir una bóveda con 3 cerraduras. 
Tienes energía y tiempo limitados. 
Si abres las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganas.
""")
# Ingresamos las variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
total_cerraduras = 0
alarma = False
codigo_parcial = ""
# Con respecto a la alarma, entiendo que si se dispara el jugador pierde, asi que no inclui la condicionde que si la alarma == True y el tiempo <= 3, y la boveda no esta abierta se pierde, porque con solo la alarma es suficiente para perder.
# Contador de veces que forzo la cerradura. Se suma cuando se usa la opcion 1 y vuelve a 0 en las otras.
cont = 0
# Solicitamos nombre del agente y validamos
agente = input("Ingrese el nombre del agente: ").strip().lower()
while not agente.replace(" ", "").isalpha():
    print("Solo se admiten caracteres alfabeticos.")
    agente = input("Por favor, ingrese un nuevo nombre: ").strip().lower()
print(f"Hola agente {agente}, gracias por unirte a esta misión!")
# Detallar los recursos iniciales:
print("""Recursos iniciales:
Energia = 100
Tiempo = 12
""")
# Usar un ciclo while para dar continuidad al juego mostrando el menu.
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False:
    print("""Menú de acciones:
1. Forzar cerradura (energia -20, tiempo -2)
2. Hackear panel (energía -10, tiempo -3)
3. Descansar (energía + 15 (maximo 100), tiempo -1, si alarma ON energía -10)
""")
    # Ingresar la opcion y validarla
    opcion = input("Elige la acción!: ").strip()
    while not (opcion.isdigit() and (int(opcion) > 0 and int(opcion) <4)):
        opcion = input("Ingreso no válido. Ingresar cualquiera 1, 2, o 3: ").strip()
    # Al finalizar cada opcion debo evaluar las condiciones de victoria o derrota.
    match opcion:
        case "1":
            print("Forzar cerradura!")
            # Actualizo las variables
            energia -= 20
            tiempo -= 2
            cont += 1
            if cont == 3:
                print("No intentes forzar la cerradura tantas veces segidas! La cerradura se trabó!")
                alarma = True
            else:
                if energia < 40:
                    print(f"Tienes poca energia ({energia}), hay riesgo de alarma!")
                    numero = input("Rápido!, elige un numero entre 1,2 y 3: ").strip()
                    while not (numero.isdigit() or 1 <= numero <=3):
                        numero = input("No tenemos tiempo para errores! Elije un número entre 1, 2 y 3!: ").strip()
                    if numero == 3:
                        alarma = True
                    else:
                        pass
                else:
                    cerraduras_abiertas += 1
                    print(f"Abriste 1 cerradura. Quedan {3-cerraduras_abiertas} cerraduras por abrir.")
            print(f"Energia restante = {energia} - Tiempo restante = {tiempo}")
            print()
        case "2":
            print("Hackear panel!")
            cont = 0
            energia -= 10
            tiempo -=3
            for i in range(1,5):
                codigo_parcial += "A"
                if len(codigo_parcial)== 8:
                    cerraduras_abiertas += 1
                    print(f"Abriste 1 cerradura. Quedan {3-cerraduras_abiertas} cerraduras por abrir.")
                elif len(codigo_parcial)== 16:
                    cerraduras_abiertas += 1
                    print(f"Abriste 1 cerradura. Quedan {3-cerraduras_abiertas} cerraduras por abrir.")
                elif len(codigo_parcial) == 24:
                    cerraduras_abiertas += 1
                    print(f"Abriste 1 cerradura. Quedan {3-cerraduras_abiertas} cerraduras por abrir.")
            print(f"Energia restante = {energia} - Tiempo restante = {tiempo}")
            print()
        case "3":
            print("Descansar.")
            cont = 0
            if energia >= 100:
                energia += 0
                tiempo -=1
            elif energia < 100 and alarma == False:
                energia += 15
                tiempo -=1
            # La siguiente opcion la puse pero si la alarma es True y se le dio ese valor antes, ya dispararia el fin del juego. La dejo porque encontre la consigna un poco ambigua.
            elif energia < 100 and alarma == True:
                energia += 5
                tiempo -=1
            print(f"Energia restante = {energia} - Tiempo restante = {tiempo}")
            print()
if cerraduras_abiertas == 3 and energia > 0 and tiempo > 0 :
    print("VICTORIA! Has conseguido escapar de la bóveda!")
elif alarma == True and tiempo <= 3:
    print("DERROTA! La alarma te ha bloquedo")
elif energia <= 0 or tiempo <= 0: 
    print("DERROTA! Te has quedado sin recursos.")
elif alarma == True:
    print("DERROTA! Has disparado la alarma.")
# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
# Definir la cantidad de turnos como constantes e igualarlas al principio con las variables para ir restando a medida que se ocupen.
TURNOS_LUNES = 4
turnos_lunes = TURNOS_LUNES
TURNOS_MARTES = 3
turnos_martes = TURNOS_MARTES
TURNOS_TOTALES = 7
turnos_ocupados = 0

# Establcer los pacientes:
nombre_lunes1 = "LIBRE"
nombre_lunes2 = "LIBRE"
nombre_lunes3 = "LIBRE"
nombre_lunes4 = "LIBRE"
nombre_martes1 = "LIBRE"
nombre_martes2 = "LIBRE"
nombre_martes3 = "LIBRE"
# Establecer un numbre inicial para comparacion.
NOMBRE_LUNES = "xxxxxx"
NOMBRE_MARTES = "xxxxxx"
# Solicitar nombre del operador que solo acepte letras.
operador = input("Ingrese su nombre: ").strip()
while not operador.replace(" ", "").isalpha():
    print("El nombre del operador debe contener solo caracteres alfabeticos.")
    operador = input("Ingrese el operador: ").strip()

print(f"El operador es {operador}.")
# Crear una lista con match case y validar los ingresos mientra haya turnos disponibles.
print()
while turnos_ocupados <= TURNOS_TOTALES:
        print("Seleccione una opcion del menu.")
        print("""Menu:
        1. Reservar turno.
        2. Cancelar turno.
        3. Ver agenda del día.
        4. Ver resumen general.
        5. Cerrar sistema.
        """)
        opcion = input("Opción: ").strip()
        while not opcion.isdigit():
            opcion = input("Ingresar una opción válida (1 a 5): ").strip()
        match opcion:
            case "1":
                print("Reserva de turno.")
                print(""" Seleccione el día:
                1. Lunes.
                2. Martes.
                """)
                dia = input("Ingrese el número correspondiente al día: ").strip()
                while not dia.isdigit():
                    dia = input("Ingrese una opción válida (1 o 2): ").strip()
                match dia:
                    case "1":
                        # Antes de asignar un turno el lunes, confirmo la disponibilidad.
                        if 1 <= turnos_lunes <= TURNOS_LUNES:
                            print("Usted seleccionó el día Lunes.")
                            print()
                            nombre_lunes = input("Ingrese el nombre del paciente: ").strip().lower()
                            # Validamos que el nombre sea un texto.
                            while not nombre_lunes.replace(" ", "").isalpha():
                                nombre_lunes = input("Ingrese el nombre del paciente solo con caracteres alfabéticos: ").strip().lower()
                            # Validamos que el turno no se repita
                            if nombre_lunes == NOMBRE_LUNES or nombre_lunes == nombre_lunes1 or nombre_lunes == nombre_lunes2 or nombre_lunes == nombre_lunes3 or nombre_lunes == nombre_lunes4:
                                print("Ya posee un turno para este día.")
                            else:
                                if nombre_lunes1 == "LIBRE":
                                    print("Su turno quedo registrado para el día lunes en la hora 10:00.")
                                    # Resto un tunro del lunes, y la constante cambia para que el nuevo nombre a comparar sera el registrado. 
                                    # Surge el problema de si el paciente ingresa nuevamente, su nombre no queda acumulado sino que ya se reemplazo por el ultimo paciente que entro.
                                    turnos_lunes -=1
                                    turnos_ocupados +=1
                                    nombre_lunes1 = nombre_lunes
                                elif nombre_lunes2 == "LIBRE":
                                    print("Su turno quedo registrado para el día lunes en la hora 10:30.")
                                    # Resto un tunro del lunes, y la constante cambia para que el nuevo nombre a comparar sera el registrado. 
                                    # Surge el problema de si el paciente ingresa nuevamente, su nombre no queda acumulado sino que ya se reemplazo por el ultimo paciente que entro.
                                    turnos_lunes -=1
                                    turnos_ocupados +=1
                                    nombre_lunes2 = nombre_lunes
                                elif nombre_lunes3 == "LIBRE":
                                    print("Su turno quedo registrado para el día lunes en la hora 11:11.")
                                    # Resto un turoo del lunes, y la constante cambia para que el nuevo nombre a comparar sera el registrado. 
                                    # Surge el problema de si el paciente ingresa nuevamente, su nombre no queda acumulado sino que ya se reemplazo por el ultimo paciente que entro.
                                    turnos_lunes -=1
                                    turnos_ocupados +=1
                                    nombre_lunes3 = nombre_lunes
                                elif nombre_lunes4 == "LIBRE":
                                    print("Su turno quedo registrado para el día lunes en la hora 11:30.")
                                    # Resto un tunro del lunes, y la constante cambia para que el nuevo nombre a comparar sera el registrado. 
                                    # Surge el problema de si el paciente ingresa nuevamente, su nombre no queda acumulado sino que ya se reemplazo por el ultimo paciente que entro.
                                    turnos_lunes -=1
                                    turnos_ocupados +=1
                                    nombre_lunes4 = nombre_lunes
                        else:
                            print("No quedan turnos disponibles el dia lunes.")
                    case "2":
                        # Antes de asignar un turno el martes, confirmo la disponibilidad.
                        if 1 <= turnos_martes <= TURNOS_MARTES:
                            print("Usted seleccionó el día Martes.")
                            print()
                            nombre_martes = input("Ingrese el nombre del paciente: ").strip().lower()
                            while not nombre_martes.replace(" ", "").isalpha():
                                nombre_martes = input("Ingrese el nombre del paciente solo con caracteres alfabéticos: ").strip().lower()
                            # Validamos que no tenga turno para el dia
                            if nombre_martes == NOMBRE_MARTES or nombre_martes == nombre_martes1 or nombre_martes == nombre_martes2 or nombre_martes == nombre_martes3:
                                print("Ya posee un turno para este día.")
                            else:
                                if nombre_martes1 == "LIBRE":
                                    print("Su turno quedo registrado para el día lunes en la hora 10:00.")
                                    # Resto un tunro del lunes, y la constante cambia para que el nuevo nombre a comparar sera el registrado. 
                                    turnos_martes -=1
                                    turnos_ocupados +=1
                                    nombre_martes1 = nombre_martes
                                elif nombre_martes2 == "LIBRE":
                                    print("Su turno quedo registrado para el día lunes en la hora 10:30.")
                                    # Resto un tunro del lunes, y la constante cambia para que el nuevo nombre a comparar sera el registrado. 
                                    turnos_martes -=1
                                    turnos_ocupados +=1
                                    nombre_martes2 = nombre_martes
                                elif nombre_martes3 == "LIBRE":
                                    print("Su turno quedo registrado para el día lunes en la hora 11:11.")
                                    # Resto un turoo del lunes, y la constante cambia para que el nuevo nombre a comparar sera el registrado. 
                                    turnos_martes -=1
                                    turnos_ocupados +=1
                                    nombre_martes3 = nombre_martes
                        else:
                            print("No quedan turnos disponibles el dia martes.")
            case "2":
                print("Cancelar turno.")
                print(""" Seleccione el día:
                1. Lunes.
                2. Martes.
                """)
                dia = input("Ingrese el número correspondiente al día: ").strip()
                while not dia.isdigit():
                    dia = input("Ingrese una opción váalida (1 o 2): ").strip()
                match dia:
                    case "1":
                        print("Usted seleccionó el día Lunes.")
                        nombre_lunes = input("Ingrese el nombre del paciente: ").strip().lower()
                        # Validamos que el nombre sea un texto.
                        while not nombre_lunes.replace(" ", "").isalpha():
                            nombre_lunes = input("Ingrese el nombre del paciente solo con caracteres alfabéticos: ").strip().lower()
                        if nombre_lunes == nombre_lunes1:
                            print("Se cancela su turno para el día lunes a las 10:00 horas.")
                            # Sumo 1 turno al dia lunes
                            turnos_lunes +=1
                            turnos_ocupados -=1
                            nombre_lunes1 = "LIBRE"
                        elif nombre_lunes == nombre_lunes2:
                            print("Se cancela su turno para el día lunes a las 10:30 horas.")
                            # Sumo 1 turno al dia lunes
                            turnos_lunes +=1
                            turnos_ocupados -=1
                            nombre_lunes2 = "LIBRE"
                        elif nombre_lunes == nombre_lunes3:
                            print("Se cancela su turno para el día lunes a las 11:00 horas.")
                            # Sumo 1 turno al dia lunes
                            turnos_lunes +=1
                            turnos_ocupados -=1
                            nombre_lunes3 = "LIBRE"
                        elif nombre_lunes == nombre_lunes4:
                            print("Se cancela su turno para el día lunes a las 11:30 horas.")
                            # Sumo 1 turno al dia lunes
                            turnos_lunes +=1
                            turnos_ocupados -=1
                            nombre_lunes4 = "LIBRE"
                        else:
                            print("Usted no posee turnos el día lunes.")
                    case "2":
                        print("Usted seleccionó el día Martes.")
                        nombre_martes = input("Ingrese el nombre del paciente: ").strip().lower()
                        while not(nombre_martes.replace(" ", "").isalpha or str(nombre_martes)):
                            nombre_martes = input("Ingrese el nombre del paciente solo con caracteres alfabéticos: ").strip().lower()
                        if nombre_martes == nombre_martes1:
                            print("Se cancela su turno para el día martes a las 10:00 horas.")
                            # Sumo 1 turno al dia martes
                            turnos_martes +=1
                            turnos_ocupados -=1
                            nombre_martes1 = "LIBRE"
                        if nombre_martes == nombre_martes2:
                            print("Se cancela su turno para el día martes a las 10:30 horas.")
                            # Sumo 1 turno al dia martes
                            turnos_martes +=1
                            turnos_ocupados -=1
                            nombre_martes2 = "LIBRE"
                        if nombre_martes == nombre_martes3:
                            print("Se cancela su turno para el día martes a las 11:00 horas.")
                            # Sumo 1 turno al dia martes
                            turnos_martes +=1
                            turnos_ocupados -=1
                            nombre_martes3 = "LIBRE"
                        else:
                            print("Usted no posee turnos el día martes.")
            case "3":
                print('Ver agenda del dia.')
                print(f"""
                Turnos disponibles el dia lunes: {turnos_lunes}
                Lunes 10:00 - {nombre_lunes1.capitalize()}
                Lunes 10:30 - {nombre_lunes2.capitalize()}
                Lunes 11:00 - {nombre_lunes3.capitalize()}
                Lunes 11:30 - {nombre_lunes4.capitalize()}
                Turnos disponibles el dia martes: {turnos_martes}
                Martes 10:00 - {nombre_martes1.capitalize()}
                Martes 10:30 - {nombre_martes2.capitalize()}
                Martes 11:00 - {nombre_martes3.capitalize()}
                """)
        
            case "4":
                print(f"""Ver resumen general.
Los lunes hay {TURNOS_LUNES} turnos habilitados. En este momento hay disponibles {turnos_lunes} turnos:
""")
                if nombre_lunes1 == "LIBRE" and nombre_lunes2 == "LIBRE" and nombre_lunes3 == "LIBRE" and nombre_lunes4 == "LIBRE":
                    print("Lunes 10:00, 10:30, 11:00 y 11:30 h")
                elif nombre_lunes2 == "LIBRE" and nombre_lunes3 == "LIBRE" and nombre_lunes4 == "LIBRE":
                        print("Lunes 10:30, 11:00 y 11:30 h")
                elif nombre_lunes3 == "LIBRE" and nombre_lunes4 == "LIBRE":
                        print("Lunes 11:00 y 11:30 h")
                elif nombre_lunes4 == "LIBRE":
                        print("Lunes 11:30")
                print(f"""
Los martes hay {TURNOS_MARTES} turnos. En este momento hay disponibles {turnos_martes} turnos:
""")
                if nombre_martes1 == "LIBRE" and nombre_martes2 == "LIBRE" and nombre_martes3 == "LIBRE":
                    print("Martes 10:00, 10:30 Y 11:00 h")
                elif nombre_martes2 == "LIBRE" and nombre_martes3 == "LIBRE":
                    print("Martes 10:30 y 11:00 h")
                elif nombre_martes3 == "LIBRE":
                    print("Martes 11:00")
                print()
            case "5":
                print("Cerrar sistema.")
                # No se si esta forma de cerrar esta bien
                turnos_ocupados = TURNOS_TOTALES + 1
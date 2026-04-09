# Ejercicio 2  — “Acceso al Campus y Menú Seguro” 
# Objetivo: Login con intentos + menú de acciones con validación estricta.
# Definir las constantes.
USUARIO = "alumno"
CLAVE = "python123"
clave = "xxxxxx"

# Definir la variable usuario. Permitir que se ingrese en mayusculas. Eliminar espacios.
usuario = input("Ingrese el nombre de usuario: ").lower().strip()
# Definir los intentos con un ciclo while.
for cont in range(2,4):
    if usuario != USUARIO:
        usuario = input(f"Intento {cont} de 3. Usuario incorrecto. Ingrese el nombre de usuario: ").lower().strip()
        if cont == 3 and usuario != USUARIO:
            print("Cuenta bloqueada")
    else:
        pass
while usuario == USUARIO and clave != CLAVE:
        clave = input("Ingrese la clave: ").strip()
        for cont in range (2,4):
            if clave != CLAVE:
                clave = input(f"Intento {cont} de 3. Clave incorrecta. Ingrese la clave: ").strip()
                if cont == 3 and clave !=CLAVE:
                    print("Cuenta bloqueada")
                    break
            else:
                print("Acceso concedido")
                break

while usuario == USUARIO and clave == CLAVE:
    print("""Seleccione la opcion:
    1. Ver estado de inscripción.
    2. Cambiar clave.
    3. Mostrar mensaje motivacional.
    4. Salir.
    """)
    opcion = input("Opción seleccionada: ")
    while not (opcion.isdigit() or ("1" <= opcion <= "4")):
        opcion = ("Ingrese una opción válida (1 a 4): ")
    match opcion:
        case "1":
            print("Inscripto.")
            print()
        case "2": 
            nueva_clave1 = input("Ingrese la nueva clave: ").strip()
            while not (len(nueva_clave1) >= 6 ):
                print("Ingresar una clave con al menos 6 caracteres.")
                nueva_clave1 = input("Ingrese la nueva clave: ").strip()
            nueva_clave2 = input("Vuelva a ingresar la nueva clave: ").strip()
            while nueva_clave1 != nueva_clave2 :
                print("Las claves no coinciden. Vuelva a ingresar la clave.")
                nueva_clave1 = input("Ingrese la nueva clave: ").strip()
                nueva_clave2 = input("Vuelva a ingresar la nueva clave: ").strip()
            print("Clave actualizada.")
            print()
        case "3":
            print("Sigue esforzandote. Los resultados no tardarán en aparecer")
            print()
        case "4":
            break



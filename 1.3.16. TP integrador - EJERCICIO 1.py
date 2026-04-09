# EJERCICIO 1
# Objetivo: Simular una compra con validaciones y cálculo de total.

# Pedir nombre del cliente con la variable nombre, quitando los espacios sobrantes.
nombre = input("Ingrese su nombre: ").strip()
# Validar que solo sean letras.
while not nombre.isalpha():
    nombre = input("Por favor, ingrese su nombre usando solo caracteres alfabéticos: ").strip()
# Mostrar el nombre del cliente.
print(f"Cliente: {nombre}")
print()
# Solicitar el numero de productos al comprar, con la variable cantidad,  y validar que sea un entero positivo.
cantidad = input("Ingrese la cantidad de productos: ").strip()
while not (cantidad.isdigit() or int(cantidad) == 0 ):
    cantidad = input("Ingreso inválido. Por favor, ingrese la cantidad de productos: ").strip()
# Convertir cantidad en entero luego de validado.
cantidad = int(cantidad)
# Mostrar la cantidad de productos.
print(f"Cantidad de productos: {cantidad}")
print()
# Variables acumuladoras para el informe final:
total = 0
total_descuento = 0
# Crear un ciclo for para la cantidad de productos, para pedir el precio y la opcion de descuento.
for i in range(1,cantidad + 1):
    precio = input(f"Producto {i} - Precio: ").strip()
    while not (precio.isdigit() or int(precio) == 0):
        precio = input("Ingreso inválido. Ingrese un número entero positivo: ").strip()
    precio = int(precio)
    # Consultar si tiene descuento, para cada producto.
    total += precio
    descuento = input(f"El producto {i} tiene descuento del 10% ? (S/N): ").strip().lower()
    while descuento not in ("sn"):
        descuento = input(f"El producto {i} tiene descuento del 10% ? Responda solo con S (Si) o N (No)): ").strip().lower()
    if descuento == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio
    total_descuento += precio_final
    print(f"Producto {i} - Precio: {precio} - Descuento (S/N): {descuento}")
    print()

print(f"El precio total de los {i} producto/s sin descuento es {total} pesos.")
print(f"El precio total aplicados los descuentos es {total_descuento} pesos.")
print(f"Gracias a nuestra promoción usted ahorró {total - total_descuento} pesos.")
print(f"El promedio de costo por producto fue de {(total_descuento / cantidad):.2f} pesos.")

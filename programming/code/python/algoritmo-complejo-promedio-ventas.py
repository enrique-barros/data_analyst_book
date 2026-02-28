# ============================================
# Programa para calcular el promedio de ventas
# ============================================

# Creamos una lista vacía donde guardaremos las ventas
ventas = []

# Le pedimos al usuario cuántas ventas quiere ingresar
cantidad = int(input("¿Cuántas ventas deseas ingresar? "))

# Usamos un bucle para pedir cada venta una por una
for i in range(cantidad):
    # Pedimos el valor de cada venta y lo convertimos a número decimal
    venta = float(input(f"Ingresa el valor de la venta {i + 1}: "))
    # Añadimos la venta a nuestra lista
    ventas.append(venta)

# Sumamos todos los valores de la lista de ventas
suma_total = sum(ventas)

# Contamos cuántas ventas hay en la lista
total_ventas = len(ventas)

# Calculamos el promedio dividiendo la suma entre la cantidad de ventas
promedio = suma_total / total_ventas

# Mostramos el resultado por pantalla
print(f"\nSuma total de ventas: {suma_total:.2f}")
print(f"Número de ventas: {total_ventas}")
print(f"Promedio de ventas: {promedio:.2f}")

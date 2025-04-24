# CALCULADORA_DE_DESCUENTOS
# Como dice el nombre del proyecto, es un sistema que puede dar la suma y descuento del producto.

def obtener_nombre_producto():
    #Solicita al usuario el nombre del producto y valida que no esté vacío.
    nombre = input("Nombre del producto:").strip()
    while not nombre:
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()
    return nombre

def obtener_precio_unitario():
    #Solicita un precio unitario válido (número positivo).
    while True:
        try:
            precio = float(input("Precio por unidad: "))
            if precio > 0:
                return precio
            else:
                print("El precio debe ser mayor que cero.")
        except ValueError:
            print("Error. Ingrese un número válido.")

def obtener_cantidad():
    #Solicita una cantidad válida (entero positivo).
    while True:
        try:
            cantidad = int(input("Cantidad: "))
            if cantidad > 0:
                return cantidad
            else:
                print("La cantidad debe ser un número entero positivo.")
        except ValueError:
            print("Error. Ingrese un número entero.")

def obtener_descuento():
    #Solicita el porcentaje de descuento (entre 0 y 100).
    while True:
        try:
            descuento = float(input("Descuento:"))
            if 0 <= descuento <= 100:
                return descuento
            else:
                print("El descuento debe estar entre 0 y 100.")
        except ValueError:
            print("Error. Ingrese un número válido.")

def calcular_total_sin_descuento(precio, cantidad):
    return precio * cantidad

def aplicar_descuento(total, porcentaje_descuento):
    descuento = total * (porcentaje_descuento / 100)
    total_final = total - descuento
    return descuento, total_final

def mostrar_resultado(nombre, precio, cantidad, descuento_aplicado, total_final):
    print("\nFactura:")
    print(f"Producto: {nombre}")
    print(f"Precio por unidad: ${precio:.2f}")
    print(f"Cantidad: {cantidad}")
    print(f"Descuento que se aplicó: ${descuento_aplicado:.2f}")
    print(f"Total: ${total_final:.2f}")

def main():
    print("Calculadora de Compra")

    nombre_producto = obtener_nombre_producto()
    precio_unitario = obtener_precio_unitario()
    cantidad = obtener_cantidad()
    porcentaje_descuento = obtener_descuento()

    total_sin_descuento = calcular_total_sin_descuento(precio_unitario, cantidad)
    descuento_aplicado, total_final = aplicar_descuento(total_sin_descuento, porcentaje_descuento)

    mostrar_resultado(nombre_producto, precio_unitario, cantidad, descuento_aplicado, total_final)

if __name__ == "__main__":
    main()
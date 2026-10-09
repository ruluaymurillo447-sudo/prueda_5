#calcular el total de una compra (cantodad-precio )-analisis 
nombre_producto =input("ingrese el nomdre de l producto ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad: "))

total  = round(precio * cantidad) 

print(f"El total de la compra es: {precio} este s el nombre del producto {nombre_producto}")
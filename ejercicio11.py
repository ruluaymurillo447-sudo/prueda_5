precioSinIVA = float(input("Ingrese el precio sin IVA: "))

valorIVA = precioSinIVA * 0.19
valorConIVA = precioSinIVA + valorIVA

print("El valor del IVA es:", valorIVA)
print("El valor con IVA es:", valorConIVA)
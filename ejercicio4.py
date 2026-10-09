#calcular el promedio de 3 notas 
nombre=input("ingrese su nombre ")
nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))

promedio = round((nota1+nota2+nota3)/3,2)

print(f"esta es tu nota {promedio} {nombre}")
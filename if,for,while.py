## if sintaxis
a = 4
if a == 5:
    print("Es correcto")
else:
    print("No es correcto")

##else if es elif
resultado2 = "aprobado"
if resultado2 == "aprobado":
    print("Felicidades")
elif resultado2 == "pendiente":
    print("Aún no hay resultado")
elif resultado2 == "reprobado":
    print("Intentalo nuevamente")

numero = int(input("Digite un numero:"))
if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es 0")
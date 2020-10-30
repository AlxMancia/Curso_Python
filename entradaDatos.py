#Entrada de datos
print("Cual es tu nombre?")
nombre = input()

#Entrada de numeros enteros
print("Digite su edad:")
edad = int(input())

#Entrada de flotantes
print("Ingrese su promedio de notas:")
promedio = float(input())

#operador relacional
print("Eres de este grupo?(Si/No)")
respuesta = input()=="si"

#Forma mas rapida
nombre2 = input("Ingrese su nombre:\n")
edad2 = int(input("Ingrese su edad:\n"))
promedio2 = float(input("Ingrese su promedio:\n"))
respuesta2 = input("Eres de este grupo?(Si/No):\n") == "si"
#salto de linea \n
print("Mucho Gusto \n",nombre)
print("Tu edad es:\n",edad,"años")
print("Tu promedio es de :\n",promedio)
print("Bienvenido\n",respuesta)
print("________________________")
print("Mucho Gusto",nombre2)
print("Tu edad es:",edad2,"años")
print("Tu promedio es de :",promedio2)
print("Bienvenido",respuesta2)
#Manejo de listas
milista = [10,"alexis",15.2,[12,"F"],False]

dias = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

dia = dias[0]
#imprime Lunes
print(dia)
#al meter un numero negativo recorre la lista a la inversa
dia2 = dias[-7]
print(dia2)
#sublista desde el primer elemento hasta el 5to
sublista = dias[0:4]
print(sublista)
#imprime desde el inicio hasta el numero = 7
print(dias[:7])
#imprime desde 4 hasta el final
print(dias[4:])
#Imprime toda la lista
print(dias[:])
#imprime desde inicio(0), hasta el final(7), saltando (2) espacios
print(dias[0:7:2])
#imprime a la inversa
print(dias[::-1])
print("_____________________________________")
lista = [5,9,1,58,4,2.65,10.8]
#ordena ascendentemente
lista.sort()
print(lista)
#orden descendente
lista.sort(reverse=True)
print(lista)
#se captura el valor maximo en este caso la pos 0
maximo = lista[0]
print(maximo)

lista2 = [5,9,1,58,4,2.65,10.8,15,0,45]
#longitud de una lista
longitud = len(lista2)
print(longitud)
#busca algo en una lista retorna un booleano
busqueda = 5 in lista2
print(busqueda)
busqueda2 = 6 in lista2
print(busqueda2)

#index devuelve la posicion donde se encuentra el elemento argumento
indice = lista2.index(10.8)
print(indice)
#count cuenta cuantos elementos estan el la lista
cuenta= lista2.count(9)
print(cuenta)
cuenta2 = lista2.count("Alex")
print(cuenta2)
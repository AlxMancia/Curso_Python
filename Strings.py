cadena = "Bienvenido al curso de Python nivel basico"
longitud = len(cadena)
print(longitud)

item = cadena[0]
print(item)

item2 = cadena[-1]
print(item2)

item = cadena[1:29:2]
print(item)

##Concatenacion

cad1 = "Hola"
cad2 = "Mundo"
cambio = "b" + cad1[0:]
print(cambio)
ejem = "H" + cad1[1:] + " " + cad2 + str(False)
print(ejem)

##Busqueda de cadenas
##string.count("arg") regresa la cantidad de palabrs en la cadena, puede ser letra o palabra
busqueda = cadena.count("o")
print(busqueda)
## "arg" in string retorna booleano si existe o no en la cadena
busqueda2 = "curso" in cadena
print(busqueda2)
##niega lo de arriba
busqueda3 = "curso" not in cadena
print(busqueda3)
##string.find("arg") retorna un valor entero, la posicion donde empieza el argumento en la cadena o string
busqueda4 = cadena.find("curso")
print(busqueda4)

##busqueda5 = cadena[cadena: busqueda + len("texto")]
##print(busqueda5)

## string.startswith("arg"),devuelve un booleano si el arg esta al principio de la cadena
## string.endswith("arg"),devuelve un booleano si el arg esta al principio de la cadena

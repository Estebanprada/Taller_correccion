
TypeError
try:
    resultado = "35" + 78
except TypeError:
    print("Error: Tipo de dato incorrecto")

# KeyError
try:
   diccionario = {'a': 1, 'b': 2}
   valor = diccionario['c']
except KeyError:
       print("Error: Clave no encontrada")


# generica Exception
try:
    resultado = 10 / 0
except Exception as e:
    print("Ocurrio un error:", str(e))

ZeroDivisionError
try:
    resultado = 25 / 0
except ZeroDivisionError:
    print("Error: Division por cero")


IndexError
try:
    lista = [1, 2, 3]
    elemento = lista[63]
except IndexError:
    print("Error: Indice fuera de rango")








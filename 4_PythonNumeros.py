import random

"""
Hay tres tipos numericos en python 
->int
->float
->complex (complejo)
"""

#Creamos variables con los tres tipos numericos

x = 1 #entero
y = 2.8 #float
z = 1j #complex

print(f"El valor de x es: {x}")
print(f"El valor de y es: {y}")
print(f"El valor de z es: {z}")


"""
Int:
Int o entero es un numerto entero negativo o positivo sin 
decimales de longitud limitada
"""
x = 1
y = 35656222554887711
z = -3255522

print(x)
print(y)
print(z)

"""
Float:
Flotar, o "número de punto flotante" es un número, positivo o negativo, que contiene uno o más decimales.

Float también puede ser números científicos con una "e" para indicar la potencia de 10.
"""
x = 1.10
y = 1.0
z = -87.7e100

print(x)
print(y)
print(z)

"""
Complejo:
Los números complejos se escriben con una "j" como parte imaginaria
"""
x = 3+5j
y = 5j
z = -5j

print(x)
print(y)
print(z)


#-------- Tipo de Conversion --------#
"""
Se puede convertir de un tipo a otro con el int(), float(), y complex().
"""
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convirtiendo de entero a flotante:
a = float(x)

#convirtiendo de flotante a entero:
b = int(y)

#convirtiendo de entero a complejo:
c = complex(x)

print(a)
print(b)
print(c)

#-------- Numeros Complejos --------#
"""
Python no tiene una funcion random() que haga un número aleatorio, pero tiene un módulo incorporado llamado random eso se puede usar para hacer números aleatorios:
"""
print(random.randrange(1, 10))



# ---------- PYTHON CASTING ---------- #

"""
Puede que hayan momentos donde se necesite especificar el tipo de dato de la variable, esto se realiza con 
casting(Funciones constructoras)

->int() construye un número entero a partir de un entero, un Float (al eliminar todos los decimales), o una cadena (siempre que la cadena represente un número entero)
->float() construye un número de flotador a partir de de entero, de flotador o de cadena (siempre que la cadena represente un flotador o un entero)
->str() construye una cadena a partir de una amplia variedad de tipos de datos, incluidas cadenas, enteros y  flotantes
"""

a = int(1)   # x puede ser 1
b = int(2.8) # y puede ser 2

print(a)
print(b)

c = float(2.8)   # y puede ser 2.8
d = float("3")   # z puede ser 3.0

print(c)
print(d)

d = str("s1") # x puede ser 's1'
e = str(2)    # y puede ser '2'
print(d)
print(e)
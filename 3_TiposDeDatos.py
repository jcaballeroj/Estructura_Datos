"""
Las variables pueden almacenar datos de diferentes tipos, y diferentes tipos pueden hacerlo cosas diferentes.
Python tiene los siguientes tipos de datos incorporados de forma predeterminada 
"""
#Tipo string
x = "Hello World" 
#tipo int
x = 20
#Tipo float (flotante o decial)
x = 20.5
#Tipo compplex ( o complejo)
x = 1j

#Tipo List
""""
tipo de datos nativos construido dentro del lenguaje de programación
Arrays o matrices
"""
x = ["apple", "banana", "cherry"]

#Tipo tuple 
"""
colecciones de datos idéntico que no pueden ser modificados

"""
x = ("apple", "banana", "cherry")
#Tipo de dato range
#Crea una secuencia de numeros correspondientes a la funcion range()
x = range(6)

#Tipo: dict( diccionarios son una forma de almacenar elementos)
"""
Tipo: dict
En lugar de acceder a los elementos utilizando su indice
se le asigna una clave fija
"""
x = {"name" : "John", "age" : 36}

#Tipo: set( Permite almacenar varios elementos y acceder a ellos de una forma muy similar a las listas )
"""
Los elementos de un set son unicos, no pueden haber elementos duplicados
"""
x = {"apple", "banana", "cherry"}

"""
#Tipo: Fronzenset
son un tipo muy parecido a los sets con la salvedad de que son inmutables, es decir, están congelados y no pueden ser modificados una vez inicializados
"""
x = frozenset({"apple", "banana", "cherry"})

"""
Bool tipo de dato que permite almacenar valores de 
verdadero o falso
"""
x = True

"""
Los ultimos tres datos son de tipo binarios 
x1 = secuencia inmutable de bytes. Solo admiten caracteres ASCII

x2 =  representa un arreglo mutable de bytes, el cual se comporta prácticamente igual que el tipo bytes

x3 = expone la interfaz de búfer a nivel de C como un objeto Python que luego puede pasarse como cualquier otro objeto.
"""
x1 = b"Hello"

x2= bytearray(5)

x3 = memoryview(bytes(5))


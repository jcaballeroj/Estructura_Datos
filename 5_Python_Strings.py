"""
------Strings en Python------
Las cadenas (Strings) en python están rodeadas por comillas simples o comillas dobles
1-Puede usar comillas dentro de una cadena, siempre que no coincidan con las comillas que rodean la cadena:
"""
#ejemplo de numeral 1
print("He is called 'Johnny'")

"""
Tambien podemos asignar una cadena de texto a una variable o cuedas multiples en una variable
"""
a = "Hello"
print(a)
print()

b = """  
Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.
"""
print(b)


""" 
Los String son arrays:
Las cadenas en Python son matrices de bytes que representan caracteres unicode.
Sin embargo, Python no tiene un tipo de datos de caracteres, un solo carácter es simplemente una cadena con una longitud de 1.

"""
a = "Hello, World!"
print(f"Mostrando la leta {a[1]} de Hello world") #Muestra la letra e
print()
""" 
BUCLEANDO LAS CADENAS DE TEXTO:
Dado que las cadenas son matrices, podemos recorrer los caracteres en una cadena, con un for bucle.
"""
for x in "banana":
  print(x)#Muestra la palabra banana en pantalla
  
""" 
LONGITUD DEL STRING
Para obtener la longitud de una cadena, Usamos la funcion el len().
"""
a = "Hello, World!"
print(f"Mostrando el tamaño o numero de caracteres de la palabra Hello, World {len(a)}")

""" 
REVISION DE LA CADENA
Para comprobar si una determinada frase o carácter está presente en una cadena, podemos utilizar la palabra clave (in).
Nos mostrara por consola una respuesta booleana, true o false

Otra forma de verificacion seria con la bifuracacion if

Para comprobar si una determinada frase o carácter NO está presente en una cadena, podemos utilizar la palabra clave not in.
"""
txt = "The best things in life are free!"
print("free" in txt)
#Determinacion de una palabra con la bifurcacion if
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#Determinacion de una no existencia de una palabra 
txt = "The best things in life are free!"
print("expensive" not in txt) 

#Determinacion de una no existencia con bifurcacion if
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
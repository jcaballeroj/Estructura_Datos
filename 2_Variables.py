#Creacion de variables
#En python las variables no necesitan ser declaradas y se puede obtener el tipo de
#dato con la funcion type()
x = 5
y = "Jhon"
#mostrando el valor asignado a las variables
print("mostrando el valor asignado a las variables")
print(x)  # x es de tipo entero
print(y)  # y es de tipo string  
#---------------------------------------------------
print("mostrando el tipo de datos de cada variable")
print(type(x))  # x es de tipo entero
print(type(y))  # y es de tipo string  

#Si se desea especificar el tipo de dato se puede hacer con
#casting (especificando mas detalladamente el tipo de dato)
x = str(3) 
y = int(3)
z = float(3)

print(x) #string
print(y) #entero
print(z) #flotante

# ------------- NOMBRE DE VARIABLES -------------#
#las variables pueden tener un nombre corto o un nombre mas descriptivo
#Se deben respetar los criterios de creacion de nombres 
#como lo es CamelCase, PascalCase, SnakeCase

#CamelCase
myVariableName = "Jose"
#PascalCase
MyVariableName = "Juan"
#SnakeCase
my_variable_name = "Pedro"

# ------------- ASIGNACION DE MULTIPLES VARIABLES -------------#
#Python permite  asignar valores a multiples variables
#El numero de variables debe coincidir con el numero de variables
print("Mostrando La asignacion de varias variables")
x,y,z = "Naranja", "Banana","Cherry"
print(x)
print(y)
print(z)

#Tambien se puede agregar el mismo valor a varias variables
print("Mostrando La asignacion de un valor a varias variables")
x = y = z = "Naranja"
print(x)
print(y)
print(z)


#Desempaquetando una coleccion 
print("Desempaquetando una coleccion")
frutas = ["Melon", "Sandia", "Cereza"]
x,y,z = frutas
#para mostrar una sola linea de salida podemos concatenar o acomodar todo en un print con una coma
print(x,y,z)

# ------------- VARIABLES GLOBALES -------------#
#Son variables que son creadas fuera de una funcion y puede ser utilizados dentro y fuera de dicha funcion 
#Si se crea una variable con el mismo nombre dentro de una función, esta variable será local y solo se puede usar dentro de la función
print("variable fuera de la funcion")
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

print("Variable dentro y fuera de la Funcion")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)
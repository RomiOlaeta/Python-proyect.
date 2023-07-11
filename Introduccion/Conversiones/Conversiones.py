texto="Hola soy qa"

print(texto)
print(texto[-3])
print(texto[5:15]) #es para decir de donde imprimir hasta donde
nombre="Romi"
print(nombre.upper()) #mayuscula
print(nombre.lower()) #minuscula
print(nombre.capitalize()) #mayuscula al principio

cadena="java, python, javascript"

print(cadena)
print(cadena.split(",")) #los imprime con comilla por separacion
nom="Juan"
ap="Olaeta"
am="Chavez"

print("Tu nombre {} tu apellido es {} y tu apellido materno es {}".format(nom,ap, am))


#input es para guardar datos en variable

print("Cual es tu nombre:")
nom=input()

print("Tu nombre es: "+nom)

print("Dame el valor de a:")
valor=input()

print("El valor es:"+valor)
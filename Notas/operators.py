#Operadores lógicos y de comparación 

print("Lógicos")
print("------------")
#AND- cuando todas las condiciones se cumplen resulta True 
#OR-cuando alguna de las condiciones se cumple resulta True/si ninguna se cumple es False
#NOT-invierte el valor de la variable

trabaja = False
es_estudiante = True

print(es_estudiante and trabaja)#AND
print(es_estudiante or trabaja)#OR
print(not es_estudiante)#NOT

print(" ")
print(" ")

print("Comparación")
print("------------")
#== - igual o igualdad/compara si dos numeros son iguales
#!= - diferencia/compara si dos numeros son diferentes
#> - mayor que/compara si un numero es mayor a otro
#< - menor que/compara si un numero es menor a otro
#>= - mayor o igual que/compara si un numero es mayor o igual a otro
#<= - menor o igual que/compara si un numero es menor o igual que otro

numero1 = 5
numero2 = 5
numero3 = 7

print(numero1 == numero2)
print(numero1 != numero2)
print(" ")
print(numero2 > numero3)
print(numero2 < numero3)
print(" ")
print(numero3 >= numero1)
print(numero2 <= numero1)


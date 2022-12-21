numero = 3
print(numero)

numeros = [1, 3, 5, 9, 29, 52]
print(numeros)

objetos = ['Joputa', 5.6, True, 626, 'caralcaparra', False, 4.9, 2, 9, 'Rolando']
print(objetos)
print(objetos[2])

objetos.append('Nina')#metodo para agregar un elemento al final de la lista
print(objetos)

objetos.pop(4)#metodo para eliminar un elemento de la lista según su índice
print(objetos)

print(objetos[::-1])

for elemento in objetos:
    print(elemento)
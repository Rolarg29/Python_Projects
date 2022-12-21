# arrays

arreglo = ['banana', 'melon', 'sandia', 'pera', 'manzana', 'uva']

arreglo.reverse()
arreglo.remove('melon')
arreglo.append('kiwi')

# bucle for
for fruta in arreglo:
    if fruta == 'sandia':
        continue
    print('La fruta es: ' + fruta)


texto = 'Hola mundo'

for letra in texto:
    print('Letra: ' + letra)

for numero in range(5, 20):
    if (numero > 5):
        print(numero)
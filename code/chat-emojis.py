seguirChateando = True
while seguirChateando:
    texto = input('>')
    if texto == 'salir':
        seguirChateando = False

    texto = texto.replace(':)', '๐')
    texto = texto.replace(':', '๐คจ')
    texto = texto.replace(':/', '๐')
    texto = texto.replace(':(', '๐')
    texto = texto.replace(':*', '๐')
    texto = texto.replace(':p', '๐')
    texto = texto.replace(':P', '๐')

    print(texto)
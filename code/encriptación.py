# retorna un texto encriptado (textoFinal)
def encriptar(texto):
    # print('El texto a encriptar es: ' + texto)
    textoFinal = ''
    for letra in texto:
        textoFinal += letra + 'x'
    # print('> ' + textoFinal)
    return textoFinal


# retorna un textor desencriptado (textoFinal)
def desencriptar(texto):
    # print('El texto a desencriptar es: ' + texto)
    textoFinal = ''
    contador = 0
    for letra in texto:
        if contador % 2 == 0:
            textoFinal += letra
        contador += 1
    # print('> ' + textoFinal)
    return textoFinal


def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')  # abre el archivo texto.txt y lo lee y guarda
    texto = archivo.read()  # guarda el contenido del txt en 'texto'
    archivo.close()
    textoEncriptado = encriptar(texto)  # usa como parámetro el contenido del txt, encripta y guarda

    archivo = open(rutaArchivo, 'w')  # abre archivo y sobreescribe
    archivo.write(textoEncriptado)  # reemplaza texto normal por encriptado
    archivo.close()
    print('El archivo se encriptó correctamente')


def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo, 'r')  # abre el archivo texto.txt y lo lee y guarda
    texto = archivo.read()  # guarda el contenido del txt en 'texto'
    archivo.close()
    textoDesencriptado = desencriptar(texto)  # usa como parámetro el contenido del txt, encripta y guarda

    archivo = open(rutaArchivo, 'w')  # abre archivo y sobreescribe
    archivo.write(textoDesencriptado)  # reemplaza texto normal por encriptado
    archivo.close()
    print('El archivo se desencriptó correctamente')



respuestaEoD = input('Presione "E" para encriptar o "D" para desencriptar: ')
rutaArchivo = input('Ingrese la ruta del archivo: ')

if respuestaEoD == 'E':
    encriptarArchivo(rutaArchivo)
elif respuestaEoD == 'D':
    desencriptarArchivo(rutaArchivo)
else:
    print('No ha seleccionado una opción disponible')
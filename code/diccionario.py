diccionario =  {
    "Programar": "Programar es trasformar el café en código",
    "POO": "Programación Orientada a Objetos"
}

#print(diccionario["POO"])

numerosATexto = {
    "0": "cero",
    "1": "uno",
    "2": "dos",
    "3": "tres",
    "4": "cuatro",
    "5": "cinco",
    "6": "seis",
    "7": "siete",
    "8": "ocho",
    "9": "nueve"
}
texto = input('Ingrese un número: ')

textoFinal = ''

for letra in texto:
    textoFinal += numerosATexto[letra] + ' '

print(textoFinal)
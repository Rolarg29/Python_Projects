# Calculadora IMC
# IMC = Peso / (altura x altura)
# < 19: Delgadez
# entre 20 y 25: normal
# entre 26 y 30: sobrepeso
# > 30: obesidad

def calcularIMC(peso, altura):
    imc = peso / (altura * altura)
    return imc


def pedirIMC():
    peso = float(input('Ingrese su peso en Kg: '))
    altura = float(input('Ingrese su altura en metros: '))
    imc = calcularIMC(peso, altura)

    print('Su IMC es de ' + str(imc))

    if imc < 20:
        print('Estado de delgadez.')
    if imc >= 20 and imc < 26:
        print('Peso normal.')
    if imc >= 26 and imc < 30:
        print('Estado de sobrepeso.')
    if imc > 30:
        print('Estado de obesidad.')


print('Calcular el IMC de la primer persona')
pedirIMC()
print('Calcular el IMC de la segunda persona')
pedirIMC()
print('Calcular el IMC de la tercer persona')
pedirIMC()

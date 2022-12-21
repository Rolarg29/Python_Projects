def calculadora(formula):
    num1 = int(input('Escribe el primer numero: '))
    num2 = int(input('Escribe el segundo numero: '))
    if formula == 'suma':
        resultado = num1 + num2
    elif formula == 'resta':
        resultado = num1 - num2
    elif formula == 'multiplicación':
        resultado = num1 * num2
    elif formula == 'división':
        resultado = num1 / num2
    else:
        print('Falta la formula')
    print(f'La {formula} de ambos números es: {resultado}')


def main():
    menu = """
Bienvenido a la calculadora uwu

1- Suma
2- Resta
3- Multiplicación
4- División 

Escoge la operación a realizar: """

    opcion = int(input(menu))

    if opcion == 1:
        calculadora('suma')
    elif opcion == 2:
        calculadora('resta')
    elif opcion == 3:
        calculadora('multiplicación')
    elif opcion == 4:
        calculadora('división')
    else:
        print('Elige una operación disponible')
    

if __name__ == '__main__':
    main()
    
    
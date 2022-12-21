#bucle WHILE - ciclo fundamental
def run():
    LIMITE = 100000000
    
    contador = 0
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print(f'2 elevado a {contador} es igual a: {potencia_2}')
        contador = contador + 1
        potencia_2 = 2**contador
        if potencia_2 == 1024:
            continue


if __name__ == '__main__':
    run()
#Enteros, decimales, texto(string), booleanos

#no importa si usamos comillas simples o dobles, puede que haya excepciones


nombre1 = "Rolando"
print(nombre1)
print (nombre1*3)

nombre2 = 'Mayito'
print('tu pinche cola ' + nombre2 )

#CONVERTIR UN DATO A UN TIPO DIFERENTE

numero1 = input("Escribe un número:")
#numero1 = '6'
#comillas simples sigifica texto ''
numero2 = input("Escribe un número:")
#numero2 = '3'
print(numero1 + numero2)
#numero1 + numero 2 
#63 >>>> lo identifica como texto/string

numero1 = int(numero1)
print(numero1)
numero2 = int(numero2)
print(numero2)
print(numero1 + numero2)

#numero decimal
numero_decimal = 4.5
print(numero_decimal)

print(int(numero_decimal))
str(numero_decimal)
print('8' + str(numero_decimal))
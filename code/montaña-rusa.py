# Nombre de la persona
nombre = input('¿Cómo te llamas? ')
print('Hola ' + nombre)

# Edad de la persona
edad = int(input('¿Cuántos años tienes? '))
masDe12 = edad >= 12

# Filtro -> Hijo del dueño
respuestaHijoDelDueño = input('¿Es hijo del dueño? ')
esHijoDelDueño = respuestaHijoDelDueño == 'si'

# Condiciones para el if
puedePasar = masDe12 or esHijoDelDueño

if puedePasar:
    print('Usted puede pasar a la montaña rusa')
else:
    print('No puede pasar, a chingar a su madre a otro lado... puto')

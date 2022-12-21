nombre = "Rolando"

print(nombre[0])

print(nombre[0:3])#parte desde un indice hasta otro
print(nombre[:3])#parte desde el primer indice por default hasta otro
print(nombre[3:])#parte desde un indice hasta el ultimo por default
print(nombre[2:7])#parte desde un indice hasta otro
print(nombre[2:7:2])#parte desde un indice hasta otro con saltos cada 2 letras
print(nombre[2:7:3])#parte desde un indice hasta otro con saltos cada 3 letras
print(nombre[::])#muestra todo el texto porque da saltos cada letra
print(nombre[1::3])#muestra desde un indice hasta el final con saltos cada 3 letras
print(nombre[::-1])#muestra todo el texto con saltos en reversa

#cuando hay saltos SOLO se muestra la letra donde fue el salto
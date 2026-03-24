productos = ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Mouse']
precios = [1200, 25, 80, 300, 25]
cantidades = [1,3,2,1,4]

# PARTE 1
print('### PARTE 1 ###')

""" for producto in productos:

    print(producto) """

productos_unicos = set(productos)
total_prod_unicos = len(productos_unicos)
precio_alto = max(precios)
precio_bajo = min(precios)


print(f'El precio más alto es el de: {precio_alto}')
print(f'El precio más bajo es el de: {precio_bajo}')
print(f'La cantidad de productos que hay es de: {total_prod_unicos}')

# PARTE 2
print('### PARTE 2 ###')

""" ¿Cuántas veces aparece la palabra mouse? """

contador = productos.count('Mouse')
print(f'La cantidad de veces que aparece la palabra "Mouse" es de {contador}')

####

contador_1 = 0
for palabra in productos:
    if palabra == 'Mouse':
        contador_1 += 1

print(f'La palabra "Mouse" aparece {contador_1} veces en la lista')

""" ¿Qué producto aparece primero? """

primer_producto = productos[0]
print(f'El primer producto de la lista es: {primer_producto}')

# PARTE 3
print('### PARTE 3 ###')

""" ¿Qué producto parece más caro? """

producto_mas_caro = productos[precios.index(max(precios))]
precio_max = max(precios)

print(f'El producto más caro es {producto_mas_caro} con un precio de ${precio_max}')

""" ¿Qué producto se repite más? """

producto_mas_repetido = ''
max_repeticiones = 0

for producto in productos:
    contador = productos.count(producto)
    if contador > max_repeticiones:
        max_repeticiones = contador
        producto_mas_repetido = producto

print(f'El producto que más se repite es: {producto_mas_repetido} con {max_repeticiones} apariciones')

def max_area(altura):
    max_agua = 0
    izquierda = 0
    derecha = len(altura) - 1

    while izquierda < derecha:
        # Calcula el área del contenedor actual
        altura_minima = min(altura[izquierda], altura[derecha])
        ancho = derecha - izquierda
        area = altura_minima * ancho

        # Actualiza el máximo si el área es mayor
        max_agua = max(max_agua, area)

        # Mueve el puntero que apunta al valor menor
        if altura[izquierda] < altura[derecha]:
            izquierda += 1
        else:
            derecha -= 1

    return max_agua


# Ejemplos
altura1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Máxima cantidad de agua:", max_area(altura1))  # Salida esperada: 49

altura2 = [1, 1]
print("Máxima cantidad de agua:", max_area(altura2))  # Salida esperada: 1

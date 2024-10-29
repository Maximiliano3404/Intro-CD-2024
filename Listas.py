# Programa para obtener elementos comunes entre dos listas ingresadas por el usuario

def elementos_comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))

# Solicitar al usuario que ingrese las listas
lista1 = input("Introduce los elementos de la primera lista, separados por comas: ")
lista2 = input("Introduce los elementos de la segunda lista, separados por comas: ")

# Convertir las entradas en listas de enteros
lista1 = [int(x.strip()) for x in lista1.split(",")]
lista2 = [int(x.strip()) for x in lista2.split(",")]

# Obtener y mostrar los elementos comunes
comunes = elementos_comunes(lista1, lista2)
print(f"Elementos comunes: {comunes}")

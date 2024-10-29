# Programa para verificar la Conjetura de Goldbach
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def conjetura_goldbach(n):
    if n <= 2 or n % 2 != 0:
        return "Introduce un número par mayor que 2."

    pares_primos = []
    for i in range(2, n):
        if es_primo(i) and es_primo(n - i):
            pares_primos.append((i, n - i))

    return pares_primos


# Solicitar al usuario un número par mayor que 2
numero = int(input("Introduce un número par mayor que 2: "))

# Verificar y mostrar los pares de números primos
resultado = conjetura_goldbach(numero)
if isinstance(resultado, str):
    print(resultado)
else:
    print(f"Pares de números primos que suman {numero}: {resultado}")

# Programa para calcular la secuencia de Fibonacci
def fibonacci(n):
    secuencia = [0, 1]
    for i in range(2, n):
        siguiente = secuencia[-1] + secuencia[-2]
        secuencia.append(siguiente)
    return secuencia[:n]

# Solicitar al usuario la cantidad de términos
n = int(input("Introduce el número de términos que deseas en la secuencia de Fibonacci: "))

# Generar y mostrar la secuencia de Fibonacci
if n <= 0:
    print("Por favor, introduce un número mayor que cero.")
else:
    secuencia = fibonacci(n)
    print(f"Secuencia de Fibonacci con {n} términos: {secuencia}")
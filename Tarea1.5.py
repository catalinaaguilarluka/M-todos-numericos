# Tarea 1.5: Calcule el número de Euler con un error
import math

e_real = math.exp(1)
e_aprox = 0
n = 0
error = 1.0  # Valor inicial para entrar al bucle

while error >= 0.01:
    e_aprox += 1 / math.factorial(n)
    error = abs(e_real - e_aprox)
    n += 1

print("Valor aproximado de e:", e_aprox)
print("Error obtenido:", error)
print("Número de términos usados (n):", n)

# Nota: 6.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 0/1; claridad: 1/1.
# Faltan comentarios que expliquen la suma de términos y la actualización del error dentro del ciclo.

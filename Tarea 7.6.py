
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import time

# Tarea 7.6

def f(x):
    return np.log(x) / np.sqrt(np.cos(x)**2 + np.tanh(x))


# Regla de Simpson
def simpson(f, a, b):
    m = (a + b) / 2
    return (b-a)/6 * (f(a) + 4*f(m) + f(b))


# Cuadratura adaptativa
def adaptativa(f, a, b, tol):
    m = (a + b) / 2

    s = simpson(f, a, b)
    s1 = simpson(f, a, m)
    s2 = simpson(f, m, b)

    error = abs(s1 + s2 - s) / 15

    if error < tol:
        return s1 + s2 + (s1 + s2 - s)/15

    else:
        izq = adaptativa(f, a, m, tol/2)
        der = adaptativa(f, m, b, tol/2)
        return izq + der


# Límites de integración
a = 0.1
b = 1

# Precisiones que vamos a comparar
precisiones = [1e-2, 1e-4, 1e-6, 1e-8, 1e-10]

tiempo_adaptativa = []
tiempo_scipy = []

for tol in precisiones:

    # Método adaptativo
    inicio = time.perf_counter()

    for i in range(100):
        resultado1 = adaptativa(f, a, b, tol)

    t1 = (time.perf_counter() - inicio)/100
    tiempo_adaptativa.append(t1)

    # Método de scipy
    inicio = time.perf_counter()

    for i in range(100):
        resultado2, error = integrate.quad(
            f, a, b, epsabs=tol, epsrel=tol
        )

    t2 = (time.perf_counter() - inicio)/100
    tiempo_scipy.append(t2)

    print("Precisión:", tol)
    print("Adaptativa:", resultado1)
    print("Scipy:", resultado2)
    print("Tiempo adaptativa:", t1)
    print("Tiempo scipy:", t2)
    print()


# Gráfico
plt.figure(figsize=(8, 5))

plt.loglog(precisiones, tiempo_adaptativa, 'o-',
           label="Adaptativa")
plt.loglog(precisiones, tiempo_scipy, 'o-',
           label="Scipy")

plt.xlabel("Precisión")
plt.ylabel("Tiempo (s)")
plt.title("Comparación de tiempos de integración")
plt.legend()
plt.grid(True)
plt.gca().invert_xaxis()
plt.show()


# Conclusión:
# Los dos métodos permiten calcular la integral y dan resultados
# similares cuando se aumenta la precisión.
# Al pedir una precisión mayor, el tiempo de cálculo puede aumentar.
# Con el gráfico podemos comparar cuál de los dos métodos tarda
# menos en resolver esta integral.


# Nota: 7.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 1/1; claridad: 1/1.

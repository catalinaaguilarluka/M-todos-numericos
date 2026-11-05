
import numpy as np
import matplotlib.pyplot as plt
import time

# Funcion del problema
def f(x):
    return 1 - np.cos(x) - np.sin(x)/x

# Derivada de la funcion
def df(x):
    return np.sin(x) - (x*np.cos(x) - np.sin(x))/x**2


# Metodo de biseccion
def biseccion(a, b, tol):
    if f(a)*f(b) >= 0:
        raise ValueError("No hay cambio de signo")

    n = 0
    anterior = None

    while n < 1000:
        x = (a+b)/2
        n += 1

        if f(x) == 0:
            return x, n

        if anterior is not None:
            error = abs(x-anterior)/abs(x)
            if error < tol:
                return x, n

        if f(a)*f(x) < 0:
            b = x
        else:
            a = x

        anterior = x

    return x, n


# Metodo de Newton
def newton(x, tol):
    n = 0

    while n < 1000:
        if abs(df(x)) < 1e-14:
            raise ValueError("Derivada muy cercana a cero")

        nuevo = x - f(x)/df(x)
        n += 1

        error = abs(nuevo-x)/abs(nuevo)

        if error < tol or f(nuevo) == 0:
            return nuevo, n

        x = nuevo

    return x, n


# Datos iniciales
a = -6.4
b = -6.0
x0 = -6.2

tolerancias = [10**(-i) for i in range(2, 11)]

iter_b = []
iter_n = []
tiempo_b = []
tiempo_n = []

# Comparacion de los metodos
for tol in tolerancias:

    inicio = time.perf_counter()
    for j in range(100):
        raiz_b, nb = biseccion(a, b, tol)
    tb = (time.perf_counter()-inicio)/100

    inicio = time.perf_counter()
    for j in range(100):
        raiz_n, nn = newton(x0, tol)
    tn = (time.perf_counter()-inicio)/100

    iter_b.append(nb)
    iter_n.append(nn)
    tiempo_b.append(tb)
    tiempo_n.append(tn)

    print("Tolerancia:", tol)
    print("Biseccion:", raiz_b, "Iteraciones:", nb)
    print("Newton:", raiz_n, "Iteraciones:", nn)
    print()


# Grafico de iteraciones
plt.figure()

plt.plot(tolerancias, iter_b, "o-", label="Biseccion")
plt.plot(tolerancias, iter_n, "o-", label="Newton")

plt.xscale("log")
plt.gca().invert_xaxis()
plt.xlabel("Tolerancia")
plt.ylabel("Numero de iteraciones")
plt.title("Comparacion de iteraciones")
plt.legend()
plt.grid()
plt.show()


# Grafico de tiempos
plt.figure()

plt.plot(tolerancias, tiempo_b, "o-", label="Biseccion")
plt.plot(tolerancias, tiempo_n, "o-", label="Newton")

plt.xscale("log")
plt.gca().invert_xaxis()
plt.xlabel("Tolerancia")
plt.ylabel("Tiempo promedio (segundos)")
plt.title("Comparacion de tiempos")
plt.legend()
plt.grid()
plt.show()

# Conclusion y comentarios
#
# En esta tarea usamos los metodos de biseccion y Newton-Raphson
# para encontrar una raiz de la funcion.
#
# Al comparar los dos metodos, podemos ver que el numero de
# iteraciones y el tiempo que demoran cambian segun la precision
# que estamos buscando.
#
# Biseccion va reduciendo el intervalo poco a poco, mientras
# que Newton usa la derivada para acercarse a la raiz.
#
# En general, Newton puede necesitar menos iteraciones, pero
# no siempre es asi, porque depende de la funcion.
#
# Finalmente, ambos metodos sirven para encontrar raices,
# aunque cada uno tiene sus ventajas y puede funcionar
# mejor dependiendo del problema.
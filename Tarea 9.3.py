import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    return (2 - 2*t*y)/(t**2 + 1)

def exacta(t):
    return (2*t + 1)/(t**2 + 1)


def rkf(orden):

    t = 0
    w = 1
    h = 0.25
    tol = 1e-6

    ts = [t]
    sol = [w]

    while t < 3:

        if t + h > 3:
            h = 3 - t

        k1 = h*f(t, w)
        k2 = h*f(t + h/4, w + k1/4)
        k3 = h*f(t + 3*h/8, w + 3*k1/32 + 9*k2/32)
        k4 = h*f(t + 12*h/13, w + 1932*k1/2197 - 7200*k2/2197 + 7296*k3/2197)
        k5 = h*f(t + h, w + 439*k1/216 - 8*k2 + 3680*k3/513 - 845*k4/4104)
        k6 = h*f(t + h/2, w - 8*k1/27 + 2*k2 - 3544*k3/2565 + 1859*k4/4104 - 11*k5/40)

        # Soluciones de orden 4 y 5
        w4 = w + 25*k1/216 + 1408*k3/2565 + 2197*k4/4104 - k5/5

        w5 = w + 16*k1/135 + 6656*k3/12825 + 28561*k4/56430 - 9*k5/50 + 2*k6/55

        R = abs(w5 - w4)

        # Se acepta el paso si cumple la tolerancia
        if R <= tol:
            t = t + h

            if orden == 4:
                w = w4
            else:
                w = w5

            ts.append(t)
            sol.append(w)

        # Ajuste del tamaño del paso
        if R == 0:
            q = 4
        else:
            q = 0.84*(tol/R)**(1/4)

        q = max(0.1, min(q, 4))
        h = min(q*h, 0.25)

    return np.array(ts), np.array(sol)


# Comparacion de ambos metodos

t4, sol4 = rkf(4)
t5, sol5 = rkf(5)

error4 = abs(sol4 - exacta(t4))
error5 = abs(sol5 - exacta(t5))

print("Solucion exacta:", exacta(3))

print("\nOrden 4")
print("Solucion:", sol4[-1])
print("Error final:", error4[-1])
print("Error maximo:", max(error4))
print("Pasos:", len(t4)-1)

print("\nOrden 5")
print("Solucion:", sol5[-1])
print("Error final:", error5[-1])
print("Error maximo:", max(error5))
print("Pasos:", len(t5)-1)

# Grafico de los errores

plt.plot(t4, error4, label="Orden 4")
plt.plot(t5, error5, label="Orden 5")

plt.xlabel("t")
plt.ylabel("Error absoluto")
plt.title("Comparacion de errores")
plt.legend()
plt.grid()
plt.show()

# Comentario final:
# En esta tarea compare el metodo de Runge-Kutta-Fehlberg
# de orden 4 con el de orden 5, utilizando la misma
# tolerancia y las mismas condiciones iniciales.
#
# Ambos metodos permiten aproximar la solucion exacta.
# En general, se espera que el metodo de orden 5 tenga
# un error menor debido a su mayor orden.
#
# En el metodo original se utiliza la solucion de orden 4
# porque la diferencia entre ambas aproximaciones permite
# estimar principalmente el error de la solucion de orden 4
# y controlar el tamaño del paso.
#
# Sin embargo, tambien es posible utilizar la solucion
# de orden 5, aprovechando su mayor precision sin realizar
# evaluaciones adicionales de la funcion.

# Nota: 7.0
# Base: 1/1; funcionamiento: 4/4; comentarios: 1/1; claridad: 1/1.

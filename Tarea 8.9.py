
# Tarea 8.9 

# Definir Variables

m = 0.11
g = 9.8
k = 0.002

h = 0.001
t = 0
v = 8

print("Tiempo (s) | Velocidad (m/s)")
print("-----------------------------")

for i in range(1000):
    # Primera derivada
    dv = -g - (k/m)*v*abs(v)

    # Segunda derivada
    d2v = -(2*k/m)*abs(v)*dv

    # Taylor de segundo orden
    v_nueva = v + h*dv + (h**2/2)*d2v

    # Cuando la velocidad llega a cero
    if v > 0 and v_nueva <= 0:
        t_max = t + h*v/(v-v_nueva)

    v = v_nueva
    t = t + h

    # Mostrar resultados cada 0.1 segundos
    if (i+1) % 100 == 0:
        print(f"{t:.1f}        | {v:.4f}")

print(f"Altura maxima en t = {t_max:.1f} segundos")


# Comentarios finales:
# Con el metodo de Taylor de segundo orden se calculo la
# velocidad del proyectil en distintos tiempos.
# Se puede observar que la velocidad disminuye poco a poco
# por efecto de la gravedad y la resistencia del aire.
#
# El proyectil alcanza su altura maxima cerca de los 0.8
# segundos, cuando su velocidad llega a cero.
# Despues de ese momento, la velocidad pasa a ser negativa,
# lo que indica que el proyectil comienza a caer.


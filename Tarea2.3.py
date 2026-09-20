import numpy as np

# TAREA 2.3 - COSMOLOGÍA Y ERRORES NUMÉRICOS

# Datos
q_max = 0.1
N = 500000
delta_q = q_max / N

# Puntos q_i (desde i=1 hasta N)
i = np.arange(1, N + 1, dtype=np.float64)
q = i * delta_q

# 1. Calculo I1 dee I2 por separado
f1 = (q**2) * ((1.0 / (q**5)) + (3.0 / q))
f2 = (q**2) * ((-1.0 / (q**5)) + (1.0 / q))

I1 = delta_q * np.sum(f1)
I2 = delta_q * np.sum(f2)
I_separado = I1 + I2

# 2. Calculamos la integral agrupando los integrandos primero: f(q) = 4q
f_junto = (q**2) * (4.0 / q)
I_junto = delta_q * np.sum(f_junto)

# Valor analítico real 
I_exacto = 2 * (q_max**2)

# Resultados
print("Resultados")
print(f"Valor de I1 por separado : {I1:e}")
print(f"Valor de I2 por separado : {I2:e}")
print(f"Suma I1 + I2 (Método 1)  : {I_separado}")
print(f"Integral de 4q (Método 2): {I_junto:.8f}")
print(f"Valor exacto a mano      : {I_exacto}")
print("\n" + "="*60)
print(" ¿Por qué son diferentes los resultados? Compare con el resultado exacto de la integral I")
print("="*60)
print("""
1. Cancelación catastrófica (Error del PC):
   Al evaluar I1 e I2 por separado, el término (1/q^3) cerca de q=0 
   hace que la suma dé números grandes (del orden de 10^13 y -10^13). 
   Cuando la computadora intenta restar dos números tan absurdamente 
   grandes en formato decimal (float64), se pierden los decimales 
   chicos y el resultado da 0.0, perdiendo el 0.02 real.

2. Divergencia en el papel (Error matemático):
   Matemáticamente, si intentas hacer I1 e I2 por separado, ambas 
   integrales explotan a +infinito y -infinito en q=0. O sea, estás 
   haciendo (infinito - infinito), que es una indeterminación.

3. Sobre el segundo metodo:
   Al simplificar el álgebra ANTES de meterlo al código (f1 + f2 = 4q), 
   eliminamos la división por cero y la indeterminación. El valor 
   obtenido (0.02000004) es prácticamente igual al exacto (0.02); esa 
   diferencia mínima de 0.00000004 es solo el error propio de aproximar 
   una curva usando rectángulos (Suma de Riemann).
""")

# Tarea 5.6

## 1. ¿Por qué calcular el determinante por cofactores requiere $n!$ operaciones?

Si calculamos el determinante de una matriz de $n \times n$ usando expansión por cofactores, lo que hacemos en la práctica es descomponer el problema en $n$ determinantes más chicos, de tamaño $(n-1) \times (n-1)$.

Y a su vez para cada uno de esos determinantes necesitamos calcular otros $n-1$ determinantes aún más pequeños, y así sucesivamente hasta llegar a matrices de $1 \times 1$.

Multiplicando la cantidad de operaciones que se generan en cada paso, nos encontramos con la siguiente cadena:

$$
n(n-1)(n-2)\cdots 2\cdot 1=n!
$$

Esto significa que el costo computacional de este procedimiento crece de forma factorial:

$$
T_{\det}(n)=O(n!)
$$

## 2. ¿Cuántas operaciones se necesitan en total para la matriz adjunta?

Para armar la matriz adjunta necesitamos calcular un cofactor por cada posición de la matriz, lo que nos da un total de $n^2$ cofactores.

Como cada uno de estos cofactores requiere resolver un determinante de tamaño $(n-1) \times (n-1)$ —lo que a su vez toma $(n-1)!$ operaciones—, el total bruto se obtiene multiplicando ambas partes:

$$
n^2(n-1)!
$$

Como sabemos por propiedad de los factoriales que $n!=n(n-1)!$, podemos reescribir la expresión así:

$$
n^2(n-1)!=n[n(n-1)!]=n\cdot n!
$$

Por lo tanto, para calcular la matriz adjunta necesitamos en total:

$$
\boxed{n\cdot n! \text{ operaciones}}
$$

## 3. ¿Cómo se comporta el total de operaciones para un $n$ grande?

Para saber el costo global sumamos las operaciones del determinante con las de la matriz adjunta:

$$
T(n)\approx n!+n^2(n-1)!
$$

Sustituyendo el equivalente que calculamos antes, nos queda:

$$
T(n)\approx n!+n\cdot n!
$$

Si sacamos factor común:

$$
T(n)\approx (n+1)n!
$$

Cuando $n$ es un número grande, el término $n\cdot n!$ domina por completo el crecimiento, por lo que el orden general del algoritmo se define como:

$$
\boxed{T(n)=O(n\cdot n!)}
$$

Esto nos muestra que la cantidad de operaciones explota rapidísimo a medida que la matriz crece. Por esta razón, el método de los cofactores es totalmente inviable para matrices grandes en la vida real, en los que se prefieren caminos mucho más eficientes como la factorización LU, cuyo costo es de orden $O(n^3)$.
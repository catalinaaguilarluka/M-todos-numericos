import random

def unir(color, numeros):
    return {color + numero for numero in numeros}

urna = unir('B', '12345678') | unir('A', '123456') | unir('R', '123456789')

def todos_rojos(evento):
    s = [i[0] for i in evento]
    return s.count('R') == 4

def prob(evento, espacio):
    return len(evento) / len(espacio)

# haremos muchas extracciones de 4 bolas CON reemplazo
muestra = {tuple(random.choices(list(urna), k=4)) for i in range(100000)}

# casos donde las cuatro bolas son rojas
rojos = {e for e in muestra if todos_rojos(e)}

probabilidad = prob(rojos, muestra)

print(probabilidad)
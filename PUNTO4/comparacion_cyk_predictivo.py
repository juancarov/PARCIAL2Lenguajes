import time
import random
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# Parser usando el algoritmo CYK
# ------------------------------------------------------------
def cyk_parse(cadena, gramatica, simbolo_inicial):
    n = len(cadena)
    if n == 0:
        return False

    tabla = [[set() for _ in range(n)] for _ in range(n)]

    # Casos base: reglas A -> a
    for i in range(n):
        for A, reglas in gramatica.items():
            for regla in reglas:
                if len(regla) == 1 and regla[0] == cadena[i]:
                    tabla[i][i].add(A)

    # Combinaciones
    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            for k in range(i, j):
                for A, reglas in gramatica.items():
                    for regla in reglas:
                        if len(regla) == 2:
                            B, C = regla
                            if B in tabla[i][k] and C in tabla[k + 1][j]:
                                tabla[i][j].add(A)

    return simbolo_inicial in tabla[0][n - 1]


# ------------------------------------------------------------
# Parser predictivo simple (recursivo)
# ------------------------------------------------------------
def parser_predictivo(cadena, indice=0):
    def E():
        nonlocal indice
        if T():
            while indice < len(cadena) and cadena[indice] == '+':
                indice += 1
                if not T():
                    return False
            return True
        return False

    def T():
        nonlocal indice
        if F():
            while indice < len(cadena) and cadena[indice] == '*':
                indice += 1
                if not F():
                    return False
            return True
        return False

    def F():
        nonlocal indice
        if indice < len(cadena) and cadena[indice] == 'a':
            indice += 1
            return True
        elif indice < len(cadena) and cadena[indice] == '(':
            indice += 1
            if not E():
                return False
            if indice < len(cadena) and cadena[indice] == ')':
                indice += 1
                return True
        return False

    resultado = E()
    return resultado and indice == len(cadena)


# ------------------------------------------------------------
# Comparación de rendimiento
# ------------------------------------------------------------
def generar_cadena(n):
    return [random.choice(['a', '+', '*', '(', ')']) for _ in range(n)]

# Gramática para CYK (forma normal de Chomsky simplificada)
gramatica = {
    'S': [['A', 'B'], ['A']],
    'A': [['a'], ['A', 'a']],
    'B': [['b'], ['B', 'b']]
}

longitudes = [5, 10, 20, 30, 40, 50, 60]
tiempos_cyk = []
tiempos_pred = []

for n in longitudes:
    cadena = ['a'] * n  # cadena simple de 'a' repetidas

    inicio = time.time()
    cyk_parse(cadena, gramatica, 'S')
    tiempos_cyk.append(time.time() - inicio)

    expr = 'a+' * (n // 2) + 'a'
    inicio = time.time()
    parser_predictivo(list(expr.replace(' ', '')))
    tiempos_pred.append(time.time() - inicio)

# ------------------------------------------------------------
# Gráfica comparativa
# ------------------------------------------------------------
plt.plot(longitudes, tiempos_cyk, label="Parser CYK (O(n³))")
plt.plot(longitudes, tiempos_pred, label="Parser Predictivo (O(n))")
plt.xlabel("Tamaño de la cadena")
plt.ylabel("Tiempo de ejecución (s)")
plt.title("Comparación de rendimiento entre parser CYK y predictivo")
plt.legend()
plt.grid(True)
plt.show()

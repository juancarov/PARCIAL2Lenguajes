def parser(expr):
    tokens = expr.replace("(", " ( ").replace(")", " ) ").split()
    tokens.append("$")  # símbolo de fin de entrada
    pila = []
    i = 0

    def reduce():
        # E → E + T
        if len(pila) >= 3 and pila[-3:] == ['E', '+', 'T']:
            pila[-3:] = ['E']; return True
        # T → T * F
        if len(pila) >= 3 and pila[-3:] == ['T', '*', 'F']:
            pila[-3:] = ['T']; return True
        # F → ( E )
        if len(pila) >= 3 and pila[-3:] == ['(', 'E', ')']:
            pila[-3:] = ['F']; return True
        # F → id
        if len(pila) >= 1 and pila[-1] == 'id':
            pila[-1:] = ['F']; return True
        # T → F
        if len(pila) >= 1 and pila[-1] == 'F':
            pila[-1:] = ['T']; return True
        # E → T
        if len(pila) >= 1 and pila[-1] == 'T':
            pila[-1:] = ['E']; return True
        return False

    while True:
        # Intentar reducir antes de hacer shift
        if reduce():
            continue

        # Aceptar si se llegó al final correctamente
        if i >= len(tokens):
            return False
        if tokens[i] == '$' and pila == ['E']:
            return True

        # Desplazar siguiente token si queda entrada
        if tokens[i] != '$':
            pila.append(tokens[i])
            i += 1
            continue

        # Si no hay más reducciones ni desplazamientos válidos
        return False


# Pruebas
tests = [
    "id + id * id",
    "( id )",
    "id * ( id + id )",
    "id +",
    "( id * )"
]

for t in tests:
    resultado = "Válida" if parser(t) else "Inválida"
    print(f"{t:<25} -> {resultado}")

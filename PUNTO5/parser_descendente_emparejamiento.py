class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.i = 0
        self.emparejamientos = []

    def actual(self):
        return self.tokens[self.i] if self.i < len(self.tokens) else '$'

    def emparejar(self, esperado):
        if self.actual() == esperado:
            self.emparejamientos.append((esperado, "✓"))
            self.i += 1
            return True
        else:
            self.emparejamientos.append((esperado, f"x (se encontró {self.actual()})"))
            return False

    def E(self):
        if not self.T(): return False
        return self.Ep()

    def Ep(self):
        if self.actual() == '+':
            self.emparejar('+')
            if not self.T(): return False
            return self.Ep()
        return True

    def T(self):
        if not self.F(): return False
        return self.Tp()

    def Tp(self):
        if self.actual() == '*':
            self.emparejar('*')
            if not self.F(): return False
            return self.Tp()
        return True

    def F(self):
        if self.actual() == '(':
            self.emparejar('(')
            if not self.E(): return False
            return self.emparejar(')')
        elif self.actual() == 'id':
            return self.emparejar('id')
        return False

    def analizar(self):
        resultado = self.E() and self.actual() == '$'
        return resultado, self.emparejamientos


def tokenizar(expr):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isspace():
            i += 1
            continue
        if c.isalpha():
            j = i
            while j < len(expr) and expr[j].isalnum():
                j += 1
            tokens.append("id")
            i = j
        elif c in "+*()":
            tokens.append(c)
            i += 1
        else:
            raise ValueError(f"Símbolo no válido: {c}")
    tokens.append('$')
    return tokens


if __name__ == "__main__":
    expr = "id + id * ( id + id )"
    tokens = tokenizar(expr)
    parser = Parser(tokens)
    resultado, emp = parser.analizar()

    print("Expresión:", expr)
    print("Tokens:", tokens)
    print("\nEmparejamientos:")
    for e in emp:
        print(f"  {e[0]:<5} → {e[1]}")
    print("\nResultado final:", "Aceptada" if resultado else "Rechazada")

from antlr4 import *
from gramaticacrudLexer import gramaticacrudLexer
from gramaticacrudParser import gramaticacrudParser
from VisitorCRUD import VisitorCRUD


def ejecutar_codigo(codigo):
    entrada = InputStream(codigo)
    lexer = gramaticacrudLexer(entrada)
    tokens = CommonTokenStream(lexer)
    parser = gramaticacrudParser(tokens)
    arbol = parser.programa()
    visitador = VisitorCRUD()
    visitador.visit(arbol)
    return visitador.db.tablas


codigo = """
CREAR TABLA personas;
CREAR TABLA productos;

INSERTAR EN personas VALORES (1, "Ana");
INSERTAR EN personas VALORES (2, "Luis");
INSERTAR EN personas VALORES (3, "Sofía");

INSERTAR EN productos VALORES (10, "Café");
INSERTAR EN productos VALORES (11, "Pan");
INSERTAR EN productos VALORES (12, "Leche");

ACTUALIZAR personas COLOCAR 1 = "Carlos" DONDE 0 = 2;
ELIMINAR DE personas DONDE 0 = 1;

INSERTAR EN productos VALORES (13, "Chocolate");
ACTUALIZAR productos COLOCAR 1 = "Pan integral" DONDE 0 = 11;

LEER DE personas;
LEER DE productos;
"""

print("Simulación de lenguaje CRUD en memoria")
print("======================================")
print("Código de entrada:\n")
print(codigo)
print("======================================\n")

tablas = ejecutar_codigo(codigo)

print("Estado final de la base de datos")
print("======================================")
for nombre, filas in tablas.items():
    print(f"\nTabla: {nombre}")
    if not filas:
        print("   (sin registros)")
    else:
        for fila in filas:
            print("   ", fila)

print("\nEjecución finalizada correctamente.")

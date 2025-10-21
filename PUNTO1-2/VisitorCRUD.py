from gramaticacrudVisitor import gramaticacrudVisitor
from gramaticacrudParser import gramaticacrudParser

class BaseDeDatos:
    def __init__(self):
        self.tablas = {}

    def crear(self, nombre):
        if nombre in self.tablas:
            raise Exception(f"La tabla '{nombre}' ya existe.")
        self.tablas[nombre] = []

    def insertar(self, nombre, valores):
        if nombre not in self.tablas:
            raise Exception(f"La tabla '{nombre}' no existe.")
        self.tablas[nombre].append(tuple(valores))

    def leer(self, nombre, condicion):
        if nombre not in self.tablas:
            raise Exception(f"La tabla '{nombre}' no existe.")
        filas = self.tablas[nombre]
        if not condicion:
            return filas
        campo, op, valor = condicion
        return [f for f in filas if self._cumple(f, campo, op, valor)]

    def actualizar(self, nombre, asignaciones, condicion):
        if nombre not in self.tablas:
            raise Exception(f"La tabla '{nombre}' no existe.")
        nuevas = []
        actualizadas = 0
        for fila in self.tablas[nombre]:
            if not condicion or self._cumple(fila, *condicion):
                nueva = list(fila)
                for campo, valor in asignaciones:
                    try:
                        idx = int(campo)
                        nueva[idx] = valor
                    except:
                        pass
                nuevas.append(tuple(nueva))
                actualizadas += 1
            else:
                nuevas.append(fila)
        self.tablas[nombre] = nuevas
        return actualizadas

    def eliminar(self, nombre, condicion):
        if nombre not in self.tablas:
            raise Exception(f"La tabla '{nombre}' no existe.")
        nuevas = []
        eliminadas = 0
        for fila in self.tablas[nombre]:
            if not condicion or self._cumple(fila, *condicion):
                eliminadas += 1
            else:
                nuevas.append(fila)
        self.tablas[nombre] = nuevas
        return eliminadas

    def _cumple(self, fila, campo, op, valor):
        try:
            idx = int(campo)
            izq = fila[idx]
        except:
            izq = fila[0]
        if op == '=': return izq == valor
        if op == '!=': return izq != valor
        if op == '<': return izq < valor
        if op == '<=': return izq <= valor
        if op == '>': return izq > valor
        if op == '>=': return izq >= valor
        return False


class VisitorCRUD(gramaticacrudVisitor):
    def __init__(self):
        self.db = BaseDeDatos()

    def visitCrearTabla(self, ctx: gramaticacrudParser.CrearTablaContext):
        nombre = ctx.IDENT().getText()
        self.db.crear(nombre)
        return f"Tabla '{nombre}' creada."

    def visitInsertarFila(self, ctx: gramaticacrudParser.InsertarFilaContext):
        nombre = ctx.IDENT().getText()
        valores = []
        for v in ctx.listaValores().valor():
            if v.TEXTO():
                valores.append(v.TEXTO().getText().strip('"'))
            else:
                valores.append(int(v.NUM().getText()))
        self.db.insertar(nombre, valores)
        return f"Insertado en '{nombre}': {valores}"

    def visitLeerDatos(self, ctx: gramaticacrudParser.LeerDatosContext):
        nombre = ctx.IDENT().getText()
        cond = None
        if ctx.condicion():
            campo = ctx.condicion().children[0].getText()
            op = ctx.condicion().comparador().getText()
            v = ctx.condicion().valor()
            valor = v.TEXTO().getText().strip('"') if v.TEXTO() else int(v.NUM().getText())
            cond = (campo, op, valor)
        return self.db.leer(nombre, cond)

    def visitActualizarDatos(self, ctx: gramaticacrudParser.ActualizarDatosContext):
        nombre = ctx.IDENT().getText()
        asign = []
        for a in ctx.listaAsignaciones().asignacion():
            campo = a.children[0].getText()
            v = a.valor()
            valor = v.TEXTO().getText().strip('"') if v.TEXTO() else int(v.NUM().getText())
            asign.append((campo, valor))
        cond = None
        if ctx.condicion():
            campo = ctx.condicion().children[0].getText()
            op = ctx.condicion().comparador().getText()
            v = ctx.condicion().valor()
            valor = v.TEXTO().getText().strip('"') if v.TEXTO() else int(v.NUM().getText())
            cond = (campo, op, valor)
        n = self.db.actualizar(nombre, asign, cond)
        return f"Actualizadas en '{nombre}': {n}"

    def visitEliminarDatos(self, ctx: gramaticacrudParser.EliminarDatosContext):
        nombre = ctx.IDENT().getText()
        cond = None
        if ctx.condicion():
            campo = ctx.condicion().children[0].getText()
            op = ctx.condicion().comparador().getText()
            v = ctx.condicion().valor()
            valor = v.TEXTO().getText().strip('"') if v.TEXTO() else int(v.NUM().getText())
            cond = (campo, op, valor)
        n = self.db.eliminar(nombre, cond)
        return f"Eliminadas en '{nombre}': {n}"

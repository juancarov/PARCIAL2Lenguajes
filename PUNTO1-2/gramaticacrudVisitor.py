# Generated from gramaticacrud.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .gramaticacrudParser import gramaticacrudParser
else:
    from gramaticacrudParser import gramaticacrudParser

# This class defines a complete generic visitor for a parse tree produced by gramaticacrudParser.

class gramaticacrudVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by gramaticacrudParser#programa.
    def visitPrograma(self, ctx:gramaticacrudParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#operacionCrud.
    def visitOperacionCrud(self, ctx:gramaticacrudParser.OperacionCrudContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#crearTabla.
    def visitCrearTabla(self, ctx:gramaticacrudParser.CrearTablaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#insertarFila.
    def visitInsertarFila(self, ctx:gramaticacrudParser.InsertarFilaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#leerDatos.
    def visitLeerDatos(self, ctx:gramaticacrudParser.LeerDatosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#actualizarDatos.
    def visitActualizarDatos(self, ctx:gramaticacrudParser.ActualizarDatosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#eliminarDatos.
    def visitEliminarDatos(self, ctx:gramaticacrudParser.EliminarDatosContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#listaAsignaciones.
    def visitListaAsignaciones(self, ctx:gramaticacrudParser.ListaAsignacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#asignacion.
    def visitAsignacion(self, ctx:gramaticacrudParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#listaValores.
    def visitListaValores(self, ctx:gramaticacrudParser.ListaValoresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#condicion.
    def visitCondicion(self, ctx:gramaticacrudParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#valor.
    def visitValor(self, ctx:gramaticacrudParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by gramaticacrudParser#comparador.
    def visitComparador(self, ctx:gramaticacrudParser.ComparadorContext):
        return self.visitChildren(ctx)



del gramaticacrudParser
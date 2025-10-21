# Generated from gramaticacrud.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,26,106,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,1,0,
        1,0,5,0,30,8,0,10,0,12,0,33,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,
        42,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,4,1,4,1,
        4,1,4,1,4,3,4,61,8,4,1,5,1,5,1,5,1,5,1,5,1,5,3,5,69,8,5,1,6,1,6,
        1,6,1,6,1,6,3,6,76,8,6,1,7,1,7,1,7,5,7,81,8,7,10,7,12,7,84,9,7,1,
        8,1,8,1,8,1,8,1,9,1,9,1,9,5,9,93,8,9,10,9,12,9,96,9,9,1,10,1,10,
        1,10,1,10,1,11,1,11,1,12,1,12,1,12,0,0,13,0,2,4,6,8,10,12,14,16,
        18,20,22,24,0,3,1,0,22,23,1,0,23,24,1,0,5,10,102,0,31,1,0,0,0,2,
        41,1,0,0,0,4,43,1,0,0,0,6,47,1,0,0,0,8,55,1,0,0,0,10,62,1,0,0,0,
        12,70,1,0,0,0,14,77,1,0,0,0,16,85,1,0,0,0,18,89,1,0,0,0,20,97,1,
        0,0,0,22,101,1,0,0,0,24,103,1,0,0,0,26,27,3,2,1,0,27,28,5,1,0,0,
        28,30,1,0,0,0,29,26,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,
        0,0,0,32,34,1,0,0,0,33,31,1,0,0,0,34,35,5,0,0,1,35,1,1,0,0,0,36,
        42,3,4,2,0,37,42,3,6,3,0,38,42,3,8,4,0,39,42,3,10,5,0,40,42,3,12,
        6,0,41,36,1,0,0,0,41,37,1,0,0,0,41,38,1,0,0,0,41,39,1,0,0,0,41,40,
        1,0,0,0,42,3,1,0,0,0,43,44,5,11,0,0,44,45,5,12,0,0,45,46,5,22,0,
        0,46,5,1,0,0,0,47,48,5,13,0,0,48,49,5,14,0,0,49,50,5,22,0,0,50,51,
        5,15,0,0,51,52,5,2,0,0,52,53,3,18,9,0,53,54,5,3,0,0,54,7,1,0,0,0,
        55,56,5,16,0,0,56,57,5,17,0,0,57,60,5,22,0,0,58,59,5,18,0,0,59,61,
        3,20,10,0,60,58,1,0,0,0,60,61,1,0,0,0,61,9,1,0,0,0,62,63,5,19,0,
        0,63,64,5,22,0,0,64,65,5,20,0,0,65,68,3,14,7,0,66,67,5,18,0,0,67,
        69,3,20,10,0,68,66,1,0,0,0,68,69,1,0,0,0,69,11,1,0,0,0,70,71,5,21,
        0,0,71,72,5,17,0,0,72,75,5,22,0,0,73,74,5,18,0,0,74,76,3,20,10,0,
        75,73,1,0,0,0,75,76,1,0,0,0,76,13,1,0,0,0,77,82,3,16,8,0,78,79,5,
        4,0,0,79,81,3,16,8,0,80,78,1,0,0,0,81,84,1,0,0,0,82,80,1,0,0,0,82,
        83,1,0,0,0,83,15,1,0,0,0,84,82,1,0,0,0,85,86,7,0,0,0,86,87,5,5,0,
        0,87,88,3,22,11,0,88,17,1,0,0,0,89,94,3,22,11,0,90,91,5,4,0,0,91,
        93,3,22,11,0,92,90,1,0,0,0,93,96,1,0,0,0,94,92,1,0,0,0,94,95,1,0,
        0,0,95,19,1,0,0,0,96,94,1,0,0,0,97,98,7,0,0,0,98,99,3,24,12,0,99,
        100,3,22,11,0,100,21,1,0,0,0,101,102,7,1,0,0,102,23,1,0,0,0,103,
        104,7,2,0,0,104,25,1,0,0,0,7,31,41,60,68,75,82,94
    ]

class gramaticacrudParser ( Parser ):

    grammarFileName = "gramaticacrud.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'('", "')'", "','", "'='", "'!='", 
                     "'<'", "'<='", "'>'", "'>='", "'CREAR'", "'TABLA'", 
                     "'INSERTAR'", "'EN'", "'VALORES'", "'LEER'", "'DE'", 
                     "'DONDE'", "'ACTUALIZAR'", "'COLOCAR'", "'ELIMINAR'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "CREAR", "TABLA", 
                      "INSERTAR", "EN", "VALORES", "LEER", "DE", "DONDE", 
                      "ACTUALIZAR", "COLOCAR", "ELIMINAR", "IDENT", "NUM", 
                      "TEXTO", "WS", "COMENTARIO" ]

    RULE_programa = 0
    RULE_operacionCrud = 1
    RULE_crearTabla = 2
    RULE_insertarFila = 3
    RULE_leerDatos = 4
    RULE_actualizarDatos = 5
    RULE_eliminarDatos = 6
    RULE_listaAsignaciones = 7
    RULE_asignacion = 8
    RULE_listaValores = 9
    RULE_condicion = 10
    RULE_valor = 11
    RULE_comparador = 12

    ruleNames =  [ "programa", "operacionCrud", "crearTabla", "insertarFila", 
                   "leerDatos", "actualizarDatos", "eliminarDatos", "listaAsignaciones", 
                   "asignacion", "listaValores", "condicion", "valor", "comparador" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    CREAR=11
    TABLA=12
    INSERTAR=13
    EN=14
    VALORES=15
    LEER=16
    DE=17
    DONDE=18
    ACTUALIZAR=19
    COLOCAR=20
    ELIMINAR=21
    IDENT=22
    NUM=23
    TEXTO=24
    WS=25
    COMENTARIO=26

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(gramaticacrudParser.EOF, 0)

        def operacionCrud(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticacrudParser.OperacionCrudContext)
            else:
                return self.getTypedRuleContext(gramaticacrudParser.OperacionCrudContext,i)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_programa

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = gramaticacrudParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2697216) != 0):
                self.state = 26
                self.operacionCrud()
                self.state = 27
                self.match(gramaticacrudParser.T__0)
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
            self.match(gramaticacrudParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionCrudContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def crearTabla(self):
            return self.getTypedRuleContext(gramaticacrudParser.CrearTablaContext,0)


        def insertarFila(self):
            return self.getTypedRuleContext(gramaticacrudParser.InsertarFilaContext,0)


        def leerDatos(self):
            return self.getTypedRuleContext(gramaticacrudParser.LeerDatosContext,0)


        def actualizarDatos(self):
            return self.getTypedRuleContext(gramaticacrudParser.ActualizarDatosContext,0)


        def eliminarDatos(self):
            return self.getTypedRuleContext(gramaticacrudParser.EliminarDatosContext,0)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_operacionCrud

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionCrud" ):
                return visitor.visitOperacionCrud(self)
            else:
                return visitor.visitChildren(self)




    def operacionCrud(self):

        localctx = gramaticacrudParser.OperacionCrudContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_operacionCrud)
        try:
            self.state = 41
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 36
                self.crearTabla()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 37
                self.insertarFila()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.leerDatos()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 39
                self.actualizarDatos()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 5)
                self.state = 40
                self.eliminarDatos()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CrearTablaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREAR(self):
            return self.getToken(gramaticacrudParser.CREAR, 0)

        def TABLA(self):
            return self.getToken(gramaticacrudParser.TABLA, 0)

        def IDENT(self):
            return self.getToken(gramaticacrudParser.IDENT, 0)

        def getRuleIndex(self):
            return gramaticacrudParser.RULE_crearTabla

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCrearTabla" ):
                return visitor.visitCrearTabla(self)
            else:
                return visitor.visitChildren(self)




    def crearTabla(self):

        localctx = gramaticacrudParser.CrearTablaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_crearTabla)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(gramaticacrudParser.CREAR)
            self.state = 44
            self.match(gramaticacrudParser.TABLA)
            self.state = 45
            self.match(gramaticacrudParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertarFilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERTAR(self):
            return self.getToken(gramaticacrudParser.INSERTAR, 0)

        def EN(self):
            return self.getToken(gramaticacrudParser.EN, 0)

        def IDENT(self):
            return self.getToken(gramaticacrudParser.IDENT, 0)

        def VALORES(self):
            return self.getToken(gramaticacrudParser.VALORES, 0)

        def listaValores(self):
            return self.getTypedRuleContext(gramaticacrudParser.ListaValoresContext,0)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_insertarFila

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertarFila" ):
                return visitor.visitInsertarFila(self)
            else:
                return visitor.visitChildren(self)




    def insertarFila(self):

        localctx = gramaticacrudParser.InsertarFilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_insertarFila)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(gramaticacrudParser.INSERTAR)
            self.state = 48
            self.match(gramaticacrudParser.EN)
            self.state = 49
            self.match(gramaticacrudParser.IDENT)
            self.state = 50
            self.match(gramaticacrudParser.VALORES)
            self.state = 51
            self.match(gramaticacrudParser.T__1)
            self.state = 52
            self.listaValores()
            self.state = 53
            self.match(gramaticacrudParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LeerDatosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEER(self):
            return self.getToken(gramaticacrudParser.LEER, 0)

        def DE(self):
            return self.getToken(gramaticacrudParser.DE, 0)

        def IDENT(self):
            return self.getToken(gramaticacrudParser.IDENT, 0)

        def DONDE(self):
            return self.getToken(gramaticacrudParser.DONDE, 0)

        def condicion(self):
            return self.getTypedRuleContext(gramaticacrudParser.CondicionContext,0)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_leerDatos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLeerDatos" ):
                return visitor.visitLeerDatos(self)
            else:
                return visitor.visitChildren(self)




    def leerDatos(self):

        localctx = gramaticacrudParser.LeerDatosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_leerDatos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(gramaticacrudParser.LEER)
            self.state = 56
            self.match(gramaticacrudParser.DE)
            self.state = 57
            self.match(gramaticacrudParser.IDENT)
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 58
                self.match(gramaticacrudParser.DONDE)
                self.state = 59
                self.condicion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ActualizarDatosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACTUALIZAR(self):
            return self.getToken(gramaticacrudParser.ACTUALIZAR, 0)

        def IDENT(self):
            return self.getToken(gramaticacrudParser.IDENT, 0)

        def COLOCAR(self):
            return self.getToken(gramaticacrudParser.COLOCAR, 0)

        def listaAsignaciones(self):
            return self.getTypedRuleContext(gramaticacrudParser.ListaAsignacionesContext,0)


        def DONDE(self):
            return self.getToken(gramaticacrudParser.DONDE, 0)

        def condicion(self):
            return self.getTypedRuleContext(gramaticacrudParser.CondicionContext,0)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_actualizarDatos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActualizarDatos" ):
                return visitor.visitActualizarDatos(self)
            else:
                return visitor.visitChildren(self)




    def actualizarDatos(self):

        localctx = gramaticacrudParser.ActualizarDatosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_actualizarDatos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(gramaticacrudParser.ACTUALIZAR)
            self.state = 63
            self.match(gramaticacrudParser.IDENT)
            self.state = 64
            self.match(gramaticacrudParser.COLOCAR)
            self.state = 65
            self.listaAsignaciones()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 66
                self.match(gramaticacrudParser.DONDE)
                self.state = 67
                self.condicion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliminarDatosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELIMINAR(self):
            return self.getToken(gramaticacrudParser.ELIMINAR, 0)

        def DE(self):
            return self.getToken(gramaticacrudParser.DE, 0)

        def IDENT(self):
            return self.getToken(gramaticacrudParser.IDENT, 0)

        def DONDE(self):
            return self.getToken(gramaticacrudParser.DONDE, 0)

        def condicion(self):
            return self.getTypedRuleContext(gramaticacrudParser.CondicionContext,0)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_eliminarDatos

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliminarDatos" ):
                return visitor.visitEliminarDatos(self)
            else:
                return visitor.visitChildren(self)




    def eliminarDatos(self):

        localctx = gramaticacrudParser.EliminarDatosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_eliminarDatos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(gramaticacrudParser.ELIMINAR)
            self.state = 71
            self.match(gramaticacrudParser.DE)
            self.state = 72
            self.match(gramaticacrudParser.IDENT)
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 73
                self.match(gramaticacrudParser.DONDE)
                self.state = 74
                self.condicion()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAsignacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticacrudParser.AsignacionContext)
            else:
                return self.getTypedRuleContext(gramaticacrudParser.AsignacionContext,i)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_listaAsignaciones

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAsignaciones" ):
                return visitor.visitListaAsignaciones(self)
            else:
                return visitor.visitChildren(self)




    def listaAsignaciones(self):

        localctx = gramaticacrudParser.ListaAsignacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listaAsignaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.asignacion()
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 78
                self.match(gramaticacrudParser.T__3)
                self.state = 79
                self.asignacion()
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor(self):
            return self.getTypedRuleContext(gramaticacrudParser.ValorContext,0)


        def IDENT(self):
            return self.getToken(gramaticacrudParser.IDENT, 0)

        def NUM(self):
            return self.getToken(gramaticacrudParser.NUM, 0)

        def getRuleIndex(self):
            return gramaticacrudParser.RULE_asignacion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = gramaticacrudParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_asignacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 86
            self.match(gramaticacrudParser.T__4)
            self.state = 87
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaValoresContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def valor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(gramaticacrudParser.ValorContext)
            else:
                return self.getTypedRuleContext(gramaticacrudParser.ValorContext,i)


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_listaValores

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaValores" ):
                return visitor.visitListaValores(self)
            else:
                return visitor.visitChildren(self)




    def listaValores(self):

        localctx = gramaticacrudParser.ListaValoresContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_listaValores)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.valor()
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 90
                self.match(gramaticacrudParser.T__3)
                self.state = 91
                self.valor()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparador(self):
            return self.getTypedRuleContext(gramaticacrudParser.ComparadorContext,0)


        def valor(self):
            return self.getTypedRuleContext(gramaticacrudParser.ValorContext,0)


        def IDENT(self):
            return self.getToken(gramaticacrudParser.IDENT, 0)

        def NUM(self):
            return self.getToken(gramaticacrudParser.NUM, 0)

        def getRuleIndex(self):
            return gramaticacrudParser.RULE_condicion

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = gramaticacrudParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not(_la==22 or _la==23):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 98
            self.comparador()
            self.state = 99
            self.valor()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TEXTO(self):
            return self.getToken(gramaticacrudParser.TEXTO, 0)

        def NUM(self):
            return self.getToken(gramaticacrudParser.NUM, 0)

        def getRuleIndex(self):
            return gramaticacrudParser.RULE_valor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValor" ):
                return visitor.visitValor(self)
            else:
                return visitor.visitChildren(self)




    def valor(self):

        localctx = gramaticacrudParser.ValorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_valor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            _la = self._input.LA(1)
            if not(_la==23 or _la==24):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparadorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return gramaticacrudParser.RULE_comparador

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparador" ):
                return visitor.visitComparador(self)
            else:
                return visitor.visitChildren(self)




    def comparador(self):

        localctx = gramaticacrudParser.ComparadorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_comparador)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx






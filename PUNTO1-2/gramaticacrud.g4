grammar gramaticacrud;

programa : (operacionCrud ';')* EOF ;

operacionCrud
    : crearTabla
    | insertarFila
    | leerDatos
    | actualizarDatos
    | eliminarDatos
    ;

crearTabla
    : CREAR TABLA IDENT
    ;

insertarFila
    : INSERTAR EN IDENT VALORES '(' listaValores ')'
    ;

leerDatos
    : LEER DE IDENT (DONDE condicion)?
    ;

actualizarDatos
    : ACTUALIZAR IDENT COLOCAR listaAsignaciones (DONDE condicion)?
    ;

eliminarDatos
    : ELIMINAR DE IDENT (DONDE condicion)?
    ;

listaAsignaciones
    : asignacion (',' asignacion)*
    ;

asignacion
    : (IDENT | NUM) '=' valor
    ;

listaValores
    : valor (',' valor)*
    ;

condicion
    : (IDENT | NUM) comparador valor
    ;

valor
    : TEXTO
    | NUM
    ;

comparador
    : '=' | '!=' | '<' | '<=' | '>' | '>='
    ;

CREAR : 'CREAR';
TABLA : 'TABLA';
INSERTAR : 'INSERTAR';
EN : 'EN';
VALORES : 'VALORES';
LEER : 'LEER';
DE : 'DE';
DONDE : 'DONDE';
ACTUALIZAR : 'ACTUALIZAR';
COLOCAR : 'COLOCAR';
ELIMINAR : 'ELIMINAR';

IDENT : [a-zA-Z_][a-zA-Z_0-9]* ;
NUM   : [0-9]+ ;
TEXTO : '"' (~["\r\n])* '"' ;

WS : [ \t\r\n]+ -> skip ;
COMENTARIO : '--' ~[\r\n]* -> skip ;

# =================================================================
# ast_nodos.py: Definición de Clases de Nodos AST y Tabla de Gramática
# =================================================================

# --- Asignación de Códigos No Terminales (NT GOTO) ---
# **IMPORTANTE:** Estos códigos deben coincidir con las columnas GOTO de tu matriz 'lis'
NT_Programa = 24
NT_Definiciones = 25
NT_Definicion = 26
NT_DefVar = 27
NT_ListaVar = 28
# Añade el resto de códigos NT (NT_DefFunc = 29, NT_Parametros = 30, etc.) aquí...


# =================================================================
# 1. CLASES BASE Y NODOS TERMINALES
# =================================================================

class Nodo:
    """Clase base para todos los nodos del Árbol de Sintaxis Abstracta."""
    def __init__(self, hijos=None):
        self.hijos = hijos if hijos is not None else []
        
    def muestraArbol(self, nivel=0):
        tab = "  " * nivel
        print(f"{tab}├── {self.__class__.__name__}")
        
        for hijo in self.hijos:
            if hasattr(hijo, 'muestraArbol'):
                hijo.muestraArbol(nivel + 1)
            else:
                # Caso para nodos que no son clases de reducción (e.g., TokenNode)
                valor = getattr(hijo, 'valor', f"TOKEN SIN VALOR")
                print(f"{tab}  └── T: '{valor}'")


class TokenNode(Nodo):
    """Nodo para símbolos terminales con un valor léxico."""
    def __init__(self, token_code, valor):
        # Los nodos terminales no suelen tener hijos en el AST
        super().__init__() 
        self.code = token_code
        self.valor = valor
    
    def muestraArbol(self, nivel=0):
        tab = "  " * nivel
        print(f"{tab}├── T: '{self.valor}' (Code: {self.code})")

class Tipo(TokenNode): pass
class ID(TokenNode): pass # Clase para identificador


# =================================================================
# 2. CLASES DE REDUCCIÓN (Subconjunto de la Gramática)
# =================================================================

# --- Reglas Nulas (Épsilon) ---

# R7: <ListaVar> -> \e
class ListaVar_E(Nodo): 
    def muestraArbol(self, nivel=0):
        tab = "  " * nivel
        print(f"{tab}├── <ListaVar> [NULL]")

# R2: <Definiciones> -> \e
class Definiciones_E(Nodo): 
    def muestraArbol(self, nivel=0):
        tab = "  " * nivel
        print(f"{tab}├── <Definiciones> [NULL]")


# --- Reglas de Definición ---

# R6: <DefVar> ::= tipo identificador <ListaVar> ;
class DefVar(Nodo):
    # hijos: [Nodo(tipo), Nodo(id), Nodo(<ListaVar>), Nodo(;)]
    def __init__(self, hijos):
        super().__init__()
        # Almacenamos solo los nodos esenciales para el AST (tipo, id, lista)
        self.tipo_nodo = hijos[0]
        self.id_nodo = hijos[1]
        self.listavar_nodo = hijos[2]
        self.hijos = [self.tipo_nodo, self.id_nodo, self.listavar_nodo] # Orden de impresión


# R4: <Definicion> ::= <DefVar>
class Definicion_Var(Nodo):
    # hijos: [<DefVar>]
    def __init__(self, hijos):
        super().__init__()
        self.def_var = hijos[0]
        self.hijos = [self.def_var]


# R3: <Definiciones> ::= <Definición> <Definiciones>
class Definiciones_L(Nodo):
    # La clase para la reducción de longitud 2
    def __init__(self, hijos):
        super().__init__()
        # Asegúrate de que esta clase solo se dispare con R2 (-2)
        self.definicion = hijos[0] 
        self.siguientes = hijos[1] 
        self.hijos = [self.definicion, self.siguientes]

   


# R1: <programa> ::= <Definiciones>
class Programa(Nodo):
    # hijos: [<Definiciones>]
    def __init__(self, hijos):
        super().__init__()
        self.hijos = hijos # El hijo es el nodo Definiciones_L o Definiciones_E


# =================================================================
# 3. TABLA DE GRAMÁTICA (Mapeo para lex.py)
# =================================================================

# Mapeo de reglas de reducción: 
# {código_negativo: (Nombre_Clase_AST, Longitud_Beta, Código_NT_GOTO)}
GRAMATICA_AST = {
    # R4 y R3 son las que entran en bucle, debemos asignarles la longitud 0 y 2:
    -8: ("ListaVar_E", 0, NT_ListaVar),
    -7: ("DefVar", 4, NT_DefVar),
    # R4: Asumimos que esta es la recursiva (Longitud 2)
    -4: ("Definiciones_L", 2, 25),  # R4: <Definiciones> ::= <Definicion> <Definiciones>
    
    # R3: Asumimos que esta es la épsilon (Longitud 0)
    -3: ("Definiciones_E", 0, 25),  # R3: <Definiciones> -> \e
    
    # R2: Esta regla es típicamente Longitud 2, pero si tu analizador la ve, 
    # necesitamos que también tenga la lógica correcta:
    
    -2: ("Programa", 1, NT_Programa),
    # R1: Programa
 
    
    # IMPORTANTE: La otra regla de Definición, que es R5 en tu caso:
    -5: ("Definicion_Var", 1, 26),
    
    # AÑADIR AQUÍ EL RESTO DE LAS 52 REGLAS (Ej. -8, -9, -10, etc.)
}


# =================================================================
# 4. FUNCIÓN DE IMPRESIÓN PÚBLICA (Llamada desde lex.py)
# =================================================================

def imprime_ast(nodo_raiz):
    """
    Función de interfaz para imprimir el Árbol de Sintaxis Abstracta (AST).
    Llama al método recursivo muestraArbol del nodo raíz.
    """
    if nodo_raiz is None:
        print("El árbol AST no se pudo construir debido a un error sintáctico.")
        return
    
    print("\n" + "="*50)
    print("           ÁRBOL DE SINTAXIS ABSTRACTA (AST)")
    print("="*50)
    nodo_raiz.muestraArbol(nivel=0)
    print("="*50)
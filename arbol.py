# =================================================================
# ast_nodos.py - Definición de Nodos AST, Gramática y Ensamblador (emu8086)
# =================================================================

# --- 1. Códigos de No Terminales (NTs) para GOTO ---
NT_Programa = 24
NT_Definiciones = 25
NT_Definicion = 26
NT_DefVar = 27
NT_ListaVar = 28
# ... (Añade el resto de NTs si es necesario)

# --- 2. CLASES BASE Y NODOS TERMINALES ---

class Nodo:
    """Clase base para todos los nodos del AST."""
    def __init__(self):
        self.hijos = []
        self.nombre = self.__class__.__name__

    def generar_codigo(self):
        """Genera código ensamblador (recorre a los hijos por defecto)."""
        codigo = ""
        for hijo in self.hijos:
            if isinstance(hijo, Nodo):
                codigo += hijo.generar_codigo()
        return codigo

# Nodos Terminales (Tokens)
class TokenNode(Nodo):
    """Representa un token simple (ID, Tipo, ';', etc.) que contiene un valor."""
    def __init__(self, codigo, valor=None):
        super().__init__()
        self.codigo = codigo
        self.valor = valor # Este atributo es clave y solo existe aquí
        self.nombre = f"TOKEN_{valor or codigo}"
        
    def generar_codigo(self):
        return ""

class Tipo(TokenNode):
    """Representa el token de tipo (int)."""
    pass

class ID(TokenNode):
    """Representa el token de Identificador."""
    pass

# --- 3. CLASES DE NÓDOS NO TERMINALES (ESTRUCTURAS) ---

# R2: La regla de Aceptación (programa) en tu 'lis' es -2
class Programa(Nodo):
    """R2: <programa> ::= <Definiciones> (Longitud 1)"""
    def __init__(self, hijos):
        super().__init__()
        self.definiciones = hijos[0]
        self.hijos = [self.definiciones]
        
    def generar_codigo(self):
        # Llama a la generación de código del cuerpo (Definiciones)
        codigo_definiciones = self.hijos[0].generar_codigo()
        
        # Estructura base para emu8086
        codigo_ensamblador = (
            f"; Código Ensamblador generado por el compilador (emu8086)\n"
            f"#make_bin\n"
            f"\n"
            f".model small\n"
            f".stack 100h\n"
            f"\n"
            f"; === SECCIÓN DE DATOS (.data) ===\n"
            f".data\n"
            f"{codigo_definiciones}\n"
            f"\n"
            f"; === SECCIÓN DE CÓDIGO (.code) ===\n"
            f".code\n"
            f"main proc\n"
            f"    mov ax, @data\n"
            f"    mov ds, ax ; Establecer el segmento de datos\n"
            f"\n"
            f"    ; Código del programa (instrucciones)\n"
            f"    \n"
            f"    ; Terminar el programa\n"
            f"    mov ah, 4ch\n"
            f"    int 21h\n"
            f"main endp\n"
            f"end main\n"
        )
        return codigo_ensamblador


# --- Lista de Definiciones (recursiva) ---
class Definiciones_L(Nodo):
    """R4: <Definiciones> ::= <Definicion> <Definiciones> (Longitud 2)"""
    def __init__(self, hijos):
        super().__init__()
        self.definicion = hijos[0] 
        self.siguientes = hijos[1] 
        self.hijos = [self.definicion, self.siguientes]
        
# --- Lista de Definiciones (épsilon) ---
class Definiciones_E(Nodo):
    """R3: <Definiciones> -> \e (Longitud 0)"""
    def __init__(self, hijos=None):
        super().__init__()
        self.nombre = "Definiciones_Vacias"
        
    def generar_codigo(self):
        return "" 

# --- Definición Singular ---
class Definicion_Var(Nodo):
    """R5: <Definicion> ::= <DefVar> (Longitud 1)"""
    def __init__(self, hijos):
        super().__init__()
        self.def_variable = hijos[0]
        self.hijos = [self.def_variable]

# --- Declaración de Variable y Generación de Datos ---
class DefVar(Nodo):
    """R7: <DefVar> ::= tipo id <ListaVar> ; (Longitud 4)"""
    def __init__(self, hijos):
        super().__init__()
        # Almacenamos los hijos para acceso seguro
        self.tipo_nodo = hijos[0]      # TokenNode: tipo
        self.nombre_nodo = hijos[1]    # TokenNode: id
        self.lista_var = hijos[2]      # Nodo: ListaVar_E
        self.punto_coma = hijos[3]     # TokenNode: ;
        
        # Asignamos TODOS los hijos para el recorrido general del AST
        self.hijos = [self.tipo_nodo, self.nombre_nodo, self.lista_var, self.punto_coma]
        
    def generar_codigo(self):
        if isinstance(self.nombre_nodo, TokenNode):
            nombre_var = self.nombre_nodo.valor
        else:
            # Si self.nombre_nodo es ListaVar_E, lo ignoramos y asumimos un error de gramática
            print(f"❌ ERROR de AST: Se esperaba ID, se recibió {self.nombre_nodo.nombre}.")
            return ""
        # 🚨 SOLUCIÓN: Accedemos directamente a los atributos guardados en __init__
        # Evitamos recorrer self.hijos recursivamente.

        # Acceso seguro a los tokens que sí tienen 'valor'
        tipo_token = self.tipo_nodo.valor  
        nombre_var = self.nombre_nodo.valor 

        # Mapeo a directivas de emu8086 (x86 16-bit)
        if tipo_token == "int":
            directiva = "DW 0" # Define Word (2 bytes)
        elif tipo_token == "char":
            directiva = "DB 0" # Define Byte (1 byte)
        else:
            directiva = "DB ?" 
        
        # Generamos el código de la definición.
        codigo_definicion = f"{nombre_var} {directiva}\n"
        
        # Si hubiera más variables (ej: int a, b;), la lógica para recorrer
        # self.lista_var se añadiría aquí. Por ahora, solo es una línea.
        
        return codigo_definicion

# --- Lista de Variables (épsilon) ---
class ListaVar_E(Nodo):
    """R8: <ListaVar> -> \e (Longitud 0)"""
    def __init__(self, hijos=None):
        super().__init__()
        self.nombre = "ListaVar_Vacia"
        
    def generar_codigo(self):
        return "" 

# --- 4. TABLA DE GRAMÁTICA (Mapeo de reglas de reducción) ---

GRAMATICA_AST = {
    # {código_negativo: (Nombre_Clase_AST, Longitud_Beta, Código_NT_GOTO)}
    
    # Reglas Confirmadas por la traza y corrección del bucle
    -8: ("ListaVar_E", 0, NT_ListaVar),        # R8: <ListaVar> -> \e
    -7: ("DefVar", 4, NT_DefVar),              # R7: <DefVar> ::= tipo id <ListaVar> ;
    -5: ("Definicion_Var", 1, NT_Definicion),   # R5: <Definicion> ::= <DefVar>
    
    # Reglas de Definiciones
    -4: ("Definiciones_L", 2, 25),  # R4: <Definiciones> ::= <Definicion> <Definiciones>
    -3: ("Definiciones_E", 0, 25),  # R3: <Definiciones> -> \e
    
    # Regla de Aceptación (R2 es la que se disparó al final en tu 'lis')
    -2: ("Programa", 1, NT_Programa),          # R2: <programa> ::= <Definiciones> (ACEPTACIÓN)
}

# --- 5. FUNCIÓN DE IMPRESIÓN DEL AST ---

def imprime_ast(nodo, nivel=0):
    """Imprime el AST de forma recursiva."""
    espacios = "  " * nivel
    
    if isinstance(nodo, TokenNode) and nodo.valor is not None:
        print(f"{espacios}|-- {nodo.nombre}: {nodo.valor}")
    elif isinstance(nodo, Nodo):
        print(f"{espacios}|-- <{nodo.nombre}>")
        for hijo in nodo.hijos:
            imprime_ast(hijo, nivel + 1)
import re
# Asegúrate de que analizador y elementos existan y funcionen
from analizador import analizador_lexico 
from elementos import lis

# 1. Importar la tabla de reglas de la gramática
from arbol import GRAMATICA_AST 

# 2. Importar la función de impresión
from arbol import imprime_ast

# 3. Importar TODAS las clases AST que se usan como resultado de una reducción
from arbol import (
    Programa, Definiciones_L, Definiciones_E, Definicion_Var, 
    DefVar, ListaVar_E, Tipo, ID, TokenNode # Incluimos los terminales
)


codigo = 'int a;'

# --- PRE-PROCESAMIENTO LÉXICO ---
resultado_lexico, analisis_correcto = analizador_lexico(codigo)

# La lista `pila` original solo contenía los códigos de los tokens.
patron = r'-> (\d+),'
valores_numericos_str = re.findall(patron, resultado_lexico)
pila_codigos = [int(val) for val in valores_numericos_str]
pila_codigos.append(23) # Añadir el token de fin de cadena '$'
# Almacenamos los valores léxicos y códigos juntos para la construcción del nodo
datos_tokens = []
# (Asumiendo que analizador_lexico devuelve los valores también,
#  aquí simplificamos para el ejemplo 'int a;')
# Para un uso real, debes obtener los valores ('int', 'a', ';', '$') del léxico.
if codigo == 'int a;':
    datos_tokens = [('int', 4), ('a', 0), (';', 12), ('$', 23)] 

# --- ESTRUCTURAS DE PARSER ---
pilaE = [0]             # Pila de Estados
pila_simbolos = []      # Pila de Nodos AST (nueva y esencial)
ast_final = None        # Nodo raíz del AST al finalizar
pasos = 0

# Función auxiliar para mapear el nombre de la clase AST a la clase real
def get_class(name):
    # globals() busca la clase real importada
    return globals().get(name)

# La lista de códigos de tokens que se consumirá
pila_codigos_consumo = list(pila_codigos)
# La lista de tokens con valor que se consumirá para SHIFT
datos_tokens_consumo = list(datos_tokens) 

print(f"Tokens de entrada (Códigos): {pila_codigos}")
print("-" * 50)

# El bucle AHORA es controlado por la pila de códigos
while pila_codigos_consumo:
    estado_actual = pilaE[-1]
    token_actual = pila_codigos_consumo[0]
    
    try:
        accion = lis[estado_actual][token_actual]
    except IndexError:
        print(f"❌ ERROR: Estado {estado_actual} o Token {token_actual} fuera de límites de la tabla 'lis'.")
        break
        
    pasos += 1
    
    print(f"\n[Paso {pasos}] E{estado_actual}, Token: {token_actual} -> Acción: {accion}")

    if accion > 0: # --- SHIFT (Desplazar) ---
        
        # 1. Crear nodo Terminal y apilar
        valor_token, codigo_token = datos_tokens_consumo.pop(0)
        
        # Lógica para crear el nodo terminal correcto
        if codigo_token == 4:
            nodo_terminal = Tipo(codigo_token, valor=valor_token)
        elif codigo_token == 0:
            nodo_terminal = ID(codigo_token, valor=valor_token)
        else:
            nodo_terminal = TokenNode(codigo_token, valor=valor_token)
            
        pila_simbolos.append(nodo_terminal)
        
        # 2. Manipular Pilas
        pilaE.append(accion)
        pila_codigos_consumo.pop(0)
        
        print(f"  > SHIFT a E{accion}. PilaE: {pilaE}")

    elif accion < 0: # --- REDUCE (Reducir) ---
        
        num_regla = abs(accion)
        
        if accion == -1: # Aceptación
            ast_final = pila_simbolos[0]
            print("\n✅ ACEPTACIÓN Y ANÁLISIS SINTÁCTICO FINALIZADO.")
            break

        # *** LÓGICA DE REDUCCIÓN GENERALIZADA (Reemplaza todos tus 'elif x == -N') ***
        try:
            Clase_Nombre, longitud_beta, simbolo_A = GRAMATICA_AST[accion]
            Clase_AST = get_class(Clase_Nombre)
        except KeyError:
            print(f"❌ ERROR: Regla de reducción R{num_regla} no implementada en GRAMATICA_AST.")
            break
        
        # 1. Construcción del Nodo Padre
        if longitud_beta > 0:
            # Eliminar y obtener los N nodos hijos de la Pila de Símbolos
            nodos_hijos_a_reducir = pila_simbolos[-longitud_beta:]
            pila_simbolos = pila_simbolos[:-longitud_beta]
            nodos_hijos_ordenados = nodos_hijos_a_reducir[::-1] # Invertir para orden de la regla
            nodo_padre = Clase_AST(nodos_hijos_ordenados)
        else:
            pila_simbolos = pila_simbolos # No se quita nada de la pila de símbolos
            nodo_padre = Clase_AST() # Reglas épsilon
            
        pila_simbolos.append(nodo_padre) # Apilar el nuevo nodo AST

        # 2. Manipulación de la Pila de Estados (PilaE)
        # Eliminar 2 * longitud_beta elementos (estado + símbolo)
        for _ in range(longitud_beta):
            pilaE.pop()
        
        estado_viejo = pilaE[-1]
        
        # GOTO: Buscar el nuevo estado en la matriz 'lis' (Columna NT)
        nuevo_estado = lis[estado_viejo][simbolo_A]
        
        if nuevo_estado <= 0:
            print(f"❌ ERROR GOTO inválido para R{num_regla}. GOTO({estado_viejo}, {simbolo_A}) = {nuevo_estado}. El valor en la tabla LR es 0.")
            break
        
        pilaE.append(nuevo_estado)
        
        print(f"  > REDUCE R{num_regla} a <{Clase_Nombre}>. Longitud={longitud_beta}. GOTO a E{nuevo_estado}.")

    else: # --- ERROR (accion == 0) ---
        print(f"❌ ERROR SINTÁCTICO. Entrada inválida en E{estado_actual} con Token {token_actual}.")
        break

# --- 6. IMPRESIÓN DEL AST ---
if ast_final:
    imprime_ast(ast_final)
    




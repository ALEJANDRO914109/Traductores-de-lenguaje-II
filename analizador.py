def analizador_lexico(codigo):
    posicion = 0
    resultado = ''
    error = False


    while posicion < len(codigo):
        char = codigo[posicion]

        # --- ESPACIOS EN BLANCO ---
        if char.isspace():
            posicion += 1
            continue

        # --- CADENAS ENTRE COMILLAS ---
        elif char == '"':
            cadena = ''
            posicion += 1
            while posicion < len(codigo) and codigo[posicion] != '"':
                cadena += codigo[posicion]
                posicion += 1
            posicion += 1  # saltar la comilla final
            resultado += f'"{cadena}" -> 3, cadena\n'
            continue

        # --- IDENTIFICADORES O PALABRAS RESERVADAS ---
        elif char.isalpha() or char == '_':
            identificador = ''
            while posicion < len(codigo) and (codigo[posicion].isalnum() or codigo[posicion] == "_"):
                identificador += codigo[posicion]
                posicion += 1

            # Palabras reservadas
            reservadas = {
                "if": 19,
                "while": 20,
                "return": 21,
                "else": 22
            }
            tipos = {"int", "float", "string"}

            if identificador in reservadas:
                resultado += f"{identificador} -> {reservadas[identificador]}, Reservada {identificador}\n"
            elif identificador in tipos:
                resultado += f"{identificador} -> 4, tipo de dato\n"
            else:
                resultado += f"{identificador} -> 0, identificador\n"
            continue

        # --- NÚMEROS (ENTEROS Y FLOTANTES) ---
        elif char.isdigit() or (char == '.' and posicion + 1 < len(codigo) and codigo[posicion + 1].isdigit()):
            numero = ''
            punto = False
            while posicion < len(codigo) and (codigo[posicion].isdigit() or codigo[posicion] == '.'):
                if codigo[posicion] == '.':
                    if punto:  # segundo punto → fin del número
                        break
                    punto = True
                numero += codigo[posicion]
                posicion += 1

            if '.' in numero:
                resultado += f"{numero} -> 2, flotante\n"
            else:
                resultado += f"{numero} -> 1, entero\n"
            continue

        # --- OPERADORES ---
        elif char in '+-':
            resultado += f"{char} -> 5, opsuma\n"
            posicion += 1

        elif char in '*/':
            resultado += f"{char} -> 6, opmultiplicacion\n"
            posicion += 1

        elif char in '<>':
            aux = char
            posicion += 1
            if posicion < len(codigo) and codigo[posicion] == '=':
                resultado += f"{aux}= -> 7, oprelacion\n"
                posicion += 1
            else:
                resultado += f"{aux} -> 7, oprelacion\n"

        elif char == '|':
            if posicion + 1 < len(codigo) and codigo[posicion + 1] == '|':
                resultado += f"|| -> 8, opor\n"
                posicion += 2
            else:
                resultado += f"{char} -> token no reconocido (| sin pareja)\n"
                posicion += 1

        elif char == '&':
            if posicion + 1 < len(codigo) and codigo[posicion + 1] == '&':
                resultado += f"&& -> 9, opand\n"
                posicion += 2
            else:
                resultado += f"{char} -> token no reconocido (& sin pareja)\n"
                posicion += 1

        elif char == '=':
            if posicion + 1 < len(codigo) and codigo[posicion + 1] == '=':
                resultado += f"== -> 11, opigualdad\n"
                posicion += 2
            else:
                resultado += f"= -> 18, =\n"
                posicion += 1

        elif char == '!':
            if posicion + 1 < len(codigo) and codigo[posicion + 1] == '=':
                resultado += f"!= -> 11, opigualdad\n"
                posicion += 2
            else:
                resultado += f"! -> 10, opnot\n"
                posicion += 1

        # --- SÍMBOLOS ESPECIALES ---
        elif char == ';':
            resultado += f"{char} -> 12, ;\n"
            posicion += 1
        elif char == ',':
            resultado += f"{char} -> 13, ,\n"
            posicion += 1
        elif char == '(':
            resultado += f"{char} -> 14, (\n"
            posicion += 1
        elif char == ')':
            resultado += f"{char} -> 15, )\n"
            posicion += 1
        elif char == '{':
            resultado += f"{char} -> 16, {{\n"
            posicion += 1
        elif char == '}':
            resultado += f"{char} -> 17, }}\n"
            posicion += 1

        # --- TOKEN DESCONOCIDO ---
        else:
            error = True
            resultado += f"token no reconocido: {char}\n"
            posicion += 1
    print("yeii")
    return resultado, not error
    



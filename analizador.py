#FUNCION PARA ANALIZAR
def analizador_lexico(codigo):
    posicion = 0
    resultado = ''

    while posicion < len(codigo):
        char = codigo[posicion]
        #AVANZAR EN ESPACIOS EN BLANCO
        if char == " ":
            posicion += 1
        #IDENTIFICADORES
        elif char.isalpha() or char == '_' or char == '"' or char == '"': #ISALPHA PARA LETRAS O _
            identificador = ''
            while posicion < len(codigo) and (codigo[posicion].isalnum() or codigo[posicion] == "_" or codigo[posicion] == '"'):
                identificador += codigo[posicion]
                posicion += 1
            #19 CONDICIONAL if   
            if identificador == "if":
                resultado += identificador + " -> 19, Reservada if \n"
            
            #20 while   
            elif identificador == "while":
                resultado += identificador + " -> 20, Reservada while \n"

            #21 return  
            elif identificador == "return":
                resultado += identificador + " -> 21, Reservada return \n"

            #22 else  
            elif identificador == "else":
                resultado += identificador + " -> 22, Reservada else \n"

            #3 CADENA
            elif '"' in identificador:
                resultado += identificador + " -> 3, cadena \n"

            #4 TIPOS DE DATOS
            elif identificador == "int" or identificador == "float" or identificador == "string":
                resultado += identificador + " -> 4, tipo de dato \n"

            #0 IDENTIFICADOR
            else:
                resultado += identificador + " -> 0, identificador \n"
       
        #DIGITOS
        elif char.isdigit() or char==".":
            numero = ""    
            while posicion < len(codigo) and (codigo[posicion].isdigit() or codigo[posicion] =="."):
                if codigo[posicion].isalnum():
                    numero += codigo[posicion]    
                elif codigo[posicion] ==".":
                    numero += codigo[posicion]
                posicion += 1
                
            #2 FLOTANTE
            if "." in numero:
                token = " -> 2, flotante \n"
                
            #1 ENTERO
            else:
                token = " -> 1, entero \n"
            resultado += numero +  token

        #5 OPSUMA
        elif char == "+" or char == "-":
            resultado += char + " -> 5, opsuma \n"
            posicion += 1
            
        #6 OPMULTIPLICACION
        elif char == "*" or char == "/":
            resultado += char + " -> 6, opmultiplicacion \n"
            posicion += 1

        #7 OPRELACION
        elif char == "<" or char == ">":
            res_aux = char + " -> 7, oprelacion \n"
            aux = char
            posicion +=1
            char = codigo[posicion]
            if char == "=":
                res_aux = aux + char + " -> 7, oprelacion \n"
                posicion +=1
            resultado += res_aux

        #8 OPOR
        elif char == "|":
            posicion +=1
            aux = char
            char = codigo[posicion]
            if char == "|":
                resultado += aux + char + " -> 8, opor \n"
                posicion +=1

        #9 OPAND
        elif char == "&":
            posicion +=1
            aux = char
            char = codigo[posicion]
            if char == "&":
                resultado += aux + char + " -> 9, opand \n"
                posicion +=1

        #IGUALDADES
        elif char == "=" or char == "!":
            #18 =
            if char == "=":
                posicion +=1
                aux = char
                res_aux = char + " -> 18, = \n"
                char = codigo[posicion]
                #11 OPIGUALDAD
                if char == "=":
                    res_aux = aux + char + " -> 11, opigualdad \n"
                    posicion += 1
            #10 OPNOT
            elif char == "!":
                posicion +=1
                aux = char
                res_aux = char + " -> 10, opnot \n"
                char = codigo[posicion]
                #11 OPIGUALDAD
                if char == "=":
                    res_aux = aux + char + " -> 11, opigualdad \n"
                    posicion += 1
            resultado += res_aux

        #12 ;
        elif char == ";":
            resultado += char + " -> 12, ; \n"
            posicion += 1

        #13 ,
        elif char == ",":
            resultado += char + " -> 13, , \n"
            posicion += 1

        #14 (
        elif char == "(":
            resultado += char + " -> 14, ( \n"
            posicion += 1

        #15 )
        elif char == ")":
            resultado += char + " -> 15, ) \n"
            posicion += 1

        #16 {
        elif char == "{":
            resultado += char + " -> 16, { \n"
            posicion += 1

        #17 }
        elif char == "}":
            resultado += char + " -> 17, } \n"
            posicion += 1
            
            
        
       
  
        #TOKEN NO RECONOCIDO
        else:
            resultado = "token no reconocido: "
            posicion = len(codigo)

    #23 EOF O FIN DEL ARCHIVO        
    resultado += "$ -> 23, EOF (fin de archivo)\n"       
    print(resultado)


# Ejemplo
codigo = 'Aa 12 1.21 "hola" string + / <= || && ! != ; ,() {}= if while return else '



analizador_lexico(codigo)

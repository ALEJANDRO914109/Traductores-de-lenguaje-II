import re
from analizador import analizador_lexico
from elementos import lis


codigo = 'int suma(int a, int b){return a+b;}'

resultado, analisis_correcto = analizador_lexico(codigo)
resultado, correcto = analizador_lexico(codigo)

#print(resultado)
# La expresión regular busca el patrón:
# 1. '-> ' (el indicador de valor)
# 2. seguido de un grupo de captura '(\d+)' que encuentra uno o más dígitos.
# 3. seguido de una coma ','.
# re.findall() solo devuelve el contenido del grupo de captura (los números).
patron = r'-> (\d+),'
# Encontramos todos los valores numéricos como strings
valores_numericos_str = re.findall(patron, resultado)
# Convertimos los strings a enteros para formar la lista 'pila'

pila = [int(val) for val in valores_numericos_str]
pilaE = [0]
pila.append(23)

"""if analisis_correcto:
    print(resultado,end="")
    print("✅ Análisis léxico completado correctamente.")
    sintactico = True

else:
    print(resultado,end="")
    print(" Error lexico")
    sintactico = False"""

a= 2
print(a)
print(pila)
print(a)


while a > 0:
    x = lis[pilaE[-1]][pila[0]]
    print(x)
    print("pilaaaaa",pila)
    print("dodsod",pilaE)
    pilaE.append(pila[0])
    pilaE.append(x)
    pila.pop(0)
    
    
    if x == 0:
        print("eERORORORORRRRRRRR")
        a=0
    elif x <= 0:
        if x == -53:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,45)
            pilaE = pilaE[:-3]
            print("hola")
            print("pila",pila)
            print("e",pilaE)
            print("control")
            
        elif x == -37:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,42)
            pilaE = pilaE[:-3]

        elif x == -14:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,31)
            pilaE = pilaE[:-9]

        elif x == -13:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,31)
            pilaE.pop()

        elif x == -12:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,30)
            pilaE = pilaE[:-7]
            

        elif x == -8:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,28)
            pilaE.pop()
        elif x == -7:
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pila.append(27)
            pila.append(23)
        elif x == -5:
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pila.append(26)
            pila.append(23)
        elif x == -3:
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pila.append(25)
            pila.append(23)
        elif x == -2:
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pilaE.pop()
            pila.append(24)
            pila.append(23)
        elif x == -1:
            print ("aceptacion")
            a=0



   
        
        


    

    




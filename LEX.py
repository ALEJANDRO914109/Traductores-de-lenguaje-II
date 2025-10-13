import re
from analizador import analizador_lexico
from elementos import lis


codigo = 'int suma(int a, int b){return a+b;}'
#codigo = 'int asdi0dfsdfidfdpifmfd_005d ;'

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
        #REGLA NUMERO 52
        if x == -53:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,45)
            pilaE = pilaE[:-3]
        #REGLA NUMERO 47 
        elif x == -48:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,45)
            pilaE = pilaE[:-7]
            
        
        #REGLA NUMERO 36 
        elif x == -37:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,42)
            pilaE = pilaE[:-3]

        #REGLA NUMERO 30
        elif x == -31:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,39)
            pilaE = pilaE[:-3]
            
        #REGLA NUMERO 24
        elif x == -25:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,36)
            pilaE = pilaE[:-7]
            
        #REGLA NUMERO 18
        elif x == -19:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,34)
            pilaE = pilaE[:-3]

        #ESTAS TRABAJANDO EN ESTA REGLA
        #REGLA NUMERO 16
        elif x == -17:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,33)
            pilaE = pilaE[:-5]
        
        #REGLA NUMERO 15
        elif x == -16:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,33)
            pilaE.pop()
        
        #REGLA NUMERO 14
        elif x == -15:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,32)
            pilaE = pilaE[:-2]
            
            


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

        #REGLA NUMERO 9
        elif x == -10:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,29)
            pilaE = pilaE[:-18]
            
            

            

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
        
        elif x == -6:
            pilaE.pop()
            pila.insert(0,pilaE[-1])
            pila.insert(0,26)
            pilaE = pilaE[:-3]
            

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
            print("PILA",pila)
            print("E",pilaE)
            print("CONTROL")
            
            
        elif x == -1:
            print ("aceptacion")
            a=0



   
        
        


    

    




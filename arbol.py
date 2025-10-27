

class Nodo:
    pass

class Tipo(Nodo):
    
    def __init__(self,tipo):
        super().__init__()
        self.tipo = tipo


# R7 <ListaVar> -> null
class R7(Nodo):
    

    def muestraArbol():
        print("")


# R6 <DefVar> ::= tipo identificador <ListaVar> ;
class R6(Nodo):
    

    def __init__(self,pila):
        super().__init__()
        #  tipo# identificador# <ListaVar># ;#
        pila.pop() # elimna #
        pila.pop() # elimna ;
        pila.pop() # elimna #
        EP = pila.pop() # elimna Nodo <ListaVar>
        self.listavar =  EP.nodo
        pila.pop() # elimna #
        self.id = pila.pop() 
        pila.pop() # elimna #
        self.tipo = pila.pop() # elimna tipo


    def muestraArbol(self):
        tab += 1
        print(f"self.tipo")
        print(f"self.id")
        self.listavar.muestraArbol()
        print(";")

    def semantico(self):
        if existe(self.id,ambitolo):
            print("error")
        else:
            tablasimbolos[{self.id:self.tipo,AMBITO}]

    def generacodigo(self):

        return "MOV ADX,B " \
        "ADD AX, A"
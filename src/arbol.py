class nodos:
    def __init__(self, valor):
        self.valor = valor
        self.enl_izq = None
        self.enl_der = None
        
class Arbol:
    def __init__(self):
        self.raiz = None


    def insrt(self, valor):
        if self.raiz is None:
            self.raiz = nodos(valor)
        else: 
            self.insertar(valor, self.raiz)

    def insertar(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.enl_izq is None:
                nodo_actual.enl_izq = nodos(valor)
            else:
                self.insertar(valor, nodo_actual.enl_izq)
        elif valor > nodo_actual.valor:
            if nodo_actual.enl_der is None:
                nodo_actual.enl_der = nodos(valor)
            else:
                self.insertar(valor, nodo_actual.enl_der)
        else:
            print("Valor ya existe")
            
                    
    def Preorden(self):
        return self.Rpreorden(self.raiz)
            
    def Rpreorden(self, nodo):
        res=[]
        if nodo:
            res.append(nodo.valor)
            res+=self.Rpreorden(nodo.enl_izq)
            res+=self.Rpreorden(nodo.enl_der)
        return res
        
    def Inorden(self):
        return self.Rinoreden(self.raiz)
    
    def Rinoreden(self, nodo):
        res=[]
        if nodo:
            res=self.Rinoreden(nodo.enl_izq)
            res.append(nodo.valor)
            res+=self.Rinoreden(nodo.enl_der)
        return res
    
    def Postorden(self):
        return self.Rpostorden(self.raiz)
    
    def Rpostorden(self, nodo):
        res=[]
        if nodo:
            res+=self.Rpostorden(nodo.enl_izq)
            res+=self.Rpostorden(nodo.enl_der)
            res.append(nodo.valor)
        return res
    
    def altura(self,nodo):
        if nodo is None:
            return 0
        else:
            return 1+max(self.altura(nodo.enl_izq),self.altura(nodo.enl_der))  
    
    def prof(self, nodo,profNodo=0):
        if nodo is None:
            return -1
        if self.raiz == nodo:    
            return profNodo
        
    def nivel(self, nodo):
        return self.prof(nodo)
    
if __name__ == "__main__":
    arbol = Arbol()
    valores=[50,30,80,18,15,45,55,22,27,90,88,77]
    for v in valores:
        arbol.insrt(v)
        print("recorrido en pre-orden:",arbol.Preorden())
        print("recorrido en in-orden:",arbol.Inorden())
        print("recorrido en post-orden:",arbol.Postorden())
        print("altura:",arbol.altura(arbol.raiz))
        print("profundidad:",arbol.prof(arbol.raiz))
        print("nivel:",arbol.nivel(arbol.raiz))
    

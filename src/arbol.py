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
    
    def altura(self, nodo):
        if nodo is None:
            return -1  
        altura_izq = self.altura(nodo.enl_izq)
        altura_der = self.altura(nodo.enl_der)
        return max(altura_izq, altura_der) + 1  

    def prof(self, nodo, valor):
        if nodo is None:
            return -1 
        if nodo.valor == valor:
            return 0  
        elif valor < nodo.valor and nodo.enl_izq:
            profundidad_izq = self.prof(nodo.enl_izq, valor)
            if profundidad_izq != -1:
                return profundidad_izq + 1
        elif valor > nodo.valor and nodo.enl_der:
            profundidad_der = self.prof(nodo.enl_der, valor)
            if profundidad_der != -1:
                return profundidad_der + 1
        return -1

    def nivel(self, valor):
        return self.prof(self.raiz, valor)
    
if __name__ == "__main__":
    arbol = Arbol()
    valores = [50, 30, 80, 18, 15, 45, 55, 22, 27, 90, 88, 77]
    
    for v in valores:
        arbol.insrt(v)
    
    print("Recorrido en pre-orden:", arbol.Preorden())
    print("Recorrido en in-orden:", arbol.Inorden())
    print("Recorrido en post-orden:", arbol.Postorden())
    print("Altura del árbol:", arbol.altura(arbol.raiz))
    
    valor_buscado = 55
    print(f"Profundidad del nodo con valor {valor_buscado}:", arbol.prof(arbol.raiz, valor_buscado))
    print(f"Nivel del nodo con valor {valor_buscado}:", arbol.nivel(valor_buscado))

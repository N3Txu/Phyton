class Node:
    def __init__(self, valor): # constructor de la clase Node
        self.valor = valor # valor del nodo
        self.hijo_izq = None # puntero a la hoja izquierda
        self.hijo_der = None # puntero a la hoja derecha
        
    def hojas(self, nodo): # funcion que devuelve el numero de hojas que tiene el nodo recursivamente
        if nodo is None: # si el nodo es None, devuelve 0
            return 0
        if nodo.hijo_izq is None and nodo.hijo_der is None: # si no tiene hijos es una hoja y devuelve 1
            return 1
        else:
            # llama a la funcion recursivamente para calcular el numero de hojas de los hijos
            return self.hojas(nodo.hijo_izq) + self.hojas(nodo.hijo_der) 
        

if __name__ == "__main__":
    raiz = Node(1)
    raiz.hijo_izq = Node(2)
    raiz.hijo_der = Node(3) 
    raiz.hijo_izq.hijo_izq = Node(4)
    raiz.hijo_izq.hijo_der = Node(5)
    
    # se imprime el numero de hojas la cual debe devolver 3 , ya que son los nodos 4,5 y 3 son hojas
    print(raiz.hojas(raiz))
    
        
        
        
        

class Arreglo:
    def __init__(self, arr): # constructor de la clase Arreglo 
        self.arr = arr # almacena el arreglo en la variable arr
        self.n = len(arr) # almacena la longitud del arreglo en la variable n

    def is_sorted(self, n=None): # metodo que recibe un arreglo y devuelve True si el arreglo es ordenado
        if n is None:  # si n es None entonces se utiliza la variable n del constructor
            n = self.n  # inicializa n con la longitud del arreglo
        if n == 0 or n == 1: # caso base en el que se verifica si el arreglo es ordenado si hay 0 o 1 elemento
            return True # retorna True ya que el arreglo es ordenado
        else: # verifica si el elemento es mayor que el anterior
            return self.arr[n-1] >= self.arr[n-2] and self.is_sorted(n-1) # si el elemento es mayor que el anterior entonces el arreglo es ordenado


if __name__ == "__main__":

    v = [1, 2, 3, 4, 5]
    v2 = [1, 3, 2, 4, 5]
    
    instance=Arreglo(v) # v es ordenado
    print(instance.is_sorted()) # True
    
    instance2=Arreglo(v2) # v2 no es ordenado
    print(instance2.is_sorted()) # False




""" def sd(n): # funcion que devuelve el sumatorio de los digitos de un numero
    if n == 0: # si el numero es cero devuelve 0
        return 0 # devuelve 0
    else: # si no es cero devuelve el digito de la suma de los digitos de n
        return n % 10 + sd(n // 10) # devuelve el digito de la suma de los digitos de n
    # Ejemplo de uso resultado 
Resultado = sd(1234) # Resultado = 1 + 2 + 3 + 4 = 10
print(Resultado) # imprime 10 

//                                                                             //
def ii(arr, n,): # funcion recursiva que imprime el numero n de la lista arr
    if n == 0: # condicion base
        return
    print(arr[n - 1])  #imprime el ultimo elemento de la lista 
    ii(arr, n - 1) # llama a la funcion recursiva con n - 1 como parametro
#  Ejemplo  de uso
v = [1, 2, 3, 4, 5] # lista de 5 elementos
ii(v, len(v)) # llama a la funcion ii con la lista v y el tamaño de la misma como parametros e imprime el numero 5 de la lista
    
"""
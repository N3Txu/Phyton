import sys 
sys.setrecursionlimit(10**6) # para evitar el error de recursion depth exceeded por desbordamiento de pila

class recursividad:
    def __init__(self, n):
        self.n = n

    def sum_divisores(self, n, div=1):
        if div >= n:
            return 0
        if n % div == 0:
            return div + self.sum_divisores(n, div + 1)
        else:
            return self.sum_divisores(n, div + 1)

    def num_frnd(self, num1, num2):
        sum1 = self.sum_divisores(num1)
        sum2 = self.sum_divisores(num2)
        return sum1 == num2 and sum2 == num1


if __name__ == "__main__":
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))    
    rec = recursividad(num1)

    if rec.num_frnd(num1, num2):
        print(f"{num1} y {num2} son números amigos.")
    else:
        print(f"{num1} y {num2} no son números amigos.")


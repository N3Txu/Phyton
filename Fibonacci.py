class Fibonacci:
    def __init__(self, n):
        self.n = n

    def fib(self, n):
        if n <= 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


if __name__ == "__main__":
    n = int(input("Ingrese un numero entero positivo: "))
    fib = Fibonacci(n)
    print(f"El valor de Fibonacci de {n} es: {fib.fib(n)}")
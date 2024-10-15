class Maxvec:

    def __init__(self, n):
        self.n = n

    def imv(self, v, n):
        if n == 1:
            # print(f"se alcanzo el valor base el cual es: {v[0]}")
            return v[0]
        else:
            # print(f"comparando el valor {v[n-1]} con el valor maximo del arreglo (n={v[n-1]} y n={n})")
            max_resta = self.imv(v, n - 1)
            result = max(v[n - 1], max_resta)
            print(f"el maximo entre el valor {v[n-1]} y el {max_resta} es: {result}")
            return result


if __name__ == "__main__":
    v = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    n = len(v)
    maxvec = Maxvec(n)
    mv = maxvec.imv(v, n)
    print()
    print(f"El valor maximo en el arreglo es: {mv}")
    
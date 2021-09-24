import time

def f(n):

  # Loop lineal x+x
    comienzo = time.time()
    for i in range(n):
        pass
    print("Lineal: {}".format(time.time() - comienzo))


  # Loop cuadrático x**2   
    comienzo = time.time()

    for i in range(n):
        for j in range(n):
            pass
        pass

    print("Cuadrática: {}".format(time.time() - comienzo))

if __name__ == "__main__":
    f(9500)
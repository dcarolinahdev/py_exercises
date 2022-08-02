import time

def fibo_gen(max=None):
    n1 = 0
    n2 = 1
    counter = 0
    nmax = max
    while not max or (counter <= (nmax - 1)):
        # print("i="+str(counter+1))
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == '__main__':
    # fibonacci = fibo_gen()
    fibonacci = fibo_gen(8)
    for elem in fibonacci:
        print(elem)
        time.sleep(0.05)
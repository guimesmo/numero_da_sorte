import random
def numero_da_sorte():
    l = list(range(1, 61))
    random.shuffle(l)
    l = l[:6]
    l.sort()
    return " - ".join(["%02d" % i for i in l])

if __name__ == '__main__':
    print(numero_da_sorte())


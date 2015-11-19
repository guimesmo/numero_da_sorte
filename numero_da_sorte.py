import random
def numero_da_sorte():
    l = list(range(1, 61))
    random.shuffle(l)
    return "-".join([str(i) for i in l[:6]])

if __name__ == '__main__':
    print(numero_da_sorte())


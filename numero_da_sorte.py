import random
def numero_da_sorte():
    l = list(range(1, 61))
    random.shuffle(l)
    print("-".join([str(i) for i in l[:6]]))
numero_da_sorte()

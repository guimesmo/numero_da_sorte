import random
def numero_da_sorte():
    l = list(range(1, 61))
    random.shuffle(l)
    print("-".join([str(l.pop(i)) for i in range(6)]))


espace = []

def generateur_recurrent_d_espace(alphabet_de_dimension, dimension):
    global espace
    memory = list(espace)
    espace = []
    for i in alphabet_de_dimension:
        if len(alphabet_de_dimension) > 2:
            for x in memory:
                espace.append((x[::-1]+str(i))[::-1])
                yield  (x[::-1]+str(i))[::-1]
        elif len(alphabet_de_dimension) == 2:
            espace.append(str(i))
            yield str(i)

def generateur_recurrent_d_espace_infini():
    i = 0
    global espace 
    while True:
        i = i + 1
        for x in generateur_recurrent_d_espace([x for x in range(0, i)], i-1):
            yield x

for x in generateur_recurrent_d_espace_infini():
    print(x)

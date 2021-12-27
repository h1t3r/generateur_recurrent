def generateur_recurrent_d_espace(alphabet_de_dimension,  coordonnee, dimension):
    for i in alphabet_de_dimension:
        if len(coordonnee)+1 < dimension:
            for y in generateur_recurrent_d_espace(alphabet_de_dimension, coordonnee + str(i), dimension):
                yield y
        elif len(coordonnee)+1 == dimension:
            yield coordonnee + str(i)

def generateur_recurrent_d_espace_infini():
    i = 0
    while True:
        i = i + 1
        for x in generateur_recurrent_d_espace(range(0, i),  "", i):
            yield x

for x in generateur_recurrent_d_espace_infini():
    print(x)

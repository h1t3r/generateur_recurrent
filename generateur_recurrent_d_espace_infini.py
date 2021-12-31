def generateur_recurrent_d_espace(alphabet_de_dimension,  coordonnee, dimension, mem):
    for i in alphabet_de_dimension:
        if len(mem) == dimension and len(mem[0]) < dimension:
            for x in mem:
                yield (x[::-1]+str(i))[::-1]
        yield i

def generateur_recurrent_d_espace_infini():
    i = 0
    mem = []
    using_mem = False
    while True:
        i = i + 1
        if i == 1:
            for x in generateur_recurrent_d_espace(range(0, i),  "", i, [str(i) for i in range(0, i)]):
                mem.append(x)
                yield x
        elif i > 1:
            using_mem = True
            for x in generateur_recurrent_d_espace(range(0, i),  "", i, mem):
                if using_mem:
                    mem = []
                    using_mem = False
                mem.append(x)
                yield x

for x in generateur_recurrent_d_espace_infini():
    print(x)

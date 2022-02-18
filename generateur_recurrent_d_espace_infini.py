import threading

dimension = []
threads = []
def generateur_recurrent_d_espace(dimension0=[], dimension_units=[], coordonnee = "", dimension_length = 0):
    global dimension
    if isinstance(dimension0, list):
        if len(coordonnee)+1 < dimension_length:
            for i in dimension_units:
                if dimension0 == []:
                    dimension.append([coordonnee+str(i)])
                else:
                    dimension0.append([coordonnee+str(i)])
            if dimension0 == []:
                for x in dimension:
                    threads.append(threading.Thread(target=generateur_recurrent_d_espace, args=(x, dimension_units, x[0], dimension_length,)))
                    threads[len(threads)-1].start()
                for t in threads:
                    t.join()
            else:
                for x in dimension0:
                    threads.append(threading.Thread(target=generateur_recurrent_d_espace, args=(x, dimension_units, x[0], dimension_length,)))
                    threads[len(threads)-1].start()
        elif len(coordonnee)+1 == dimension_length:
            for i in dimension_units:
                dimension0.append([coordonnee+str(i)])
def generateur_recurrent_d_espace_infini():
    global dimension
    i = 0
    while True:
        dimension = []
        i = i +1
        x = threading.Thread(target=generateur_recurrent_d_espace, args=([], range(0, i), "", i,))
        x.run()
        print(dimension)
        if i == 4:
            exit()
generateur_recurrent_d_espace_infini()

import threading
import multiprocessing
from time import sleep

dimension = []

def generateur_recurrent_d_espace(z, dimension_units=[], coordonnee = "", dimension_length = 0):
    global dimension
    if isinstance(dimension, list):
        if len(coordonnee)+1 < dimension_length:
            for i in dimension_units:
                if z == []:
                    dimension.append([coordonnee+str(i)])
                else:
                    z.append([coordonnee+str(i)])
            if z == []:
                for x in dimension:
                    y = threading.Thread(target=generateur_recurrent_d_espace, args=(x, dimension_units, x[0], dimension_length,))
                    y.start()
                    print(dimension)
            else:
                for x in z:
                    y = threading.Thread(target=generateur_recurrent_d_espace, args=(x, dimension_units, x[0], dimension_length,))
                    y.start()
        elif len(coordonnee)+1 == dimension_length:
            for i in dimension_units:
                z.append([coordonnee+str(i)])

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

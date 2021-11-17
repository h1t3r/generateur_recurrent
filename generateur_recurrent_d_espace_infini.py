def generateur_recurrent_d_espace(dimension, unité_de_dimension, coordonné, a, length_dimension):
	if isinstance(dimension, list):
		if a < length_dimension:
			for i in unité_de_dimension:
				dimension.append([coordonné+str(i)])
			for x in dimension:
				for y in generateur_recurrent_d_espace(x, unité_de_dimension, x[0], a+1, length_dimension):
					dimension[dimension.index(x)].append(y)
			yield dimension
		elif a == length_dimension:
			for i in unité_de_dimension:
				dimension.append([coordonné+str(i)])
			yield dimension

def generateur_recurrent_d_espace_infini():
	i = 0
	while True:
		i = i +1
		for y in generateur_recurrent_d_espace([], [x for x in range(0, i)], "", 1, i):
			yield y
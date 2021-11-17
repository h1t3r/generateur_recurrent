def generateur_recurrent_d_espace(dimension, dimension_units, coordonnee, dimension_length):
	if isinstance(dimension, list):
		if len(coordonnee)+1 < dimension_length:
			for i in dimension_units:
				dimension.append([coordonnee+str(i)])
			for x in dimension:
				for y in generateur_recurrent_d_espace(x, dimension_units, x[0], dimension_length):
					pass
			yield dimension
		elif len(coordonnee)+1 == dimension_length:
			for i in dimension_units:
				dimension.append([coordonnee+str(i)])
			yield dimension

def generateur_recurrent_d_espace_infini():
	i = 0
	while True:
		i = i +1
		for y in generateur_recurrent_d_espace([], range(0, i), "", i):
			yield y
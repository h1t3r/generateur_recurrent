def generateur_recurrent_d_espace(dimension, dimension_units, coordonnee, dimension_length):
	if isinstance(dimension, list):
		if len(coordonnee)+1 < dimension_length:
			for i in dimension_units:
				dimension.append([coordonnee+str(i)])
			for x in dimension:
				for y in generateur_recurrent_d_espace(x, dimension_units, x[0], dimension_length):
					pass
				yield x

def generateur_recurrent_d_espace_infini():
	i = 0
	while True:
		i += 1
		for x in generateur_recurrent_d_espace([], [x for x in "abcdefghijklmnopqrstuvwxyz"], "", i):
			yield x

def main():
		for x in generateur_recurrent_d_espace_infini():
			print(x)

if __name__ == "__main__":
	main()
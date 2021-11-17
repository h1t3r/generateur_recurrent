def generateur_d_espace(dimension, a, coordonné, tmp, c, length_dimension):
	if isinstance(dimension, list):
		if a < length_dimension:
			for i in coordonné:
				dimension.append([tmp+str(i)])
			for x in dimension:
				if a == 1:
					for y in generateur_d_espace(x, a+1, coordonné, tmp+x[c], c+1,length_dimension):
						dimension[dimension.index(x)].append(y)
				elif a > 1:
					for y in generateur_d_espace(x, a+1, coordonné, x[0], c+1, length_dimension):
						dimension[dimension.index(x)].append(y)
			yield dimension
		elif a == length_dimension:
			for i in range(0, length_dimension):
				dimension.append([tmp+str(i)])
			yield dimension

def generateur_d_espace_infini():
	i = 0
	while True:
		i = i +1
		for y in generateur_d_espace([], 1, [x for x in range(0, i)], "",0, i):
			yield y
		if i == 3:
			exit()

for x in generateur_d_espace_infini():
	print(x)
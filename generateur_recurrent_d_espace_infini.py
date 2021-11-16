def generateur_recurrent_d_espace(alphabet_de_dimension,  coordonné, dimension):
	for x in alphabet_de_dimension:
		if len(coordonné)+1 < dimension:
			for y in generateur_recurrent_d_espace(alphabet_de_dimension, coordonné + str(x), dimension):
				yield y
		elif len(coordonné)+1 == dimension:
			yield coordonné + str(x)

def rentrer_dans_dimension(dim, a, l, c,alphabet):
	if a < l:
		print(a)
		if isinstance(dim, list):
			dim.append([[c+str(i)] for i in range(0, l+1)])
			print(dim)
			for x in dim:
				for i in range(0, l+1):
					print("i="+str(i))
					print("a="+str(a))
					for y in rentrer_dans_dimension(x, a+1, l ,c+str(i), alphabet):
						yield y
	elif a == l:
		if isinstance(dim, list):
			for i in range(0, l+1):	
				dim.append(c+str(i))
		print(dim)
		yield dim




for x in rentrer_dans_dimension([], 1, 3, "", [x for x in range(1, 4)]):
	print(x)
	print("\n")

#generateur_recurrent_d_espace_2d()
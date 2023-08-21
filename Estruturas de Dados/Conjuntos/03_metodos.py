#Métodos

#{}.union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

resultado = conjunto_a.union(conjunto_b)
print(resultado)

#{}.intersection
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.intersection(conjunto_b)
print(resultado)

#{}.difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)

#{}.symmetric_difference
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)	# {1, 4}
print(resultado)

#{}.issubset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)	#Elementos de A pertencem a B

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)	#Elementos de B pertencem a A

#{}.issuperset
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)	#Elementos de B pertencem a A

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)	#Elementos de A pertencem a B

#{}.isdisjoint
#Conjuntos sem intersecção
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)
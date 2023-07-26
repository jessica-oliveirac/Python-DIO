#Método [].copy
#Ter uma cópia com os mesmos valores, sem afetar o original
lista = [1, "Python", [40, 30, 20]]

lista.copy()

print(lista)  # [1, "Python", [40, 30, 20]]

#lista = [1, "Python", [40, 30, 20]]

#l2 = lista.copy()

#print(lista)  # [1, "Python", [40, 30, 20]]

#print(id(l2), id(lista))

#l2[0] = 2

#print(l2)
#print(lista)
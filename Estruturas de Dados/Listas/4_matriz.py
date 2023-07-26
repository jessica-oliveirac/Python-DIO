#Lista aninhadas(Matriz)

#Listas podem armazenar todosos tipod de objetos Python, portanto podemos ter 
#listas que armazenam outras listas. Com isso podemos criar estruturas 
#bidimensionais (tabelas), e acessar informando os índices de cada linha e 
#coluna
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"
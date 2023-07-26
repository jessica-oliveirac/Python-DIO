#[].index

linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0


# Ele encontra a primeira ocorreência do elemento. Somente a primeira vez que o 
#elento apareceu na lista
linguagens = ["python", "java", "c", "java", "csharp"]

print(linguagens.index("java"))  # 1

#Todas as vezes em que ocorre
#Usano o count e decrementando
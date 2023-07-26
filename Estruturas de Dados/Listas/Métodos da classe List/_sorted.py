#sorted
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]

#função built in: função que já está inclusa na linguagem, na bateria padrão
#ex: len e sorted(ao contrário do sorted, ele é uma função)

print(sorted(linguagens)) 
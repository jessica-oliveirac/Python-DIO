texto = input("Informe um texto: ")
VOGAIS = "AEIOU"
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

    print()

#ou (o else não é muito comum no dia-a dia)

# Exemplo utilizando um iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()  # adiciona uma quebra de linha
    print("Executa no final do laço")


# Exemplo utilizando a função built-in range
# range(stop)-> range object    range(4)    range(0,4)
#list(range(10)) ou list(range(0, 10))
# range(start, stop[, step])-> range object
for numero in range(0, 51, 5):
    print(numero, end=" ")
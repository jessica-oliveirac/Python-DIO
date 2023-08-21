#Acessando os dados
#Conjuntos em Python não suportam indexação

#Solução: converter uma lista(para acessar o valor)
numeros = {1, 2, 3, 2}

numeros = list(numeros)

print(numeros[0])

#Iterar conjuntos
carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")
#para saber qual o índice do objeto dentro do laço for
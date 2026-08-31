# EXERCÍCIO 1 
frutas = ("maçã", "banana", "laranja", "uva", "abacaxi")
print(frutas)
print(frutas[0])
print(frutas[4])
print(frutas[1:4])

# EXERCÍCIO 2
numeros = (10, 25, 7, 42, 18, 30)
maior = 0
menor = 999999
soma = 0
print(len(numeros))
for i in numeros:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    soma += i
print(maior)
print(menor)
print(soma)

# EXERCÍCIO 3
qnt = {}
cores = ("vermelho", "azul", "verde", "amarelo", "azul")
cor = input("Digite uma cor: ")
for i in cores:
    if i not in qnt:
        qnt[cor] = 1
    else:
        qnt[cor] += 1
print(f"A cor {cor} aparece {qnt[cor]} vezes")

# EXERCÍCIO 4
pessoa = ("Bruno", 18, "São Paulo")

print(f"Nome: {pessoa[0]}")
print(f"idade: {pessoa[1]}")
print(f"Cidade: {pessoa[2]}")
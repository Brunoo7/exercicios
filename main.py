# EXERCÍCIO 1   
'''frutas = ["maçã", "banana", "laranja", "uva", "manga"]
for fruta in frutas:
    print(fruta)'''

# EXERCÍCIO 2
'''infos = [
            {"nome": "ana", "idade": "30"}, 
            {"nome": "bob", "idade": "63"}, 
            {"nome": "carlos", "idade": "83"}, 
            {"nome": "daniel", "idade": "23"},
            {"nome": "eduardo", "idade": "29"}
]
for info in infos:
    nome = info ["nome"]
    idade = info ["idade"]
    print(f"{nome} tem {idade} anos")'''

# EXERCÍCIO 3

'''infos = [
            {"nome": "placa de vídeo", "preço": 4000, "estoque": 0}, 
            {"nome": "processador", "preço": 1000, "estoque": 43},
            {"nome": "gabinete", "preço": 350, "estoque": 70},
            {"nome": "monitor", "preço": 2000, "estoque": 0},
            {"nome": "teclado", "preço": 100, "estoque": 29}, 
        ]

for info in infos:
    nome = info ["nome"]
    estoque = info ["estoque"]
    if estoque > 0:
        print(f"O produto {nome} está com {estoque} número de itens no estoque")'''

# EXERCÍCIO 4

'''i = 0
num = 10000000000000000000000000000
while num != 0:
    num = int(input("Digite um número: "))
    if num != 0:
        i += 1
print(f"Você digitou {i} números")'''

# EXERCÍCIO 5

'''nomes = []
novo_nome = 0
while novo_nome != "sair":
    novo_nome = input("Digite o nome que deseja adicionar à lista ou digite 'sair' para sair do programa: ")
    if novo_nome != "sair":
        nomes.append(novo_nome)
print(nomes)'''

# EXERCÍCIO 6

'''frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã", "uva"]
qnt_frutas = {}

for frut in frutas:
    if frut not in qnt_frutas:
        qnt_frutas[frut] = 1 # adiociona uma nova chave
    else:
        qnt_frutas[frut] = qnt_frutas[frut] + 1 # aumenta a quiantidade
print(qnt_frutas)'''

# EXERCÍCIO 7

'''nuns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for nun in nuns:
    if nun % 2 == 0:
        print(nun)'''

# EXERCÍCIO 8

'''nuns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
soma = 0
media = 0
qnt = 0
for i in nuns:
    qnt += 1
for nun in nuns:
    soma = soma + nun
    media = soma / qnt 
print(f"Soma de todos os números: {soma}, quantidades de números: {qnt}, média dos números: {media}")'''

# EXERCÍCIO 9

alunos = {
    "Ana": [8, 7, 9],
    "Bruno": [5, 6, 4],
    "Carlos": [10, 9, 8]
}

for aluno in alunos:
    media = 0
    soma = 0
    for notas in alunos [aluno]:
        soma = notas + soma
    media = soma / 3
    if media >= 7:
        print(f"O aluno {aluno} está aprovado")
    elif media >= 5:
        print(f"O aluno {aluno} está de recuperação")
    else:
        print(f"O aluno {aluno} está reprovado")
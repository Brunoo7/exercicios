# EXERCÍCIO 1

"""
Exercício 1 - Percorrendo uma lista

Objetivo:
Percorrer uma lista de frutas utilizando um laço for
e exibir cada fruta individualmente.
"""

frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Percorre cada elemento da lista
for fruta in frutas:
    print(fruta)


# ============================================================
# EXERCÍCIO 2

"""
Exercício 2 - Lista de dicionários

Objetivo:
Percorrer uma lista que contém dicionários e acessar
os valores armazenados nas chaves "nome" e "idade".
"""

infos = [
    {"nome": "ana", "idade": "30"},
    {"nome": "bob", "idade": "63"},
    {"nome": "carlos", "idade": "83"},
    {"nome": "daniel", "idade": "23"},
    {"nome": "eduardo", "idade": "29"}
]

# Percorre cada dicionário da lista
for info in infos:
    nome = info["nome"]
    idade = info["idade"]

    print(f"{nome} tem {idade} anos")


# ============================================================
# EXERCÍCIO 3

"""
Exercício 3 - Verificando estoque

Objetivo:
Percorrer uma lista de produtos e mostrar somente aqueles
que possuem pelo menos uma unidade disponível em estoque.
"""

infos = [
    {"nome": "placa de vídeo", "preço": 4000, "estoque": 0},
    {"nome": "processador", "preço": 1000, "estoque": 43},
    {"nome": "gabinete", "preço": 350, "estoque": 70},
    {"nome": "monitor", "preço": 2000, "estoque": 0},
    {"nome": "teclado", "preço": 100, "estoque": 29}
]

for info in infos:
    nome = info["nome"]
    estoque = info["estoque"]

    # Mostra somente produtos que possuem estoque
    if estoque > 0:
        print(
            f"O produto {nome} está com "
            f"{estoque} número de itens no estoque"
        )


# ============================================================
# EXERCÍCIO 4

"""
Exercício 4 - Contando números digitados

Objetivo:
Permitir que o usuário digite vários números e contar
quantos números diferentes de zero foram digitados.

O programa termina quando o usuário digita 0.
"""

i = 0
num = 10000000000000000000000000000

while num != 0:
    num = int(input("Digite um número: "))

    # Só conta os números diferentes de zero
    if num != 0:
        i += 1

print(f"Você digitou {i} números")


# ============================================================
# EXERCÍCIO 5

"""
Exercício 5 - Adicionando nomes a uma lista

Objetivo:
Permitir que o usuário adicione nomes a uma lista.
O programa continua funcionando até que o usuário digite
"sair".
"""

nomes = []
novo_nome = 0

while novo_nome != "sair":
    novo_nome = input(
        "Digite o nome que deseja adicionar à lista "
        "ou digite 'sair' para sair do programa: "
    )

    # Não adiciona "sair" à lista
    if novo_nome != "sair":
        nomes.append(novo_nome)

print(nomes)


# ============================================================
# EXERCÍCIO 6

"""
Exercício 6 - Contando elementos com um dicionário

Objetivo:
Contar quantas vezes cada fruta aparece na lista.

O dicionário utiliza o nome da fruta como chave
e a quantidade de ocorrências como valor.
"""

frutas = [
    "maçã",
    "banana",
    "maçã",
    "laranja",
    "banana",
    "maçã",
    "uva"
]

qnt_frutas = {}

for frut in frutas:

    # Se a fruta ainda não existe, cria uma nova chave
    if frut not in qnt_frutas:
        qnt_frutas[frut] = 1

    # Se a fruta já existe, aumenta sua quantidade
    else:
        qnt_frutas[frut] = qnt_frutas[frut] + 1

print(qnt_frutas)


# ============================================================
# EXERCÍCIO 7

"""
Exercício 7 - Números pares

Objetivo:
Percorrer os números de 1 a 10 e mostrar somente
aqueles que são pares.
"""

nuns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for nun in nuns:

    # Números divisíveis por 2 são pares
    if nun % 2 == 0:
        print(nun)


# ============================================================
# EXERCÍCIO 8

"""
Exercício 8 - Soma e média

Objetivo:
Calcular a soma, a quantidade e a média dos números
presentes em uma lista.
"""

nuns = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

soma = 0
media = 0
qnt = 0

# Conta quantos números existem na lista
for i in nuns:
    qnt += 1

# Soma todos os números da lista
for nun in nuns:
    soma = soma + nun

# Calcula a média
media = soma / qnt

print(
    f"Soma de todos os números: {soma}, "
    f"quantidade de números: {qnt}, "
    f"média dos números: {media}"
)


# ============================================================
# EXERCÍCIO 9

"""
Exercício 9 - Média e situação dos alunos

Objetivo:
Calcular a média de cada aluno e informar se ele está:
- Aprovado
- De recuperação
- Reprovado
"""

alunos = {
    "Ana": [8, 7, 9],
    "Bruno": [5, 6, 4],
    "Carlos": [10, 9, 8]
}

# Percorre cada aluno do dicionário
for aluno in alunos:

    media = 0
    soma = 0

    # Percorre as notas daquele aluno
    for notas in alunos[aluno]:
        soma = notas + soma

    # Cada aluno possui 3 notas
    media = soma / 3

    # Verifica a situação do aluno
    if media >= 7:
        print(f"O aluno {aluno} está aprovado")

    elif media >= 5:
        print(f"O aluno {aluno} está de recuperação")

    else:
        print(f"O aluno {aluno} está reprovado")


# ============================================================
# EXERCÍCIO 10

"""
Exercício 10 - Acessando dados de um produto

Objetivo:
Acessar informações armazenadas em um dicionário
e exibir os dados do produto.
"""

produto = {
    "nome": "Notebook",
    "preco": 3500,
    "estoque": 10
}

# Acessa os valores através das chaves do dicionário
nome = produto["nome"]
preco = produto["preco"]
estoque = produto["estoque"]

print(
    f"O produto {nome} está custando R${preco} "
    f"e ainda tem {estoque} unidades disponíveis"
)


# ============================================================
# EXERCÍCIO 11

"""
Exercício 11 - Menu de números

Objetivo:
Criar um menu que permita ao usuário:
1. Adicionar números
2. Listar números
3. Mostrar o maior número
4. Sair

Conceitos utilizados:
- Lista
- Função
- while
- match/case
- for
- if/else
"""

nuns = []


def menu():
    """Exibe o menu e executa a opção escolhida pelo usuário."""

    opcao = 0

    # Mantém o programa funcionando até escolher a opção 4
    while opcao != 4:

        print("1 - Adicionar número")
        print("2 - Listar números")
        print("3 - Mostrar maior número")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1:
                num_add = int(
                    input("Digite o número que deseja adicionar à lista: ")
                )

                nuns.append(num_add)

            case 2:
                print(nuns)

            case 3:

                # Verifica se a lista possui números
                if len(nuns) > 0:

                    # Assume inicialmente que o primeiro número
                    # é o maior
                    maior_num = nuns[0]

                    for num in nuns:
                        if num > maior_num:
                            maior_num = num

                    print(maior_num)

                else:
                    print("A lista está vazia")

    print("Saindo")


menu()


# ============================================================
# EXERCÍCIO 12

"""
Exercício 12 - Sistema de produtos

Objetivo:
Criar um pequeno sistema de estoque que permita:
1. Cadastrar produtos
2. Listar produtos
3. Calcular o valor total do estoque
4. Sair

Conceitos utilizados:
- Lista de dicionários
- Função
- while
- match/case
- for
- acumulador
"""

produtos_loja = []


def menu():
    """Exibe o menu e executa as funções do sistema."""

    opcao = 0

    while opcao != 4:

        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Mostrar valor total do estoque")
        print("4 - Sair")

        opcao = int(input("Escolha uma opção: "))

        match opcao:

            case 1:
                print("Cadastrar produto")

                nome = input("Digite o nome do produto: ")
                preco = int(input("Digite o preço do produto: "))
                estoque = int(
                    input("Digite a quantidade em estoque do produto: ")
                )

                # Cria um dicionário para representar o produto
                novo_produto = {
                    "nome": nome,
                    "preço": preco,
                    "quantidade": estoque
                }

                # Adiciona o produto à lista
                produtos_loja.append(novo_produto)

                print(
                    f"O produto {nome} foi cadastrado com sucesso!"
                )

            case 2:
                print("Produtos:")

                # Percorre todos os produtos cadastrados
                for produto in produtos_loja:

                    nome = produto["nome"]
                    preco = produto["preço"]
                    estoque = produto["quantidade"]

                    print(
                        f"Nome: {nome}, "
                        f"Preço: {preco}, "
                        f"Quantidade: {estoque}"
                    )

            case 3:
                print("Valor total do estoque")

                valor_total = 0

                # Calcula o valor de cada produto e acumula o resultado
                for produto in produtos_loja:

                    preco = produto["preço"]
                    estoque = produto["quantidade"]

                    valor_total = valor_total + (preco * estoque)

                print(
                    f"O valor total do estoque é: {valor_total}"
                )

    print("Saindo...")


menu()


# ============================================================
# EXERCÍCIO 13

"""
Exercício 13 - Múltiplos de 3

Objetivo:
Percorrer os números de 1 a 19 e mostrar somente
os números divisíveis por 3.
"""

for i in range(1, 20):

    # Verifica se o número é divisível por 3
    if i % 3 == 0:
        print(i)


# ============================================================
# EXERCÍCIO 14

"""
Exercício 14 - Filtrando números

Objetivo:
Percorrer uma lista e criar uma nova lista contendo
somente os números maiores que 10.
"""

numeros = [12, 5, 8, 21, 30, 7, 14, 3, 18]
maiores = []

for num in numeros:

    # Adiciona à nova lista somente números maiores que 10
    if num > 10:
        maiores.append(num)

print(maiores)


# ============================================================
# EXERCÍCIO 15

"""
Exercício 15 - Faturamento por produto

Objetivo:
Percorrer uma lista de vendas e calcular o faturamento
total de cada produto.

Quando um produto aparece mais de uma vez, seu faturamento
é acumulado no mesmo valor do dicionário.

Resultado esperado:

{
    "Mouse": 250,
    "Teclado": 100,
    "Monitor": 800
}
"""

vendas = [
    {"produto": "Mouse", "preco": 50, "quantidade": 2},
    {"produto": "Teclado", "preco": 100, "quantidade": 1},
    {"produto": "Mouse", "preco": 50, "quantidade": 3},
    {"produto": "Monitor", "preco": 800, "quantidade": 1}
]

# Dicionário que armazenará o faturamento de cada produto
faturamento_total = {}

for produto in vendas:

    nome = produto["produto"]
    preco = produto["preco"]
    quantidade = produto["quantidade"]

    # Calcula o faturamento da venda atual
    faturamento = preco * quantidade

    # Se o produto ainda não existe, cria uma nova chave
    if nome not in faturamento_total:
        faturamento_total[nome] = faturamento

    # Se o produto já existe, soma o novo faturamento ao anterior
    else:
        faturamento_total[nome] = (
            faturamento_total[nome] + faturamento
        )

print(faturamento_total)
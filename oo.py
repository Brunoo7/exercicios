# EXERCÍCIO 1
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# p1 = Pessoa("Bruno", 18)
# p2 = Pessoa("Ana", 30)

# print(f"Nome: {p1.nome}")
# print(f"Idade: {p1.idade}")
# print(f"Nome: {p2.nome}")
# print(f"Idade: {p2.idade}")

# EXERCÍCIO 2
# class Carro:
#     def __init__(self, marca, modelo, ano):
#         self.marca = marca
#         self.modelo = modelo
#         self.ano = ano
#     def exibir_infos(self):
#         print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")

# c1 = Carro("Chevrolet", "Onix", 2023)
# c2 = Carro("Toyota", "Hilux", 2022)
# c3 = Carro("Volkswagen", "Gol", 2021)

# c1.exibir_infos()
# c2.exibir_infos()
# c3.exibir_infos()

# EXERCÍCIO 3
# class Produto:
#     def __init__(self, nome, preco, estoque):
#         self.nome = nome
#         self.preco = preco
#         self.estoque = estoque
#     def exibir_infos(self):
#         print(f"Produto: {self.nome}, Preço: {self.preco}, estoque: {self.estoque}")

# p1 = Produto("Teclado", 150, 50)

# p1.exibir_infos()

# EXERCÍCIO 4
# class Produto:
#     def __init__(self, nome, preco, estoque):
#         self.nome = nome
#         self.preco = preco
#         self.estoque = estoque

#     def exibir_infos(self):
#         print(f"Produto: {self.nome}, Preço: {self.preco}, estoque: {self.estoque}")

#     def atualizar_produto(self):
#         novo_preco = float(input("Digite o valor do novo preço: "))
#         self.preco = novo_preco
#         novo_estoque = int(input("Digite o valor do novo estoque: "))
#         self.estoque = novo_estoque

# produtos = Produto("Teclado", 150, 50)

# def menu():
#     opcao = 0
#     while opcao != 3:
#         print("1- Mostrar produtos")
#         print("2- Atualizar produtos")
#         print("3- Sair")

#         opcao = int(input("Escolha uma opção: "))

#         match opcao:
#             case 1:
#                 produtos.exibir_infos() 

#             case 2:
#                 produtos.atualizar_produto()

#             case 3:
#                 print("Saindo...")

# menu()

# EXERCÍCIO  5
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#     def apresentar(self):
#         print(f"Olá! meu nome é {self.nome} e tenho {self.idade} anos.")

# p1 = Pessoa("Bruno", 18)
# p2 = Pessoa("Ana", 30)

# p1.apresentar()
# p2.apresentar()

# EXERCÍCIO 6
# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

#     def fazer_aniversario(self):
#         self.idade += 1

# p1 = Pessoa("Bruno", 18)
# p2 = Pessoa("Ana", 30)

# p1.fazer_aniversario()
# p2.fazer_aniversario()
# p2.fazer_aniversario()

# print(p1.idade)
# print(p2.idade)

# EXERCÍCIO 7
# class ContaBancaria:
#     def __init__(self, titular, saldo):
#         self.saldo = saldo
#         self.titular = titular

#     def depositar(self, valor):
#         self.saldo += valor

#     def sacar(self, valor):
#         if valor > self.saldo:
#             print("Valor inválido")
#         else:
#             self.saldo -= valor

#     def mostrar_saldo(self):
#         print(f"O saldo da conta do titular {self.titular} é de R${self.saldo}")

# conta = ContaBancaria("Bruno", 100)

# valor = float(input("Digite o valor que quer depositar: "))
# conta.depositar(valor)

# valor = float(input("Digite o valor que quer sacar: "))
# conta.sacar(valor)

# conta.mostrar_saldo()

# EXERCÍCIO 8
# class Calculadora:
    
#     def somar (self, a, b):
#         return a + b

#     def subtrair (self, a, b):
#         return a - b

#     def multiplicar (self, a, b):
#         return a * b

#     def dividir (self, a, b):
#         if a == 0 or b == 0:
#             print("Valor inválido, impossível dividir por 0")
#         else:
#             return a / b

# a = float(input("Digite o primeiro valor: "))
# b = float(input("Digite o segundo valor: "))

# calc = Calculadora()

# print(f"O valor da soma é: {calc.somar(a,b)}")
# print(f"O valor da subtração é: {calc.subtrair(a,b)}")
# print(f"O valor da multiplicação é: {calc.multiplicar(a,b)}")
# print(f"O valor da divisão é: {calc.dividir(a,b)}")

# EXERCÍCO 9
# class Cliente:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

# cliente = Cliente("Bruno", 19)


# class Conta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo

#     def deposito(self, valor):
#         self.saldo += valor

#     def saque(self, valor):
#         if valor > self.saldo:
#             print("Saldo insuficiente")
#         else:
#             self.saldo -= valor

#     def consultar_saldo(self):
#         print(f"O saldo do titular {self.titular.nome} é de {self.saldo}")

# conta = Conta(cliente, 100)

# valor = float(input("Digite o valor que quer depositar: "))
# conta.deposito(valor)

# valor = float(input("Digite o valor que quer sacar: "))
# conta.saque(valor)

# conta.consultar_saldo()

# EXERCÍCO 10
# class Produto:
#     def __init__(self, nome, preco):
#         self.nome = nome
#         self.preco = preco

# class Carrinho:
#     def __init__(self):
#         self.produtos = []

#     def adicionar_produto(self, produto):
#         self.produtos.append(produto)

#     def remover_produto(self, produto):
#         self.produtos.remove(produto)

#     def mostrar_produtos(self):
#         print("====PRODUTOS====")
#         for i in self.produtos:
#             print(f"Nome: {i.nome.ljust(20)} | Preco: {i.preco}")

#     def calcular_total(self):
#         total = 0
#         for produto in self.produtos:
#             total += produto.preco
#         print(f"\nO valor total do seu carrinho é: R${total}")


# produto_01 = Produto("Teclado", 150)
# produto_02 = Produto("Monitor", 350)
# produto_03 = Produto("Placa de vídeo", 150)

# carrinho = Carrinho()

# carrinho.adicionar_produto(produto_01)
# carrinho.adicionar_produto(produto_02)
# carrinho.adicionar_produto(produto_03)

# carrinho.remover_produto(produto_02)

# carrinho.mostrar_produtos()

# carrinho.calcular_total()
# EXERCÍCIO 11
class Livro:
    def __init__(self, titulo, autor, disponivel):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        print("====LIVROS====")
        for i in self.livros:
            print(f"Título: {i.titulo.ljust(20)} | Autor: {i.autor.ljust(20)} | Disponível: {i.disponivel}")

    def emprestar_livro(self):
        livro_desejado = input("\nQual livro deseja pegar emprestado? ")
        encontrado = False
        for i in self.livros:
            if livro_desejado in i.titulo:
                encontrado = True

                if i.disponivel == False:
                    print("Livro não disponível")
                else:
                    i.disponivel = False
                    print("Livro emprestado!")
        if encontrado == False:
            print("Livro não encontrado")

    def devolver_livro(self):
        devolucao = input("\nQual livro deseja devolver? ")
        encontrado = False
        for i in self.livros:
            if devolucao in i.titulo:
                encontrado = True

                if i.disponivel == True:
                    print("Livro já devolvido")
                else:
                    i.disponivel = True
                    print("Livro devolvido!")

        if encontrado == False:          
            print("Livro não encontrado")

livro_01 = Livro("Dom Casmurro", "Machado de Assis", True)
livro_02 = Livro("O Hobbit", "J. R. R. Tolkien", False)
livro_03 = Livro("1984", "George Orwell", True)

biblioteca = Biblioteca()

biblioteca.adicionar_livro(livro_01)
biblioteca.adicionar_livro(livro_02)
biblioteca.adicionar_livro(livro_03)

biblioteca.listar_livros()

biblioteca.emprestar_livro()

biblioteca.devolver_livro()